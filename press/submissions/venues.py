exec(open('build.py').read().split('# shared attachments')[0])
sh='_shared'
rows=[]
def email(v,to,subj,body,atts=(),status='ready',notes='',method='email',addr=None,url=''):
    p=d(v); wr(f'{p}/email.txt',f"TO: {to}\nSUBJECT: {subj}\nATTACHMENTS: {', '.join(atts) or 'none'}\n\n---BODY---\n{body}")
    rows.append((v,method,addr or to,subj,f'press/submissions/{v}/email.txt',atts,status,notes,url))
def other(v,method,addr,fname,text,atts=(),status='ready',notes='',subj='—',url=''):
    p=d(v); wr(f'{p}/{fname}',text); rows.append((v,method,addr,subj,f'press/submissions/{v}/{fname}',atts,status,notes,url))
A=lambda f:f'press/submissions/_shared/{f}'

# 0 Strategic Culture
rows.append(('00-strategic-culture','email','info@strategic-culture.su','—','—',(),'skipped: already emailed (sent earlier today)','',''))

# 1 Global Research
body=f"""Dear Editor,

Please consider the article below for publication on Global Research. It was first published as an X Article and on my blog The Ukraine Files ({U['iqt']}); you are welcome to republish it in full with a link back.

{iqt_title.upper()}
{BY}

{iqt}

---
{ "_"+BIO1+"_" }

Contact: {PHONE} | {EMAIL}

Best regards,
{SIG}

{LINKS}"""
email('01-global-research','crgeditor@yahoo.com',f'Article submission: {iqt_title}',body,
 status='ready',notes=f'Article in email body per guidelines (no attachment). {words(iqt)} words. Bio in italics (underscores mark italics; set italic in Gmail). v2 text has inline sources but no endnote list. Alternates: Useful Idiots, Sweeps and Spies.',
 url='https://www.globalresearch.ca/submission-guidelines/17320')

# 2 Antiwar
body=f"""Dear Antiwar.com editors,

I'd like to offer my article "{ui_title}" for republication on Antiwar.com. It is not original to you: it was first published on my blog, The Ukraine Files ({U['ui']}). The Word file is attached; sources are listed and linked at the end.

The piece documents, from Western reporting (The Guardian, The Intercept, Responsible Statecraft, Bloomberg, the DoD Inspector General and others), how members of Congress, retired generals, lobbyists and defense contractors profit from prolonging the Ukraine war: stock trading around weapons packages, the Pentagon revolving door, and weapons leakage. It runs about 9,600 words; I'm glad to cut it to a length that suits you, or to split it into a series.

About me: {FIRST}

Best regards,
{SIG}

{LINKS}"""
email('02-antiwar','editor@antiwar.com' ,f'Submission (reprint): {ui_title}',body,(A('Turner_Useful-Idiots.docx'),),
 status='ready',notes='Word attachment, bio, title and linked sources; states it is a reprint. Address taken from the submissions page today. Very long (about 9,600 words); offers a cut or a series.',
 url='https://www.antiwar.com/submissions.php')

# 3 Countercurrents
keep=[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,18,19,20,34,35,36,37]
ps=ra_body.split('\n\n'); cc='\n\n'.join(ps[i] for i in keep)
cc_bio=BIO1
body=f"""{ra_title}
{BY}

{cc}

{cc_bio}

(A longer version with references was first published on the Russia-Africa Report: {U['ra']})

Image: Pull-quote graphic from "The Partnership That Delivers." Credit: Infinitum Corporation.

Contact: {PHONE} | {EMAIL}"""
email('03-countercurrents','editor@countercurrents.org','SUBMISSION',body,(A('russia-africa-pull-quote-1080x1350.jpg'),),
 status='ready',notes=f'Plain text in body, {words(cc)} words (<1,000), third-person bio, image with credit, no PDF. Condensed by cutting whole paragraphs from his article; no wording added. William may want to eyeball the cut.',
 url='https://countercurrents.org/countercurrents-submission-policy/')

