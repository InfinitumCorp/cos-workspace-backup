#!/usr/bin/env python3
"""Build the expanded Corporate Cognitive Warfare white paper from the approved source docx.
Keeps the approved cover, styles, header/footer; swaps the cover logo for the official hi-res
Infinitum stacked logo (cropped to content, no watermark); appends the expanded body from src/*.md."""
import re, sys, copy, glob, os
from docx import Document
from docx.shared import Pt, Emu, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DOCX = sys.argv[1]
OUT = sys.argv[2]
LOGO_SRC = '/workspace/brand/hires/infinitum-logo-stacked-black-on-white-4000.jpg'

# --- logo: crop official hi-res stacked logo to its content with even padding (no alteration of artwork)
im = Image.open(LOGO_SRC).convert('RGB')
from PIL import ImageOps
bbox = ImageOps.invert(im.convert('L')).point(lambda v: 255 if v > 40 else 0).getbbox()
pad = int(0.10 * max(bbox[2]-bbox[0], bbox[3]-bbox[1]))
box = (max(0,bbox[0]-pad), max(0,bbox[1]-pad), min(im.width,bbox[2]+pad), min(im.height,bbox[3]+pad))
logo = im.crop(box)
logo.thumbnail((1400, 1400), Image.LANCZOS)
logo_path = os.path.join(ROOT, 'assets', 'infinitum-logo-stacked-cover.png')
logo.save(logo_path, optimize=True)

doc = Document(SRC_DOCX)
body = doc.element.body
paras = doc.paragraphs
# keep cover paragraphs 0..4 (logo, title, subtitle, author, org); remove the rest (keep sectPr)
keep = set(id(p._p) for p in paras[:5])
for el in list(body):
    if el.tag == qn('w:sectPr'): continue
    if id(el) in keep: continue
    body.remove(el)

# swap logo image blob + fix extent to the new aspect ratio
blip = body.xpath('.//a:blip')[0]
rid = blip.get(qn('r:embed'))
img_part = doc.part.related_parts[rid]
img_part._blob = open(logo_path, 'rb').read()
ext = body.xpath('.//wp:inline/wp:extent')[0]
w_emu = int(1.9 * 914400); h_emu = int(w_emu * logo.height / logo.width)
ext.set('cx', str(w_emu)); ext.set('cy', str(h_emu))
for e in body.xpath('.//a:ext'):
    if e.getparent().tag.endswith('xfrm'):
        e.set('cx', str(w_emu)); e.set('cy', str(h_emu))

def sty(sid):
    for s in doc.styles:
        if s.style_id == sid: return s
    raise KeyError(sid)

def run_props(r, size=None, color=None, bold=None, italic=None, font='Calibri'):
    if font: r.font.name = font
    if size: r.font.size = Pt(size)
    if color: r.font.color.rgb = RGBColor.from_string(color)
    if bold is not None: r.bold = bold
    if italic is not None: r.italic = italic

# add "Expanded Edition" line on cover after subtitle (paragraph index 2)
cover_sub = doc.paragraphs[2]
newp = OxmlElement('w:p'); cover_sub._p.addnext(newp)
from docx.text.paragraph import Paragraph
ep = Paragraph(newp, cover_sub._parent)
ep.alignment = 1
ep.paragraph_format.space_before = Pt(6)
r = ep.add_run('EXPANDED EDITION  ·  OCTOBER 2026'); run_props(r, 9, '4A5568', bold=True)

# attribution line on cover
newp2 = OxmlElement('w:p'); ep._p.addnext(newp2)
ap = Paragraph(newp2, cover_sub._parent)
ap.alignment = 1
ap.paragraph_format.space_before = Pt(10)
r = ap.add_run('“Corporate Cognitive Warfare” is a term coined by William Aaron Turner, Founder & President of Infinitum Corporation')
run_props(r, 9, '4A5568', italic=True)

# --- numbering: helper to create restartable numbered lists from abstractNum of numId 3
numbering = doc.part.numbering_part.element
def abstract_of(numId):
    for n in numbering.findall(qn('w:num')):
        if n.get(qn('w:numId')) == str(numId):
            return n.find(qn('w:abstractNumId')).get(qn('w:val'))
ABS_NUM = abstract_of(3)
next_num = [max(int(n.get(qn('w:numId'))) for n in numbering.findall(qn('w:num'))) + 1]
def new_numbered():
    nid = next_num[0]; next_num[0] += 1
    num = OxmlElement('w:num'); num.set(qn('w:numId'), str(nid))
    a = OxmlElement('w:abstractNumId'); a.set(qn('w:val'), ABS_NUM); num.append(a)
    ov = OxmlElement('w:lvlOverride'); ov.set(qn('w:ilvl'), '0')
    so = OxmlElement('w:startOverride'); so.set(qn('w:val'), '1'); ov.append(so); num.append(ov)
    numbering.append(num)
    return nid

def set_num(p, numId):
    pPr = p._p.get_or_add_pPr()
    numPr = OxmlElement('w:numPr')
    il = OxmlElement('w:ilvl'); il.set(qn('w:val'), '0')
    ni = OxmlElement('w:numId'); ni.set(qn('w:val'), str(numId))
    numPr.append(il); numPr.append(ni); pPr.append(numPr)

