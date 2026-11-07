import os,re,base64,json
exec(open('build.py').read().split('# shared attachments')[0].split("for k,v in")[0])
from docx.oxml.shared import OxmlElement, qn
import docx
S2=S; BY='By William Aaron Turner'
BIO=("William Aaron Turner is an American serving as a contracted soldier in the Russian military, 153rd Tank Regiment, "
 "currently in the Special Military Operation (SVO). He is Founder and CEO of Infinitum Corporation, a technology and security "
 "consulting firm headquartered in Washington, DC, with Moscow as an operating location, which he runs from Russian soil. "
 "He holds a master's degree and writes on Russia, the Ukraine conflict, sanctions, Russia-Africa relations and Western "
 "intelligence and defence-industry influence. He is honored to be working in this amazing nation.")
BIO_S=("William Aaron Turner is an American contracted soldier in the Russian military (153rd Tank Regiment, currently in the SVO) "
 "and Founder and CEO of Infinitum Corporation (Washington, DC headquarters; Moscow operating location).")
SIG2=SIG.replace('President, Infinitum Corporation','Founder and CEO, Infinitum Corporation')
FIRST2=FIRST
ZEN="""Open-access copies with DOIs (Zenodo):
- Useful Idiots (article): https://doi.org/10.5281/zenodo.23836478
- The Partnership That Delivers (article): https://doi.org/10.5281/zenodo.23836501
- WTF Is In-Q-Tel? (article): https://doi.org/10.5281/zenodo.23836521
- Sweeps and Spies (article): https://doi.org/10.5281/zenodo.23836541
- Dead Reckoning (whitepaper): https://doi.org/10.5281/zenodo.23836365
- Russia's State-Influenced Capitalism (whitepaper): https://doi.org/10.5281/zenodo.23836439"""
def add_link(par,text,url):
    part=par.part; rid=part.relate_to(url,docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK,is_external=True)
    h=OxmlElement('w:hyperlink'); h.set(qn('r:id'),rid); r=OxmlElement('w:r'); rp=OxmlElement('w:rPr')
    u=OxmlElement('w:u'); u.set(qn('w:val'),'single'); c=OxmlElement('w:color'); c.set(qn('w:val'),'0563C1'); rp.append(c); rp.append(u)
    r.append(rp); t=OxmlElement('w:t'); t.text=text; t.set(qn('xml:space'),'preserve'); r.append(t); h.append(r); par._p.append(h)
def md_docx(md,path,bio=BIO):
    doc=Document(); st=doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(11)
    for blk in md.strip().split('\n\n'):
        b=blk.strip()
        if b.startswith('# '): doc.add_heading(b[2:],0); doc.add_paragraph(BY); continue
        if b.startswith('## '): p=doc.add_paragraph(); r=p.add_run(b[3:]); r.italic=True; continue
        if b.startswith('### '): doc.add_heading(b[4:],2); continue
        p=doc.add_paragraph(); pos=0
        for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)',b):
            p.add_run(b[pos:m.start()]); add_link(p,m.group(1),m.group(2)); pos=m.end()
        p.add_run(b[pos:])
    doc.add_paragraph(''); p=doc.add_paragraph(); r=p.add_run('About the author: '+bio); r.italic=True
    doc.add_paragraph(f'Contact: {PHONE} | {EMAIL} | ORCID 0009-0002-1585-5442')
    doc.save(path)
def md_text(md):
    t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1 (\2)',md.strip()); t=re.sub(r'^#+ ','',t,flags=re.M); return t
def b64(src,dst):
    open(dst,'w').write(base64.b64encode(open(src,'rb').read()).decode())