# 4 Eurasia Review (form)
other('04-eurasia-review','form','https://www.eurasiareview.com/submit-an-article/ (contact form: Name, Email, Message)','form.txt',f"""Name: William Aaron Turner
Email: {EMAIL}
Message:
I'd like to pitch an original, previously unpublished analysis (800-2,000 words, AP style, fully sourced) for Eurasia Review. Proposed angles:
1) Africa as the Ukraine war's second front: Ukrainian drone teams in Mali and Sudan versus Russia's Africa Corps in the Sahel, and what the Sahel teaches both militaries.
2) After the 2026 Russia-Africa Summit: can floating nuclear plants and grain-for-fertilizer supply chains turn $27 billion in trade into Putin's $50 billion target?
3) AI in the security operations center: why mid-size organizations should treat AI triage as a new attack surface, not just a productivity tool (a practitioner's op-ed).

Affiliation: President, Infinitum Corporation (Washington, DC headquarters; Moscow operating location). I am an American serving as a contracted soldier in the Russian military (153rd Tank Regiment, currently in the SVO) and run my firm from Russian soil.
Past work: {U['ra']} ; {U['iqt']} ; {U['wp01']} ; https://orcid.org/0009-0002-1585-5442
If approved, I will send the Word file, a short bio and a high-resolution photo.""",
 status='needs-new-piece',notes='Pitch form text is ready to paste; the article itself must be written new (original-only). Angle 3 must not reuse the Academia Technical Note.',url='https://www.eurasiareview.com/submit-an-article/')

# 5 Modern Diplomacy
other('05-modern-diplomacy','email','authors@moderndiplomacy.eu','angles.md',f"""# Modern Diplomacy: needs a NEW piece written by William himself
Rules: not previously published; NO AI-generated or AI-assisted content; 1,000-1,500 words; British English; no footnotes; Word file; 50-100 word bio; subject "Submission – [Title]".
Because of the AI ban, no bot should draft this. Suggested angles for William to write:
1. A soldier's view of the Sahel: why African governments choose Russian security partners.
2. Sanctions at 15,000 measures: what the Russia-Africa trade numbers say about isolation.
3. The Eastern Economic Forum and Russia's turn to Asian markets.
When William's text is ready, email template:
SUBJECT: Submission – [Title]
BODY: Dear Editors, please find attached my original, unpublished article "[Title]" (about [N] words) for consideration. It is my own work and was written without AI assistance. Bio (75 words): {BIO_SHORT} He writes on Russia, sanctions and Russia-Africa relations. Contact: {PHONE} | {EMAIL}. Best regards, William Aaron Turner""",
 status='needs-new-piece',notes='Human-written only; William must write it himself.',subj='Submission – [Title]',url='https://moderndiplomacy.eu/contribute-modern-diplomacy/')

# 6 CounterPunch
body=f"""Dear CounterPunch editors,

Please consider my article "{ra_title}" ({words(ra_body)} words, within your 500-2,000 range). It was first published on my blog, the Russia-Africa Report ({U['ra']}). The full text is below and attached as a Word file.

{ra_title.upper()}
{BY}

{ra_body}

About the author: {BIO1}

Best regards,
{SIG}"""
email('06-counterpunch','counterpunch@counterpunch.org',f'Submission: {ra_title}',body,(A('Turner_Russia-Africa-Partnership-That-Delivers.docx'),),
 status='ready',notes='Address from venue list (page obfuscates it; confirm on https://www.counterpunch.org/about/). No response guaranteed.',url='https://www.counterpunch.org/about/')

