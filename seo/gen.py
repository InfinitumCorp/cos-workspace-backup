import json,re,os,glob
from bs4 import BeautifulSoup
LIVE='/workspace/seo/live/'
UF='https://ukrainianfiles.blogspot.com'; WP='https://infinitumwhitepapers.blogspot.com'
TG='https://t.me/infinitumcorporation'; X='https://x.com/infinitumceo'; DC='https://discord.gg/QVT7dWHUQa'
ORG='https://www.theinfinitumcorporation.com/#organization'
SERIES_BC=lambda name,url:[{"@type":"ListItem","position":1,"name":"The Ukraine Files","item":UF+"/"},{"@type":"ListItem","position":2,"name":"Full Series","item":UF+"/p/the-ukraine-files-full-series.html"},{"@type":"ListItem","position":3,"name":name,"item":url}]
def live(fn):
    s=BeautifulSoup(open(LIVE+fn).read(),'html.parser')
    ld=[json.loads(j.string) for j in s.find_all('script',type='application/ld+json')]
    bp=[x for x in ld if isinstance(x,dict) and x.get('@type')=='BlogPosting']
    b=s.find(class_='post-body'); img=b.find('img') if b else None
    return dict(dp=bp[0]['datePublished'] if bp else None,dm=bp[0]['dateModified'] if bp else None,
      img=img['src'] if img else None,alt=(img.get('alt') or '') if img else '',
      title=s.title.string,desc=(s.find('meta',attrs={'name':'description'}) or {}).get('content',''))
def f(u): return re.sub(r'\W+','_',u.split('//')[1])+'.html'

P=[]  # entries
def add(**k): P.append(k)
# ---------------- Ukraine Files: posts ----------------
add(id='uf-01',blog='uf',kind='post',url=UF+'/2026/10/ukraine-aid-ngos-audit-donations.html',
 title='Ukraine Aid NGOs: How to Audit Where Donations Go',
 desc='How to audit a Ukraine aid NGO: registrations, Form 990 filings and funders, plus the claims The Ukraine Files makes. Full article coming soon.',
 labels=['Aid & NGOs','Ukraine Files Series'],permalink='ukraine-aid-ngos-audit-donations (keep)',
 primary='audit Ukraine aid NGO',secondary=['how to check a charity before donating','Ukraine charity Form 990','Ukraine aid NGO funders'],
 longtail=['how to trace where Ukraine aid donations go','how to verify a Ukraine charity is legitimate','Ukraine NGO tax filings and funders'],
 serp='Top results for charity-vetting queries are Charity Navigator, Candid, BBB Give.org, FTC and DC DISB consumer pages (WebSearch 2026-10-26). Those are generic consumer guides; the open angle is a funder-and-filings audit method specific to Ukraine NGOs.',
 alt='Ukraine aid NGO donation audit: tracing funders, tax filings and registrations, The Ukraine Files',
 links_in=['/2026/10/russia-economy-sanctions-gdp-aid.html','/2026/10/zelenskyy-rise-backers-media-network.html'],
 links_out=['Link the words "Form 990" and "Charity Navigator / Candid" to the primary registries (candid.org, charitynavigator.org) as rel=noopener outbound authority links.'],
 issues=['Image alt text is empty.','Teaser only (309 words): thin content. Either expand when the X Article is published or keep indexable but do not promote as a pillar.','Description ends "Full article coming soon", which reads weak in results. Update when full text lands.'],
 about='Auditing Ukraine aid NGOs and charity donations',kw='Ukraine aid, NGO audit, donations, Form 990, charity vetting')
add(id='uf-02',blog='uf',kind='post',url=UF+'/2026/10/russia-economy-sanctions-gdp-aid.html',
 title="Russia's Economy Under Sanctions: GDP, Aid, Stalemate",
 desc="What the GDP, sanctions-count and aid figures say about Russia's economy, and where The Ukraine Files argues Western strategy has stalled.",
 labels=['Sanctions & Economy','Russia & the World','Ukraine Files Series'],permalink='russia-economy-sanctions-gdp-aid (keep)',
 primary='Russia economy under sanctions',secondary=['Russia GDP growth 2026','sanctions effectiveness Russia','Ukraine Defense Contact Group Ramstein'],
 longtail=['is Russia economy collapsing under sanctions 2026','Russia GDP growth forecast 2026 IMF World Bank','how Russia adapted to Western sanctions'],
 serp='SERP leaders: Reuters (Russia cut 2026 growth forecast to 0.4%, May 2026), World Bank (0.8% for 2026), IMF October update (0.9%), BOFIT (about 1%), Carnegie (WebSearch 2026-10-26). Freshness matters for this query class.',
 alt='Russia economy under sanctions: GDP, aid and battlefield figures, The Ukraine Files Part 2',
 links_in=['/2026/10/eastern-economic-forum-2026-vladivostok.html'],links_out=['Cite IMF WEO and World Bank pages as outbound links beside the GDP discussion.'],
 issues=['Image alt text is empty.','FACT FLAG (body not changed): post cites the European Commission raising Russia 2026 GDP growth to 1.3%. Later sources found: Russian government cut its own forecast to 0.4% (Reuters, May 2026), World Bank 0.8%, IMF 0.9% (Oct 2026). William should decide whether to add a dated update note.'],
 about="Russia's economy under Western sanctions",kw='Russia economy, sanctions, GDP, Ramstein, Ukraine aid')
