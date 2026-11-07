from pressbox import *
r=[x for x in R if x['slug']=='russias-economy-under-sanctions'][0]
h=s.get('https://pressbox.com/press-releases/submit',timeout=30).text
tok=re.search(r'name="csrf" value="([^"]+)"',h).group(1)
d=dict(csrf=tok,website='',headline=r['title'],summary=r['summary'],body=full(r),category='Financial',release_date='2026-11-02',company='Infinitum Corporation',location='Washington, DC',contact_name='William Aaron Turner',contact_email='theinfinitumcorp+pressbox@gmail.com',source_url=r['source'],responsibility_accepted='yes')
x=s.post('https://pressbox.com/press-releases/submit',data=d,timeout=60)
open('/tmp/pbpass.html','w').write(x.text)
for f in re.findall(r'<form.*?</form>',x.text,re.S):
    print(re.search(r'<form[^>]*>',f).group(0))
    for m in re.finditer(r'<(?:input|textarea|select|button)[^>]*>',f): print('  ',m.group(0)[:160])
i=x.text.find('QUALITY CHECK'); print(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',x.text[i-300:i+2500])))