# 7 Consortium News pitch (<=150 words)
pitch=("Pitch: Who profits from a war nobody is allowed to end? I propose an original piece tracing how U.S. lawmakers' stock trades, generals' post-retirement board seats and lobbyists' Ukrainian contracts line up with each new aid package, "
"using STOCK Act disclosures, DoD Inspector General audits, and reporting from The Intercept, The Guardian and Responsible Statecraft. "
"Qualifications: I am an American serving as a contracted soldier in the Russian military (153rd Tank Regiment, currently in the SVO) and President of Infinitum Corporation, a Washington, DC security consultancy. "
"I bring a frontline vantage no Western correspondent has, and I have researched this subject at length (published work: ukrainianfiles.blogspot.com). About 1,500 words, fully sourced.")
assert words(pitch)<=150, words(pitch)
email('07-consortium-news','submissions@consortiumnews.com','Pitch: Who profits from a war nobody is allowed to end?',
 f"Dear Editors,\n\n{pitch}\n\nWilliam Aaron Turner\nPhone: {PHONE} | Email: {EMAIL}",
 status='ready',notes=f'Pitch only ({words(pitch)} words in the pitch paragraph). If accepted, the article must be newly written for them. No follow-up; silence after 10 days = no.',url='https://consortiumnews.com/2025/01/19/writing-for-consortium-news/')

# 8 Libertarian Institute
other('08-libertarian-institute','email','editor@libertarianinstitute.org','HOLD-needs-confirmation.md',f"""# Libertarian Institute: HOLD, needs William to confirm authorship
Rules: Word doc, 600-1,800 words, bio, linked sources; reprints OK; NO AI-generated or AI-assisted content at all.
None of his on-disk pieces is confirmed as written by William without AI help, so nothing has been drafted for sending.
Candidates if William confirms he wrote them himself (and only those pieces):
- Russia-Africa: "{ra_title}" ({words(ra_body)} words, fits the limit as-is): {A('Turner_Russia-Africa-Partnership-That-Delivers.docx')}
- Medium: "Missiles, Murders and Media: A Tale of Two Warzones" (https://medium.com/@williamaaronturner/missiles-murders-and-media-a-tale-of-two-warzones-14af79d18ee9)
- Medium: "Friendly Fire" (https://medium.com/@williamaaronturner/friendly-fire-e70d34ae2221)
Email template once confirmed: SUBJECT: Submission: [Title] (reprint) / BODY: Dear Editor, attached is my article "[Title]" ([N] words), first published at [URL]. I wrote it myself without AI assistance. Sources are linked in the text. Bio: {BIO_SHORT} Contact: {PHONE} | {EMAIL}""",
 status='needs-confirmation',notes='AI ban: William must confirm which piece he wrote himself.',url='https://libertarianinstitute.org/submission/')

# 9 NEO
neo=f"""Dear Editors of New Eastern Outlook,

I would like to propose writing exclusive, original articles for New Eastern Outlook. I understand you publish only exclusive work that has not appeared on personal blogs or been sent to other outlets, so the pieces below are new and would be written for NEO alone (500-1,200 words each, with hyperlinked sources).

1) Africa as the second front of the Ukraine war: reported Ukrainian drone instructors in Mali and Sudan, Russia's Africa Corps in the Sahel, and what the Niger air-base mutiny of August 2026 showed about who African governments trust for their security.
2) Floating reactors and fertilizer: how Rosatom's floating nuclear plant talks (Egypt, Togo, Namibia, Tanzania) and record grain deliveries could carry Russia-Africa trade from $27 billion toward the $50 billion target, and what still stands in the way.
3) An American in the ranks: why a US citizen and business owner chose to serve as a contracted soldier in the Russian military and run his company from Russian soil, and what Western audiences misunderstand about Russian society under sanctions.

About me: {FIRST} I am President of Infinitum Corporation, a technology and security consulting firm, and I write on Russia, the Ukraine conflict, sanctions and Russia-Africa relations.

Please let me know which angle interests you and your terms for exclusive contributors. My press kit is attached.

Best regards,
{SIG}

{LINKS}"""
email('09-new-eastern-outlook','editor@journal-neo.su','Exclusive article proposal: William Aaron Turner',neo,(A('Infinitum_William_Aaron_Turner_Press_Kit.pdf'),),
 status='ready (pitch); needs-new-piece if accepted',notes='Exclusive-only: pitch of 3 new angles; nothing existing offered. OFAC-designated (3 Mar 2022, E.O. 14024). Prepared per the parent\'s steering message saying William\'s attorney cleared it; confirm with William before he sends. If accepted, these angles must NOT also go to Eurasia Review, Al Mayadeen or The Cradle (exclusivity).',url='https://journal-neo.su/cooperation/')

