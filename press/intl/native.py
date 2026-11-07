import sys,html as H,pickle;from common import *
T='/workspace/press/pr-campaign-2026-11/translations/'
def load(f):
    t=open(T+f).read(); L=t.split('\n'); title=L[0].lstrip('# ').strip(); rest='\n'.join(L[1:]).strip().split('\n\n')
    summ=rest[0]; body='\n\n'.join(rest[1:])
    body=re.sub(r'\s*\|?\s*Telegram: https://t\.me/\S+','',body)
    body=re.sub(r'\n?(Contacto de prensa|Contact presse|Contact média)[^\n]*','',body)
    return title,summ,body.strip()
site=sys.argv[1]
if site=='valencia':
    title,summ,body=load('ccw-es.md'); body+='\n\nContacto de prensa: William Aaron Turner, fundador y presidente, Infinitum Corporation, Washington, DC. Teléfono 202-729-9509. info@theinfinitumcorporation.com. https://www.theinfinitumcorporation.com'
    s=requests.Session();s.headers.update(UA); s.get('https://valenciaya.com/enviar-comunicado/'); t0=int(time.time()*1000); time.sleep(60)
    bh=''.join('<p>'+H.escape(p).replace('\n','<br>')+'</p>' for p in body.split('\n\n'))
    d=dict(title=title[:200],excerpt=summ,company='Infinitum Corporation',website='https://www.theinfinitumcorporation.com',contact_name='William Aaron Turner',contact_email='info@theinfinitumcorporation.com',phone='+1 202-729-9509',web='',consent='1',domain='valenciaya.com',t=str(t0),body=bh,body_format='html')
    x=s.post('https://valenciaya.com/api/submit-release/',data=d,files={'image':img({'image':None},True)},headers={'Referer':'https://valenciaya.com/enviar-comunicado/','Origin':'https://valenciaya.com'})
    print(x.status_code,x.text[:200]); log('ValenciaYa','ccw (native ES, corrected)',f'{x.status_code} {x.text[:100]}')
if site=='libpress':
    title,summ,body=load('ccw-fr.md'); body=body.replace('Façonner','Modeler').replace('façonner','modeler'); summ=summ.replace('façonner','modeler'); body+='\n\nContact presse : William Aaron Turner, fondateur et président, Infinitum Corporation, Washington, DC. Téléphone 202-729-9509. info@theinfinitumcorporation.com'
    urls=re.findall(r'https?://\S+',body); keep=urls[0]
    for u in urls[1:]: body=body.replace(u,re.sub(r'^https?://(www\.)?','',u).split('/')[0] if len(u)>60 else re.sub(r'^https?://','',u))
    print('links kept:',keep)
    s=requests.Session();s.headers.update(UA);s.cookies=pickle.load(open('libpress.ck','rb'))
    h=s.get('https://libpress.fr/publier?offre=libre').text; tok=re.search(r'name="_csrf" value="([^"]+)"',h).group(1)
    btn=re.findall(r'<button[^>]*name="([^"]+)"[^>]*value="([^"]+)"',h); print(btn)
    d=dict(_csrf=tok,category='Tech',offer='libre',title=title[:255],excerpt=summ[:500],body=body,city='Washington',region='',website_url='https://www.theinfinitumcorporation.com',
      press_contact_name='William Aaron Turner',press_contact_phone='+1 202-729-9509',press_contact_email='info@theinfinitumcorporation.com',action='publish')
    for k,v in btn:
        if 'publi' in v.lower() or 'submit' in v.lower(): d[k]=v
    x=s.post('https://libpress.fr/publier',data=d,files={'cover':img({'image':None},True)},timeout=60)
    t=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style).*?</\1>','',x.text,flags=re.S)))
    print(x.status_code,x.url,t[:1500]); log('Libpress','ccw (native FR)',f'{x.status_code}',x.url)
