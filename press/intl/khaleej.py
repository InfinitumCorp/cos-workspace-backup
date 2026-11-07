import sys;from common import *
s=requests.Session();s.headers.update(UA)
def one(r):
    h=s.get('https://thekhaleejpost.com/submit-a-press-release/',timeout=30).text
    f=re.search(r'<form.*?wpcf7-form.*?</form>',h,re.S).group(0)
    d={m.group(1):m.group(2) for m in re.finditer(r'name="(_[^"]+)" value="([^"]*)"',f)}
    d.update({'your-name':'William Aaron Turner','your-email':'info@theinfinitumcorporation.com','press-title':r['title'],'Pressreleasecontent':excerpt(r,1800),'map_post_id':''})
    fid=d['_wpcf7']
    x=s.post('https://thekhaleejpost.com/submit-a-press-release/',data=d,files={'press-photo':img(r,True)},timeout=90)
    m=re.search(r'wpcf7-response-output[^>]*>(.*?)</div>',x.text,re.S); st=re.search(r'class="wpcf7-form ([a-z-]+)',x.text)
    j={'status':st.group(1) if st else x.status_code,'message':re.sub('<[^>]+>','',m.group(1)).strip() if m else ''}
    return j
for i,r in enumerate([r for r in R if r['slug'] in sys.argv[1:]] if len(sys.argv)>1 and sys.argv[1]!='ALL' else R):
    j=one(r); print(r['slug'],j.get('status'),j.get('message'),j.get('invalid_fields'),flush=True)
    log('KhaleejPost',r['slug'],str(j.get('status'))+' '+str(j.get('message'))[:80])
    if j.get('status') not in ('sent','invalid'): break
    time.sleep(120)
