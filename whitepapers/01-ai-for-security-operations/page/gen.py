import re, json
src=open('../Infinitum-Whitepaper-01-Dead-Reckoning-RELEASE.md').read()
src=re.sub(r'<!--.*?-->\n?','',src,flags=re.S)
def clean(s):
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m: m.group(2) if m.group(1)==m.group(2) else f"{m.group(1)} ({m.group(2)})",s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'\1',s)
    s=re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])',r'\1',s)
    s=re.sub(r'\s*\{#[^}]+\}','',s)
    return s.strip()
lines=src.split('\n')
secs=[]; cur=None; sub=None
def target():
    return sub['blocks'] if sub is not None else cur['blocks']
def slug(h): return re.sub(r'[^a-z0-9]+','-',h.lower()).strip('-')
i=0; para=[]
def flush():
    global para
    if para:
        t=clean(' '.join(para)); 
        if t: target().append({'t':'p','s':t})
        para=[]
def new_sec(h):
    global cur,sub
    cur={'id':slug(h),'heading':h,'blocks':[],'subs':[]}; secs.append(cur); sub=None
def new_sub(h):
    global sub
    sub={'heading':h,'blocks':[]}; cur['subs'].append(sub)
refs_mode=False
while i<len(lines):
    l=lines[i]
    if re.match(r'^</?div',l):
        flush()
        if 'class="scenario"' in l:
            target().append({'t':'p','s':'Illustrative · Hypothetical'})
        i+=1; continue
    m=re.match(r'^(#{1,4}) (.*)$',l)
    if m:
        flush(); lvl=len(m.group(1)); h=clean(m.group(2))
        if lvl<=2: new_sec(h); refs_mode=(h=='References')
        else: new_sub(h)
        i+=1; continue
    if l.strip()=='' : flush(); i+=1; continue
    if l.startswith('|'):
        flush(); rows=[]
        while i<len(lines) and lines[i].startswith('|'):
            rows.append(lines[i]); i+=1
        cells=[[clean(c) for c in r.strip().strip('|').split('|')] for r in rows if not re.match(r'^\|\s*:?-{3}',r)]
        hdr,body=cells[0],cells[1:]
        if all(c=='' for c in hdr) and len(hdr)==2:
            target().append({'t':'props','items':[{'label':r[0],'value':r[1]} for r in body]})
        else:
            target().append({'t':'table','cols':hdr,'rows':body})
        continue
    if l.startswith('> '):
        flush(); q=[]
        while i<len(lines) and lines[i].startswith('>'):
            q.append(lines[i][1:].strip()); i+=1
        target().append({'t':'quote','s':clean(' '.join(q))}); continue
    mb=re.match(r'^(- |\d+\. )(.*)$',l)
    if mb:
        flush(); kind='ul' if mb.group(1)=='- ' else 'ol'; items=[]
        while i<len(lines):
            mm=re.match(r'^(- |\d+\. )(.*)$',lines[i])
            if mm and (('ul' if mm.group(1)=='- ' else 'ol')==kind):
                raw=mm.group(2); i+=1
                # continuation lines
                while i<len(lines) and lines[i].strip() and not re.match(r'^(- |\d+\. |#|\||>|<)',lines[i]):
                    raw+=' '+lines[i].strip(); i+=1
                items.append(raw)
            elif lines[i].strip()=='' and i+1<len(lines) and re.match(r'^(- |\d+\. )',lines[i+1]) and (('ul' if lines[i+1].startswith('- ') else 'ol')==kind):
                i+=1
            else: break
        if refs_mode and kind=='ol':
            links=[]
            for it in items:
                urls=re.findall(r'\]\((https?://[^)]+)\)',it)
                title=re.sub(r'\s*\[[^\]]+\]\([^)]+\)','',it)
                title=re.sub(r'\s*\(cited as [^)]*\)','',title)
                cited=re.search(r'\(cited as ([^)]*)\)',it)
                title=clean(title)
                if cited: title+=f" (cited as {cited.group(1)})"
                links.append({'title':title.strip(),'href':urls[-1] if urls else ''})
            assert all(x['href'] for x in links)
            target().append({'t':'links','links':links})
        else:
            target().append({'t':kind,'items':[clean(x) for x in items]})
        continue
    para.append(l.strip()); i+=1