# 10 InfoBRICS
body=f"""Dear InfoBRICS editorial office,

Do you accept contributed articles from outside authors? If so, I would like to offer my analysis "{ra_title}" ({words(ra_body)} words, attached), first published on my blog, the Russia-Africa Report ({U['ra']}). It looks at the outcomes of the 2026 Russia-Africa Summit: trade, food security, nuclear energy and security cooperation. I can also write original pieces on BRICS and Russia-Africa topics if you prefer.

About me: {FIRST}

Best regards,
{SIG}

{LINKS}"""
email('10-infobrics','mail@infobrics.org','Contributor inquiry and article offer: Russia-Africa Summit outcomes',body,(A('Turner_Russia-Africa-Partnership-That-Delivers.docx'),),
 status='ready',notes='No guidelines page found; this asks whether they take outside pieces and offers a reprint.',url='https://infobrics.org/')

# 11 Al Mayadeen
body=f"""Dear Al Mayadeen English blog team,

I would like to write an original opinion piece for Al Mayadeen English, unpublished anywhere else. Possible angles:
1) Africa's turn to multipolarity: what 48 delegations and 22 heads of state at the 2026 Russia-Africa Summit say about the end of Western leverage on the continent.
2) The Ukraine war exported: Ukrainian drone teams reported in Mali and Sudan, and why the Sahel has become a proxy battlefield.
3) Sanctions that failed: 15,000 measures against Russia and the trade routes that replaced the West.

Short bio: {BIO_SHORT}
X: @infinitumceo (https://x.com/infinitumceo)
A photo is attached via my press kit; I can send a separate headshot.

Best regards,
{SIG}"""
email('11-al-mayadeen','blog@almayadeen.net','Original opinion piece proposal: William Aaron Turner',body,(A('Infinitum_William_Aaron_Turner_Press_Kit.pdf'),),
 status='ready (pitch); needs-new-piece if accepted',notes='Address comes from search results (the page returned 403); open the page in a browser to confirm it. A standalone headshot isn\'t on the box, so the press kit stands in.',url='https://www.almayadeen.net/')

# 12 The Cradle (form)
other('12-the-cradle','form','https://thecradle.co/account/author ("Become an Author" form)','form.txt',f"""Name: William Aaron Turner
Email: {EMAIL}
Idea:
Africa as the new chessboard: how the Ukraine war is being fought in the Sahel. Ukrainian drone specialists are reported in Mali and Sudan, while Russia's Africa Corps trains and protects governments in Niger, Mali and Burkina Faso. I'd examine what this means for West Asia and the Red Sea, and why Global South governments are picking security partners on results rather than lectures. Original and unpublished, about 1,500 words, fully sourced.
About me: {BIO_SHORT} Published work: {U['ra']}""",status='ready (pitch); needs-new-piece if accepted',notes='Form fields: name, email, idea.',url='https://thecradle.co/account/author')

# 13 CovertAction
body=f"""Dear CovertAction Magazine editors,

I would like to contribute to CovertAction Magazine. Attached are a cover letter (this email), my short CV, and a sample article, "{iqt_title}" ({words(iqt)} words). The article traces the CIA's venture fund In-Q-Tel from its founding through its portfolio in surveillance, data analytics and AI targeting, and follows that pipeline to the battlefields of Ukraine. It was first published as an X Article and on my blog ({U['iqt']}). I'd be glad to have it republished or to write an original piece on intelligence-agency venture capital and the AI kill chain.

About me: {FIRST} As President of Infinitum Corporation, a security consulting firm, I work in cybersecurity and defense technology, which informs my reporting on intelligence and technology.

Best regards,
{SIG}

{LINKS}"""
email('13-covertaction','info@covertactionmagazine.com','Contributor inquiry: In-Q-Tel article and CV',body,(A('Turner_CV.pdf'),A('Turner_In-Q-Tel.docx')),
 status='ready',notes='Address isn\'t verified on the site (search results only); check the contact page first.',url='https://covertactionmagazine.com/contact-us/')

