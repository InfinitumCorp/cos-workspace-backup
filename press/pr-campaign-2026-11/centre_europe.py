import requests,re,datetime
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36','Referer':'https://www.centre-europe.com/publier-un-communique-de-presse/'}
t=open('translations/ccw-fr.md').read().split('\n')
title="Corporate Cognitive Warfare, édition augmentée : l'étude de 15 000 mots de William Aaron Turner"
assert len(title)<=100,len(title)
body='\n'.join(t[2:]).strip()
s=requests.Session(); s.headers.update(UA)
s.get('https://www.centre-europe.com/publier-un-communique-de-presse/',timeout=30)
d=dict(nom='William Aaron Turner',email='theinfinitumcorp+press@gmail.com',entreprise='Infinitum Corporation',categorie='Tech',titre=title,contenu=body,lien='',mot_cle='',offre='gratuit')
f={'photo':('ccw-flyer.png',open('/workspace/whitepapers/corporate-cognitive-warfare/flyer.png','rb'),'image/png')}
r=s.post('https://centre-europe.com/communiques/soumettre.php',data=d,files=f,timeout=90)
open('/tmp/pr/ce-resp.html','w').write(r.text)
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),r.status_code,r.url,[h.url for h in r.history])
x=re.sub(r'<(script|style)[^>]*>.*?</\1>',' ',r.text,flags=re.S); x=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',x))
print(x[:800])
