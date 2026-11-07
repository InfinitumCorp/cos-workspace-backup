import subprocess,json,re,html,concurrent.futures,os
from html.parser import HTMLParser
out='/workspace/blog-audit/'
def get(u):
 p=subprocess.run(['curl','-L','-sS','--max-time','40','-w','\n%{http_code}',u],capture_output=True,text=True); body,_,status=p.stdout.rpartition('\n');return body,status
blogs=['infinitumwhitepapers','ukrainianfiles','adversarialmirrorratchet','russiaafricabythenumbers','russiaafricareport','williamaaronturner','nfiles','nnfiles']
rows=[]; stats=[]; discovered=set(); profiles=set()
class P(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if v and k in ['href','src','srcset']:
    if re.search(r'https?://(?:raw\.githubusercontent\.com|github\.com|[^/]+\.github\.io)(?:/|$)',v):rows.append(dict(blog=blog,post=post,url=html.unescape(v),kind='image' if tag=='img' or k=='srcset' else 'link'))
for b in blogs:
 blog=b+'.blogspot.com';home,s=get('https://'+blog+'/');open(out+b+'-home.html','w').write(home)
 discovered.update(re.findall(r'([\w-]+\.blogspot\.com)',home)); profiles.update(re.findall(r'https?://(?:www\.)?blogger\.com/profile/\d+',home))
 counts={}
 for typ in ['posts','pages']:
  n=1;total=0
  while True:
   body,s=get(f'https://{blog}/feeds/{typ}/default?max-results=500&alt=json&start-index={n}');open(out+b+'-'+typ+f'-{n}.json','w').write(body)
   try:data=json.loads(body)['feed']
   except:counts[typ]='ERROR '+s;break
   entries=data.get('entry',[]);total+=len(entries)
   for e in entries:
    post=next((x['href'] for x in e.get('link',[]) if x['rel']=='alternate'),'')
    if 'dead-reckoning-ai-security-operations' in post:continue
    content=e.get('content',e.get('summary',{})).get('$t','');P().feed(content)
    discovered.update(re.findall(r'([\w-]+\.blogspot\.com)',content))
   if not entries or total>=int(data.get('openSearch$totalResults',{}).get('$t',total)):counts[typ]=total;break
   n+=len(entries)
 stats.append(dict(blog=blog,counts=counts,home_status=s))
for profile in profiles:
 body,s=get(profile);open(out+'profile-'+profile.rsplit('/',1)[1]+'.html','w').write(body);discovered.update(re.findall(r'([\w-]+\.blogspot\.com)',body))
urls=set(r['url'] for r in rows)
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as ex:statuses=dict(zip(urls,ex.map(lambda u:get(u)[1],urls)))
for r in rows:r['status']=statuses[r['url']]
open(out+'results.json','w').write(json.dumps(dict(stats=stats,discovered=sorted(discovered),profiles=sorted(profiles),rows=rows),indent=2));print(json.dumps(dict(stats=stats,discovered=sorted(discovered),profiles=sorted(profiles),rows=rows),indent=2))
