from pathlib import Path
import csv,json,re,html,hashlib
ROOT=Path('/workspace/seo-master'); OUT=ROOT/'refresh-2026-11-07'; OLD=ROOT/'publications-2026-10-31'
def brand(s):
 return re.sub(r'Infinitum(?:®)? Corporation(?:®)?', 'Infinitum Corporation®', s)
def display(s):
 if isinstance(s,str): return s if s.startswith(('http://','https://','mailto:')) else brand(s).replace('153rd Tank Battalion','153rd Tank Regiment')
 if isinstance(s,list): return [display(v) for v in s]
 if isinstance(s,dict): return {k:display(v) for k,v in s.items()}
 return s
def writecsv(p,rows,fields=None):
 if not rows:return
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rows[0])); w.writeheader();w.writerows(rows)
changed=[]
for name in ['00-dispatch.md','01-blog-summary.md','02-x-thread.md','04-newsletter-blurb.md','05-abstract-keywords.md']:
 p=Path('/workspace/whitepapers/echoform/release-kit')/name
 s=p.read_text();n=s.replace('Infinitum® Corporation','Infinitum Corporation®')
 if n!=s:p.write_text(n);changed.append(str(p))
p=OLD/'per-post/echoform.html'; s=p.read_text();s=s.replace('echoform-reflexive-control-theory//','echoform-reflexive-control-theory/')
s=re.sub(r'^\s*"datePublished": "2026-11-07T00:00:00\+02:00",\n','',s,flags=re.M)
s=brand(s);p.write_text(s);changed.append(str(p))
p=ROOT/'audit-2026-10-31/keyword-map.md';s=p.read_text()
s='\n'.join(line for line in s.splitlines() if not any(x in line.lower() for x in ['ethical hacking','penetration testing','pentest']))+'\n'
s=brand(s);s=s.replace('Keyword map (2026-10-31)','Keyword map (refreshed 2026-11-07)')
s+='\n## 2026-11-07 controls\nNo pentest promotion. Website implementation paused. Publication-level map: ../refresh-2026-11-07/keyword-map.csv. No search-volume estimates or ranking guarantees.\n'
p.write_text(s);changed.append(str(p))
posts={}
for p in (OLD/'per-post').glob('*.html'):
 s=p.read_text();m=re.search(r'<script type="application/ld\+json">\s*(.*?)\s*</script>',s,re.S)
 if m:
  d=display(json.loads(m[1]));u=d['url'];posts[u]={'slug':p.stem,'schema':d,'title':d.get('headline',d.get('name','')),'description':d.get('description',''),'source':str(p)}
# Include all cached published blog-feed entries, not drafts or manuscripts.
for p in (OLD/'raw').glob('feed_*.json'):
 for e in json.loads(p.read_text()).get('feed',{}).get('entry',[]):
  u=next((x['href'] for x in e.get('link',[]) if x.get('rel')=='alternate'),'')
  if not u or u in posts:continue
  title=brand(e['title']['$t']);summary=html.unescape(re.sub('<[^>]+>',' ',e.get('summary',{}).get('$t','')));summary=' '.join(summary.split())
  desc=summary[:152].rsplit(' ',1)[0]+'…' if len(summary)>155 else summary
  posts[u]={'slug':u.rsplit('/',1)[-1].replace('.html',''),'title':title,'description':brand(desc),'source':str(p),'schema':{'@context':'https://schema.org','@type':'BlogPosting','@id':u+'#article','url':u,'headline':title,'description':brand(desc),'author':{'@type':'Person','name':'William Aaron Turner','sameAs':'https://orcid.org/0009-0002-1585-5442'},'publisher':{'@type':'Organization','name':'Infinitum Corporation®','url':'https://www.theinfinitumcorporation.com/','telephone':'202-729-9509'}}}
# Published repository and X versions receive independent local drafts, not live edits.
for r in csv.DictReader((OLD/'pubs.csv').open()):
 u=r.get('live_url','')
 if r.get('status')!='published' or not u or u in posts:continue
 title=brand(r['title']);same=next((p for p in posts.values() if p['title']==title),None)
 desc=same['description'] if same else f'{title} — research by William Aaron Turner, Infinitum Corporation®.'
 if len(desc)>155:desc=desc[:152].rsplit(' ',1)[0]+'…'
 posts[u]={'slug':u.rstrip('/').split('/')[-1],'title':title,'description':desc,'source':str(OLD/'pubs.csv'),'schema':{'@context':'https://schema.org','@type':'Report' if 'whitepaper' in r['type'].lower() else 'Article','@id':u+'#article','url':u,'headline':title,'description':desc,'author':{'@type':'Person','name':'William Aaron Turner','sameAs':'https://orcid.org/0009-0002-1585-5442'},'publisher':{'@type':'Organization','name':'Infinitum Corporation®','telephone':'202-729-9509'}}}
