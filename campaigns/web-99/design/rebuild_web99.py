#!/usr/bin/env python3
"""$99 AI-enhanced website promo: flyer (letter @300dpi) + social cards. Local only, no watermark."""
import importlib.util
from pathlib import Path
from PIL import Image, ImageDraw
R=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('h','/workspace/academia-promo/flyer-gen/make_flyers.py')
h=importlib.util.module_from_spec(s);s.loader.exec_module(h)
RED=(200,16,32)
mark=Image.open('/workspace/brand/infinitum-mark-white-transparent.png').convert('RGBA')
def render(w,ht,name):
 k=w/1200 if w!=1080 else 1080/1200
 if w==2550:k=2.125
 m=int(60*k);im=Image.new('RGB',(w,ht),h.BG);d=ImageDraw.Draw(im)
 ms=int(56*k);mk=mark.copy();mk.thumbnail((ms,ms));im.paste(mk,(m,int(42*k)),mk)
 d.text((m+ms+int(16*k),int(57*k)),'Infinitum Corporation®',font=h.inter(int(28*k),600),fill=h.WHITE,anchor='lt')
 d.line((m,int(110*k),w-m,int(110*k)),fill=h.RULE,width=max(2,int(2*k)))
 # vertical layout scales with height
 y=int(ht*(0.22 if ht>w else 0.27 if ht==w else 0.215))
 d.text((m,y),'CYBER  /  WEB SERVICES',font=h.inter(int(21*k),500),fill=h.GREY,anchor='lt');y+=int(50*k)
 big=int((92 if ht>=w else 76)*k)
 for t in ['AI-enhanced','websites.']:
  d.text((m,y),t,font=h.osw(big),fill=h.WHITE,anchor='lt');y+=int(big*1.15)
 if w>ht: d.text((w-m,int(ht*0.30)),'$99.',font=h.osw(int(190*k)),fill=RED,anchor='rt');y+=int(12*k)
 else: d.text((m,y),'$99.',font=h.osw(big),fill=RED,anchor='lt');y+=int(big*1.25)
 d.rectangle((m,y,m+int(110*k),y+int(5*k)),fill=RED);y+=int(32*k)
 d.text((m,y),'Rework or new site',font=h.inter(int(34*k),500),fill=h.GREY,anchor='lt')
 fy=ht-int(52*k)-int(23*k)
 d.text((m,fy-int(70*k)),'Get started: info@theinfinitumcorporation.com',font=h.inter(int(24*k),600),fill=h.WHITE,anchor='lt')
 d.line((m,fy-int(22*k),w-m,fy-int(22*k)),fill=h.RULE,width=max(2,int(2*k)))
 d.text((m,fy),'202-729-9509',font=h.inter(int(23*k),400),fill=h.WHITE,anchor='lt')
 d.text((w-m,fy),'Washington, DC',font=h.inter(int(23*k),400),fill=h.WHITE,anchor='rt')
 p=R/name;im.save(p,dpi=(300,300) if w==2550 else (72,72));return p
out=[render(1200,627,'web99-card-1200x627.png'),render(1080,1080,'web99-card-1080x1080.png'),render(2550,3300,'web99-flyer-letter-2550x3300.png')]
Image.open(out[2]).save(R/'web99-flyer-letter.pdf',resolution=300)
sh=Image.new('RGB',(1700,1100),(225,225,225))
for p,(x,yy,tw) in zip(out,[(20,20,800),(20,460,560),(850,20,820)]):
 t=Image.open(p);t.thumbnail((tw,1060));sh.paste(t,(x,yy))
sh.save(R/'contact-sheet.png');print(*out,sep='\n')