add(id='uf-03',blog='uf',kind='post',url=UF+'/2026/10/eastern-economic-forum-2026-vladivostok.html',
 title='Eastern Economic Forum 2026: Is Russia Isolated?',
 desc='The 11th Eastern Economic Forum in Vladivostok: who attended, what was signed, and what it says about Russia and isolation. Sources inside.',
 labels=['Russia & the World','Sanctions & Economy','Ukraine Files Series'],permalink='eastern-economic-forum-2026-vladivostok (keep)',
 primary='Eastern Economic Forum 2026',secondary=['EEF 2026 Vladivostok','Eastern Economic Forum agreements signed','Russia Asia pivot'],
 longtail=['how many countries attended Eastern Economic Forum 2026','is Russia isolated 2026','Eastern Economic Forum 2026 agreements value rubles'],
 serp='SERP leaders: the organizer final PDF (forumvostok.ru), TASS, Kommersant, JETRO (WebSearch 2026-10-26). Organizer figures: 1-4 Sept 2026, 9,300+ participants, 78 countries, 328 agreements worth RUB 6.815 trillion.',
 alt='Eastern Economic Forum 2026 in Vladivostok: delegations, agreements and the isolation question',
 links_in=['/2026/10/russia-economy-sanctions-gdp-aid.html'],links_out=['Link the organizer site forumvostok.ru for the headline figures.'],
 issues=['Image alt text is empty.','FACT FLAG (body not changed): post says 80 countries and 5,000+ representatives and a 358-agreement 2025 baseline. Organizer final results say 78 countries, 9,300+ participants, 328 agreements, RUB 6.815 trillion. Early in-forum TASS counts said 7,000+ and nearly 80 countries, so the post may reflect a mid-forum count. Suggest William adds a dated update line.'],
 about='Eastern Economic Forum 2026 in Vladivostok',kw='Eastern Economic Forum, EEF 2026, Vladivostok, Russia, sanctions')
add(id='uf-04',blog='uf',kind='post',url=UF+'/2026/10/in-q-tel-cia-venture-capital-explained.html',
 title="In-Q-Tel Explained: The CIA's Venture Capital Arm",
 desc="What In-Q-Tel is, how it funds startups, and the Palantir, Anduril, Capella and ICEYE links to Ukraine and defense tech that The Ukraine Files traces.",
 labels=['Intelligence & Tech','Aid & NGOs','Ukraine Files Series'],permalink='in-q-tel-cia-venture-capital-explained (keep)',
 primary='In-Q-Tel',secondary=['CIA venture capital arm','In-Q-Tel portfolio companies','In-Q-Tel Palantir Anduril'],
 longtail=['what is In-Q-Tel and who funds it','In-Q-Tel investments in Ukraine defense tech','how In-Q-Tel invests: technology development agreements'],
 serp='SERP leaders: iqt.org (About, Portfolio), Fortune, Stanford SVUSG (WebSearch 2026-10-26). IQT states a development agreement is typically $500K-$3M and equity-only $250K-$500K. The head term is owned by iqt.org; the realistic target is the long-tail "CIA venture capital arm" plus the Ukraine angle.',
 alt="In-Q-Tel explained: the CIA's venture capital arm and its defense-tech portfolio, The Ukraine Files",
 links_in=['/2026/10/zelenskyy-rise-backers-media-network.html','/2026/10/ukraine-aid-ngos-audit-donations.html'],links_out=['Link iqt.org (About, Portfolio) where the post describes structure and portfolio.'],
 issues=['Labelled "Aid & NGOs": consider dropping that label, it dilutes the topic cluster (optional).'],
 about='In-Q-Tel, the CIA-backed venture investor',kw='In-Q-Tel, IQT, CIA, venture capital, Palantir, Anduril')
