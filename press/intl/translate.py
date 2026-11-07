import json,sys,time,re,html
import argostranslate.translate as AT
lang=sys.argv[1]
R=json.load(open('releases.json'))

URL=re.compile(r'https?://\S+')
def tr(text):
    out=[];buf=''
    for p in text.split('\n\n'):
        if len(buf)+len(p)>4000: out.append(buf);buf=''
        buf+=('\n\n' if buf else '')+p
    if buf: out.append(buf)
    res=[]
    for chunk in out:
        urls=URL.findall(chunk); c=chunk.replace(' & ',' and ')
        for i,u in enumerate(urls): c=c.replace(u,f'[[U{i}]]',1)
        t='\n\n'.join(AT.translate(pp,'en',lang) if pp.strip() else pp for pp in c.split('\n\n'))
        for i,u in enumerate(urls): t=re.sub(r'\[\[\s*U\s*%d\s*\]\]'%i,u,t)
        res.append(html.unescape(t))
    return '\n\n'.join(res)
import os
fn=f'releases_{lang}.json'
o=json.load(open(fn)) if os.path.exists(fn) else []
have={x['slug'] for x in o}
for r in R:
    if r['slug'] in have: continue
    x=dict(r); x['title']=tr(r['title']); x['summary']=tr(r['summary']); x['body']=tr(r['body'])
    x['about']=tr(r['about']); x['contact']=tr(r['contact']); x['about_h']=tr('About Infinitum Corporation'); x['full_h']=tr('Full article')+': '
    x['body']=x['body'].replace('Regimiento','Regimiento')  # placeholder
    o.append(x); print(r['slug'],flush=True)
    json.dump(o,open(fn,'w'),ensure_ascii=False,indent=1)
