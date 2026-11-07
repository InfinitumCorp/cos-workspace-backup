import re,datetime,html,subprocess
from data import *
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,Image,PageBreak,KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from PIL import Image as PI
RED=colors.HexColor('#C8102E')
st={l.split()[1]:l.split()[0] for l in open('/tmp/checked.txt')}
SKIP=re.compile(r'(x\.com|t\.me|instagram|tiktok|linkedin|medium\.com|academia\.edu)')
def status(u):
    if not u: return 'no link yet'
    if SKIP.search(u): return 'live (not auto-checked)'
    c=st.get(u,'?')
    return {'200':'live','410':'REMOVED (410 Gone)','404':'NOT FOUND (404)','403':'live (site blocks checks)'}.get(c,c)
def xdate(i): return datetime.datetime.utcfromtimestamp(((int(i)>>22)+1288834974657)/1000).strftime('%Y-%m-%d')
xids=sorted({l.strip() for l in open('/tmp/xids.txt') if l.strip()},key=int)
tg=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,38,39]
# dedupe by url
seen=set();rows=[]
for it in items:
    k=it[4] or it[1]
    if k in seen: continue
    seen.add(k);rows.append(it)
order=[W,S,B,WP,A,HB,AC,PR,XA]
pending=[]
for l in open('/workspace/press/submissions/index.md'):
    if re.match(r'\|\s*\d+\s*\|',l):
        c=[x.strip() for x in l.strip().strip('|').split('|')]
        s=c[7] if len(c)>7 else ""
        if s.upper().startswith(('SENT','BOUNCED')) or 'already emailed' in s:
            outlet=re.sub(r'\s*\(.*','',c[1]).replace('-',' ').title().replace('Rt Op Ed','RT (op-ed)').replace('Riac','RIAC').replace('Cgtn','CGTN').replace('Mr Online','MR Online')
            subj=c[4] if c[4]!='—' else '(earlier email)'
            stt='bounced (not delivered)' if 'BOUNCED' in s.upper() else ('sent 31 Oct; awaiting reply' if s.upper().startswith('SENT') else 'sent earlier; awaiting reply')
            pending.append((outlet,subj,stt))
pending.append(('Unz Review','Article offer: Useful Idiots','sent 31 Oct; awaiting reply'))
pending.append(('OpEdNews','account registered','awaiting email confirmation; not posted'))
journals=[('MGIMO Review of International Relations','#4474','under review'),('Vestnik RUDN. International Relations','#53176','under review'),('Russia in Global Affairs','(emailed)','under review')]
# ---------- markdown/html ----------
md=['# Infinitum Corporation & William Aaron Turner — Published Works & Links','31 Oct 2026','']
for sec in order:
    rs=[r for r in rows if r[0]==sec]
    md+=[f'## {sec} ({sum(1 for r in rs if r[4])} links)','','| Title | Platform | Date | Link | Status |','|---|---|---|---|---|']
    md+=[f'| {r[1]} | {r[2]} | {r[3]} | {r[4]} | {status(r[4])}{"; "+r[5] if r[5] else ""} |' for r in rs]; md.append('')