images=list(csv.DictReader((ROOT/'images-2026-11-01/images.csv').open()))
index=[];keywords=[];flags=[];(OUT/'per-post').mkdir(exist_ok=True)
for u,p in posts.items():
 slug=re.sub('[^a-zA-Z0-9_-]+','-',p['slug'])[:85]+'-'+hashlib.sha256(u.encode()).hexdigest()[:8];folder=OUT/'per-post'/slug;folder.mkdir(exist_ok=True)
 d=p['schema'];d['publisher']={'@type':'Organization','@id':'https://www.theinfinitumcorporation.com/#organization','name':'Infinitum Corporation®','url':'https://www.theinfinitumcorporation.com/','telephone':'202-729-9509'}
 if 'whop.com/infinitum-corporation/echoform' in u:
  d.pop('datePublished',None);d['isPartOf']={'@type':'WebSite','name':'Whop','url':'https://whop.com/'}
 if d.get('@type')=='ScholarlyArticle':d['@type']='Article' # do not imply peer review
 primary=', '.join(x.get('name','') for x in d.get('about',[]) if isinstance(x,dict)) or p['title'].split(':')[0]
 meta={'url':u,'title':p['title'],'meta_description':p['description'],'primary_topic':primary.split(',')[0],'supporting_topics':primary,'source':p['source'],'status':'LOCAL DRAFT — cached publication evidence; current live state not checked','canonical_note':'Preserve existing URL. Review duplicate-source canonical before applying.'}
 (folder/'metadata.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n');(folder/'schema.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 (folder/'meta-head.html').write_text('<!-- LOCAL DRAFT: platform head/template only, not Blogger body -->\n<meta name="description" content="'+html.escape(p['description'],quote=True)+'">\n')
 rows=[]
 for i in images:
  if i['post_url']!=u:continue
  rows.append({'image_src':i['image_src'],'alt':p['title'].split(':')[0]+' — cover','title':p['title']+' | Infinitum Corporation®','caption':p['title']+' — William Aaron Turner, Infinitum Corporation®.','review':'Title-derived draft; visually confirm image subject. Decorative images need empty alt. Preserve image URL.'})
 if not rows:rows=[{'image_src':'','alt':'','title':'','caption':'','review':'No mapped image; inspect live page before writing descriptive alt. Every PR requires an approved image.'}]
 writecsv(folder/'images.csv',rows)
 index.append({'url':u,'action':'review then request indexing after approved live update','status':'not submitted; live state not rechecked','draft_path':str(folder)})
 keywords.append({'url':u,'primary_topic':meta['primary_topic'],'supporting_topics':primary,'intent':'research / informational'})
 if 'Battalion' in json.dumps(d):flags.append({'url':u,'finding':'Battalion in cached metadata; inspect context before replacing.'})
writecsv(OUT/'indexing.csv',index);writecsv(OUT/'keyword-map.csv',keywords)
for name in ['images.csv','local-images.csv']:
 rows=list(csv.DictReader((ROOT/'images-2026-11-01'/name).open()))
 for row in rows:
  for k,v in row.items():
   if v and not any(t in k for t in ['url','src','path','filename']):row[k]=brand(v).replace('153rd Tank Battalion','153rd Tank Regiment')
 writecsv(OUT/('image-inventory-'+name),rows)
(OUT/'changed-files.txt').write_text('\n'.join(changed)+'\n')
(OUT/'README.md').write_text(f'''# Local SEO refresh — 2026-11-07 MSK
{len(posts)} publication URL draft packages in per-post/. No live writes, website-code edits, DNS changes, indexing requests or scheduling.

Sources: cached Blogger feeds, publication manifest and existing SEO snippets. Current publication/HTTP status was NOT verified this turn. No claim of comprehensive current-live coverage. No confirmed live press-release URLs were available in these sources; no unpublished release or manuscript was included. No live Battalion finding is asserted.

Each package contains metadata.json, schema.json, meta-head.html and images.csv. Image text is a title-derived draft requiring visual review, not verified visual description. Missing images are flagged rather than invented. Schema dates preserved only where previously recorded; unsupported EchoForm timestamp removed. ® kept out of URL and ID values. Phone 202-729-9509. No forced keywords, paid/spam links or pentest promotion.

indexing.csv is a review queue, not proof URLs are unindexed. Apply approved updates before submitting URLs via the appropriate verified property. Repository/X pages may not permit custom head/schema; their drafts are reference-only. Duplicate article copies need canonical review. Do not paste head tags into Blogger bodies. Keep withheld/exclusive and under-review work unpublished.

Changed source paths: changed-files.txt. Local normalized image inventories accompany per-post image drafts. Existing images were not replaced or rehosted. Website domains remain paused.
''')
print(f'Created {len(posts)} per-URL packages; changed {len(changed)} source files. Output: {OUT}')
