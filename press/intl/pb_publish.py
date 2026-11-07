import sys;from common import *
import html
H=lambda s: html.escape(s,quote=True).replace("&#x27;","&#39;")
s=requests.Session();s.headers.update(UA)
url=sys.argv[1]; x=s.get(url,timeout=30); h=x.text
slug=None
for r in R:
    if H(r['title'])[:60] in h or r['title'][:60] in h: slug=r['slug']
print('slug',slug)
if not slug: print(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style).*?</\1>','',h,flags=re.S)))[:2500]); sys.exit()
if any(l.split('\t')[1:3]==['Pressbox',slug] and 'published' in l for l in open('/workspace/press/intl/log.tsv')): print('ALREADY PUBLISHED, skip');sys.exit()
r=[q for q in R if q['slug']==slug][0]
tok=re.search(r'name="csrf" value="([^"]+)"',h).group(1)
i=img(r); d=dict(csrf=tok)
if i: d.update(alt_text=r['title'][:290],caption=r['title'][:590],rights_confirmed='yes')
y=s.post(url,data=d,files={'image_file':i} if i else None,timeout=60)
links=set(re.findall(r'https://pressbox\.com/(?:news|press-releases|newsroom)/[a-z0-9][^"\s<>]*',y.text))
t=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style).*?</\1>','',y.text,flags=re.S)))
print(y.status_code,y.url); print(t[:700]); print(links)
log('Pressbox',slug,f'published {y.status_code}',y.url)
