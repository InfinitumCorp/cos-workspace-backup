import sys;sys.path.insert(0,'/workspace/wp-covers');sys.path.insert(0,'.')
from PIL import Image,ImageDraw
import importlib.util
src=open('/workspace/wp-covers/gen.py').read().split('W,H=1500,600')[0]
exec(src)
from data import R,Q
W,H=1500,600
def wrap(d,text,f,maxw):
    words=text.split();lines=[];cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t,font=f)<=maxw: cur=t
        else: lines.append(cur);cur=w
    lines.append(cur);return lines
BP=open('/workspace/press/boilerplate.md').read().strip()
for r in R:
    title,sub=r['cover']
    im=Image.new("RGB",(W,H),(255,255,255));d=ImageDraw.Draw(im);ink=(0,0,0)
    d.rectangle([0,0,W-1,H-1],outline=ink,width=2)
    d.text((80,52),"INFINITUM CORPORATION",font=font(INT,19,600),fill=ink)
    d.rectangle([80,92,W-80,93],fill=ink)
    tag="RESEARCH & ANALYSIS";lab=font(INT,17,500)
    d.text((W-80-d.textlength(tag,font=lab),56),tag,font=lab,fill=ink)
    size=104
    while True:
        tf=font(CG,size,700);lines=wrap(d,title,tf,W-160)
        if len(lines)<=2 or size<=60: break
        size-=6
    lh=int(size*1.02);sf=font(CGI,42,500);sl=wrap(d,sub,sf,W-300)
    y=110+(H-220-(lh*len(lines)+14+52*len(sl)))//2
    for l in lines: d.text((80,y),l,font=tf,fill=ink);y+=lh
    y+=14
    for l in sl: d.text((80,y),l,font=sf,fill=ink);y+=52
    d.rectangle([80,H-96,W-80,H-95],fill=ink);ff=font(INT,17,400)
    d.text((80,H-76),"William Aaron Turner  |  Founder & President, Infinitum Corporation",font=ff,fill=ink)
    t="theinfinitumcorporation.com";d.text((W-80-d.textlength(t,font=ff),H-76),t,font=ff,fill=ink)
    p=f"img/{r['slug']}.jpg";im.save(p,quality=93);r['image']='/workspace/press/pr-campaign-2026-11/rewrites/'+p
    md=f"""# {r['title']}

**Summary:** {r['summary']}

**Dateline:** WASHINGTON, DC, November 2, 2026

{r['intro']}

{r['details']}

"{r['quote']}" said {Q}.

**Read the original:** {r['orig']} ({r['olabel']})

## About Infinitum Corporation
{BP}

**Media contact:** William Aaron Turner, Infinitum Corporation, 202-729-9509, info@theinfinitumcorporation.com

---
Image: {r['image']} (neutral Infinitum cover, no watermark)
Keywords: {r['keywords']}
Replaces removed PressLiftoff URL: https://pressliftoff.com/press-release/{r['dead']} (410)
"""
    open(f"{r['slug']}.md",'w').write(md)
print(len(R))
