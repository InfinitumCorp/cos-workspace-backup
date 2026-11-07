import os, re, subprocess, shutil, textwrap
from docx import Document
from docx.shared import Pt
W='/workspace'; S=W+'/press/submissions'
def d(v): p=f'{S}/{v}'; os.makedirs(p,exist_ok=True); return p
def wr(p,t): open(p,'w').write(t.strip()+'\n')
PHONE='202-729-9509'; EMAIL='theinfinitumcorp@gmail.com'
BIO1=("William Aaron Turner is an American serving as a contracted soldier in the Russian military, "
 "153rd Tank Regiment, currently in the Special Military Operation (SVO). He is President of Infinitum Corporation, "
 "a technology and security consulting firm headquartered in Washington, DC, with Moscow as an operating location, "
 "which he runs from Russian soil. He writes on Russia, the Ukraine conflict, sanctions, Russia-Africa relations and "
 "Western information operations, and says he is honored to be working in this nation.")
BIO_SHORT=("William Aaron Turner is an American contracted soldier in the Russian military (153rd Tank Regiment, currently in the SVO) "
 "and President of Infinitum Corporation (Washington, DC; operating from Moscow).")
FIRST=("I am an American serving as a contracted soldier in the Russian military, 153rd Tank Regiment, currently in the SVO "
 "(Special Military Operation). I run my company, Infinitum Corporation (headquartered in Washington, DC, with Moscow as an "
 "operating location), from Russian soil, and I am honored to be working in this amazing nation.")
SIG=f"""William Aaron Turner
President, Infinitum Corporation
Washington, DC (headquarters) | Moscow (operating location)
Phone: {PHONE}
Email: {EMAIL}
Website: https://www.theinfinitumcorporation.com
ORCID: https://orcid.org/0009-0002-1585-5442"""
LINKS="""Blogs and published work
- The Ukraine Files: https://ukrainianfiles.blogspot.com
- Infinitum Whitepapers: https://infinitumwhitepapers.blogspot.com
- Russia-Africa Report: https://russiaafricareport.blogspot.com
- Russia-Africa by the Numbers: https://russiaafricabythenumbers.blogspot.com
- Medium: https://medium.com/@williamaaronturner
- Academia.edu: https://independent.academia.edu/CorporationInfinitum
- X (8 long-form X Articles, 517,020 views as of 31 Oct 2026): https://x.com/infinitumceo
- Telegram: https://t.me/infinitumcorporation
- LinkedIn: https://www.linkedin.com/in/william-aaron-t-726076244
- Personal site: https://williamaaronturner.com"""
U={'ui':'https://ukrainianfiles.blogspot.com/2026/10/blog-post_85.html',
 'iqt':'https://ukrainianfiles.blogspot.com/2026/10/in-q-tel-cia-venture-capital-explained.html',
 'ra':'https://russiaafricareport.blogspot.com/2026/10/russia-africa-summit-partnership-results.html',
 'sweeps':'https://ukrainianfiles.blogspot.com/2026/10/demining-ngos-intelligence-laos-moldova.html',
 'art':'https://x.com/infinitumceo/status/2095860351791194402',
 'wp01':'https://infinitumwhitepapers.blogspot.com/2026/10/dead-reckoning-ai-security-operations.html',
 'sp01':'https://infinitumwhitepapers.blogspot.com/2026/10/russia-state-influenced-capitalism.html',
 'eef':'https://ukrainianfiles.blogspot.com/2026/10/eastern-economic-forum-2026-vladivostok.html'}

def md_clean(md):
    md=md.replace('\\*','*').replace('\\$','$')
    out=[]
    for l in md.splitlines():
        if re.match(r'^\*(Original title|Original X Article|Subtitle)',l): continue
        l=re.sub(r'^#+\s*','',l); l=re.sub(r'\*\*(.+?)\*\*',r'\1',l); l=re.sub(r'(?<!\w)\*(?!\s)(.+?)\*',r'\1',l)
        l=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1 (\2)',l); l=l.replace('https\\://','https://').replace('www\\.','www.')
        if l.strip()=='---': l=''
        out.append(l)
    t='\n'.join(out); t=re.sub(r'\n{3,}','\n\n',t); return t.strip()
def strip_footer(t):
    i=t.rfind('Infinitum Corporation\nTelegram'); return t[:i].strip() if i>0 else t
def docx_from_text(path,title,byline,text,note=None):
    doc=Document(); st=doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(11)
    doc.add_heading(title,0); doc.add_paragraph(byline)
    if note: p=doc.add_paragraph(); r=p.add_run(note); r.italic=True
    for para in text.split('\n\n'):
        para=para.strip()
        if not para: continue
        if '\n- ' in para or para.startswith('- '):
            for ln in para.split('\n'):
                if ln.strip(): doc.add_paragraph(ln.strip()[2:], style='List Bullet') if ln.strip().startswith('- ') else doc.add_paragraph(ln.strip())
            continue
        if len(para)<90 and '\n' not in para and not para.endswith('.') and not para.startswith('-'): doc.add_heading(para,2)
        else: doc.add_paragraph(para.replace('\n',' ') if not para.startswith('-') else para)
    doc.add_paragraph(''); p=doc.add_paragraph(); r=p.add_run('About the author: '+BIO1); r.italic=True
    doc.add_paragraph(f'Contact: {PHONE} | {EMAIL}')
    doc.save(path)