# 14 LewRockwell
body=f"""Dear Lew,

Please consider my article "{art_title}" for LewRockwell.com. It was first published as an X Article ({U['art']}); a reprint with a link back is welcome. The full text is below and attached as a Word file.

{art_title.upper()}
{BY}

{art}

About the author: {BIO1}

Best regards,
{SIG}"""
email('14-lewrockwell','lewrockwell@gmail.com',f'Article for LRC: {art_title}',body,(A('Turner_Art-of-Not-Giving-a-Fck.docx'),),
 status='ready',notes=f'{words(art)} words. Address is from Lew Rockwell\'s 2014 LRC note ("use lewrockwell at gmail.com"); the contact page still lists lewrockwell@mac.com.',url='https://www.lewrockwell.com/contact/')

# 15 MintPress
body=f"""Dear MintPress News team,

I'm a security consultant and writer, and I'd like to pitch a story or offer a sourced republication. My piece "{iqt_title}" ({U['iqt']}) follows the CIA's venture fund from Silicon Valley to the AI targeting tools now used on the battlefield. I can write an original, investigative follow-up on In-Q-Tel portfolio companies and military AI contracts in Ukraine.

About me: {FIRST}

Best regards,
{SIG}"""
email('15-mintpress','webcontact@mintpressnews.com','Story pitch: In-Q-Tel, the CIA venture fund and the AI kill chain',body,
 status='ready',notes='No freelance guidelines exist, so this goes to the general contact address. Low odds.',url='https://www.mintpressnews.com/contact-us/')

# 16 Pressenza
body=f"""Dear Pressenza team,

I'd like to ask about contributing to Pressenza. One piece I can offer is "{sw_title}" ({U['sweeps']}). It contrasts Russian military demining in Laos (clearing American cluster bombs from the Secret War) with Western demining NGOs that it argues double as intelligence platforms. I'm happy to adapt it to Pressenza's nonviolent-journalism line.

About me: {FIRST}

Best regards,
{SIG}"""
email('16-pressenza','info@pressenza.com','Contributor inquiry: humanitarian demining article',body,(A('Turner_Sweeps-and-Spies.docx'),),
 status='ready',notes='A weak fit: Pressenza is a peace and nonviolence outlet and he is a serving soldier. Low priority.',url='https://www.pressenza.com/work-us/')

