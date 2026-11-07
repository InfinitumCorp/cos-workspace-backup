import re,requests,html,sys,spr_submit as S
UA={'User-Agent':'Mozilla/5.0 Chrome/130'}
def form(h,act):
    f=h[h.find('action="%s"'%act):];f=f[:f.find('</form>')];d={}
    for i in re.findall(r'<input[^>]*>',f):
        n=re.search(r'name="([^"]+)"',i)
        if not n: continue
        t=re.search(r'type="([^"]+)"',i);t=t.group(1) if t else 'text'
        if t=='file': continue
        if t in('radio','checkbox') and 'checked' not in i: continue
        v=re.search(r'value="([^"]*)"',i);d[n.group(1)]=html.unescape(v.group(1)) if v else 'on'
    for n,v in re.findall(r'<textarea[^>]*name="([^"]+)"[^>]*>(.*?)</textarea>',f,re.S): d[n]=html.unescape(v)
    for n,body in re.findall(r'<select[^>]*name="([^"]+)"[^>]*>(.*?)</select>',f,re.S):
        m=re.search(r'<option[^>]*value="([^"]*)"[^>]*selected',body) or re.search(r'<option[^>]*selected[^>]*value="([^"]*)"',body)
        d[n]=html.unescape(m.group(1)) if m else ''
    return d
def edit(url):
    s=requests.Session();s.headers.update(UA)
    r=s.get(url,timeout=30)
    if r.status_code!=200: return 'HTTP %d'%r.status_code
    d=form(r.text,'/api/preview')
    if d.get('boilerplate','').strip()==S.BP: return 'already current'
    d['boilerplate']=S.BP; d['publish_choice']='free'; d['is_boosted']='0'; d['agree_terms']='on'
    if not d.get('tz_offset'): d['tz_offset']='-180'
    p=s.post('https://pressliftoff.com/api/preview',data=d,files={'_':('',b'','application/octet-stream')},timeout=60)
    d2=form(p.text,'/api/publish')
    if not d2: return 'preview failed %d'%p.status_code
    assert d2.get('publish_choice')=='free' and d2.get('is_boosted')=='0'
    q=s.post('https://pressliftoff.com/api/publish',data=d2,timeout=60)
    t=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style)[^>]*>.*?</\1>','',q.text,flags=re.S)))
    i=t.find('Privacy Policy');return 'publish %d: %s'%(q.status_code,t[i+15:i+200])
if __name__=='__main__':
    for u in sys.argv[1:]: print(u,'->',edit(u))