add(id='uf-05',blog='uf',kind='post',url=UF+'/2026/10/ukraine-organ-trade-allegations.html',
 title='Ukrainian Casualties and Organ-Trade Allegations: Sources',
 desc="My investigation's organ-trafficking claims tied to the war in Ukraine, with named sources and denials. Read the full original X Article.",
 labels=['Casualties & Human Cost','Ukraine Files Series'],permalink='ukraine-organ-trade-allegations (keep)',
 primary='Ukraine organ trade allegations',secondary=['organ trafficking allegations war in Ukraine','black transplantology claims','Sboyev case organ'],
 longtail=['Ukraine organ harvesting allegations sources and denials','OSCE organ trafficking Ukraine statement','prisoner exchange organ claims'],
 serp='SERP is dominated by fact-checks and denials: OSCE statement, VOA fact-checks, EFE Verifica, VoxUkraine (WebSearch 2026-10-26). The post already frames claims as allegations with named sources and denials, which suits this SERP. Keep that framing in all snippets; do not use stronger wording in meta tags.',
 alt='Organ-trade allegations tied to the war in Ukraine: named sources and denials, The Ukraine Files',
 links_in=['/2026/10/ukraine-forced-mobilization-evidence.html'],links_out=['Outbound-link the OSCE and fact-check pages the post already discusses, if present in the denials section.'],
 issues=['Existing description is already accurate; only trimmed to the 150-character limit.'],
 about='Allegations of organ trafficking linked to the war in Ukraine, and the denials',kw='organ trade allegations, Ukraine, sources, denials')
add(id='uf-06',blog='uf',kind='post',url=UF+'/2026/10/zelenskyy-rise-backers-media-network.html',
 title="Zelenskyy's Rise: Backers, Media and Political Network",
 desc="How Volodymyr Zelenskyy went from entertainer to president, who backed him, and why The Ukraine Files argues his rise was engineered.",
 labels=['Politics & Power','Intelligence & Tech','Aid & NGOs','Ukraine Files Series'],permalink='zelenskyy-rise-backers-media-network (keep)',
 primary='Zelensky rise to power',secondary=['Zelensky backers Kolomoisky 1+1','Servant of the People media network','Zelensky political network FARA'],
 longtail=['who backed Zelensky 2019 election campaign','Zelensky Kolomoisky relationship explained','Zelensky comedian to president timeline'],
 serp='SERP leaders: Atlantic Council (Kolomoisky), ECFR, academic papers on the 2019 campaign (WebSearch 2026-10-26). Note spelling: the post uses "Zelenskyy", most search demand text uses "Zelensky"; include both in body headings/alt where natural.',
 alt="Zelenskyy (Zelensky) rise to power: backers, media and political network, The Ukraine Files",
 links_in=['/2026/10/in-q-tel-cia-venture-capital-explained.html'],links_out=['Link Atlantic Council and ECFR pieces where the post discusses Kolomoisky and oligarch relations.'],
 issues=['Spelling split Zelenskyy/Zelensky: add "Zelensky" once in the alt text and first paragraph (done in alt text below, body unchanged).'],
 about='Volodymyr Zelenskyy, his backers and media network',kw='Zelenskyy, Zelensky, Kolomoisky, Servant of the People, FARA')
add(id='uf-07',blog='uf',kind='post',url=UF+'/2026/10/ukraine-forced-mobilization-evidence.html',
 title="Ukraine's Forced Mobilization: Reports, Evidence, Law",
 desc="What reports, cases and official statements say about forced mobilization in Ukraine, plus the Russian civilian toll. Claims and sources laid out.",
 labels=['Mobilization','Casualties & Human Cost','Ukraine Files Series'],permalink='ukraine-forced-mobilization-evidence (keep)',
 primary='Ukraine forced mobilization',secondary=['TCC conscription officers complaints','Ukraine ombudsman Lubinets mobilization complaints','busification Ukraine'],
 longtail=['Ukraine ombudsman complaints against enlistment officers 2025','Ukraine forced conscription reports and law','TCC detention violations Ukraine'],
 serp='SERP leaders: the Ukrainian Ombudsman site, Kyiv Independent, UNN (6,127 complaints in 2025, 3,312 in 2024, 514 in 2023, 18 in 2022; WebSearch 2026-10-26). The post already cites 3,312 and 6,127, which matches.',
 alt="Ukraine's forced mobilization: reports, evidence and law, The Ukraine Files Part 7",
 links_in=['/2026/10/blog-post_26.html (companion article, currently not linked back)'],links_out=['Link the Ombudsman release and Kyiv Independent report next to the complaint statistics.'],
 issues=['Body links to no post for the companion article: add a visible link to /2026/10/blog-post_26.html where the post says it combines it with The Kidnapping of a Nation (post 9 links here, this one does not link back).'],
 about='Forced mobilization and conscription practices in Ukraine',kw='Ukraine mobilization, TCC, conscription, ombudsman, busification')
