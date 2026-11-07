import sys, re, subprocess, copy
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
PANDOC='/workspace/journal/.venv/lib/python3.13/site-packages/pypandoc/files/pandoc'

def pandoc(md, out):
    subprocess.run([PANDOC, md, '-f', 'markdown+smart', '-t', 'docx', '-o', out], check=True)

def setfont(run_or_style, size, name='Times New Roman'):
    f=run_or_style.font; f.name=name; f.size=Pt(size)
    rpr=run_or_style.element.get_or_add_rPr() if hasattr(run_or_style,'element') else None
    if rpr is not None:
        rf=rpr.find(qn('w:rFonts'))
        if rf is None: rf=rpr.makeelement(qn('w:rFonts'),{}); rpr.append(rf)
        for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a),name)

def fmt(path, size, spacing, margins, small=None, justify=True):
    d=Document(path)
    for s in d.sections:
        s.left_margin,s.right_margin,s.top_margin,s.bottom_margin=[Cm(x) for x in margins]
    for st in d.styles:
        try:
            if st.type==1:
                st.font.name='Times New Roman'; st.font.color.rgb=None
                rpr=st.element.get_or_add_rPr(); rf=rpr.find(qn('w:rFonts'))
                if rf is None: rf=rpr.makeelement(qn('w:rFonts'),{}); rpr.append(rf)
                for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a),'Times New Roman')
                for a in ('w:asciiTheme','w:hAnsiTheme','w:cstheme','w:eastAsiaTheme'):
                    if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
        except Exception: pass
    for name in ['Normal','Body Text','First Paragraph','Compact','Block Text']:
        if name in [s.name for s in d.styles]:
            st=d.styles[name]; st.font.size=Pt(size)
            st.paragraph_format.line_spacing=spacing; st.paragraph_format.space_after=Pt(0)
            if justify: st.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY
    for name,sz in [('Title',size+2),('Heading 1',size),('Heading 2',size),('Heading 3',size)]:
        if name in [s.name for s in d.styles]:
            st=d.styles[name]; st.font.size=Pt(sz); st.font.bold=True; st.font.color.rgb=None
            st.paragraph_format.space_before=Pt(12); st.paragraph_format.space_after=Pt(6)
            st.paragraph_format.line_spacing=spacing
    small=small or size
    for name in ['Footnote Text','Footnote Reference']:
        if name in [s.name for s in d.styles]:
            st=d.styles[name]
            if name=='Footnote Text':
                st.font.size=Pt(small); st.paragraph_format.line_spacing=1.0; st.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.LEFT
    # tables
    for t in d.tables:
        t.style = d.styles['Table Grid'] if 'Table Grid' in [s.name for s in d.styles] else t.style
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    p.paragraph_format.line_spacing=1.0; p.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.LEFT
                    for r in p.runs: r.font.size=Pt(small if small<size else size-2)
    d.save(path)
    return d

def refs_small(path, start_heads, size):
    d=Document(path); on=False
    for p in d.paragraphs:
        if p.style.name.startswith('Heading'):
            on = p.text.strip() in start_heads
            continue
        if on:
            p.paragraph_format.line_spacing=1.0; p.paragraph_format.space_after=Pt(3)
            p.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs: r.font.size=Pt(size)
    d.save(path)

def captions(path):
    d=Document(path)
    for p in d.paragraphs:
        if p.style.name in ('Table Caption','Table Source','Rubric'):
            p.alignment=WD_ALIGN_PARAGRAPH.CENTER if p.style.name!='Table Source' else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing=1.0
            for r in p.runs:
                r.font.size=Pt(12 if p.style.name!='Table Source' else 10); r.font.bold = p.style.name!='Table Source'
    d.save(path)
