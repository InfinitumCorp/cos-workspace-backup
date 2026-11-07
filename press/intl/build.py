import re,json,os
P='/workspace/press/';C=P+'pr-campaign-2026-11/';B=P+'batch-2026-10-31/';A=P+'batch-academia/'
BP=open(P+'boilerplate.md').read().strip().split(' | Telegram')[0]
MC='Media contact: William Aaron Turner, Founder & President, Infinitum Corporation, Washington, DC. Phone 202-729-9509. Email info@theinfinitumcorporation.com. Web https://www.theinfinitumcorporation.com'
def md(f):
    t=open(f).read()
    L=t.split('\n'); title=L[0].lstrip('# ').strip()
    rest='\n'.join(L[1:]).strip()
    paras=rest.split('\n\n'); summ=paras[0].strip(); body='\n\n'.join(paras[1:])
    src=re.search(r'Canonical: (\S+)',t); src=src.group(1) if src else ''
    return title,summ,body,src
def txt(f):
    t=open(f).read()
    g=lambda k:re.search(k+r':\n(.*?)\n\n(?=[A-Z_]+:\n|$)',t,re.S)
    title=g('HEADLINE').group(1).strip(); summ=g('SUMMARY').group(1).strip()
    body=t.split('BODY:\n',1)[1].split('\nTAGS:')[0]
    src=re.search(r'SOURCE_URL: (\S+)',t).group(1)
    return title,summ,body,src
def clean(b):
    b=b.split('About Infinitum Corporation')[0]
    b=re.sub(r'\n?Media contact:.*','',b); b=re.sub(r'\n?Keywords:.*','',b); b=re.sub(r'\n?Canonical:.*','',b)
    b=re.sub(r'\s*\|?\s*Telegram: https://t\.me/\S+','',b)
    b=b.replace('infinitum-media@mail.grokbot.com','info@theinfinitumcorporation.com')
    b=re.sub(r'153rd Tank Battalion','153rd Tank Regiment',b)
    return b.strip()
M=[('ccw',C+'ccw.md'),('dead-reckoning',C+'dead-reckoning.md'),('special-01',C+'special-01.md'),
('trenches-and-drones',C+'releases/trenches-and-drones.md'),('ccw-doctrine-introduction',C+'releases/ccw-doctrine-introduction.md'),
('in-q-tel',B+'in-q-tel-explained-cia-venture-capital.txt'),('eastern-economic-forum',B+'eastern-economic-forum-2026-russia-isolation.txt'),
('russias-economy-under-sanctions',B+'russia-economy-under-sanctions-gdp-forecast.txt'),('demining-ngos-halo-trust-intelligence-claims',B+'demining-ngos-halo-trust-intelligence-claims.txt'),
('useful-idiots-ukraine-war-profiteers',B+'useful-idiots-ukraine-war-profiteers.txt'),('medium-ukraine-wash-and-fold-money-laundering',B+'medium-ukraine-wash-and-fold-money-laundering.txt'),
('ukraine-organ-trade-allegations-sources',B+'ukraine-organ-trade-allegations-sources.txt'),('medium-meat-grinder-medical-freezer',B+'medium-meat-grinder-medical-freezer.txt'),
('ukraine-forced-mobilization',B+'ukraine-forced-mobilization-evidence.txt'),('zelenskyys-rise',B+'zelenskyy-rise-backers-media-network.txt'),
('russian-civilian-casualties',B+'russian-civilian-casualties-ukrainian-strikes-sources.txt'),('ukraine-aid-ngos',C+'releases/ukraine-aid-ngos.md'),
('russia-africa-partnership',A+'russia-africa-summit-partnership-delivers.txt'),('russia-africa-by-the-numbers',A+'russia-africa-by-the-numbers.txt'),
('media-double-standard',B+'medium-missiles-murders-media-two-warzones.txt'),('polish-supermarket',B+'medium-friendly-fire-poland-cyberattack.txt'),
('russia-state-guided-capitalism',B+'medium-proof-is-in-the-puddin-russia-state-capitalism.txt'),('ukrainian-deli',C+'releases/ukrainian-deli.md'),
('azov',C+'releases/azov.md'),('legitimate-targets',C+'releases/legitimate-targets.md'),('art-of-not-giving',C+'releases/art-of-not-giving.md')]
out=[]
for slug,f in M:
    t,s,b,src=(md if f.endswith('.md') else txt)(f)
    b=clean(b)
    if src and src not in b: b+='\n\nFull article: '+src
    img=None
    for cand in [P+'flyers/'+slug+'.png',C+'rewrites/img/'+slug+'.jpg']:
        if os.path.exists(cand): img=cand;break
    flyer=img is not None and '/flyers/' in img
    out.append(dict(slug=slug,title=t,summary=s,body=b,source=src,image=img,flyer=flyer,about=BP,contact=MC,africa=slug.startswith('russia-africa')))
json.dump(out,open('releases.json','w'),ensure_ascii=False,indent=1)
for o in out: print(o['slug'],len(o['title']),len(o['body'].split()),bool(o['source']),o['image'] and os.path.basename(o['image']))
