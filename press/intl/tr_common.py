import os
from common import *
TD='/workspace/press/intl/translations/'
def load_tr(lang,slug):
    p=f'{TD}{lang}/{slug}.txt'
    if not os.path.exists(p): return None
    t=open(p).read().strip(); parts=t.split('\n\n')
    title,summ,body=parts[0].strip(),parts[1].strip(),'\n\n'.join(parts[2:]).strip()
    foot=open(f'{TD}{lang}/_footer.txt').read().strip()
    r=[x for x in R if x['slug']==slug][0]
    return dict(slug=slug,title=title,summary=summ,body=body,full=body+'\n\n'+foot,image=r['image'])
