import sys;from tr_common import *
done=set(l.split('\t')[2] for l in open('log.tsv') if '\tColumnaDigital-native\t' in l and '200' in l)
for slug in sys.argv[1:]:
    while load_tr('es',slug) is None: time.sleep(60)
    if slug in done: continue
    r=load_tr('es',slug)
    s=requests.Session();s.headers.update(UA); s.get('https://columnadigital.com/prensa/',timeout=30); time.sleep(30)
    d=dict(nombre='William Aaron Turner',organizacion='Infinitum Corporation',email='info@theinfinitumcorporation.com',telefono='+1 202-729-9509',asunto=r['title'][:250],embargo='',texto=r['summary']+'\n\n'+r['full'],website='',consent='on')
    x=s.post('https://columnadigital.com/prensa/enviar',data=d,files={'archivos':img(r,True)},headers={'Accept':'application/json','Referer':'https://columnadigital.com/prensa/'},timeout=60)
    print(slug,x.status_code,x.text[:200],flush=True); log('ColumnaDigital-native',slug,f'{x.status_code} {x.text[:100]}')
    if x.status_code!=200: break
    time.sleep(150)