add(id='uf-08',blog='uf',kind='post',url=UF+'/2026/10/demining-ngos-intelligence-laos-moldova.html',
 title='Demining NGOs and Intelligence: The Laos and Moldova Claims',
 desc="Russian sappers in Laos versus Western mine-action NGOs: the intelligence-front allegations in The Ukraine Files, with the cited sources.",
 labels=['Aid & NGOs','Intelligence & Tech','Ukraine Files Series'],permalink='demining-ngos-intelligence-laos-moldova (keep)',
 primary='demining NGOs intelligence',secondary=['HALO Trust funding State Department','Russian demining in Laos IMAC','Kolbasna Moldova'],
 longtail=['HALO Trust board and funding sources','Russia humanitarian demining Laos since 2018','mine action NGO intelligence allegations'],
 serp='SERP leaders: halotrust.org (boards, funding), Lao KPL and Russian MFA pages on IMAC Laos (eighth mission completed spring 2026: 228+ hectares, 4,367 items, 213 sappers trained), Counter-IED Report (WebSearch 2026-10-26).',
 alt='Demining NGOs and intelligence claims: Russian sappers in Laos and HALO Trust funding, The Ukraine Files',
 links_in=['/2026/10/in-q-tel-cia-venture-capital-explained.html'],links_out=['Link halotrust.org boards and annual report where funders are named.'],
 issues=['None critical. Body stats (2 million sq m cleared since 2018) are consistent with 228+ hectares reported by Lao/Russian sources.'],
 about='Demining NGOs and intelligence allegations in Laos and Moldova',kw='demining, HALO Trust, IMAC, Laos, Moldova, NGOs, intelligence')
add(id='uf-09',blog='uf',kind='post',url=UF+'/2026/10/blog-post_26.html',
 title='Russian Civilian Casualties and Ukrainian Strikes: Cases, Sources, Claims',
 title_alt='Russian Civilian Casualties and Ukrainian Strikes: Sources',
 desc='Russian civilian deaths and Ukrainian strikes: Wildberries, Arkhipo-Osipovka, Nizhnekamsk and border cases with BBC, AP and ABC sources.',
 labels=['Casualties & Human Cost','Russia & the World','Ukraine Files Series'],permalink='NOT custom: live URL is blog-post_26.html. Ideal slug: russian-civilian-casualties-ukrainian-strikes. Blogger cannot change a published permalink; leave it, or create a new post and add Settings > Errors and redirects > custom redirect (permanent).',
 primary='Russian civilian casualties Ukrainian strikes',secondary=['Wildberries warehouse strike','Belgorod civilian deaths','Nizhnekamsk TANECO strike'],
 longtail=['Russian civilians killed Ukrainian strikes 2026 BBC','Wildberries warehouse strikes killed employees','Arkhipo-Osipovka beach strike'],
 serp='SERP leaders: BBC News articles on 2026 Belgorod strikes and the Wildberries warehouse strikes (BBC: eight killed, 62 injured on 18 July 2026), Eastern Herald (WebSearch 2026-10-26). Event-specific long-tails are less contested than the head term.',
 alt='Russian civilian casualties and Ukrainian strikes: Wildberries, Arkhipo-Osipovka and Nizhnekamsk cases, The Ukraine Files',
 links_in=['/2026/10/ukraine-forced-mobilization-evidence.html (this post links to it; reverse link missing)','/p/the-ukraine-files-full-series.html (hub does not list it)'],links_out=['Link the BBC and AP articles named in the body to their canonical URLs.'],
 issues=['Auto-generated permalink blog-post_26.html (no keywords).','No labels set: add the three suggested labels.','Missing from the hub page list and from the Previous/Next series navigation.','Newest post (2026-10-26) so not yet in the Popular Posts list.'],
 about='Russian civilian casualties from Ukrainian strikes in 2026',kw='Russian civilian casualties, Ukrainian strikes, Wildberries, Belgorod, TANECO')
