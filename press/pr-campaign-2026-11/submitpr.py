import requests,re,sys,datetime
from releases import R
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36'}
for k in sys.argv[1:]:
    r=R[k]; s=requests.Session(); s.headers.update(UA)
    h=s.get('https://submitpr.org/submit',timeout=30).text
    tok=re.search(r'name="csrf_token" value="([^"]+)"',h).group(1)
    d=dict(csrf_token=tok,selected_plan='free',linkback_url='',title=r['title'],custom_slug=r['slug'][:120],summary=r['summary'],body=r['full'],category_id=r['category_spr'],keywords=r['keywords'],company_name='Infinitum Corporation',company_website='https://www.theinfinitumcorporation.com',company_phone='202-729-9509',company_address='1629 K Street NW, Suite 300',city='Washington',state='DC',country='United States',author_name='William Aaron Turner',author_email='theinfinitumcorp+press@gmail.com',source_url=r['source'],agree_terms='1',image_alt='',image_caption='')
    files=None
    if k=='ccw':
        files={'pr_image':('flyer.png',open('/workspace/whitepapers/corporate-cognitive-warfare/flyer.png','rb'),'image/png')}
        d['image_alt']='Corporate Cognitive Warfare Expanded Edition white paper by William Aaron Turner'
    else: files={'_x':('', b'')}
    resp=s.post('https://submitpr.org/submit',data=d,files=files if k=='ccw' else None,timeout=60,allow_redirects=True)
    t=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    open(f'/tmp/spr-{k}.html','w').write(resp.text)
    err=re.findall(r'class="[^"]*(?:error|alert)[^"]*"[^>]*>([^<]{3,200})',resp.text)
    print(k,t,resp.status_code,resp.url,err[:3])