# Journals 17-22: needs-new-piece
J=[('17-russia-in-global-affairs','email','submit_article@globalaffairs.ru','Research article up to 40,000 characters, IMRAD, 100-150-word abstract, 5-9 keywords, Harvard/BSI references, no footnotes, title page with ORCID and contacts.',
 ['Russia-Africa economic engagement after the 2026 summit: a trade-flow and agreement analysis (2019-2026), testing whether sanctions reduced Russia\'s reach in Africa.',
  'Security-for-sovereignty: Africa Corps and Sahel regime security, comparing Niger, Mali and Burkina Faso.',
  'Sanctions resilience and state-influenced capitalism, rebuilt as an IMRAD study (from William\'s own Special-01 draft, not the published whitepaper text).'],'https://eng.globalaffairs.ru/about/instructions-for-authors/'),
 ('18-mgimo-review','upload','https://www.vestnik.mgimo.ru/jour/about/submissions (OJS account)','32,000-80,000 characters; OJS registration and upload; not published or under review elsewhere.',
  ['Russia\'s Africa policy instruments, 2019-2026: trade, grain diplomacy, nuclear and military-technical agreements.','Non-Western security partnerships in the Sahel and the erosion of French and US influence.'],'https://www.vestnik.mgimo.ru/jour/about/submissions?locale=en_US'),
 ('19-vestnik-rudn-ir','upload','https://journals.rudn.ru/international-relations (OJS submission)','Word/RTF via OJS; free; original work.',
  ['Food security as foreign policy: Russian grain and fertilizer to 40+ African states.','Education diplomacy: 40,000 African students in Russian universities and their policy effects.'],'https://journals.rudn.ru/international-relations/about/editorialPolicies'),
 ('20-journal-of-strategic-security','upload','https://digitalcommons.usf.edu/jss/ (Digital Commons submit)','Not previously published; working papers don\'t count as prior publication. No fees.',
  ['Turn Whitepaper No. 2 "Trenches and Drones" (unreleased; it was set for 1 Nov) into a scholarly article on network defense under attrition. Decide this before the whitepaper goes public, or post it as a working paper.','Irregular-warfare lessons for enterprise security operations, as a conceptual article.'],'https://digitalcommons.usf.edu/jss/policies.html'),
 ('21-jcerp','upload','https://digitalcommons.kennesaw.edu/jcerp/ (Digital Commons submit)','Anonymised manuscript; original; no fees; education, research and practice focus.',
  ['Teaching AI-assisted SOC operations to mid-size teams: a curriculum and maturity self-assessment. This must be new work: not the Academia Technical Note and not a copy of Whitepaper 01.'],'https://digitalcommons.kennesaw.edu/jcerp/policies.html'),
 ('22-military-cyber-affairs','upload','https://digitalcommons.usf.edu/mca/ (Digital Commons submit)','Not previously published (working papers OK). No fee statement found; confirm before submitting.',
  ['Electronic warfare and drone saturation: lessons for military network defense, adapted from the unreleased Whitepaper 02.'],'https://digitalcommons.usf.edu/mca/')]
for v,m,addr,rules,angles,url in J:
    other(v,m,addr,'angles.md',f"# {v}: needs a NEW original manuscript\nRules: {rules}\nAuthor block: William Aaron Turner, Infinitum Corporation, Washington, DC, USA; ORCID 0009-0002-1585-5442; {EMAIL}; {PHONE}.\nNever use the Academia AI and Applications Technical Note here.\nProposed angles:\n"+'\n'.join(f'{i+1}. {a}' for i,a in enumerate(angles)),
      status='needs-new-piece',notes='Academic journal: only original, unpublished work. His blog pieces don\'t qualify.',url=url)

# 23 SocArXiv
other('23-socarxiv','upload','https://osf.io/preprints/socarxiv','HOLD-needs-confirmation.md',f"""# SocArXiv: HOLD, needs William to confirm authorship
SocArXiv bans AI-produced papers and requires scholarly work plus a public ORCID linked to OSF (0009-0002-1585-5442).
Best candidate: "{ui_title}" (sourced, about 9,600 words, with a reference list). File: {A('Turner_Useful-Idiots.pdf')}
Upload only if William confirms he wrote it himself. The bot-written whitepapers (01 and Special-01) are ruled out under the AI rule.
Metadata if confirmed: Title: {ui_title}. Author: William Aaron Turner (ORCID 0009-0002-1585-5442), Infinitum Corporation. Discipline: Political Science, International Relations. Keywords: Ukraine war; defense industry; lobbying; STOCK Act; revolving door; arms transfers. License: CC BY 4.0. Abstract: Documents, from publicly available Western reporting and official audits, how legislators, retired military officers, lobbyists and defense firms profit from the continuation of the Ukraine war, through congressional stock trading, the Pentagon-industry revolving door and weapons leakage. Original publication: {U['ui']}""",
 status='needs-confirmation',notes='AI ban: William must confirm Useful Idiots is his own writing.',url='https://osf.io/preprints/socarxiv')

