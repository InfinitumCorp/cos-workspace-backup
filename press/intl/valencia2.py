import sys,html as H;from tr_common import *
done=set(l.split('\t')[2] for l in open('log.tsv') if '\tValenciaYa-native\t' in l)
for slug in sys.argv[1:]:
    while load_tr('es',slug) is None: time.sleep(60)
    if slug in done: continue
    r=load_tr('es',slug)
    s=requests.Session();s.headers.update(UA); s.get('https://valenciaya.com/enviar-comunicado/',timeout=30); t0=int(time.time()*1000); time.sleep(60)
    bh=''.join('<p>'+H.escape(p).replace('\n','<br>')+'</p>' for p in r['full'].split('\n\n'))
    d=dict(title=r['title'][:200],excerpt=r['summary'],company='Infinitum Corporation',website='https://www.theinfinitumcorporation.com',contact_name='William Aaron Turner',contact_email='info@theinfinitumcorporation.com',phone='+1 202-729-9509',web='',consent='1',domain='valenciaya.com',t=str(t0),body=bh,body_format='html')
    x=s.post('https://valenciaya.com/api/submit-release/',data=d,files={'image':img(r,True)},headers={'Referer':'https://valenciaya.com/enviar-comunicado/','Origin':'https://valenciaya.com'},timeout=60)
    print(slug,x.status_code,x.text[:150],flush=True); log('ValenciaYa-native',slug,f'{x.status_code} {x.text[:100]}')
    if '"ok":true' not in x.text: break
    time.sleep(150)
