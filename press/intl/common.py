import json,re,requests,time,datetime,mimetypes,os
R=json.load(open('/workspace/press/intl/releases.json'))
FALLBACK='/workspace/press/pr-campaign-2026-11/flyer.jpg'
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130 Safari/537.36'}
def full(r,lang='en',sep='\n\n'):
    if lang=='en': return r['body']+sep+'About Infinitum Corporation'+sep+r['about']+sep+r['contact']
    return r['body']+sep+r['about_h']+sep+r['about']+sep+r['contact']
def img(r,required=False):
    p=r['image'] or (FALLBACK if required else None)
    if not p: return None
    return (os.path.basename(p),open(p,'rb'),mimetypes.guess_type(p)[0])
def log(site,slug,status,url=''):
    with open('/workspace/press/intl/log.tsv','a') as f:
        f.write('\t'.join([datetime.datetime.now().strftime('%Y-%m-%d %H:%M'),site,slug,status,url])+'\n')
def excerpt(r,limit,lang='en'):
    tail='\n\n'+('Full article: ' if lang=='en' else r.get('full_h','Full article: '))+r['source']+'\n\n'+r['contact']
    out=''
    for p in r['body'].split('\n\n'):
        if p.strip().startswith(('Full article','Infinitum Corporation: http','Artículo completo','Article complet')): continue
        if len(out)+len(p)+2+len(tail)>limit: break
        out+=('\n\n' if out else '')+p
    return out+tail
