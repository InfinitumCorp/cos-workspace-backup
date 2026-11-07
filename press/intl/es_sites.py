import sys,html as H;from common import *
site=sys.argv[1]; slugs=sys.argv[2:]
def RE():
    try: return {r['slug']:r for r in json.load(open('releases_es.json'))}
    except Exception: return {}
def columna(r):
    s=requests.Session();s.headers.update(UA)
    s.get('https://columnadigital.com/prensa/',timeout=30); time.sleep(30)
    d=dict(nombre='William Aaron Turner',organizacion='Infinitum Corporation',email='info@theinfinitumcorporation.com',telefono='+1 202-729-9509',
      asunto=r['title'],embargo='',texto=r['summary']+'\n\n'+full(r,'es'),website='',consent='on')
    i=img(r); x=s.post('https://columnadigital.com/prensa/enviar',data=d,files={'archivos':i} if i else None,timeout=60,headers={'Referer':'https://columnadigital.com/prensa/'})
    t=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style).*?</\1>','',x.text,flags=re.S)))
    return x.status_code,x.url,t[:300]
def valencia(r):
    s=requests.Session();s.headers.update(UA)
    s.get('https://valenciaya.com/enviar-comunicado/',timeout=30); t0=int(time.time()*1000); time.sleep(45)
    body=''.join('<p>'+H.escape(p).replace('\n','<br>')+'</p>' for p in full(r,'es').split('\n\n'))
    d=dict(title=r['title'],excerpt=r['summary'],company='Infinitum Corporation',website='https://www.theinfinitumcorporation.com',contact_name='William Aaron Turner',
      contact_email='info@theinfinitumcorporation.com',phone='+1 202-729-9509',web='',consent='1',domain='valenciaya.com',t=str(t0),body=body,body_format='html')
    x=s.post('https://valenciaya.com/api/submit-release/',data=d,files={'image':img(r,True)},timeout=60,headers={'Referer':'https://valenciaya.com/enviar-comunicado/','Origin':'https://valenciaya.com'})
    return x.status_code,x.url,x.text[:300]
F={'columna':columna,'valencia':valencia}[site]
done=set()
while True:
    E=RE(); todo=[s for s in slugs if s in E and s not in done]
    if not todo:
        if len(done)==len(slugs): break
        time.sleep(60); continue
    r=E[todo[0]]; c,u,t=F(r); done.add(r['slug'])
    print(r['slug'],c,t,flush=True); log({'columna':'ColumnaDigital','valencia':'ValenciaYa'}[site],r['slug'],f'{c} {t[:120]}')
    if c>=400 or ('ok' not in t.lower() and 'gracias' not in t.lower() and 'recib' not in t.lower()): print('STOP');break
    time.sleep(120)
