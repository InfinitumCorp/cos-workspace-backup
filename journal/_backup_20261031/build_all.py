import re, os, sys, subprocess
sys.path.insert(0,'/workspace/journal'); from build import *
def plain(s): return re.sub(r'\[\^[A-Za-z0-9]+\]|[#*|`{}]|:::.*','',s)
def anon(t, start_marker):
    return t
J='/workspace/journal'
# ---------- RGA ----------
R=f'{J}/russia-in-global-affairs'; t=open(f'{R}/src/manuscript.md').read()
abs_w=len(t.split('**Abstract**')[1].split('**Keywords')[0].split())
noref=t.split('# References')[0]
chars=len(plain(noref).replace('\n',' ').strip())
words_body=len(plain(t.split('# Introduction')[1].split('# Statements')[0]).split())
print('RGA chars excl refs (incl title/abstract/statements):',chars,'abstract',abs_w,'body words',words_body,'total words',len(plain(t).split()))
# anonymised: remove author block lines 5-11 and anonymise statements
a=re.sub(r'\*\*William A\. Turner\*\*.*?(?=\*\*Abstract\*\*)','',t,flags=re.S)
st=a.split('# Statements')[1].split('# References')[0]
a=a.replace(st,'\n\n*Funding, conflict-of-interest, AI-use and data-availability statements are provided on the separate title page to preserve anonymity for double-blind review.*\n\n')
os.makedirs(f'{R}/build',exist_ok=True)
open(f'{R}/build/anon.md','w').write(a)
for name,md in [('Turner_RGA_manuscript_full',f'{R}/src/manuscript.md'),('Turner_RGA_manuscript_anonymised',f'{R}/build/anon.md')]:
    out=f'{R}/{name}.docx'; pandoc(md,out); fmt(out,12,1.5,(2.5,2.5,2.5,2.5)); refs_small(out,{'References'},11)
for name in ['title-page','cover-letter']:
    s=open(f'{R}/src/{name}.md').read().replace('an abstract of [N] words',f'an abstract of {abs_w} words').replace('approximately [N] characters',f'approximately {round(chars,-2):,} characters').replace('[N] characters with spaces, excluding references; abstract [N] words',f'approx. {round(chars,-2):,} characters with spaces, excluding references; abstract {abs_w} words')
    if name=='cover-letter': s=s.replace('\n','  \n',5)
    open(f'{R}/build/{name}.md','w').write(s); out=f'{R}/Turner_RGA_{name}.docx'; pandoc(f'{R}/build/{name}.md',out); fmt(out,12,1.15,(2.5,2.5,2.5,2.5),justify=False)
# ---------- MGIMO ----------
M=f'{J}/mgimo-review'; t=open(f'{M}/src/manuscript.md').read(); os.makedirs(f'{M}/build',exist_ok=True)
body=t.split('# Introduction')[1].split('# Список литературы')[0]
fn='\n'.join(l for l in t.splitlines() if l.startswith('[^'))
refs=t.split('# Список литературы')[1].split('# Об авторе')[0]
print('MGIMO body chars',len(plain(body).replace('\n',' ')),'with footnotes',len(plain(body+fn).replace('\n',' ')),'with refs',len(plain(body+fn+refs).replace('\n',' ')),'words body',len(plain(body).split()),'total words',len(plain(t).split()))
out=f'{M}/Turner_MGIMO_manuscript_full.docx'; pandoc(f'{M}/src/manuscript.md',out); fmt(out,14,1.5,(3,1.5,2,2),small=10); refs_small(out,{'Список литературы','References'},10); captions(out)
a=re.sub(r'\*\*У\.А\. Тёрнер\*\*\n\nInfinitum Corporation \(Вашингтон, США\)\n\n','',t)
a=re.sub(r'\*\*William A\. Turner\*\*\n\nInfinitum Corporation \(Washington, D\.C\., USA\)\n\n','',a)
a=a.replace('Тёрнер У.А. ','[Автор] ').replace('Turner W.A. ','[Author] ')
a=a.split('# Об авторе')[0]+'\n# Благодарности / Acknowledgements\n\nСведения об авторе, финансировании, использовании ИИ и конфликте интересов приводятся в метаданных статьи (удалены для слепого рецензирования). / Author information, funding, AI-use and conflict-of-interest statements are provided in the submission metadata (removed for blind review).\n\n'+'\n'.join(l for l in t.splitlines() if l.startswith('[^'))
open(f'{M}/build/anon.md','w').write(a)
out=f'{M}/Turner_MGIMO_manuscript_anonymised.docx'; pandoc(f'{M}/build/anon.md',out); fmt(out,14,1.5,(3,1.5,2,2),small=10); refs_small(out,{'Список литературы','References'},10); captions(out)
s=open(f'{M}/src/cover-letter.md').read().replace('\n','  \n',5); open(f'{M}/build/cl.md','w').write(s)
out=f'{M}/Turner_MGIMO_cover-letter.docx'; pandoc(f'{M}/build/cl.md',out); fmt(out,12,1.15,(2.5,2.5,2.5,2.5),justify=False)
# ---------- RUDN ----------
U=f'{J}/vestnik-rudn-ir'; t=open(f'{U}/src/manuscript.md').read(); os.makedirs(f'{U}/build',exist_ok=True)
total=len(plain(t).split()); nref=len([l for l in t.split('## References')[1].splitlines() if l.strip()])
print('RUDN total words',total,'refs',nref,'abstract',len(t.split('## Abstract')[1].split('**Keywords')[0].split()))
a=t.split('## Acknowledgements')[0]+'## Acknowledgements\n\n*Conflict-of-interest and funding statements are provided on the separate title page to preserve anonymity for double-blind review.*\n\n## References'+t.split('## References')[1]
open(f'{U}/build/anon.md','w').write(a)
for name,md in [('Turner_RUDN_manuscript_full',f'{U}/src/manuscript.md'),('Turner_RUDN_manuscript_anonymised',f'{U}/build/anon.md')]:
    out=f'{U}/{name}.docx'; pandoc(md,out); fmt(out,12,1.5,(2,2,2,2)); refs_small(out,{'References'},12)
out=f'{U}/Turner_RUDN_title-page_EN-RU.docx'; s=open(f'{U}/src/title-page.md').read().replace('**Word count:** see cover letter.',f'**Word count:** {total} words including tables and references; {nref} references.'); open(f'{U}/build/tp.md','w').write(s); pandoc(f'{U}/build/tp.md',out); fmt(out,12,1.5,(2,2,2,2))
s=open(f'{U}/src/cover-letter.md').read().replace('[N] words',f'{total:,} words').replace('\n','  \n',4); open(f'{U}/build/cl.md','w').write(s)
out=f'{U}/Turner_RUDN_cover-letter_UNSIGNED.docx'; pandoc(f'{U}/build/cl.md',out); fmt(out,12,1.15,(2.5,2.5,2.5,2.5),justify=False)
subprocess.run(['soffice','--headless','--convert-to','pdf','--outdir',U,out],check=True,capture_output=True)