def add_hyperlink(p, text, url):
    rid = doc.part.relate_to(url, RT.HYPERLINK, is_external=True)
    h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), rid); h.set(qn('w:history'), '1')
    r = OxmlElement('w:r'); rPr = OxmlElement('w:rPr')
    rs = OxmlElement('w:rStyle'); rs.set(qn('w:val'), 'Hyperlink'); rPr.append(rs); r.append(rPr)
    t = OxmlElement('w:t'); t.text = text; t.set(qn('xml:space'), 'preserve'); r.append(t)
    h.append(r); p._p.append(h)

TOKEN = re.compile(r'(\[\[[^\]]+\]\]|\*\*[^*]+\*\*|\*[^*]+\*|https?://[^\s)]+[^\s).,;])')
def add_inline(p, text, size=None, color=None, base_bold=None, base_italic=None):
    pos = 0
    for m in TOKEN.finditer(text):
        if m.start() > pos:
            r = p.add_run(text[pos:m.start()]); run_props(r, size, color, base_bold, base_italic, font=None)
        tok = m.group(0)
        if tok.startswith('[['):
            label, url = tok[2:-2].split('|', 1); add_hyperlink(p, label, url)
        elif tok.startswith('**'):
            r = p.add_run(tok[2:-2]); run_props(r, size, color, True, base_italic, font=None)
        elif tok.startswith('*'):
            r = p.add_run(tok[1:-1]); run_props(r, size, color, base_bold, True, font=None)
        else:
            add_hyperlink(p, tok, tok)
        pos = m.end()
    if pos < len(text):
        r = p.add_run(text[pos:]); run_props(r, size, color, base_bold, base_italic, font=None)

def set_cell_shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd'); shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), hexcolor)
    tcPr.append(shd)

def set_table_borders(tbl):
    tblPr = tbl._tbl.tblPr
    b = OxmlElement('w:tblBorders')
    for side in ('top','left','bottom','right','insideH','insideV'):
        e = OxmlElement(f'w:{side}'); e.set(qn('w:val'),'single'); e.set(qn('w:sz'),'4'); e.set(qn('w:color'),'A0AEC0'); b.append(e)
    tblPr.append(b)

def add_table(rows):
    ncol = len(rows[0])
    t = doc.add_table(rows=len(rows), cols=ncol)
    t.autofit = True
    set_table_borders(t)
    for i, row in enumerate(rows):
        for j in range(ncol):
            cell = t.cell(i, j); cell.text = ''
            p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(2)
            txt = row[j] if j < len(row) else ''
            if i == 0:
                add_inline(p, txt, size=9, color='FFFFFF', base_bold=True); set_cell_shade(cell, '1A365D')
            else:
                add_inline(p, txt, size=9)
                if i % 2 == 0: set_cell_shade(cell, 'EDF2F7')
    sp = doc.add_paragraph(); sp.paragraph_format.space_after = Pt(4)

def para(text, style=None, after=200):
    p = doc.add_paragraph(style=style) if style else doc.add_paragraph()
    if not style: p.paragraph_format.space_after = Emu(after * 635)  # twips->EMU
    add_inline(p, text)
    return p

def page_break():
    p = doc.add_paragraph(); r = p.add_run(); br = OxmlElement('w:br'); br.set(qn('w:type'), 'page'); r._r.append(br)

# page break after cover
page_break()

files = sorted(glob.glob(os.path.join(ROOT, 'src', '[0-9][0-9]-*.md')))
for f in files:
    lines = open(f, encoding='utf-8').read().split('\n')
    i = 0; cur_num = None
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            cur_num = None; i += 1; continue
        if ln.strip() == '::pagebreak':
            page_break(); i += 1; continue
        if ln.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                rows.append(cells); i += 1
            add_table(rows); continue
        if ln.startswith('### '):
            doc.add_paragraph(ln[4:], style=sty('Heading3')); i += 1; continue
        if ln.startswith('## '):
            doc.add_paragraph(ln[3:], style=sty('Heading2')); i += 1; continue
        if ln.startswith('# '):
            doc.add_paragraph(ln[2:], style=sty('Heading1')); i += 1; continue
        if ln.startswith('- '):
            p = doc.add_paragraph(style=sty('ListParagraph')); set_num(p, 2); add_inline(p, ln[2:]); i += 1; continue
        m = re.match(r'^(\d+)\. (.*)', ln)
        if m:
            if cur_num is None: cur_num = new_numbered()
            p = doc.add_paragraph(style=sty('ListParagraph')); set_num(p, cur_num); add_inline(p, m.group(2)); i += 1; continue
        cur_num = None
        if ln.startswith('— End of White Paper —'):
            p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(20)
            r = p.add_run(ln); run_props(r, None, '718096', italic=True, font=None); i += 1; continue
        if ln.startswith('Term "Corporate Cognitive Warfare" coined'):
            p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(10)
            r = p.add_run(ln.replace('"', '“', 1).replace('"', '”', 1)); run_props(r, 9, '718096', italic=True, font=None); i += 1; continue
        para(ln); i += 1

cp = doc.core_properties
cp.title = 'Corporate Cognitive Warfare: Irregular Warfare for Market Supremacy (Expanded Edition)'
cp.author = 'William Aaron Turner'
cp.subject = 'Corporate Cognitive Warfare white paper, expanded edition, October 2026'
cp.keywords = 'Corporate Cognitive Warfare; William Aaron Turner; Infinitum Corporation; reflexive control; cognitive domain operations; influence; counter-influence'
cp.comments = 'Term "Corporate Cognitive Warfare" coined by William Aaron Turner, 2026.'
cp.last_modified_by = 'Infinitum Corporation'
doc.save(OUT)
print('saved', OUT)
