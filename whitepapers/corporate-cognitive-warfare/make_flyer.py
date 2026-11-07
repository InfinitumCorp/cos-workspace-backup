from PIL import Image, ImageDraw, ImageFont, ImageOps
import os, shutil
os.makedirs("assets",exist_ok=True)
P="/usr/share/fonts/truetype/sand-box/google/Poppins/Poppins-"
def F(w,s): return ImageFont.truetype(P+w+".ttf",max(8,int(s)))
NAVY=(0x1A,0x36,0x5D); BLK=(14,14,14); GRY=(100,100,100)
logo=Image.open("/workspace/brand/hires/infinitum-logo-stacked-black-on-white-4000.jpg").convert("L")
bbox=ImageOps.invert(logo).getbbox(); logo=logo.crop(bbox)
# use luminance as alpha so it sits cleanly on white without a box
LA=Image.new("RGBA",logo.size,BLK+(0,)); LA.putalpha(ImageOps.invert(logo))
def L(h): return LA.resize((int(LA.width*h/LA.height),int(h)),Image.LANCZOS)
BY='"Corporate Cognitive Warfare," a term coined by William Aaron Turner, Founder & President, Infinitum Corporation'
LINES=["Military doctrine, presented neutrally: reflexive control and cognitive domain operations",
       "Five lawful disciplines and twelve use cases",
       "A defensive playbook against disinformation, fake reviews and deepfakes"]
CONTACT="theinfinitumcorporation.com  ·  info@theinfinitumcorporation.com  ·  t.me/infinitumcorporation  ·  x.com/infinitumceo"
READ="Read on Academia.edu  ·  DOI 10.5281/zenodo.23838097"
def wrap(d,t,f,mw):
    out,line=[],""
    for w in t.split():
        x=(line+" "+w).strip()
        if d.textlength(x,font=f)<=mw: line=x
        else: out.append(line); line=w
    return out+[line]
def put(d,x,y,t,f,fill,mw,gap=1.2):
    for l in wrap(d,t,f,mw): d.text((x,y),l,font=f,fill=fill); y+=f.size*gap
    return y
def card(W,H,u,nlines,path,logo_h,title_s,contact=True,y0=0):
    im=Image.new("RGB",(W,H),(255,255,255)); d=ImageDraw.Draw(im); m=u*1.6
    d.rectangle([0,0,W,u*0.22],fill=NAVY)
    lg=L(logo_h); im.paste(lg,(int(W-m-lg.width),int(m)),lg)
    y=m+u*0.2+y0; mw=W-2*m-lg.width-u
    d.text((m,y),"WHITE PAPER  ·  EXPANDED EDITION",font=F("SemiBold",u*0.45),fill=NAVY); y+=u*0.95
    tf=F("Bold",u*title_s); y=put(d,m,y,"Corporate Cognitive Warfare",tf,BLK,max(mw,W*0.6),1.12)
    y=put(d,m,y+u*0.1,"Irregular Warfare for Market Supremacy",F("Regular",u*0.8),(50,50,50),W-2*m)
    y+=u*0.35; d.rectangle([m,y,m+u*3,y+u*0.12],fill=NAVY); y+=u*0.6
    bf=F("Regular",u*0.5)
    for t in LINES[:nlines]:
        d.ellipse([m,y+bf.size*0.45,m+u*0.18,y+bf.size*0.45+u*0.18],fill=NAVY)
        y=put(d,m+u*0.5,y,t,bf,BLK,W-2*m-u*0.5)+u*0.15
    y+=u*0.2; y=put(d,m,y,BY,F("Medium",u*0.4),GRY,W-2*m)
    d.text((m,y+u*0.25),READ,font=F("SemiBold",u*0.42),fill=NAVY); im.endy=y+u*0.25+u*0.42*1.6
    d.rectangle([0,H-u*1.25,W,H],fill=NAVY)
    cf=F("Medium",u*0.36)
    ct=CONTACT if d.textlength(CONTACT,font=cf)<W-2*m else "theinfinitumcorporation.com  ·  t.me/infinitumcorporation  ·  x.com/infinitumceo"
    d.text((W/2,H-u*0.62),ct,font=cf,fill=(255,255,255),anchor="mm")
    return im
card(1200,627,627/16.5,2,None,150,1.7).save("assets/flyer-ccw-expanded-1200x627.png")
card(1080,1080,1080/22,3,None,170,1.8,y0=150).save("assets/flyer-ccw-expanded-1080.png")
# Letter one-pager at 150 DPI with full Academia URL
im=card(1275,1650,1275/19,3,None,260,2.1,y0=330); d=ImageDraw.Draw(im); u=1275/22
url="academia.edu/179983771/Corporate_Cognitive_Warfare_Irregular_Warfare_for_Market_Supremacy_Whitepaper_Expanded_Edition_"
u=1275/19; uf=F("Regular",u*0.3); yy=im.endy+u*0.15
for i in range(0,len(url),70): d.text((u*1.6,yy),url[i:i+70],font=uf,fill=GRY); yy+=uf.size*1.3
im.save("assets/flyer-ccw-expanded-letter.pdf","PDF",resolution=150)
shutil.copy("assets/flyer-ccw-expanded-1200x627.png","flyer.png")
shutil.copy("assets/flyer-ccw-expanded-1080.png","flyer-1080.png")
shutil.copy("assets/flyer-ccw-expanded-letter.pdf","flyer.pdf")