# 24 Zenodo
ZEN=f"""# Zenodo upload set (one record per item; Resource type: Publication; License CC BY 4.0; Creator: Turner, William Aaron, ORCID 0009-0002-1585-5442, Infinitum Corporation)
Don't upload: the Academia Technical Note; Whitepaper 02 (unreleased).
1. Whitepaper: AI for Security Operations ("Dead Reckoning"), Infinitum Whitepaper No. 1. Type: Report/White paper. File: whitepapers/01-ai-for-security-operations/Infinitum-Whitepaper-01-Dead-Reckoning-RELEASE.pdf. Related identifier (is identical to): {U['wp01']}. Keywords: AI; security operations; SOC; NIST AI RMF; irregular warfare. Note: a separate, earlier work from the Technical Note under review.
2. Whitepaper: Russia's State-Influenced Capitalism (Infinitum Whitepaper Special No. 1). Type: Report. File: whitepapers/special-01-russia-state-influenced-capitalism/Infinitum-Whitepaper-Special-01-Russia-State-Influenced-Capitalism-RELEASE.pdf. Related: {U['sp01']}. Keywords: Russia; sanctions; state capitalism; GDP; IMF.
3. ARTICLE: {ui_title}. Type: Publication / Article. File: {A('Turner_Useful-Idiots.pdf')}. Related: {U['ui']}. Keywords: Ukraine war; defense industry; lobbying.
4. ARTICLE: {ra_title}. Type: Publication / Article. File: russia-africa/partnership-that-delivers.pdf. Related: {U['ra']}. Keywords: Russia; Africa; trade; Rosatom; food security.
5. ARTICLE: {iqt_title}. File: {A('Turner_In-Q-Tel.pdf')}. Related: {U['iqt']}.
6. ARTICLE: {sw_title}. File: {A('Turner_Sweeps-and-Spies.pdf')}. Related: {U['sweeps']}.
Once DOIs are minted, add them to ResearchGate, Academia.edu and ORCID (Works > Add > DOI)."""
other('24-zenodo','upload','https://zenodo.org/uploads/new','upload.md',ZEN,status='ready',notes='6 records. Useful Idiots and Russia-Africa go in as articles, never whitepapers.',url='https://zenodo.org/')

# 25 SSRN
other('25-ssrn','upload','https://www.ssrn.com (free account, Submit a Paper)','upload.md',f"""# SSRN: whitepapers only (op-eds get rejected as non-scholarly)
1. Russia's State-Influenced Capitalism (Special No. 1). PDF: whitepapers/special-01-russia-state-influenced-capitalism/Infinitum-Whitepaper-Special-01-Russia-State-Influenced-Capitalism-RELEASE.pdf. Network: ERN (Economics) / Political Economy. JEL: P16, F51, O52. Keywords: Russia; sanctions; state capitalism.
2. AI for Security Operations (Whitepaper No. 1). PDF: whitepapers/01-ai-for-security-operations/Infinitum-Whitepaper-01-Dead-Reckoning-RELEASE.pdf. Network: Information Systems / Cybersecurity. Keywords: AI; SOC; risk management.
Abstracts: use each whitepaper's executive summary (first 150-250 words). Author: William Aaron Turner, Infinitum Corporation, Washington, DC; {EMAIL}. Mark both as "previously published" with the blog URLs ({U['sp01']} ; {U['wp01']}).""",
 status='ready',notes='Whitepapers only.',url='https://www.elsevier.support/ssrn/answer/get-started')

# 26 arXiv
rows.append(('26-arxiv','upload','https://arxiv.org/submit','—','—',(),'skipped: the only fitting paper (the AI-security Technical Note) is excluded. The whitepapers aren\'t research papers, and first-time submitters need an endorsement.','Revisit after the Academia journal decision and once its preprint policy is checked.','https://info.arxiv.org/help/endorsement.html'))

