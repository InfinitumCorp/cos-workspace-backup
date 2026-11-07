import json,html,os
exec(open('data.py').read())
SITE="https://www.theinfinitumcorporation.com"
ORG_ID=SITE+"/#organization"; PER_ID=SITE+"/#william-aaron-turner"
KW=["Corporate Cognitive Warfare","cognitive warfare","cognitive dominance","narrative strategy"]
PERSON_SAMEAS=[ORCID,"https://williamaaronturner.com/","https://x.com/infinitumceo","https://www.linkedin.com/in/william-aaron-t-726076244","https://umassmarine.academia.edu/WilliamAaronTurner","https://github.com/InfinitumCorp","https://ukrainianfiles.blogspot.com/"]
ORG_SAMEAS=["https://x.com/infinitumusa","https://t.me/infinitumcorporation","https://discord.gg/QVT7dWHUQa","https://github.com/InfinitumCorp","https://www.instagram.com/infinitumcorporation/","https://whop.com/infinitum-corporation/",ACAD_PROFILE,"https://infinitumwhitepapers.blogspot.com/"]
def person(full=False):
  p={"@type":"Person","@id":PER_ID,"name":"William Aaron Turner","url":"https://williamaaronturner.com/","identifier":{"@type":"PropertyValue","propertyID":"ORCID","value":"0009-0002-1585-5442","url":ORCID},"sameAs":PERSON_SAMEAS,"jobTitle":"Founder and President","worksFor":{"@id":ORG_ID}}
  if full:
    p["knowsAbout"]=KW+["cybersecurity","AI for security operations","network defense","ethical hacking","geopolitical risk assessment","defense technology","Russia sanctions","Russia-Africa relations"]
    p["description"]="William Aaron Turner is founder and president of Infinitum Corporation, a Washington, DC security consulting firm, and the person who coined the term Corporate Cognitive Warfare."
  return p
def org(full=False):
  o={"@type":"Organization","@id":ORG_ID,"name":"Infinitum Corporation","url":SITE+"/"}
  if full:
    o.update({"legalName":"INFINITUM CORPORATION","logo":SITE+"/favicon.ico","email":"info@theinfinitumcorporation.com","telephone":"+1-202-729-9509",
     "address":{"@type":"PostalAddress","streetAddress":"1629 K Street NW, Suite 300","addressLocality":"Washington","addressRegion":"DC","postalCode":"20006","addressCountry":"US"},
     "founder":{"@id":PER_ID},"sameAs":ORG_SAMEAS,
     "contactPoint":[{"@type":"ContactPoint","contactType":"customer service","telephone":"+1-202-729-9509","email":"info@theinfinitumcorporation.com","availableLanguage":["English","Russian"],
       "hoursAvailable":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"21:00"}}],
     "knowsAbout":KW+["cybersecurity consulting","network defense","ethical hacking","AI for security operations","strategic risk assessment","defense technology advisory"],
     "makesOffer":[{"@type":"Offer","itemOffered":{"@type":"Service","name":"Corporate Cognitive Warfare","serviceType":"Corporate Cognitive Warfare consulting","description":"Corporate Cognitive Warfare, a term coined by William Aaron Turner: narrative strategy, ethical persuasion and search and AI-discovery optimization that help companies win the contest for perception and attention (cognitive dominance), informed by the established discipline of cognitive warfare.","provider":{"@id":ORG_ID},"areaServed":"Worldwide"}},
       {"@type":"Offer","itemOffered":{"@type":"Service","name":"Cybersecurity consulting","provider":{"@id":ORG_ID},"areaServed":"Washington, DC"}},
       {"@type":"Offer","itemOffered":{"@type":"Service","name":"AI for security operations","provider":{"@id":ORG_ID}}}],
     "subjectOf":[{"@id":p["url"]+"#article"} for p in PUBS]})
  return o
def doi(p): return f"10.5281/zenodo.{p['zen']}" if p.get('zen') else None
def wb(p): return "https://web.archive.org/web/2026/"+p['url']
def sameas(p):
  s=[]
  if p.get('zen'): s+=["https://doi.org/"+doi(p),f"https://zenodo.org/records/{p['zen']}"]
  if p.get('acad'): s.append(p['acad'])
  if not p.get('todo'): s.append(wb(p))
  return s
def article(p):
  a={"@context":"https://schema.org","@type":p['schema'],"@id":p['url']+"#article","headline":p['nt'],"name":p['title'],"description":p['desc'],"url":p['url'],"mainEntityOfPage":p['url'],
     "datePublished":p['date'],"inLanguage":"en","author":person(),"abstract":p.get("abstract",p["desc"]),"publisher":org(),"keywords":", ".join(p['about']),"about":[{"@type":"Thing","name":a} for a in p['about']],
     "isPartOf":{"@type":"Blog","name":p['venue'].split(' (')[0],"url":p['url'].split('/2026')[0]+"/"},"sameAs":sameas(p)}
  if p['type']=="whitepaper": a["additionalType"]="https://schema.org/Report"; a["genre"]="Whitepaper"
  else: a["genre"]="Article"
  if p.get('zen'):
    a["identifier"]=[{"@type":"PropertyValue","propertyID":"DOI","value":doi(p),"url":"https://doi.org/"+doi(p)}]
    a["encoding"]={"@type":"MediaObject","encodingFormat":"application/pdf","contentUrl":f"https://zenodo.org/records/{p['zen']}/files/{p['pdf']}"}
  return a
