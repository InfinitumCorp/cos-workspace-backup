import os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import data2
D = data2.D
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
D.verify_quotes()
BLACK = RGBColor(0x0B, 0x0B, 0x0B); WHITE = RGBColor(255, 255, 255); GREY = RGBColor(0xA8, 0xA8, 0xA8); ALT = RGBColor(0x17, 0x17, 0x17); LINE = RGBColor(0x3A, 0x3A, 0x3A)
FONT = "IBM Plex Sans"
prs = Presentation(); prs.slide_width = Inches(13.333); prs.slide_height = Inches(7.5)
BL = prs.slide_layouts[6]
L, R = Inches(0.7), Inches(13.333 - 0.7); W = R - L
links_by_section = {}
cur = [None]
def fmt_date(d):
    if len(d) == 7: return datetime.date(int(d[:4]), int(d[5:]), 1).strftime('%b %Y')
    return datetime.date(*map(int, d.split('-'))).strftime('%b %-d, %Y')

def rule(s, y, w=None, weight=0.75):
    c = s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, L, y, L + (w or W), y)
    c.line.color.rgb = LINE; c.line.width = Pt(weight); c.shadow.inherit = False

def run(p, text, size=14, bold=False, light=False, url=None, color=None):
    r = p.add_run(); r.text = text
    f = r.font; f.name = FONT; f.size = Pt(size); f.bold = bold; f.color.rgb = color or WHITE
    if url:
        r.hyperlink.address = url
        f.underline = True
        links_by_section.setdefault(cur[0], []).append(url)
    return r

def textbox(s, x, y, w, h, wrap=True):
    tb = s.shapes.add_textbox(x, y, w, h); tf = tb.text_frame; tf.word_wrap = wrap
    tf.margin_left = tf.margin_right = 0; tf.margin_top = tf.margin_bottom = 0
    return tf

page = [0]
def new_slide(kicker, title):
    s = prs.slides.add_slide(BL); page[0] += 1
    s.background.fill.solid(); s.background.fill.fore_color.rgb = BLACK
    s.shapes.add_picture('assets/infinitum-logo-horizontal-white.png', R - Inches(2.1), Inches(0.42), width=Inches(2.1))
    tf = textbox(s, L, Inches(0.42), Inches(8), Inches(0.3)); run(tf.paragraphs[0], kicker.upper(), 10, color=GREY)
    tf = textbox(s, L, Inches(0.72), Inches(11), Inches(0.7)); run(tf.paragraphs[0], title.upper(), 28, bold=True)
    bar = s.shapes.add_shape(1, L, Inches(1.42), Inches(0.9), Pt(3)); bar.fill.solid(); bar.fill.fore_color.rgb = WHITE; bar.line.fill.background()
    rule(s, Inches(7.0), weight=0.5)
    s.shapes.add_picture('assets/infinitum-wordmark-white.png', L, Inches(7.13), height=Inches(0.11))
    tf = textbox(s, L + Inches(1.5), Inches(7.08), Inches(7), Inches(0.3)); run(tf.paragraphs[0], "Press Kit 2026  \u00b7  theinfinitumcorporation.com  \u00b7  202-729-9509", 9, color=GREY)
    tf = textbox(s, R - Inches(1), Inches(7.08), Inches(1), Inches(0.3)); p = tf.paragraphs[0]; p.alignment = PP_ALIGN.RIGHT; run(p, f"{page[0]:02d}", 9, bold=True)
    return s

def para(tf, first=[True]):
    return tf.paragraphs[0] if (len(tf.paragraphs) == 1 and not tf.paragraphs[0].runs) else tf.add_paragraph()

def table(s, headers, rows, widths, y=Inches(1.75), size=10.5, url_cols=()):
    n = len(rows) + 1
    shp = s.shapes.add_table(n, len(headers), L, y, W, Inches(0.35) * n)
    tbl = shp.table
    tblPr = shp._element.graphic.graphicData.tbl.tblPr
    # remove default style banding/colors
    tblPr.set('bandRow', '0'); tblPr.set('firstRow', '0')
    total = sum(widths)
    for i, w in enumerate(widths): tbl.columns[i].width = int(W * w / total)
    for r in range(n):
        for c in range(len(headers)):
            cell = tbl.cell(r, c); cell.fill.solid(); cell.fill.fore_color.rgb = (RGBColor(0x2A,0x2A,0x2A) if r == 0 else (ALT if r % 2 == 0 else BLACK))
            cell.margin_left = Inches(0.02); cell.margin_right = Inches(0.1); cell.margin_top = Inches(0.05); cell.margin_bottom = Inches(0.05)
            cell.vertical_anchor = MSO_ANCHOR.TOP
            tf = cell.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]
            if r == 0: run(p, headers[c].upper(), size - 1.5, bold=True)
            else:
                v = rows[r - 1][c]
                if c in url_cols and v and v.startswith('http'): run(p, v, size - 1.5, url=v)
                else: run(p, v, size)
            set_borders(cell, bottom=(1.0 if r == 0 else 0.5))
    return shp