md+=[f'## X posts by @infinitumceo ({len(xids)} links)','']+[f'- {xdate(i)} https://x.com/infinitumceo/status/{i}' for i in xids]+['']
md+=[f'## Telegram channel posts ({len(tg)} links)','']+[f'- https://t.me/infinitumcorporation/{n}' for n in tg]+['']
md+=['## Outlet submissions pending (no live links yet)','','| Outlet | Piece | Status |','|---|---|---|']+[f'| {a} | {b} | {c} |' for a,b,c in pending]+['']
md+=['## Journal submissions pending','','| Journal | Ref | Status |','|---|---|---|']+[f'| {a} | {b} | {c} |' for a,b,c in journals]+['']
md+=['## Not found / removed','']+[f'- {u} ({"404" if u in dead else ""})' for u in dead]
open('infinitum-published-links-2026-10-31.md','w').write('\n'.join(md))
# ---------- PDF ----------
logo='/tmp/logo.png'
im=PI.open('/workspace/brand/hires/infinitum-logo-horizontal-black-on-white-4000.jpg').convert('RGB'); im.thumbnail((1200,1200)); im.save(logo)
lw,lh=im.size
ss=dict(fontName='Helvetica',fontSize=7.5,leading=9.2)
P=ParagraphStyle('p',**ss); PL_=ParagraphStyle('l',**ss,textColor=colors.HexColor('#0B0B0B'))
H1=ParagraphStyle('h1',fontName='Helvetica-Bold',fontSize=17,leading=21,spaceAfter=4)
H2=ParagraphStyle('h2',fontName='Helvetica-Bold',fontSize=12,leading=15,textColor=RED,spaceBefore=10,spaceAfter=4)
SM=ParagraphStyle('sm',fontName='Helvetica',fontSize=8.5,leading=11)
e=lambda s:html.escape(s,quote=True)
def link(u,label=None): return f'<link href="{e(u)}" color="#C8102E"><u>{e(label or u)}</u></link>'
def tbl(data,widths,hdr):
    t=Table([[Paragraph(f'<b>{h}</b>',ParagraphStyle('h',**ss,textColor=colors.white)) for h in hdr]]+data,colWidths=widths,repeatRows=1)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.black),('VALIGN',(0,0),(-1,-1),'TOP'),
      ('LINEBELOW',(0,0),(-1,-1),0.3,colors.HexColor('#BBBBBB')),('LINEBELOW',(0,0),(-1,0),1.2,RED),
      ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5),('LEFTPADDING',(0,0),(-1,-1),3),('RIGHTPADDING',(0,0),(-1,-1),3)]))
    return t
story=[Image(logo,width=2.6*inch,height=2.6*inch*lh/lw),Spacer(1,6),
 Paragraph('Infinitum Corporation &amp; William Aaron Turner — Published Works &amp; Links',H1),
 Paragraph('Dated 31 Oct 2026 · Compiled from Infinitum bot records · Every link is clickable',SM),Spacer(1,4),
 Paragraph('<b>Infinitum Corporation</b> — Headquarters: Washington, DC · Operating location: Moscow · Phone: 202-729-9509 · '+link('https://www.theinfinitumcorporation.com/','theinfinitumcorporation.com')+' · Founder &amp; President: William Aaron Turner',SM),
 Spacer(1,4),Paragraph('Status key: <b>live</b> = page answered 200 on 31 Oct; <b>live (not auto-checked)</b> = X, Telegram, LinkedIn, Instagram, TikTok, Medium and Academia.edu block automated checks; <b>REMOVED / NOT FOUND</b> = page no longer exists.',SM)]
counts={}
W_=[2.55*inch,0.95*inch,0.62*inch,2.6*inch,0.78*inch]
for sec in order:
    rs=[r for r in rows if r[0]==sec]; counts[sec]=sum(1 for r in rs if r[4])
    story.append(Paragraph(f'{sec} ({counts[sec]})',H2))
    data=[[Paragraph(e(r[1]),P),Paragraph(e(r[2]),P),Paragraph(e(r[3]),P),Paragraph(link(r[4]) if r[4] else '—',PL_),Paragraph(e(status(r[4])+('; '+r[5] if r[5] else '')),P)] for r in rs]
    story.append(tbl(data,W_,['Title','Platform','Date','Link','Status']))