add(id='uf-10',blog='uf',kind='post',nolive=True,url=UF+'/2026/10/infinitum-corporation-defense-technology-advisory.html',
 title='Where Warfare Meets Technology: Infinitum Defense Advisory',
 desc='How Infinitum Corporation is expanding defense advisory work in cybersecurity, ISTAR, electronic warfare and AI, by founder William Aaron Turner.',
 labels=['Infinitum Corporation','Cybersecurity','Defense Technology','William Aaron Turner'],permalink='infinitum-corporation-defense-technology-advisory (as in manifest)',
 primary='defense technology advisory Washington DC',secondary=['cybersecurity ISTAR electronic warfare consulting','Infinitum Corporation defense advisory','irregular warfare analysis consulting'],
 longtail=['defense technology advisory firm Washington DC','AI for defense and cybersecurity consulting'],
 serp='Local-intent query: DC competitors found were The Wolverine Group, CADRE and DC Strategic Group (WebSearch 2026-10-26). Add DC address, phone 202-729-9509, open 24 hours and the Telegram/X/Discord links to the closing section.',
 alt='Infinitum Corporation defense technology advisory: cybersecurity, ISTAR, electronic warfare and AI',
 links_in=['/p/about.html','/2026/10/in-q-tel-cia-venture-capital-explained.html'],links_out=['Link www.theinfinitumcorporation.com with keyword anchor.'],
 issues=['LIVE URL RETURNS 404 on both blogs (not in the Ukraine Files feed or sitemap). An earlier browser task reported editing it (post id 763564419624243468), so it may have been reverted to draft or deleted. The press plan (press/blog-promo-plan.md, release U1, Oct 28) links to this URL: do not submit until it is live again.','Original title is 85 characters; shorter title suggested.'],
 about='Infinitum Corporation defense technology advisory',kw='defense advisory, cybersecurity, ISTAR, electronic warfare, Infinitum Corporation')
# ---------------- Ukraine Files: pages ----------------
add(id='uf-page-hub',blog='uf',kind='page',url=UF+'/p/the-ukraine-files-full-series.html',title='The Ukraine Files: Full Series',
 desc='The complete Ukraine Files series by William Aaron Turner: sanctions, the Eastern Economic Forum, In-Q-Tel, NGOs and mobilization, in reading order.',
 labels=[],permalink='the-ukraine-files-full-series (keep)',primary='The Ukraine Files series',secondary=['William Aaron Turner Ukraine Files','Ukraine Files full series'],longtail=['The Ukraine Files reading order'],serp='Brand/navigational page: the hub for internal links; should be the first sitelink candidate.',
 alt='The Ukraine Files full series index',links_in=[],links_out=[],issues=['Does not list the companion post (blog-post_26.html).','No og:image on pages (Blogger only sets it when the page has an image): add a banner image to the page body.'],about='The Ukraine Files series by William Aaron Turner',kw='Ukraine Files, series, William Aaron Turner')
add(id='uf-page-about',blog='uf',kind='page',url=UF+'/p/about.html',title='About William Aaron Turner and The Ukraine Files',title_alt='About William Aaron Turner | The Ukraine Files',
 desc='William Aaron Turner, President of Infinitum Corporation: the mission behind The Ukraine Files, how each post is built and how to reach me.',
 labels=[],permalink='about (keep)',primary='William Aaron Turner',secondary=['William Aaron Turner Infinitum Corporation','The Ukraine Files author'],longtail=['who is William Aaron Turner Infinitum Corporation'],serp='Entity page: used as the Person @id in structured data. Make it the sameAs hub for Telegram, X, Discord and the company site.',
 alt='William Aaron Turner, President of Infinitum Corporation',links_in=[],links_out=[],issues=['No image: add a portrait/logo with alt text for og:image.','Person JSON-LD sameAs lacks Telegram and Discord.'],about='William Aaron Turner, President of Infinitum Corporation',kw='William Aaron Turner, Infinitum Corporation, Ukraine Files')
add(id='uf-page-contact',blog='uf',kind='page',url=UF+'/p/contact.html',title='Contact The Ukraine Files and Infinitum Corporation',
 desc='Contact William Aaron Turner and The Ukraine Files: email info@theinfinitumcorporation.com or reach me on X at @infinitumceo. Open 24 hours.',
 labels=[],permalink='contact (keep)',primary='contact William Aaron Turner',secondary=['Infinitum Corporation contact'],longtail=[],serp='Low-volume utility page. Add NAP: 1629 K Street NW, Suite 300, Washington, DC 20006; 202-729-9509; open 24 hours; Telegram, X, Discord links.',
 alt='Contact Infinitum Corporation, Washington, DC',links_in=[],links_out=[],issues=['Only 50 words and no address/phone: add NAP block (body addition, no claims changed).','Title "Contact" is generic.'],about='Contact details for Infinitum Corporation',kw='contact, Infinitum Corporation, Washington DC')
