#!/usr/bin/env python3
"""Local-only campaign cards; retypeset source titles without cropping existing covers.
Style helpers reused from the existing Academia flyer generator. No source is modified.
"""
import json, importlib.util
from pathlib import Path
from PIL import Image, ImageDraw
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('house','/workspace/academia-promo/flyer-gen/make_flyers.py')
house=importlib.util.module_from_spec(spec);spec.loader.exec_module(house)
papers=json.loads(Path('/workspace/campaigns/techpapers/papers.json').read_text())
slugs=['dead-reckoning','trenches-and-drones','corporate-cognitive-warfare','battlefield-cyber-hygiene','counter-drone-handbook','reconnaissance-fusion-handbook','decentralized-disinformation']
subtitles=[
'AI security operations, governance and cyber defense for mid-size organizations.',
'Defense in depth, segmentation and cyber resilience through a battlefield lens.',
'Irregular-warfare concepts applied to corporate competition and communications risk.',
'Digital hygiene and OPSEC for personnel in contested environments.',
'Defending against unmanned aircraft systems at unit level.',
'Fusing FPV drone, social media and open-source intelligence.',
'How organic narratives spread and are exploited in influence operations.'
]
sources=[
'/workspace/whitepapers/01-ai-for-security-operations/assets/cover-hi.png',
'/workspace/whitepapers/02-trenches-and-drones/assets/cover-v2-black.png',
'/workspace/whitepapers/corporate-cognitive-warfare/cover.jpg',
'/workspace/academia-promo/flyers/19-battlefield-cyber-hygiene.png',
'/workspace/academia-promo/flyers/18-counter-drone-handbook.png',
'/workspace/academia-promo/flyers/16-reconnaissance-fusion.png',
'/workspace/academia-promo/flyers/17-decentralized-disinformation.png']
manifest=[]
checks=[]
def block(d,text,x,y,width,height,start,minimum,font,fill):
 for sz in range(start,minimum-1,-1):
  f=font(sz); lines=house.wrap(d,text,f,width); lh=round(sz*1.25)
  if font is house.osw and len(lines)>1 and d.textlength(lines[-1],font=f)<width*.28:
   for candidate_width in range(width-15,int(width*.65),-15):
    candidate=house.wrap(d,text,f,candidate_width)
    if len(candidate)*lh<=height and d.textlength(candidate[-1],font=f)>=width*.28:
     lines=candidate;break
   else:continue
  if len(lines)*lh<=height and all(d.textlength(t,font=f)<=width for t in lines):break
 else:raise ValueError('Cannot fit '+text)
 for line in lines:
  d.text((x,y),line,font=f,fill=fill,anchor='lt');y+=lh
 return sz,len(lines),y
for p,slug,sub,source in zip(papers,slugs,subtitles,sources):
 assert Path(source).exists(),source
 row={'id':p[0],'title':p[1],'subtitle':sub,'source_cover_or_flyer':source,'files':[]}
 for w,h in [(1200,627),(1080,1080)]:
  square=h==1080;m=60;live=w-2*m
  im=Image.new('RGB',(w,h),house.BG);d=ImageDraw.Draw(im)
  d.text((m,57),'Infinitum Corporation®',font=house.inter(28,600),fill=house.WHITE,anchor='lt')
  d.line((m,105,w-m,105),fill=house.RULE,width=2)
  d.text((m,124),'RESEARCH PAPER  /  '+p[0],font=house.inter(19,500),fill=house.GREY,anchor='lt')
  title_y=183 if square else 167
  title_h=410 if square else 220
  ts,n,end=block(d,p[1],m,title_y,live,title_h,82 if square else 65,38,house.osw,house.WHITE)
  bar_y=title_y+title_h+12
  d.rectangle((m,bar_y,m+110,bar_y+5),fill=house.WHITE)
  sy=bar_y+30
  ss,sn,se=block(d,sub,m,sy,live,116 if square else 70,32 if square else 28,24,house.inter,house.GREY)
  ay=850 if square else 510
  assert se<ay-18,(slug,se,ay)
  d.text((m,ay),'William Aaron Turner',font=house.inter(27,600),fill=house.WHITE,anchor='lt')
  d.text((m,ay+37),'Founder & President  ·  Washington, DC',font=house.inter(24,400),fill=house.GREY,anchor='lt')
  fy=975 if square else 588
  d.line((m,fy-20,w-m,fy-20),fill=house.RULE,width=2)
  d.text((m,fy),'info@theinfinitumcorporation.com',font=house.inter(23,400),fill=house.WHITE,anchor='lt')
  d.text((w-m,fy),'202-729-9509',font=house.inter(23,400),fill=house.WHITE,anchor='rt')
  name=f'{p[0].lower()}-{slug}-{w}x{h}.png';path=ROOT/name
  im.save(path,optimize=True);row['files'].append(str(path))
  checks.append({'file':str(path),'dimensions':[w,h],'title_font_px':ts,'title_lines':n,'subtitle_font_px':ss,'subtitle_lines':sn,'safe_layout':True})
 manifest.append(row)
for w,h in [(1200,627),(1080,1080)]:
 tw=600 if w==1200 else 432;th=round(h*tw/w); cols=2; rows=4
 sheet=Image.new('RGB',(cols*tw,rows*(th+38)),(225,225,225));d=ImageDraw.Draw(sheet)
 for i,row in enumerate(manifest):
  path=next(x for x in row['files'] if x.endswith(f'{w}x{h}.png'))
  thumb=Image.open(path).resize((tw,th),Image.Resampling.LANCZOS)
  x=(i%cols)*tw;y=(i//cols)*(th+38)
  sheet.paste(thumb,(x,y));d.text((x+10,y+th+7),row['id']+' / '+str(w)+'x'+str(h),font=house.inter(18),fill=(0,0,0))
 sheet.save(ROOT/f'contact-sheet-{w}x{h}.jpg',quality=95)
(ROOT/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
(ROOT/'layout-checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print('Rendered',len(checks),'cards and two contact sheets.')
