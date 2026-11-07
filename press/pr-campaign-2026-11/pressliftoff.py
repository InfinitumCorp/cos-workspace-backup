import requests,re
from releases import R
BP=open('/workspace/press/boilerplate.md').read().strip()
r=R['ccw']; s=requests.Session(); s.headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36'
s.get('https://pressliftoff.com/submit',timeout=30)
d=dict(edit_token='',existing_image_url='',is_boosted='0',boost_unlocked='0',original_created_at='',publish_choice='free',headline=r['title'],summary=r['summary'],dateline_city='Washington',dateline_state='DC',dateline_country='USA',body_intro=r['intro'],body_details=r['body_details'],quote_text=r['quote'],quote_attribution='William Aaron Turner, Founder & President, Infinitum Corporation',boilerplate=BP,category='Business',category2='Technology',keywords=r['keywords'],image_alt='Corporate Cognitive Warfare Expanded Edition flyer',image_caption='',publish_at_local='',tz_offset='-180',video_url='',link1_label='Zenodo (DOI)',link1_url='https://zenodo.org/records/23838097',link2_label='Academia.edu',link2_url='https://www.academia.edu/179983771/Corporate_Cognitive_Warfare_Irregular_Warfare_for_Market_Supremacy_Whitepaper_Expanded_Edition_',company_name='Infinitum Corporation',company_website='https://www.theinfinitumcorporation.com',company_phone='202-729-9509',company_address='1629 K Street NW, Suite 300, Washington, DC 20006',contact_name='William Aaron Turner',contact_email='theinfinitumcorp+press@gmail.com',source_url=r['source'],heard_from='other',agree_terms='on')
for i in range(4): d[f'faq_q{i}']='';d[f'faq_a{i}']=''
for i in (1,2,3): d[f'existing_extra_image_{i}']='';d[f'extra_alt_{i}']=''
f={'image':('flyer.png',open('/workspace/whitepapers/corporate-cognitive-warfare/flyer.png','rb'),'image/png')}
p=s.post('https://pressliftoff.com/api/preview',data=d,files=f,timeout=60)
open('/tmp/pl-prev.html','w').write(p.text)
print(p.status_code,p.url)
for m in re.finditer(r'<form[^>]*>',p.text): print(m.group(0))
for m in re.finditer(r'<input[^>]*type="hidden"[^>]*>',p.text): print(m.group(0)[:200])
t=re.sub(r'<script.*?</script>|<style.*?</style>','',p.text,flags=re.S);t=re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',t))
print(t[:1200])