add(id='uf-page-privacy',blog='uf',kind='page',url=UF+'/p/privacy-policy.html',title='Privacy Policy',desc='Privacy information for The Ukraine Files blog: cookies, Google services, the survey form and comments.',
 labels=[],permalink='privacy-policy (keep)',primary='privacy policy',secondary=[],longtail=[],serp='Utility page: no ranking goal. Consider noindex via per-page robots (Blogger: custom robots tags per post/page) so it does not dilute the site.',
 alt='n/a',links_in=[],links_out=[],issues=['105 words; leave as is.'],about='Privacy policy',kw='privacy')
# ---------------- Whitepapers ----------------
add(id='wp-01',blog='wp',kind='post',url=WP+'/2026/10/dead-reckoning-ai-security-operations.html',
 title='Dead Reckoning: AI for Security Operations (Whitepaper)',
 desc="Infinitum Corporation's first whitepaper: how AI, governance and independent checks help security teams navigate jammed, spoofed signals.",
 labels=['AI','Cybersecurity','Security Operations','Whitepaper','Infinitum Corporation'],permalink='dead-reckoning-ai-security-operations (keep)',
 primary='AI for security operations',secondary=['AI in the SOC','security AI automation breach cost','resilient PNT security operations','NIST AI RMF governance'],
 longtail=['AI for security operations whitepaper 2026','does security AI reduce data breach cost','independent second source GNSS spoofing security teams','dead reckoning cybersecurity'],
 serp='IBM Cost of a Data Breach 2026 (WebSearch 2026-10-26): extensive security AI and automation saves an average $1.93M per breach ($5.93M down to $4.00M), matching the post figures; only 36% of breached organizations use these tools extensively. Resilient PNT results are dominated by CISA, NIST (IR 8323, TN 2187) and DHS. Head terms are enterprise vendor-owned; target the whitepaper and "dead reckoning" long-tails.',
 alt='Cover of Infinitum Corporation Whitepaper 01, Dead Reckoning: AI for Security Operations',
 links_in=['(none today) link to Special Edition 01 and to the Infinitum site'],links_out=['Link IBM Cost of a Data Breach 2026 and Verizon DBIR where the post cites figures; link www.theinfinitumcorporation.com with anchor "Infinitum Corporation cybersecurity consulting in Washington, DC".'],
 issues=['No internal links to the other whitepaper or to the company site.','Hero image served from raw.githubusercontent.com: slow/unstable host and no image metadata; upload the cover to Blogger so it is served by googleusercontent.','No Organization JSON-LD (only Blogger default BlogPosting with publisher "Blogger").','H1 on post pages is the blog title, post title is not the H1 (template issue): fix in theme (post title in h1/h3.post-title).','Publish timezone is Pacific (-07:00) vs company Moscow/DC: cosmetic.'],
 about='AI for security operations and independent signal checks',kw='AI for security operations, SOC, whitepaper, dead reckoning, NIST AI RMF')
add(id='wp-special01',blog='wp',kind='post',url=WP+'/2026/10/russia-state-influenced-capitalism.html',
 title="Russia's State-Influenced Capitalism: A Sanctions Whitepaper",
 desc="Infinitum Corporation Special Edition 01: an argued-position paper on Russia's state-influenced capitalism, with every figure sourced.",
 labels=['Russia','Sanctions','Special Edition','Whitepaper','Infinitum Corporation'],permalink='russia-state-influenced-capitalism (keep)',
 primary='Russia state-influenced capitalism',secondary=['Russia sanctions resilience','state capitalism Russia analysis','Russia public debt unemployment IMF'],
 longtail=['why Russia economy survived sanctions','Russia state capitalism sanctions-proof whitepaper','Russia 1990s GDP decline World Bank'],
 serp='SERP leaders: PIIE policy brief on Russia state capitalism, Carnegie, Cambridge University Press, Springer (WebSearch 2026-10-26). Those are academic; a plain-language whitepaper with sourced figures has room under long-tails.',
 alt="Cover of Infinitum Corporation Special Edition 01, Russia's State-Influenced Capitalism",
 links_in=['(none today) link to Whitepaper 01 and to The Ukraine Files economy posts'],links_out=['Link the World Bank, IMF and Castellum.AI pages named in the key figures.'],
 issues=['Title is 80 characters: the search result cuts it. Suggested shorter title keeps the same subject (original subtitle "Sanctions-Proof, War-Proof, and Chaos-Proof" stays in the first heading/dek).','Same image-host, JSON-LD, internal-link and H1 issues as Whitepaper 01.'],
 about="Russia's state-influenced capitalism and sanctions resilience",kw='Russia, state capitalism, sanctions, whitepaper, special edition')