from pptx.oxml.ns import qn
from lxml import etree
def set_borders(cell, bottom=0.5):
    tcPr = cell._tc.get_or_add_tcPr()
    for tag in ('a:lnL', 'a:lnR', 'a:lnT', 'a:lnB'):
        ln = etree.SubElement(tcPr, qn(tag))
        if tag == 'a:lnB':
            ln.set('w', str(int(Pt(bottom)))); sf = etree.SubElement(ln, qn('a:solidFill')); clr = etree.SubElement(sf, qn('a:srgbClr')); clr.set('val', '3A3A3A')
        else:
            ln.set('w', '0'); etree.SubElement(ln, qn('a:noFill'))

def chunks(lst, n): return [lst[i:i + n] for i in range(0, len(lst), n)]

# 1 Cover
cur[0] = 'Cover'
s = prs.slides.add_slide(BL); page[0] += 1
s.background.fill.solid(); s.background.fill.fore_color.rgb = BLACK
s.shapes.add_picture('assets/cover-photo.jpg', prs.slide_width - Inches(7.5), 0, height=Inches(7.5))
s.shapes.add_picture('assets/infinitum-logo-horizontal-white.png', L, Inches(0.7), width=Inches(3.0))
tf = textbox(s, L, Inches(2.75), Inches(7), Inches(0.3)); run(tf.paragraphs[0], "PRESS KIT \u00b7 NOVEMBER 2026", 11, color=GREY)
tf = textbox(s, L, Inches(3.1), Inches(7), Inches(1.8)); run(tf.paragraphs[0], "WILLIAM AARON", 48, bold=True); run(tf.add_paragraph(), "TURNER", 48, bold=True)
tf = textbox(s, L, Inches(4.95), Inches(6.2), Inches(1)); run(tf.paragraphs[0], "Founder and President, Infinitum Corporation", 18)
p = tf.add_paragraph(); p.space_before = Pt(6); run(p, "Technology and security consulting, including Corporate Cognitive Warfare. Headquartered in Washington, DC.", 12, color=GREY)
rule(s, Inches(6.05), w=Inches(5.6))
tf = textbox(s, L, Inches(6.18), Inches(6), Inches(0.9)); p = tf.paragraphs[0]; run(p, D.ADDRESS, 10.5, color=GREY)
p = tf.add_paragraph(); run(p, data2.HOURS, 10.5, color=GREY)
p = tf.add_paragraph(); run(p, D.PHONE, 10.5, url='tel:+12027299509'); run(p, "  \u00b7  ", 10.5); run(p, D.EMAIL, 10.5, url='mailto:' + D.EMAIL); run(p, "  \u00b7  ", 10.5); run(p, D.WEB.replace('https://', ''), 10.5, url=D.WEB)

# Contents
cur[0] = 'Contents'
titles = ["Fast facts", "About Infinitum Corporation", "Founder: William Aaron Turner", "Services", "Media contact",
          "Official channels and social links", "Publications, whitepapers and articles", "Press releases", "Media coverage", "Quotes", "Downloadable assets"]
s = new_slide("Contents", "Contents")
tf = textbox(s, L, Inches(1.8), W, Inches(5))
for i, t in enumerate(titles):
    p = para(tf); run(p, f"{i + 2:02d}   ", 16); run(p, t, 16); p.space_after = Pt(6)

# 2 Fast facts
cur[0] = 'Fast facts'
s = new_slide("Section 02", "Fast facts")
rows = [(k, v) for k, v in D.FAST_FACTS]
shp = table(s, ["Item", "Detail"], rows, [1, 3], size=11.5, url_cols=(1,))

