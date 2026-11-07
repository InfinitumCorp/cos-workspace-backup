import requests,re,spr_submit as S
slug='demining-ngos-halo-trust-intelligence-claims'
head,summ,body,tags,src=S.parse(slug)
main=body.split('\n\nAbout Infinitum Corporation')[0]
main=re.sub(r'^WASHINGTON, DC, [A-Za-z]+ \d+, \d{4} - ','',main)
intro,rest=main.split('\n\n',1)
s=requests.Session();s.headers.update(S.UA);s.get('https://pressliftoff.com/submit',timeout=30)
d=dict(headline=head,summary=summ,body_intro=intro,body_details=rest,boilerplate=S.BP,category='Business',keywords=tags[:250],
 company_name='Infinitum Corporation',company_website='https://www.theinfinitumcorporation.com',company_phone='202-729-9509',
 company_address='1629 K Street NW, Suite 300, Washington, DC 20006',contact_name='William Aaron Turner',contact_email='theinfinitumcorp+press@gmail.com',
 dateline_city='Washington',dateline_state='DC',dateline_country='United States',source_url=src,publish_choice='free',agree_terms='on',
 is_boosted='0',boost_unlocked='0',tz_offset='-180',image_alt=head[:120],image_caption=head[:120])
r=s.post('https://pressliftoff.com/api/preview',data=d,files={'image':(slug+'.png',open(S.F+slug+'.png','rb'),'image/png')},timeout=90)
print(r.status_code,r.url)
open('/tmp/plprev.html','w').write(r.text)
t=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style)[^>]*>.*?</\1>','',r.text,flags=re.S)))
print(t[:1200])
print(re.findall(r'<form[^>]*>',r.text))