# ---------------- Home pages ----------------
add(id='uf-home',blog='uf',kind='home',url=UF+'/',title='The Ukraine Files | William Aaron Turner',
 desc='The Ukraine Files: sourced analysis of Ukraine aid NGOs, In-Q-Tel, sanctions and mobilization by William Aaron Turner of Infinitum Corporation.',
 labels=[],permalink='/',primary='The Ukraine Files',secondary=['William Aaron Turner blog','Ukraine NGO In-Q-Tel sanctions analysis'],longtail=[],serp='Brand home: rename the blog title (Settings > Title) from "Ukrainian Files" to "The Ukraine Files" so title, posts, About page and X Articles use one name.',
 alt='The Ukraine Files header banner',links_in=[],links_out=[],issues=['Blog title "Ukrainian Files" differs from "The Ukraine Files" used everywhere else.','Home page shows full post bodies; set Settings > Posts > show Jump break / 7 posts per page to avoid duplicate content between home and posts.'],about='The Ukraine Files blog',kw='Ukraine Files, William Aaron Turner')
add(id='wp-home',blog='wp',kind='home',url=WP+'/',title='Infinitum Corporation Whitepapers | Security Research',
 desc='Free security and technology whitepapers from Infinitum Corporation, Washington, DC. Written by William Aaron Turner. Open 24 hours.',
 labels=[],permalink='/',primary='Infinitum Corporation whitepapers',secondary=['cybersecurity whitepaper','AI security operations whitepaper'],longtail=[],serp='Brand home page.',
 alt='Infinitum Corporation Whitepapers banner',links_in=[],links_out=[],issues=['Blog description lacks the DC headquarters/Telegram/X/Discord links in a visible widget; add them in a Link List gadget.'],about='Infinitum Corporation whitepapers',kw='Infinitum Corporation, whitepapers, cybersecurity')

# validation
for p in P:
    assert len(p['title'])<=60 or p.get('title_alt'),(p['id'],len(p['title']))
    print(p['id'],len(p['title']),len(p['desc'])) if len(p['desc'])>150 or (len(p['title'])>60 and not p.get('title_alt')) else None
print('ok')
# JSON-LD builders
def ld_org(blog):
    own = UF+'/' if blog=='uf' else WP+'/'
    return {"@context":"https://schema.org","@graph":[
     {"@type":["Organization","ProfessionalService"],"@id":ORG,"name":"Infinitum Corporation","url":"https://www.theinfinitumcorporation.com",
      "description":"International security and technology consulting firm headquartered in Washington, DC, with Moscow as an operating location. Cybersecurity, IT and network security, ethical hacking, ISTAR, irregular warfare analysis and defense technology advisory. Open 24 hours.",
      "email":"info@theinfinitumcorporation.com","telephone":"+1-202-729-9509",
      "address":{"@type":"PostalAddress","streetAddress":"1629 K Street NW, Suite 300","addressLocality":"Washington","addressRegion":"DC","postalCode":"20006","addressCountry":"US"},
      "openingHoursSpecification":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"},
      "founder":{"@id":UF+"/p/about.html#william-aaron-turner"},
      "sameAs":[TG,X,DC,"https://github.com/InfinitumCorp",UF+"/",WP+"/"]},
     {"@type":"Person","@id":UF+"/p/about.html#william-aaron-turner","name":"William Aaron Turner","jobTitle":"Founder and President","url":UF+"/p/about.html","worksFor":{"@id":ORG},
      "sameAs":[X,TG,"https://www.theinfinitumcorporation.com"]},
     {"@type":"WebSite","@id":own+"#website","url":own,"name":"The Ukraine Files" if blog=='uf' else "Infinitum Corporation Whitepapers","publisher":{"@id":ORG},"inLanguage":"en"}]}
