import sys,html as H;from common import *
s=requests.Session();s.headers.update(UA)
for r in [r for r in R if r['slug'] in sys.argv[1:]]:
    h=s.get('https://uaeinsider.net/submit-a-press-release/',timeout=30).text
    n=re.search(r'"nonce":"([^"]+)"',h).group(1)
    body=''.join('<p>'+H.escape(p).replace('\n','<br>')+'</p>' for p in (r['summary']+'\n\n'+full(r)).split('\n\n'))
    d=dict(nonce=n,_wp_http_referer='/submit-a-press-release/',full_name='William Aaron Turner',company='Infinitum Corporation',email='info@theinfinitumcorporation.com',
      phone='+1 202-729-9509',title=r['title'],content=body,website='https://www.theinfinitumcorporation.com',action='prs_submit_press_release')
    i=img(r); x=s.post('https://uaeinsider.net/wp-admin/admin-ajax.php',data=d,files={'featured_image':i} if i else None,timeout=60)
    print(r['slug'],x.status_code,x.text[:200],flush=True); log('UAEInsider',r['slug'],f'{x.status_code} {x.text[:120]}')
    if '"success":true' not in x.text: break
    time.sleep(120)