story.append(Paragraph(f'X posts by @infinitumceo ({len(xids)})',H2))
story.append(Paragraph('Every post URL found in the bot records, oldest first. Dates are derived from the post ID (UTC).',SM)); story.append(Spacer(1,3))
cells=[Paragraph(f'{xdate(i)} '+link(f'https://x.com/infinitumceo/status/{i}',i),P) for i in xids]
ncol=3; data=[cells[k:k+ncol]+[Paragraph('',P)]*(ncol-len(cells[k:k+ncol])) for k in range(0,len(cells),ncol)]
story.append(tbl(data,[2.5*inch]*3,['Post','Post','Post']))
story.append(Paragraph(f'Telegram channel posts ({len(tg)})',H2))
cells=[Paragraph(link(f'https://t.me/infinitumcorporation/{n}',f't.me/infinitumcorporation/{n}'),P) for n in tg]
data=[cells[k:k+4]+[Paragraph('',P)]*(4-len(cells[k:k+4])) for k in range(0,len(cells),4)]
story.append(tbl(data,[1.875*inch]*4,['Post','Post','Post','Post']))
story.append(Paragraph(f'Outlet submissions pending ({len(pending)}) — no live links yet',H2))
story.append(tbl([[Paragraph(e(a),P),Paragraph(e(b),P),Paragraph(e(c),P)] for a,b,c in pending],[1.6*inch,4.2*inch,1.7*inch],['Outlet','Piece / subject','Status']))
story.append(Paragraph('Journal submissions pending',H2))
story.append(tbl([[Paragraph(e(a),P),Paragraph(e(b),P),Paragraph(e(c),P)] for a,b,c in journals],[3.6*inch,1.6*inch,2.3*inch],['Journal','Ref','Status']))
story.append(Paragraph('Old links that no longer work',H2))
story.append(tbl([[Paragraph(link(u),PL_),Paragraph('NOT FOUND (404)',P)] for u in dead],[6*inch,1.5*inch],['URL','Status']))
def deco(c,d):
    c.saveState(); c.setFillColor(RED); c.rect(0,letter[1]-8,letter[0],8,fill=1,stroke=0)
    c.setFont('Helvetica',7); c.setFillColor(colors.black)
    c.drawString(0.5*inch,0.4*inch,'Infinitum Corporation · Published Works & Links · 31 Oct 2026'); c.drawRightString(letter[0]-0.5*inch,0.4*inch,f'Page {d.page}'); c.restoreState()
out='infinitum-published-links-2026-10-31.pdf'
SimpleDocTemplate(out,pagesize=letter,leftMargin=0.5*inch,rightMargin=0.5*inch,topMargin=0.5*inch,bottomMargin=0.6*inch,
  title='Infinitum Corporation & William Aaron Turner — Published Works & Links',author='Infinitum Corporation').build(story,onFirstPage=deco,onLaterPages=deco)
# html
h=['<!doctype html><meta charset=utf-8><title>Infinitum Published Links</title><style>body{font-family:Helvetica,Arial;color:#000;background:#fff;max-width:1000px;margin:auto}h1{border-bottom:4px solid #C8102E}h2{color:#C8102E}table{border-collapse:collapse;width:100%;font-size:12px}th{background:#000;color:#fff}td,th{border-bottom:1px solid #ccc;padding:3px;text-align:left}a{color:#C8102E}</style>']
for l in md:
    l2=re.sub(r'(https?://[^\s|]+)',lambda m:f'<a href="{e(m.group(1))}">{e(m.group(1))}</a>',e(l) if 'http' not in l else l)
    if l.startswith('# '): h.append(f'<h1>{e(l[2:])}</h1>')
    elif l.startswith('## '): h.append(f'<h2>{e(l[3:])}</h2>')
    elif l.startswith('|---'): continue
    elif l.startswith('|'): h.append('<table><tr>'+''.join(f'<td>{c.strip()}</td>' for c in l2.strip('|').split('|'))+'</tr></table>')
    elif l.startswith('- '): h.append(f'<div>{l2[2:]}</div>')
    elif l: h.append(f'<p>{l2}</p>')
open('infinitum-published-links-2026-10-31.html','w').write('\n'.join(h))
counts['X posts']=len(xids); counts['Telegram posts']=len(tg); counts['Outlet submissions pending (no links)']=len(pending)
for k,v in counts.items(): print(k,v)
print('removed/404:',[r[4] for r in rows if r[4] and status(r[4]).startswith(('REMOVED','NOT'))])
