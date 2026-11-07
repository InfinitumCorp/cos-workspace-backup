import json
A=[
("meat-grinder-to-the-medical-freezer","2083666042295906307","2026-08-02","Meat Grinder to the Medical Freezer: A One Stop Shop For a Ukrainian Soldier",
 "Meat Grinder to the Medical Freezer | Ukraine Files",
 "William Aaron Turner examines organ-harvesting allegations tied to Ukraine's war dead, name by name, using open sources. A Ukraine Files X Article.",
 "Ukraine organ harvesting allegations, Ukrainian soldiers, war casualties, Ukraine Files, William Aaron Turner","Organ-trade allegations and Ukraine's war casualties"),
("grandmas-toddlers-and-forklift-drivers","2089708406206586880","2026-08-18","Grandmas, Toddlers, and Forklift Drivers",
 "Grandmas, Toddlers and Forklift Drivers | Ukraine Files",
 "How Ukraine's list of \"military targets\" keeps widening to civilians: grandmothers, children and workers. An X Article by William Aaron Turner.",
 "Ukraine civilian targets, Myrotvorets, civilian casualties, Ukraine war, Ukraine Files, William Aaron Turner","Civilians labelled as targets"),
("the-kidnapping-of-a-nation","2090751273901457408","2026-08-21","The Kidnapping of a Nation: Ukraine's Forced Mobilization, Human Trafficking, & Organ Harvesting",
 "The Kidnapping of a Nation: Ukraine Forced Mobilization",
 "Vans, detention and a state at war with its own men: William Aaron Turner documents Ukraine's forced mobilization and trafficking claims.",
 "Ukraine forced mobilization, busification, TCC conscription, human trafficking, Ukraine Files, William Aaron Turner","Forced mobilization"),
("zelenskyy-west-lil-frankenstein-monster","2091939536875958273","2026-08-24","Zelenskyy: The West's lil' Frankenstein Monster – the Anatomy of a Geopolitical Puppet",
 "Zelenskyy, the West's Lil' Frankenstein | Ukraine Files",
 "Who built Zelenskyy's rise, part by part: backers, media networks and Western money. A Ukraine Files X Article by William Aaron Turner.",
 "Zelenskyy, Kolomoisky, Kvartal 95, Western influence Ukraine, geopolitics, Ukraine Files, William Aaron Turner","Zelenskyy's backers and media network"),
("wtf-is-in-q-tel","2091940977485156352","2026-08-24","WTF is IN-Q-TEL: CIA Investment Arm That Has Its Hand in Everything",
 "WTF Is In-Q-Tel? The CIA's Venture Fund Explained",
 "In-Q-Tel, the CIA's venture capital arm, and the pipeline from Silicon Valley to Ukraine's battlefields. An X Article by William Aaron Turner.",
 "In-Q-Tel, CIA venture capital, Palantir, defense tech, Ukraine kill chain, intelligence community, William Aaron Turner","CIA venture capital and defense tech"),
("the-art-of-not-giving-a-fck","2095859080581554178","2026-09-04","The Art of Not Giving a F*ck: How Russia Is Laughing All the Way to Victory While the West Panics",
 "The Art of Not Giving a F*ck: Russia vs. 50 Countries",
 "Sanctions, aid and GDP: why 50 countries' pressure has not broken Russia's economy. A Ukraine Files X Article by William Aaron Turner.",
 "Russia sanctions, Russian economy, GDP, Western aid to Ukraine, geopolitics, Ukraine Files, William Aaron Turner","Russia's economy under sanctions"),
("checkmate-in-vladivostok","2096677873231044608","2026-09-08","Checkmate in Vladivostok: EEF (Eastern Economic Forum)",
 "Checkmate in Vladivostok: Eastern Economic Forum 2026",
 "The Eastern Economic Forum 2026 in Vladivostok: delegations from dozens of countries and the deals that challenge Russia's isolation story.",
 "Eastern Economic Forum 2026, EEF Vladivostok, Russia isolation, Russia Asia trade, Ukraine Files, William Aaron Turner","Eastern Economic Forum 2026"),
("sweeps-and-spies","2096961143344635905","2026-09-08","SWEEPS AND SPIES",
 "Sweeps and Spies: Demining NGOs and Intelligence",
 "Russia clears the bombs; the West clears the data. William Aaron Turner on demining NGOs and intelligence links from Laos to Moldova.",
 "demining NGOs, HALO Trust, intelligence, Laos, Moldova, Ukraine mine clearance, Ukraine Files, William Aaron Turner","Demining NGOs and intelligence"),
]
AUTH={"@type":"Person","name":"William Aaron Turner","url":"https://x.com/infinitumceo","sameAs":["https://orcid.org/0009-0002-1585-5442","https://x.com/infinitumceo"],"identifier":"https://orcid.org/0009-0002-1585-5442","jobTitle":"President, Infinitum Corporation"}
PUB={"@type":"Organization","name":"Infinitum Corporation","url":"https://www.theinfinitumcorporation.com","email":"info@theinfinitumcorporation.com","telephone":"+1-202-729-9509","address":{"@type":"PostalAddress","streetAddress":"1629 K Street NW, Suite 300","addressLocality":"Washington","addressRegion":"DC","postalCode":"20006","addressCountry":"US"}}
inv=["# X Articles inventory (@infinitumceo)","","Source: xa/articles.backup.json (X API article.title on parent post) + xarticles-v2/ + X search 2026-11-02. 8 articles; no newer articles found on X since Sep 8.","","| # | Title | URL | Published (parent post date) | Topic | Meta file |","|---|---|---|---|---|---|"]
idx=[]
for n,(slug,id_,d,title,st,md,kw,topic) in enumerate(A,1):
  assert len(st)<=60,(slug,len(st)); assert len(md)<=155,(slug,len(md))
  url=f"https://x.com/i/article/{id_}"
  ld={"@context":"https://schema.org","@type":"Article","headline":title[:110],"name":title,"description":md,"url":url,"mainEntityOfPage":url,"datePublished":d,"inLanguage":"en","keywords":kw,"author":AUTH,"publisher":PUB,"isPartOf":{"@type":"CreativeWorkSeries","name":"The Ukraine Files","url":"https://ukrainianfiles.blogspot.com/p/the-ukraine-files-full-series.html"}}
  if n==8: pass
  open(f"{slug}.md","w").write(f"""# {title}

- URL: {url}
- Published: {d}
- Topic: {topic}

## SEO title ({len(st)} chars)
{st}

## Meta description ({len(md)} chars)
{md}

## Keywords
{kw}

## Head tags (use where republished/linked)
```html
<title>{st}</title>
<meta name="description" content="{md.replace('"','&quot;')}">
<meta name="keywords" content="{kw}">
<meta name="author" content="William Aaron Turner">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:title" content="{st}">
<meta property="og:description" content="{md.replace('"','&quot;')}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@infinitumceo">
<meta name="twitter:creator" content="@infinitumceo">
```

## Article JSON-LD
```html
<script type="application/ld+json">
{json.dumps(ld,indent=1,ensure_ascii=False)}
</script>
```
""")
  inv.append(f"| {n} | {title} | {url} | {d} | {topic} | {slug}.md |")
  idx.append((n,title,url,d,md,st))
