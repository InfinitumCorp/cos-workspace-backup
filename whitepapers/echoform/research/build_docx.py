from pathlib import Path
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
root=Path('/workspace/whitepapers/echoform')
stem='EchoForm-Modern-Applications-of-Reflexive-Control-Theory-DRAFT'
s=(root/(stem+'.md')).read_text()
doc=Document()
sec=doc.sections[0]
sec.top_margin=sec.bottom_margin=Inches(.8)
sec.left_margin=sec.right_margin=Inches(.85)
normal=doc.styles['Normal']
normal.font.name='Calibri'; normal.font.size=Pt(11)
normal.paragraph_format.space_after=Pt(7)
normal.paragraph_format.line_spacing=1.1
for h in ['Title','Heading 1','Heading 2','Heading 3']:
 doc.styles[h].font.name='Calibri'
 doc.styles[h].font.color.rgb=RGBColor.from_string('19364D')
header=sec.header.paragraphs[0]
header.text='INFINITUM® CORPORATION  |  DRAFT FOR REVIEW'
header.style='Caption'
footer=sec.footer.paragraphs[0]
footer.text='Not for distribution.  |  © 2026 Infinitum® Corporation  |  '
fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE'); footer._p.append(fld)

def inline(p,text):
 for t in re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*)',text):
  if not t: continue
  r=p.add_run(t.strip('*') if t.startswith('*') else t)
  if t.startswith('**'):r.bold=True
  elif t.startswith('*'):r.italic=True

expected=[]
for line in s.splitlines():
 if not line.strip():continue
 if line.startswith('# '):
  p=doc.add_paragraph(style='Title'); txt=line[2:]
 elif line.startswith('### '):
  p=doc.add_paragraph(style='Heading 2'); txt=line[4:]
 elif line.startswith('## '):
  txt=line[3:]
  if txt=='Executive Summary':doc.add_page_break()
  p=doc.add_paragraph(style='Heading 1')
 elif line.startswith('> '):
  p=doc.add_paragraph(style='Quote'); txt=line[2:]
 elif line.startswith('- '):
  p=doc.add_paragraph(style='List Bullet'); txt=line[2:]
 else:
  p=doc.add_paragraph();txt=line
 inline(p,txt)
 expected.append(re.sub(r'\*\*([^*]+)\*\*|\*([^*]+)\*',lambda m:m.group(1) or m.group(2),txt))
doc.core_properties.title='EchoForm™: Modern Applications of Reflexive Control Theory'
doc.core_properties.author='William Aaron Turner, Founder & President, Infinitum® Corporation'
doc.core_properties.subject='DRAFT FOR REVIEW. Not for distribution.'
doc.save(root/(stem+'.docx'))
actual=[p.text for p in Document(root/(stem+'.docx')).paragraphs if p.text.strip()]
assert actual==expected, 'Markdown/DOCX textual mismatch'
assert '<grok' not in s and 'citation_id' not in s
for term in ['EchoForm','Corporate Cognitive Warfare','Reflexive Capital Warfare','RiskFab','DoubtSprout','CCW']:
 assert not re.search(re.escape(term)+r'(?![\w™])',s), 'Unmarked coined term '+term
assert not re.search(r'\bInfinitum(?!®)',s), 'Unmarked corporate brand'
print('DOCX saved; complete text parity and branding checks passed.')
print('DOCX paragraphs:',len(actual))
