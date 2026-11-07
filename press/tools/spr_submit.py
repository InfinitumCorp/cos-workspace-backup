import requests,re,sys,time
D='/workspace/press/batch-2026-10-31/';F='/workspace/press/flyers/'
BP=open('/workspace/press/boilerplate.md').read().strip().split(' | Telegram')[0]
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) Chrome/130'}
def parse(slug):
    t=open(D+slug+'.txt').read()
    g=lambda k:re.search(k+r':\n(.*?)\n\n(?=[A-Z_]+:\n|$)',t,re.S)
    head=g('HEADLINE').group(1).strip(); summ=g('SUMMARY').group(1).strip()
    body=t.split('BODY:\n',1)[1].split('\nTAGS:')[0]
    body=body.split('About Infinitum Corporation')[0].rstrip()
    body=re.sub(r'\n?Media contact:.*','',body)
    body=re.sub(r'\s*\|?\s*Telegram: https://t\.me/\S+','',body)
    body+='\n\nAbout Infinitum Corporation\n\n'+BP
    tags=t.split('\nTAGS:\n',1)[1].strip() if '\nTAGS:\n' in t else ''
    src=re.search(r'SOURCE_URL: (\S+)',t).group(1)
    return head,summ,body,tags,src
def submit(slug):
    head,summ,body,tags,src=parse(slug)
    s=requests.Session();s.headers.update(UA)
    h=s.get('https://submitpr.org/submit',timeout=30).text
    tok=re.search(r'name="csrf_token" value="([^"]+)"',h).group(1)
    d=dict(csrf_token=tok,selected_plan='free',linkback_url='',agree_terms='1',title=head,summary=summ,body=body,category_id='1',
      company_name='Infinitum Corporation',company_website='https://www.theinfinitumcorporation.com',company_phone='202-729-9509',
      company_address='1629 K Street NW, Suite 300, Washington, DC 20006',city='Washington',state='DC',country='United States',
      author_name='William Aaron Turner',author_email='theinfinitumcorp+press@gmail.com',keywords=tags[:250],source_url=src,
      image_alt=head[:120],image_caption=head[:120],custom_slug='')
    fl={'pr_image':(slug+'.png',open(F+slug+'.png','rb'),'image/png')}
    r=s.post('https://submitpr.org/submit',data=d,files=fl,timeout=90,allow_redirects=True)
    return r
if __name__=='__main__':
    r=submit(sys.argv[1]); print(r.status_code,r.url)
    txt=re.sub(r'<[^>]+>',' ',r.text); txt=re.sub(r'\s+',' ',txt)
    for k in ['error','Error','success','Success','published','Slow','limit']:
        i=txt.find(k)
        if i>=0: print(k,'::',txt[max(0,i-150):i+250])
    print(set(re.findall(r'https://submitpr\.org/press-release/[a-z0-9-]+',r.text)))
