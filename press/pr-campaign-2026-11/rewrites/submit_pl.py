import sys,re,requests
sys.path.insert(0,'/workspace/press/tools');sys.path.insert(0,'.')
from pl_edit import form
from data import R,Q
BP=open('/workspace/press/boilerplate.md').read().strip().split(' | Telegram')[0]
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36'}
def txt(h): return re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style)[^>]*>.*?</\1>','',h,flags=re.S)))
def go(slug):
    r=[x for x in R if x['slug']==slug][0]
    s=requests.Session();s.headers.update(UA);s.get('https://pressliftoff.com/submit',timeout=30)
    det=r['details']+"\n\nRead the original: "+r['orig']
    d=dict(edit_token='',existing_image_url='',is_boosted='0',boost_unlocked='0',original_created_at='',publish_choice='free',
      headline=r['title'],summary=r['summary'],dateline_city='Washington',dateline_state='DC',dateline_country='United States',
      body_intro=r['intro'],body_details=det,quote_text=r['quote'],quote_attribution=Q,boilerplate=BP,category='Business',category2='',
      keywords=r['keywords'][:250],image_alt=r['cover'][0]+' - Infinitum Corporation cover',image_caption=r['cover'][0],publish_at_local='',tz_offset='-180',video_url='',
      link1_label='Read the original ('+r['olabel']+')',link1_url=r['orig'],link2_label='',link2_url='',
      company_name='Infinitum Corporation',company_website='https://www.theinfinitumcorporation.com',company_phone='202-729-9509',
      company_address='1629 K Street NW, Suite 300, Washington, DC 20006',contact_name='William Aaron Turner',contact_email='info@theinfinitumcorporation.com',
      source_url=r['orig'],heard_from='other',agree_terms='on')
    for i in range(4): d[f'faq_q{i}']='';d[f'faq_a{i}']=''
    for i in (1,2,3): d[f'existing_extra_image_{i}']='';d[f'extra_alt_{i}']=''
    p=s.post('https://pressliftoff.com/api/preview',data=d,files={'image':(slug+'.jpg',open('img/'+slug+'.jpg','rb'),'image/jpeg')},timeout=90)
    d2=form(p.text,'/api/publish')
    if not d2:
        t=txt(p.text);i=max(t.find('Slow'),t.find('rror'),0);return 'PREVIEW FAIL %d: %s'%(p.status_code,t[i:i+400])
    assert d2.get('publish_choice')=='free' and d2.get('is_boosted','0')=='0',d2.get('publish_choice')
    q=s.post('https://pressliftoff.com/api/publish',data=d2,timeout=90)
    open(f'/tmp/plpub-{slug}.html','w').write(q.text)
    t=txt(q.text);links=set(re.findall(r'https://pressliftoff\.com/(?:press-release|edit)/[A-Za-z0-9-]+',q.text))|set(re.findall(r'/(?:press-release|edit)/[A-Za-z0-9-]+',q.text))
    i=t.find('Privacy Policy');return 'PUBLISH %d %s :: %s :: %s'%(q.status_code,q.url,t[i+15:i+500],links)
if __name__=='__main__': print(sys.argv[1],'->',go(sys.argv[1]))