def highwire(p):
  t=[("citation_title",p['title']),("citation_author","Turner, William Aaron"),("citation_author_orcid",ORCID),("citation_publication_date",p['date'][:10].replace('-','/')),("citation_publisher","Infinitum Corporation"),("citation_journal_title",p['venue'].split(' (')[0]),("citation_language","en"),("citation_abstract_html_url",p['url'])]
  if p.get('zen'): t+= [("citation_doi",doi(p)),("citation_pdf_url",f"https://zenodo.org/records/{p['zen']}/files/{p['pdf']}")]
  if p['type']=="whitepaper": t.append(("citation_technical_report_institution","Infinitum Corporation"))
  return "\n".join(f'<meta name="{k}" content="{html.escape(v,quote=True)}" />' for k,v in t)
def footer(p):
  L=[]
  if p.get('zen'):
    L.append(f'<li>DOI: <a href="https://doi.org/{doi(p)}">https://doi.org/{doi(p)}</a></li>')
    L.append(f'<li>Zenodo (PDF): <a href="https://zenodo.org/records/{p["zen"]}">zenodo.org/records/{p["zen"]}</a></li>')
  L.append(f'<li>Academia.edu: <a href="{p.get("acad",ACAD_PROFILE)}">{"paper" if p.get("acad") else "Infinitum Corporation research profile"}</a></li>')
  if not p.get('todo'): L.append(f'<li>Archived copy: <a href="{wb(p)}">Wayback Machine</a></li>')
  rel="".join(f'<li><a href="{BY[r]["url"]}">{html.escape(BY[r]["nt"])}</a></li>' for r in p['rel'])
  cite=f'Turner, W. A. (2026). <i>{html.escape(p["title"])}</i>. {html.escape(p["venue"].split(" (")[0])}. Infinitum Corporation.' + (f' https://doi.org/{doi(p)}' if p.get('zen') else f' {p["url"]}')
  return f'''<div class="cite-also" style="border-top:1px solid #ccc;margin-top:2em;padding-top:1em">
<h3>Cite this {"whitepaper" if p["type"]=="whitepaper" else "article"}</h3>
<p>{cite}</p>
<h3>Also available</h3>
<ul>{"".join(L)}</ul>
<h3>Related from Infinitum Corporation</h3>
<ul>{rel}</ul>
<p><small>By <a href="https://williamaaronturner.com/" rel="author">William Aaron Turner</a> (ORCID <a href="{ORCID}">0009-0002-1585-5442</a>), founder of <a href="{SITE}/">Infinitum Corporation</a>, Washington, DC, and the person who coined the term <b>Corporate Cognitive Warfare</b>: narrative strategy and cognitive dominance for companies, drawing on the established field of cognitive warfare. Contact: 202-729-9509 (Mon&ndash;Fri 9 AM&ndash;9 PM ET) &middot; <a href="https://t.me/infinitumcorporation">Telegram</a> &middot; <a href="https://discord.gg/QVT7dWHUQa">Discord</a></small></p>
</div>'''
os.makedirs('per-post',exist_ok=True)
for p in PUBS:
  if p.get('todo'): pass
  edit=f"https://www.blogger.com/blog/post/edit/{p['blog']}/{p['post']}" if p['post']!='TODO' else "TODO: blog post not yet published (Blog Bot). Then set url/post in data.py and rerun build.py"
  out=f'''<!-- {p['slug']} | live: {p['url']}
     Blogger edit: {edit}
     1) Post settings > Title -> "{p['nt']}"  ({len(p['nt'])} chars; URL/permalink stays unchanged)
     2) Post settings > Search description -> "{p['desc']}"  ({len(p['desc'])} chars; enable Settings > Meta tags > Enable search description first)
     3) Switch editor to HTML view; paste everything from BEGIN to END at the very bottom of the post body.
     Highwire (Google Scholar) tags: Blogger strips/ignores <meta> in post bodies, so they are NOT in the paste block. Use blogger-theme-head.xml (template-level, b:if per post URL). -->
<!-- BEGIN paste -->
<script type="application/ld+json">
{json.dumps(article(p),indent=1,ensure_ascii=False)}
</script>
{footer(p)}
<!-- END paste -->

<!-- Reference only (template-level head tags for this post):
{highwire(p)}
-->
'''
  open(f"per-post/{p['slug']}.html","w").write(out)
# theme head snippets per blog
blogs={}
for p in PUBS: blogs.setdefault(p['url'].split('/2026')[0],[]).append(p)
T=["<!-- Paste inside <head> of each blog's theme (Theme > Edit HTML), right after <b:include data='blog' name='all-head-content'/>. One section per blog. Generated 2026-10-31. -->"]
for b,ps in blogs.items():
  T.append(f"\n<!-- ===== {b} ===== -->")
  for p in ps:
    if p.get('todo'): T.append(f"<!-- TODO {p['slug']}: add b:if block once blog URL exists -->"); continue
    T.append(f"<b:if cond='data:view.url == &quot;{p['url']}&quot;'>\n{highwire(p)}\n</b:if>")
open('blogger-theme-head.xml','w').write("\n".join(T)+"\n")
# site schema
graph={"@context":"https://schema.org","@graph":[org(True),person(True)|{"subjectOf":[{"@id":p["url"]+"#article"} for p in PUBS],"workExample":[{"@type":p["schema"],"@id":p["url"]+"#article","name":p["title"],"url":p["url"],**({"identifier":"https://doi.org/"+doi(p)} if p.get('zen') else {})} for p in PUBS]}]}
open('site-schema.html','w').write('<!-- Sitewide Organization + Person JSON-LD. Paste in <head> of theinfinitumcorporation.com, williamaaronturner.com and each Blogger theme. DC entity only; phone 202-729-9509 only; hours Mon-Fri 09:00-21:00. -->\n<script type="application/ld+json">\n'+json.dumps(graph,indent=1,ensure_ascii=False)+'\n</script>\n')
json.dump(graph,open('site-schema.json','w'),indent=1)
print("ok")
