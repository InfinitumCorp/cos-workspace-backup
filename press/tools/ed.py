D='/workspace/press/batch-2026-10-31/'
def rep(f,a,b):
    p=D+f; t=open(p).read(); assert t.count(a)==1,(f,a[:50],t.count(a)); open(p,'w').write(t.replace(a,b))
def before(f,marker,text): rep(f,marker,text.strip()+'\n\n'+marker)
def wc(f):
    t=open(D+f).read(); b=t.split('BODY:')[1].split('About Infinitum Corporation')[0]; return len(b.split())