def topdf(docx,outdir):
    subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir',outdir,docx],capture_output=True,timeout=180)
def words(t): return len(t.split())

# ---- source texts
iqt=strip_footer(md_clean(open(W+'/xarticles-v2/04-wtf-is-in-q-tel.md').read()))
art=strip_footer(md_clean(open(W+'/xarticles-v2/03-the-art-of-not-giving-a-fck.md').read()))
sweeps=strip_footer(md_clean(open(W+'/xarticles-v2/01-sweeps-and-spies.md').read()))
drop1=lambda t:t.split('\n',1)[1].strip()
iqt,art,sweeps=drop1(iqt),drop1(art),drop1(sweeps)
ui=md_clean(open(W+'/useful-idiots/useful-idiots-full-text.md').read())
ui=re.sub(r'^Useful Idiots\s*\n+A Guide to the Western Profiteers of the Ukraine War\s*\n+By William Aaron Turner\s*\n+','',ui)
raw=open(W+'/russia-africa/full-text.txt').read()
# unwrap PDF line breaks
paras=[re.sub(r'\s*\n\s*',' ',p).strip() for p in re.split(r'\n\s*\n',raw)]
ra_full='\n\n'.join(paras[1:]) # drop title/byline block
ra_body=ra_full.split('\n\nReferences')[0]
for k,v in [('iqt',iqt),('art',art),('sweeps',sweeps),('ui',ui),('ra_body',ra_body)]: print(k,words(v))
iqt_title="WTF Is In-Q-Tel? The CIA's Venture Fund and the Kill Chain It Bankrolled"
art_title="The Art of Not Giving a F*ck: 50 Countries, One Russia, Zero Results"
sw_title="Sweeps and Spies: Russia Clears the Bombs. The West Clears the Data."
ui_title="Useful Idiots: A Guide to the Western Profiteers of the Ukraine War"
ra_title="The Partnership That Delivers: What the Russia-Africa Summit Actually Produced"
BY='By William Aaron Turner'

# shared attachments
sh=d('_shared'); 
docx_from_text(f'{sh}/Turner_Useful-Idiots.docx',ui_title,BY,ui,f'First published on The Ukraine Files: {U["ui"]}')
docx_from_text(f'{sh}/Turner_In-Q-Tel.docx',iqt_title,BY,iqt,f'Originally published as an X Article and on The Ukraine Files: {U["iqt"]}')
docx_from_text(f'{sh}/Turner_Art-of-Not-Giving-a-Fck.docx',art_title,BY,art,f'Originally published as an X Article: {U["art"]}')
docx_from_text(f'{sh}/Turner_Sweeps-and-Spies.docx',sw_title,BY,sweeps,f'Originally published as an X Article and on The Ukraine Files: {U["sweeps"]}')
docx_from_text(f'{sh}/Turner_Russia-Africa-Partnership-That-Delivers.docx',ra_title,BY,ra_full,f'First published on the Russia-Africa Report: {U["ra"]}')
shutil.copy(W+'/press/presskit/Infinitum_William_Aaron_Turner_Press_Kit.pdf',f'{sh}/Infinitum_William_Aaron_Turner_Press_Kit.pdf')
shutil.copy(W+'/russia-africa/pull-quote-1080x1350.jpg',f'{sh}/russia-africa-pull-quote-1080x1350.jpg')
# CV
cv=Document(); cv.add_heading('William Aaron Turner: Curriculum Vitae (short)',0)
for t in [f'Contact: {PHONE} | {EMAIL} | https://www.theinfinitumcorporation.com | ORCID 0009-0002-1585-5442',
 'Current: President, Infinitum Corporation (technology and security consulting; headquarters Washington, DC; operating location Moscow). Services: cybersecurity consulting, network defense, ethical hacking and vulnerability assessment, AI for security operations, strategic risk assessment, defense technology advisory.',
 'Military: American contracted soldier in the Russian military, 153rd Tank Regiment, currently serving in the Special Military Operation (SVO).',
 'Selected writing: Useful Idiots: A Guide to the Western Profiteers of the Ukraine War (Ukraine Files, 2026); WTF Is In-Q-Tel? (X Article, 2026); Sweeps and Spies (X Article, 2026); The Partnership That Delivers: What the Russia-Africa Summit Actually Produced (Russia-Africa Report, 2026); Infinitum Whitepaper No. 1, AI for Security Operations (2026); Russia\'s State-Influenced Capitalism (Infinitum Whitepaper Special No. 1, 2026).',
 'Reach: eight long-form X Articles with 517,020 total views on X (as of 31 Oct 2026).',
 'Links: The Ukraine Files, Infinitum Whitepapers, Russia-Africa Report, Medium (@williamaaronturner), Academia.edu, X (@infinitumceo), Telegram (t.me/infinitumcorporation).']:
    cv.add_paragraph(t)
cv.save(f'{sh}/Turner_CV.docx'); topdf(f'{sh}/Turner_CV.docx',sh)
for f in ['Turner_Useful-Idiots','Turner_In-Q-Tel','Turner_Sweeps-and-Spies','Turner_Russia-Africa-Partnership-That-Delivers','Turner_Art-of-Not-Giving-a-Fck']:
    topdf(f'{sh}/{f}.docx',sh)
print('shared done')