# 3 About
cur[0] = 'About'
s = new_slide("Section 03", "About Infinitum Corporation")
tf = textbox(s, L, Inches(1.85), W, Inches(4.5))
text = D.BOILERPLATE
p = tf.paragraphs[0]
# split boilerplate to linkify URLs/email
import re
for part in re.split(r'(https?://\S+|\S+@\S+\.com)', text):
    if not part: continue
    if part.startswith('http'): run(p, part, 20, url=part)
    elif '@' in part: run(p, part, 20, url='mailto:' + part.rstrip('.'))
    else: run(p, part, 20)
tf = textbox(s, L, Inches(6.5), W, Inches(0.3)); run(tf.paragraphs[0], "Official boilerplate.", 10)

# 4 Bio
cur[0] = 'Bio'
s = new_slide("Section 04", "Founder: William Aaron Turner")
s.shapes.add_picture('assets/william-headshot.jpg', L, Inches(1.8), height=Inches(3.9))
tf = textbox(s, L + Inches(4.25), Inches(1.8), W - Inches(4.25), Inches(3.9))
for b in D.BIO:
    p = para(tf); run(p, b, 13.5); p.space_after = Pt(8)
tf = textbox(s, L, Inches(5.95), W, Inches(1.0)); run(tf.paragraphs[0], "SOURCES", 10, bold=True)
for n, u in D.BIO_SOURCES:
    p = tf.add_paragraph(); run(p, n + ": ", 9.5); run(p, u, 9.5, url=u)

# 5 Services
cur[0] = 'Services'
s = new_slide("Section 05", "Services")
tf = textbox(s, L, Inches(1.8), Inches(4.2), Inches(4.8)); run(tf.paragraphs[0], "PRACTICE AREAS", 11, bold=True)
for x in D.SERVICES_CORE: p = tf.add_paragraph(); run(p, "\u2014  " + x, 14); p.space_before = Pt(5)
tf = textbox(s, L + Inches(4.6), Inches(1.8), W - Inches(4.6), Inches(4.8)); run(tf.paragraphs[0], "CORE COMPETENCIES", 11, bold=True)
for x in D.SERVICES_COMPETENCIES: p = tf.add_paragraph(); run(p, "\u2014  " + x, 12.5); p.space_before = Pt(3)
tf = textbox(s, L, Inches(6.55), W, Inches(0.4)); p = tf.paragraphs[0]; run(p, "Source: " + D.SERVICES_SOURCE[0] + ": ", 9); run(p, D.SERVICES_SOURCE[1], 9, url=D.SERVICES_SOURCE[1])

# 6 Contact
cur[0] = 'Contact'
s = new_slide("Section 06", "Media contact")
tf = textbox(s, L, Inches(1.9), W, Inches(4.8))
for k, v in D.CONTACT:
    p = para(tf); run(p, f"{k}:  ", 18, bold=True)
    if k == 'Phone': run(p, v, 18, url='tel:+1' + v.replace('-', ''))
    elif k == 'Email': run(p, v, 18, url='mailto:' + v)
    elif v.startswith('http'): run(p, v, 18, url=v)
    else: run(p, v, 18)
    p.space_after = Pt(10)

# 7 Channels
cur[0] = 'Channels'
for i, ch in enumerate(chunks(D.CHANNELS, 6)):
    s = new_slide("Section 07", "Official channels and social links" + (" (cont.)" if i else ""))
    table(s, ["Platform", "Account", "Link", "Note"], [(a, b, c, d) for a, b, c, d in ch], [1.2, 1.8, 3.6, 2.6], size=12, url_cols=(2,))

# 8 Publications
cur[0] = 'Publications'
s = new_slide("Section 08", "Publications, whitepapers and articles")
tf = textbox(s, L, Inches(1.8), W, Inches(1.6)); run(tf.paragraphs[0], "BLOGS", 11, bold=True)
for n, u in D.BLOG_HOMES:
    p = tf.add_paragraph(); run(p, n + ":  ", 16); run(p, u, 16, url=u); p.space_before = Pt(6)
tf = textbox(s, L, Inches(3.6), W, Inches(2)); run(tf.paragraphs[0], f"{len(D.PUBLICATIONS)} items follow: Infinitum whitepapers (with PDFs), the Russia Africa Report, Russia-Africa by the Numbers, The Ukraine Files posts and the Academia.edu papers.", 14)
for i, ch in enumerate(chunks(D.PUBLICATIONS, 7)):
    s = new_slide("Section 08", "Publications" + f" ({i + 1}/{len(chunks(D.PUBLICATIONS, 7))})")
    table(s, ["Title", "Outlet", "Date", "Link"], [(t, o, fmt_date(d), u) for t, o, d, u in ch], [4, 1.7, 1.1, 4.4], size=11, url_cols=(3,))