flush()
# front matter section
front={'id':'about-this-paper','heading':'About this paper','blocks':[
 {'t':'p','s':'Dead Reckoning: AI for Security Operations in a Jammed, Spoofed, Watched World'},
 {'t':'p','s':'Practical, Integrated Steps for Mid-Size Organizations'},
 {'t':'p','s':'By William Aaron Turner, Founder and President, Infinitum Corporation. Infinitum Corporation Whitepaper No. 1. October 2026. Released October 25, 2026.'},
 {'t':'p','s':'Neutrality statement. This paper draws general lessons about technology and conflict from public sources. It takes no side and makes no claim about any party.'},
 {'t':'p','s':'© 2026 Infinitum Corporation. All rights reserved. No part of this publication may be reproduced or distributed without written permission, except for brief quotations with attribution.'},
 {'t':'p','s':'Disclaimer. This whitepaper is provided for general information only. It is not legal, regulatory or professional advice for any specific situation, and it does not create a client relationship. Statistics are taken from the public sources cited and remain the property of their publishers; they describe the samples studied by those publishers and are not benchmarks or predictions for any particular organization. Infinitum Corporation makes no promise or guarantee about the security outcome any organization will achieve.'},
 {'t':'p','s':'This paper is strictly analytical and defensive. References to irregular warfare, gray-zone competition and hybrid threats are used as an analytic lens for defense and resilience. Nothing in this paper is instruction for offensive activity. Any security testing referred to here means authorized, scoped testing performed with the written permission of the system owner.'},
 {'t':'p','s':'Scenarios in Part IX are illustrative and hypothetical. They do not describe any real organization, client or incident.'},
 {'t':'p','s':'Trademarks and framework names belong to their respective owners. Citation of a source does not imply that its publisher endorses this paper or Infinitum Corporation.'},
 {'t':'props','items':[{'label':'Contact','value':'Infinitum Corporation, Washington, DC, 1629 K Street NW, Suite 300'},{'label':'Phone','value':'(202) 980-9300'},{'label':'Website','value':'https://www.theinfinitumcorporation.com'},{'label':'Email','value':'info@theinfinitumcorporation.com'},{'label':'Telegram','value':'https://t.me/infinitumcorporation'},{'label':'X','value':'https://x.com/infinitumceo'}]},
 {'t':'p','s':'All data comes from the public record. All conclusions are mine. W.A.T.'}],'subs':[]}
secs=[front]+secs
json.dump(secs,open('data.json','w'),ensure_ascii=False)
# word counts
def words(x): return len([t for t in x.split() if re.search(r'[A-Za-z0-9]',t)])
def blk_words(b):
    if b['t'] in('p','quote'): return words(b['s'])
    if b['t'] in('ul','ol'): return sum(words(x) for x in b['items'])
    if b['t']=='table': return sum(words(c) for c in b['cols'])+sum(words(c) for r in b['rows'] for c in r)
    if b['t']=='links': return sum(words(x['title']) for x in b['links'])
    if b['t']=='props': return sum(words(x['label'])+words(x['value']) for x in b['items'])
tot={}
for s in secs:
    w=sum(blk_words(b) for b in s['blocks'])+sum(blk_words(b) for sb in s['subs'] for b in sb['blocks'])+words(s['heading'])+sum(words(sb['heading']) for sb in s['subs'])
    tot[s['heading']]=w
for k,v in tot.items(): print(v,k)
print('sections',len(secs),'subs',sum(len(s['subs']) for s in secs))