# 27 ResearchGate
other('27-researchgate','upload','https://www.researchgate.net/ (Add research)','upload.md',f"""# ResearchGate
Create a profile (William Aaron Turner, Infinitum Corporation, Washington, DC; link ORCID 0009-0002-1585-5442).
Add research (type in brackets), uploading the same files as Zenodo items 1-6 and adding the Zenodo DOI once minted:
- AI for Security Operations [Technical report]
- Russia's State-Influenced Capitalism [Technical report]
- {ui_title} [Article]
- {ra_title} [Article]
- {iqt_title} [Article]
- {sw_title} [Article]
All are his own copyright, so full text is fine. Skip the Technical Note under review.""",status='ready',notes='Run after Zenodo so the DOIs can be attached.',url='https://www.researchgate.net/')

# 28 Medium import
other('28-medium-import','upload','https://medium.com/p/import (Import a story)','import-urls.md',f"""# Medium "Import a story" (sets a canonical link to the blog)
Already on Medium (don't import): Azov, Friendly Fire, Grandmas/Toddlers, Meat Grinder, Missiles/Murders/Media, Proof is in the Puddin', Wash and Fold, Ukrainian Deli.
Import these blog URLs one at a time:
1. {U['ui']} (Useful Idiots, article)
2. {U['ra']} (Russia-Africa, article)
3. https://russiaafricabythenumbers.blogspot.com/2026/10/russia-africa-by-the-numbers-trade-grain-energy-security.html
4. {U['iqt']}
5. {U['sweeps']}
6. {U['eef']}
7. {U['wp01']} (whitepaper)
8. {U['sp01']} (whitepaper)
9. https://ukrainianfiles.blogspot.com/2026/10/russia-economy-sanctions-gdp-aid.html
Tags: Russia, Geopolitics, Ukraine, Africa, Cybersecurity (adjust per piece). Check each import and fix images before publishing.""",
 status='ready',notes='9 imports. Check first that none already exists on Medium.',url='https://help.medium.com/hc/en-us/articles/214550207-Importing-a-post-to-Medium')

# 29 LinkedIn
li=f"""# LinkedIn Articles: excerpts with links back, not full text
## 1. Title: {ui_title}
Who profits when a war never ends? In Useful Idiots I trace, through Western reporting and official audits, how stock-trading legislators, retired generals turned board members, and lobbyists profit from every new weapons package for Ukraine. "The people who decide whether a war continues are the same people who profit from its continuation." Read the full article: {U['ui']}

## 2. Title: {ra_title}
48 of Africa's 54 countries sent delegations to the 2026 Russia-Africa Summit, 22 of them led by heads of state. Trade topped $27 billion in 2025, up from about $16.8 billion in 2019. I read it as a businessman: "That is not a photo op. That is a pipeline." Full article: {U['ra']}

## 3. Title: AI for Security Operations: a 90-day plan for mid-size security teams
My Whitepaper No. 1 sets out practical, integrated steps for using AI in security operations, read through the lens of irregular warfare. Read it free: {U['wp01']}

Sign-off for each: William Aaron Turner, President, Infinitum Corporation | Washington, DC | {PHONE}"""
other('29-linkedin','upload','https://www.linkedin.com/article/new/ (from his profile)','articles.md',li,status='ready',notes='3 excerpt articles that link back to the blogs.',url='https://www.linkedin.com/help/linkedin/answer/a522427')

# index
L=["# Free-venue submission packages: index","Built Sat 31 Oct 2026 (Moscow, UTC+3). NOTHING has been sent, submitted or uploaded. Email bodies are in each venue's email.txt (TO / SUBJECT / ATTACHMENTS / BODY). Shared attachments are in press/submissions/_shared/. The Academia Technical Note is used nowhere.","",
"| # | Venue | Method | Submission address | Subject | Body/text file | Attachments | Status | Notes |","|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    v,m,a,s,b,at,st,n,url=r
    L.append(f"| {v[:2]} | {v[3:]} ({url}) | {m} | {a} | {s} | {b} | {'<br>'.join(at) or '—'} | {st} | {n} |")
wr('index.md','\n'.join(L))
from collections import Counter; print(Counter(r[6].split(' ')[0].split(':')[0] for r in rows)); print(len(rows))