# 9 Releases
cur[0] = 'Releases'
for i, ch in enumerate(chunks(D.RELEASES, 6)):
    s = new_slide("Section 09", "Press releases" + f" ({i + 1}/{len(chunks(D.RELEASES, 6))})")
    table(s, ["Title", "Outlet", "Date", "Link"], [(t, o, fmt_date(d), u) for t, o, d, u in ch], [4.2, 1.5, 1.1, 4.4], size=11, url_cols=(3,))

# 10 Coverage
cur[0] = 'Coverage'
s = new_slide("Section 10", "Media coverage")
table(s, ["Title", "Outlet", "Date", "Link"], [(t, o, fmt_date(d), u) for t, o, d, u in D.COVERAGE], [3.5, 2.2, 1.1, 4.4], size=11, url_cols=(3,))
tf = textbox(s, L, Inches(3.55), W, Inches(3.3))
p = tf.paragraphs[0]; run(p, D.COVERAGE_NOTE, 13); p.space_after = Pt(12)
p = tf.add_paragraph(); run(p, "RUSSIAN MEDIA", 11, bold=True); p.space_after = Pt(4)
p = tf.add_paragraph(); run(p, D.RUSSIAN_MEDIA_NOTE, 13)

# 11 Quotes
cur[0] = 'Quotes'
allq = [(t, st, o, d, u) for t, st, o, d, u, _ in D.QUOTES] + [(t, st, o, d, u) for t, st, o, d, u in D.RELEASE_QUOTES]
for i, ch in enumerate(chunks(allq, 3)):
    s = new_slide("Section 11", "Quotes" + f" ({i + 1}/{len(chunks(allq, 3))})")
    y = Inches(1.8)
    for t, st, o, d, u in ch:
        tf = textbox(s, L, y, W, Inches(1.6))
        p = tf.paragraphs[0]; run(p, "\u201c" + t + "\u201d", 19 if len(t) < 130 else 16)
        p = tf.add_paragraph(); p.space_before = Pt(4); run(p, f"William Aaron Turner, {st}, {o}, {fmt_date(d)}.  ", 10); run(p, u, 9, url=u)
        y += Inches(1.7)

# 12 Assets
cur[0] = 'Assets'
s = new_slide("Section 12", "Downloadable assets")
table(s, ["Asset", "File (assets folder)", "Public source"], [(n, f, u or "Included with this kit") for n, f, u in D.ASSETS], [4, 3.6, 4], size=9.5, url_cols=(2,))
for k, (n, f, u) in enumerate(D.ASSETS[:2] + D.ASSETS[2:3]):
    pass
s.shapes.add_picture('assets/infinitum-logo-stacked-white.png', L, Inches(5.6), height=Inches(1.2))
tf = textbox(s, L + Inches(2), Inches(5.9), W - Inches(2), Inches(0.8)); run(tf.paragraphs[0], D.ASSETS_NOTE, 13)

prs.save('Infinitum-Press-Kit-2026.pptx')
import json
json.dump({k: v for k, v in links_by_section.items()}, open('pptx_links.json', 'w'), indent=1)
print('slides', len(prs.slides), {k: len(v) for k, v in links_by_section.items()})

# Force theme hyperlink colors to black (B&W design)
import zipfile, shutil, re as _re
src = 'Infinitum-Press-Kit-2026.pptx'; tmp = src + '.tmp'
with zipfile.ZipFile(src) as zin, zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        b = zin.read(item.filename)
        if item.filename.startswith('ppt/theme/') and item.filename.endswith('.xml'):
            t = b.decode('utf8')
            t = _re.sub(r'<a:hlink>.*?</a:hlink>', '<a:hlink><a:srgbClr val="FFFFFF"/></a:hlink>', t, flags=_re.S)
            t = _re.sub(r'<a:folHlink>.*?</a:folHlink>', '<a:folHlink><a:srgbClr val="DDDDDD"/></a:folHlink>', t, flags=_re.S)
            b = t.encode('utf8')
        zout.writestr(item, b)
shutil.move(tmp, src)
print('theme hyperlinks black')
