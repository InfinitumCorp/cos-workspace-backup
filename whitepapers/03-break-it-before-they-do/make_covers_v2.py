from PIL import Image, ImageDraw, ImageFont
P="/usr/share/fonts/truetype/sand-box/google/Poppins/Poppins-"
def F(w,s): return ImageFont.truetype(P+w+".ttf",max(8,int(s)))
RED=(200,16,32)
def mk(c):
    m=Image.open(f"/workspace/brand/infinitum-mark-{c}-transparent.png").convert("RGBA"); return m.crop(m.getbbox())
MARK={"white":mk("black"),"black":mk("white")}
TH={"white":dict(bg=(255,255,255),grid=(246,246,246),fg=(14,14,14),sub=(55,55,55),gry=(105,105,105)),
    "black":dict(bg=(12,12,12),grid=(24,24,24),fg=(250,250,250),sub=(205,205,205),gry=(140,140,140))}
TITLE="Break It Before They Do"; SUB="Authorized Hacking for Organizations Under Siege"; SUB2=""
def wrap(d,t,f,mw):
    out,line=[],""
    for w in t.split():
        x=(line+" "+w).strip()
        if d.textlength(x,font=f)<=mw: line=x
        else: out.append(line); line=w
    return out+[line]
def put(d,x,y,t,f,fill,mw,g=1.15):
    for l in wrap(d,t,f,mw): d.text((x,y),l,font=f,fill=fill); y+=f.size*g
    return y
def base(W,H,th):
    t=TH[th]; im=Image.new("RGB",(W,H),t["bg"]); d=ImageDraw.Draw(im); s=max(24,min(W,H)//14)
    for x in range(0,W,s): d.line([(x,0),(x,H)],fill=t["grid"])
    for y in range(0,H,s): d.line([(0,y),(W,y)],fill=t["grid"])
    return im,d,t
def header(im,d,t,th,u,x0,y0,x1):
    m=MARK[th]; m=m.resize((int(m.width*u*1.1/m.height),int(u*1.1)),Image.LANCZOS); im.paste(m,(int(x0),int(y0)),m)
    lab="I N F I N I T U M   C O R P O R A T I O N"; f=F("Medium",u*0.42)
    tx=x0+m.width+u*0.5; d.text((tx,y0+m.height/2),lab,font=f,fill=t["fg"],anchor="lm")
    e=tx+d.textlength(lab,font=f)+u*0.6
    if e<x1-u: d.line([(e,y0+m.height/2),(x1,y0+m.height/2)],fill=t["fg"],width=max(1,int(u*0.04)))
def cover(th):
    W,H=1700,2200; u=64; m=150; im,d,t=base(W,H,th)
    header(im,d,t,th,u,m,m,W-m)
    y=H*0.36; d.text((m,y),"WHITEPAPER NO. 3",font=F("SemiBold",u*0.45),fill=RED); y+=u*0.95
    y=put(d,m,y,TITLE,F("Bold",u*2.4),t["fg"],W-2*m)
    y=put(d,m,y+u*0.15,SUB,F("Medium",u*0.85),t["fg"],W-2*m)
    y=put(d,m,y+u*0.1,SUB2,F("Regular",u*0.65),t["sub"],W-2*m)
    y+=u*0.45; d.rectangle([m,y,m+u*3,y+u*0.12],fill=RED)
    rf=F("Regular",u*0.42)
    d.text((W-m,H-m-u*1.7),"William Aaron Turner, Founder & President",font=rf,fill=t["gry"],anchor="rs")
    d.text((W-m,H-m-u*1.0),"Infinitum Corporation, Washington, DC",font=rf,fill=t["gry"],anchor="rs")
    d.text((m,H-m-u*1.7),"Whitepaper No. 3",font=F("SemiBold",u*0.55),fill=t["fg"],anchor="ls")
    d.text((m,H-m-u*0.95),"NOVEMBER 2026",font=F("Regular",u*0.38),fill=t["gry"],anchor="ls")
    d.rectangle([0,H-14,W,H],fill=RED)
    im.save(f"assets/cover-v2-{th}.png"); im.save(f"assets/cover-v2-{th}.jpg",quality=93,dpi=(300,300))
def post(th):
    W,H=1200,627; u=H/16; m=u*1.6; im,d,t=base(W,H,th)
    header(im,d,t,th,u,m,m*0.8,W-m)
    y=H*0.27; d.text((m,y),"WHITEPAPER NO. 3  ·  NOVEMBER 2026",font=F("SemiBold",u*0.45),fill=RED); y+=u*0.9
    y=put(d,m,y,TITLE,F("Bold",u*2.0),t["fg"],W-2*m)
    y=put(d,m,y+u*0.1,SUB,F("Medium",u*0.8),t["fg"],W-2*m)
    y=put(d,m,y+u*0.05,SUB2,F("Regular",u*0.6),t["sub"],W-2*m)
    y+=u*0.35; d.rectangle([m,y,m+u*3,y+u*0.12],fill=RED)
    d.rectangle([0,H-6,W,H],fill=RED)
    d.text((m,H-u*1.1),"William Aaron Turner, Founder & President  ·  Infinitum Corporation, Washington, DC",font=F("Regular",u*0.4),fill=t["gry"],anchor="ls")
    im.save(f"assets/post-03-v2-{th}-1200x627.png")
for th in ("white","black"): cover(th); post(th)
