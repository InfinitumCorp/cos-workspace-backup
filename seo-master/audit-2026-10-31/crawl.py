import requests,json,re,time,csv,hashlib
from bs4 import BeautifulSoup
from urllib.parse import urlparse
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36'}
rows=[]
for line in open('urls.txt'):
    line=line.strip()
    if not line: continue
    cat,u=line.split('|',1)
    r={'category':cat,'url':u}
    try:
        t=time.time(); resp=requests.get(u,headers=UA,timeout=25,allow_redirects=True)
        r['status']=resp.status_code; r['final_url']=resp.url; r['secs']=round(time.time()-t,2); r['bytes']=len(resp.content)
        r['x_robots']=resp.headers.get('x-robots-tag','')
        open('raw/'+hashlib.md5(u.encode()).hexdigest()[:10]+'.html','wb').write(resp.content)
        s=BeautifulSoup(resp.text,'html.parser')
        g=lambda **k:(s.find('meta',attrs=k) or {}).get('content','') if s.find('meta',attrs=k) else ''
        r['title']=(s.title.string or '').strip() if s.title else ''
        r['meta_desc']=g(name='description')
        r['robots_meta']=g(name='robots')
        c=s.find('link',rel='canonical'); r['canonical']=c.get('href','') if c else ''
        h1=[h.get_text(' ',strip=True) for h in s.find_all('h1')]; r['h1_count']=len(h1); r['h1']=' || '.join(h1)[:150]
        r['og_title']=g(property='og:title'); r['og_image']=bool(g(property='og:image'))
        types=[]
        for sc in s.find_all('script',type='application/ld+json'):
            types+=re.findall(r'"@type"\s*:\s*"?\[?"?([A-Za-z]+)',sc.string or sc.get_text() or '')
        r['jsonld_types']=','.join(sorted(set(types)))
        for x in s(['script','style','noscript']): x.decompose()
        r['words']=len(s.get_text(' ',strip=True).split())
        host=urlparse(resp.url).netloc
        links=[a.get('href','') for a in s.find_all('a') if a.get('href','').startswith('http')]
        r['int_links']=sum(1 for l in links if urlparse(l).netloc==host); r['ext_links']=len(links)-r['int_links']
        own=[l for l in links if re.search(r'theinfinitumcorporation|ukrainianfiles|infinitumwhitepapers|t\.me/infinitum|x\.com/infinitumceo|whop\.com/infinitum|academia\.edu/Corporation|williamaaronturner',l) and urlparse(l).netloc!=host]
        r['links_to_owned']=len(set(own))
        r['links_to_site']=int(any('theinfinitumcorporation.com' in l for l in links))
        r['has_phone_7299509']=int('729-9509' in resp.text or '7299509' in resp.text)
        r['has_old_phone']=','.join(p for p in ['681-0120','980-9300'] if p in resp.text)
    except Exception as e:
        r['status']='ERR'; r['error']=str(e)[:120]
    rows.append(r); print(r.get('status'),u,r.get('title','')[:70])
keys=['category','url','status','final_url','secs','bytes','title','meta_desc','h1_count','h1','canonical','robots_meta','x_robots','og_title','og_image','jsonld_types','words','int_links','ext_links','links_to_owned','links_to_site','has_phone_7299509','has_old_phone','error']
with open('crawl.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys,extrasaction='ignore'); w.writeheader(); w.writerows(rows)
json.dump(rows,open('crawl.json','w'),indent=1)