def ld_post(p,l):
    own=UF if p['blog']=='uf' else WP
    out=[]
    bp={"@context":"https://schema.org","@type":"BlogPosting","@id":p['url']+"#article","mainEntityOfPage":{"@type":"WebPage","@id":p['url']},
        "headline":p.get('title_alt') or p['title'] if p['kind']=='post' else p['title'],"description":p['desc'],"keywords":p['kw'],
        "about":p['about'],"inLanguage":"en","author":{"@id":UF+"/p/about.html#william-aaron-turner"},"publisher":{"@id":ORG},
        "isPartOf":{"@id":own+"/#website"}}
    if l['dp']: bp['datePublished']=l['dp']; bp['dateModified']=l['dm']
    if l['img']: bp['image']=l['img']
    if p['kind']=='post': out.append(bp)
    if p['blog']=='uf' and p['kind']=='post':
        out.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":SERIES_BC(p['title'],p['url'])})
    elif p['kind']=='post':
        out.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Infinitum Corporation Whitepapers","item":WP+"/"},{"@type":"ListItem","position":2,"name":p['title'],"item":p['url']}]})
    elif p['kind']=='page':
        pg={"@context":"https://schema.org","@type":"AboutPage" if 'about' in p['url'] else "CollectionPage" if 'series' in p['url'] else "WebPage","@id":p['url'],"url":p['url'],"name":p['title'],"description":p['desc'],"isPartOf":{"@id":own+"/#website"},"publisher":{"@id":ORG}}
        if 'about' in p['url']: pg['mainEntity']={"@id":UF+"/p/about.html#william-aaron-turner"}
        out.append(pg)
    return out
# write files
man=[]
for p in P:
    fn=f(p['url']) if p['kind']!='home' else None
    l=live(f(p['url'])) if not p.get('nolive') else dict(dp=None,dm=None,img=None,alt='',title='(404 - not live)',desc='')
    p['live']=dict(title=l['title'],desc=l['desc'],alt=l['alt'])
    ld=ld_post(p,l)
    fnout=f"/workspace/seo/posts/{p['id']}.md"
    ttl=p.get('title_alt') or p['title']
    md=[f"# {p['id']}: {p['title']}",f"- Live URL: {p['url']}",f"- Type: {p['kind']} ({'Ukraine Files blog' if p['blog']=='uf' else 'Whitepapers blog'})",
      "","## Current (live)",f"- Title tag: {l['title']} ({len(l['title'] or '')} chars)",f"- Meta description: {l['desc']} ({len(l['desc'])} chars)",f"- First image alt: {l['alt']!r}","",
      "## Optimized","- Post title / title tag (<=60): "+f"{p['title']} ({len(p['title'])} chars)"+("" if len(p['title'])<=60 else f"  -> use shorter: {p['title_alt']} ({len(p['title_alt'])} chars)"),
      f"- Meta / search description (<=150, covers 155 limit): {p['desc']} ({len(p['desc'])} chars)",
      f"- Labels: {', '.join(p['labels']) or 'n/a'}",f"- Permalink: {p['permalink']}",f"- Image alt text: {p['alt']}","",
      "## Keywords (no search volumes: none available from the tools used; SERP observations only)",f"- Primary: {p['primary']}",f"- Secondary: {'; '.join(p['secondary']) or 'n/a'}",f"- Long tail: {'; '.join(p['longtail']) or 'n/a'}",f"- SERP evidence: {p['serp']}","",
      "## Internal / outbound linking",f"- Add links to/from: {'; '.join(p['links_in']) or 'n/a'}",f"- Outbound authority links: {'; '.join(p['links_out']) or 'n/a'}","",
      "## Issues found"]+[f"- {i}" for i in p['issues']]+["","## JSON-LD (paste in HTML view at the bottom of the body; site-wide Organization graph is separate: snippets/)",""]
    for o in ld: md+=["```html",'<script type="application/ld+json">',json.dumps(o,indent=2,ensure_ascii=False),'</script>',"```",""]
    open(fnout,'w').write('\n'.join(md))
    man.append(dict(id=p['id'],blog=p['blog'],kind=p['kind'],url=p['url'],current_title=l['title'],new_title=p['title'],new_title_short=p.get('title_alt'),
        current_description=l['desc'],new_description=p['desc'],search_description=p['desc'],labels=p['labels'],permalink=p['permalink'],image_alt=p['alt'],
        primary_keyword=p['primary'],secondary_keywords=p['secondary'],long_tail=p['longtail'],file=fnout,applied_live=False))
json.dump(man,open('/workspace/seo/seo-manifest.json','w'),indent=1,ensure_ascii=False)
# site-wide snippets
for b,nm in (('uf','ukrainianfiles'),('wp','infinitumwhitepapers')):
    open(f'/workspace/seo/snippets/{nm}-sitewide-jsonld.html','w').write('<script type="application/ld+json">\n'+json.dumps(ld_org(b),indent=2,ensure_ascii=False)+'\n</script>\n')
print(len(P),'entries')