open("inventory.md","w").write("\n".join(inv)+"\n")
json.dump(idx,open("index.json","w"),ensure_ascii=False,indent=1)
# GitHub index
g=["# X Articles by William Aaron Turner","","Long-form X Articles by **William Aaron Turner** ([@infinitumceo](https://x.com/infinitumceo), ORCID [0009-0002-1585-5442](https://orcid.org/0009-0002-1585-5442)), President of [Infinitum Corporation](https://www.theinfinitumcorporation.com), Washington, DC. Part of [The Ukraine Files](https://ukrainianfiles.blogspot.com/p/the-ukraine-files-full-series.html).",""]
for n,t,u,d,md,st in idx: g+= [f"{n}. **[{t}]({u})** ({d})  ",f"   {md}",""]
g+=["Media contact: info@theinfinitumcorporation.com · 202-729-9509",""]
open("X-ARTICLES.md","w").write("\n".join(g))
# itemlist JSON-LD for website draft
il={"@context":"https://schema.org","@type":"ItemList","name":"X Articles by William Aaron Turner","itemListElement":[{"@type":"ListItem","position":n,"url":u,"name":t} for n,t,u,d,md,st in idx]}
open("itemlist.jsonld","w").write(json.dumps(il,indent=1,ensure_ascii=False))
print("ok")
