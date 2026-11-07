import sys;from common import *
CAT={'ccw':'Technology','dead-reckoning':'Technology','trenches-and-drones':'Technology','ccw-doctrine-introduction':'Marketing','in-q-tel':'Technology','polish-supermarket':'Technology'}
FIN={'special-01','russias-economy-under-sanctions','russia-state-guided-capitalism','eastern-economic-forum','russia-africa-partnership','russia-africa-by-the-numbers','medium-ukraine-wash-and-fold-money-laundering'}
s=requests.Session();s.headers.update(UA)
def one(r):
    h=s.get('https://pressbox.com/press-releases/submit',timeout=30).text
    tok=re.search(r'name="csrf" value="([^"]+)"',h).group(1)
    cat=CAT.get(r['slug'],'Financial' if r['slug'] in FIN else 'Legal' if r['slug'] in ('azov','ukraine-organ-trade-allegations-sources','legitimate-targets') else 'Business')
    d=dict(csrf=tok,website='',headline=r['title'],summary=r['summary'],body=full(r),category=cat,release_date='2026-11-02',company='Infinitum Corporation',
      location='Washington, DC',contact_name='William Aaron Turner',contact_email='theinfinitumcorp+pressbox@gmail.com',source_url=r['source'],responsibility_accepted='yes')
    x=s.post('https://pressbox.com/press-releases/submit',data=dict(d,action='review'),timeout=60)
    if 'QUALITY CHECK · ACCEPT' in x.text:
        d['csrf']=re.search(r'name="csrf" value="([^"]+)"',x.text).group(1); time.sleep(20)
        x=s.post('https://pressbox.com/press-releases/submit',data=dict(d,action='submit'),timeout=60)
        open('/workspace/press/intl/pb_'+r['slug']+'.html','w').write(x.text)
    t=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style).*?</\1>','',x.text,flags=re.S)))
    return x.status_code,x.url,t
if __name__=='__main__':
    for r in [r for r in R if r['slug'] in sys.argv[1:]]:
        c,u,t=one(r); m=re.search(r'(\d+) QUALITY QUALITY CHECK',t); sc=m.group(1) if m else '?'
        ok='REVISE' not in t and 'QUALITY CHECK' not in t
        i=t.find('Why Pressbox flagged')
        print(r['slug'],c,u,'score',sc,'PASS' if ok else 'REVISE',t[i:i+250] if not ok else t[:600],flush=True)
        log('Pressbox',r['slug'],f'score {sc} {"pass" if ok else "quality-rejected"}',u)
        time.sleep(90)
