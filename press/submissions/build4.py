exec(open('venues2.py').read())
iqt_title="WTF Is In-Q-Tel? The CIA's Venture Fund and the Kill Chain It Bankrolled"; art_title="The Art of Not Giving a F*ck: 50 Countries, One Russia, Zero Results"; sw_title="Sweeps and Spies: Russia Clears the Bombs. The West Clears the Data."; ui_title="Useful Idiots: A Guide to the Western Profiteers of the Ukraine War"; ra_title="The Partnership That Delivers: What the Russia-Africa Summit Actually Produced"
N=S+'/_new'; G=S+'/_gmail'; SH=S+'/_shared'; R=[]
AI="Disclosure: this piece was drafted with AI assistance and reviewed and verified by the author."
def em(v,to,subj,body,atts=(),notes='',url=''):
    p=f'{S}/{v}'; os.makedirs(p,exist_ok=True)
    wr(f'{p}/email.txt',f"TO: {to}\nSUBJECT: {subj}\nATTACHMENTS: {', '.join(os.path.basename(a) for a in atts) or 'none'}\nGUIDELINES: {url}\n\n---BODY---\n{body}")
    wr(f'{G}/{v}.body.txt',body); R.append(dict(v=v,addr=to,subj=subj,atts=[os.path.basename(a) for a in atts],notes=notes,url=url))
gt=open(N+'/globaltimes_cut.txt').read()
def offer(outlet,title,src,doi,what,att):
    return f"""Dear {outlet} editors,

I'd like to offer my article "{title}" for publication on {outlet}, in full or adapted to your length. {what} It was first published at {src} and is archived open access (DOI {doi}). The Word file with sources is attached; I'm also glad to write an original piece for you.

About me: {FIRST2}

Best regards,
{SIG2}

{LINKS}"""
UI_W="It documents, from Western reporting, how members of Congress, retired generals, lobbyists and defense contractors profit from prolonging the Ukraine war (about 9,600 words; I can cut it or split it into a series)."
IQ_W="It explains how In-Q-Tel, the CIA's venture fund, financed the data, AI and targeting technology now in military use (about 3,200 words)."
ART_W="It is a sourced, sardonic look at why 50 countries' aid and the largest sanctions regime in history have failed to break Russia (about 2,900 words)."
SW_W="It compares Russia's military demining missions in Laos and Syria with the Western demining-charity model and its intelligence links (about 2,100 words)."
d=lambda f:f'{SH}/{f}'
em('49-oriental-review','or@orientalreview.su',f"Submission: {ra_title}",f"""Dear Oriental Review editors,

Please consider the article below ({words(gt)} words, within your 1,000-word limit). News hook: the third Russia-Africa Summit in Moscow, 28–29 October 2026. It is condensed from a longer, fully referenced version first published on my blog ({U['ra']}; DOI 10.5281/zenodo.23836501), where every figure is linked to its source (TASS, AP, Reuters, BBC, CNN and others).

{ra_title.upper()}
{BY}

{gt}

---
{BIO_S}

Best regards,
{SIG2}""",notes='OFAC-designated (3 Mar 2022); sent on William\'s statement that his attorney cleared sanctioned outlets.',url='https://orientalreview.su/submission-guidelines/')
em('50-katehon','editor@katehon.com',f"Article offer: {ui_title}",offer('Katehon',ui_title,U['ui'],'10.5281/zenodo.23836478',UI_W,1),(d('Turner_Useful-Idiots.docx'),),notes='OFAC SDN; address from UK sanctions record/2022 profile. Attorney-cleared per William.',url='https://katehon.com/')
em('51-rt-op-ed','feedback@rttv.ru',f"Op-ed offer for RT: {art_title}",offer('RT',art_title,U['art'],'—',ART_W,1).replace('and is archived open access (DOI —)','as an X Article'),(d('Turner_Art-of-Not-Giving-a-Fck.docx'),),notes='No op-ed submission address published; feedback@ is RT online projects (rt.com). OFAC-designated; attorney-cleared per William.',url='https://russian.rt.com/about-us/contact-info/')
em('52-sputnik','feedback@sputniknews.com',f"Opinion article offer: {iqt_title}",offer('Sputnik',iqt_title,U['iqt'],'10.5281/zenodo.23836521',IQ_W,1),(d('Turner_In-Q-Tel.docx'),),notes='Editorial address from sputnikglobe.com/docs/about. Rossiya Segodnya sanctioned; attorney-cleared per William.',url='https://sputnikglobe.com/docs/about/')
em('53-press-tv','presstv@presstv.co.uk',f"Op-ed offer for Press TV: {ui_title}",offer('Press TV',ui_title,U['ui'],'10.5281/zenodo.23836478',UI_W,1),(d('Turner_Useful-Idiots.docx'),),notes='Editorial address from presstv contact page. Iran sanctions (IRIB SDN); sent on William\'s attorney-clearance statement.',url='http://www.presstv.media/aboutus/ContactUs')
em('54-tehran-times','info@tehrantimes.com',f"Op-ed offer for Tehran Times: {sw_title}",offer('Tehran Times',sw_title,U['sweeps'],'10.5281/zenodo.23836541',SW_W,1),(d('Turner_Sweeps-and-Spies.docx'),),notes='No op-ed address; general info@ from contact page. Iran sanctions; attorney-cleared per William.',url='https://www.tehrantimes.com/news/300001/')
# Mises excerpt
ap=art.split('\n\n'); mx='\n\n'.join(ap[i] for i in [3,11,12,13,14,28,29,30,31,32,33,34,35,36,84,85,86,87,92,93])
mt="The Sanctions That Didn't: How Russia's Economy Routed Around the West"
md=f"# {mt}\n\n"+"\n\n".join(('### '+x if len(x.split())<9 and not x.startswith('-') else x) for x in mx.split('\n\n'))+f"\n\n{AI}"
md_docx(md,N+'/Turner_Sanctions-That-Didnt_Mises.docx')
em('55-mises-wire','rwmcmaken@mises.org, bill@mises.org, jmawhorter@mises.com',f"Mises Wire submission: {mt}",f"""Dear Mises Wire editors,

Please consider the attached essay "{mt}" ({words(mx)} words, .docx, links rather than footnotes). It argues that the Western sanctions on Russia failed for reasons any market economist would predict: trade rerouted, prices adjusted and new suppliers and buyers appeared.

{AI}

Full transparency: the essay is adapted from my longer X Article "{art_title}" ({U['art']}), which I also offered to LewRockwell.com as a reprint earlier today. I am not seeking payment.

About me: {FIRST2}

Best regards,
{SIG2}""",(N+'/Turner_Sanctions-That-Didnt_Mises.docx',),notes='AI-ban venue: honest AI disclosure in email and docx, per William. Prior publication and the LRC offer disclosed.',url='https://mises.org/submissions')
cg=open(N+'/cgtn.md').read(); md_docx(cg+f"\n\n{AI}",N+'/Turner_Africas-Partners-Are-Plural_CGTN.docx')
cgt="Africa's Partners Are Plural Now. The Moscow Summit Proved It."
em('56-cgtn-opinion','opinions@cgtn.com',f"Op-ed submission: {cgt}",f"""Dear CGTN Opinion editors,

Please consider the original op-ed below ({words(md_text(cg))} words), written for and submitted exclusively to CGTN. Sources are linked in the text and in the attached Word file.

{AI}

{md_text(cg).split(chr(10),2)[2].strip()}

---
Bio: {BIO_S}
I don't have a high-resolution headshot to hand; I can send one on request.

Best regards,
{SIG2}""",(N+'/Turner_Africas-Partners-Are-Plural_CGTN.docx',),notes='NEW original exclusive piece; AI-ban venue, honest disclosure included.',url='https://www.cgtn.com/opinions/Contact-Us.html')
em('57-american-conservative','submissions@theamericanconservative.com',"Pitch: Fifty countries, the biggest sanctions regime in history, and a Russian economy that kept growing",f"""Dear TAC editors,

Pitch (800–1,500 words, written for TAC and not offered elsewhere): Four and a half years of Western sanctions and aid were supposed to break Russia's economy and force a settlement. They did neither. I'd argue, from a restraint perspective, that Washington keeps doubling down on a tool that has failed on its own terms, and that the cost falls on American and European taxpayers and on Ukrainians. The piece would draw on European Commission forecasts, Interfax/TASS economic data, CSIS and ISW battlefield assessments, and reporting on the shadow fleet and Russia's turn East.

{AI}

My longer published take on this subject is here: {U['art']}.

About me: {FIRST2}

Best regards,
{SIG2}""",notes='Pitch; AI-ban venue, honest disclosure included.',url='https://www.theamericanconservative.com/contact-us/')
em('58-pambazuka','submissions@pambazuka.org',f"Submission: {ra_title}",f"""Dear Pambazuka News editors,

Please consider my article "{ra_title}" (about 1,600 words, Word document attached, references at the end).

As your guidelines ask: this piece has appeared before, on my blog Russia-Africa Report ({U['ra']}), and has also been offered to other outlets.

{AI}

Byline (30 words): An American businessman and contracted soldier reads the third Russia-Africa Summit as a trade fair: grain, fertilizer, nuclear power, security cooperation and education, measured against Western rhetoric and sanctions.

Bio: {BIO}

Social media: X @infinitumceo (https://x.com/infinitumceo); Telegram https://t.me/infinitumcorporation; LinkedIn https://www.linkedin.com/in/william-aaron-t-726076244

Best regards,
{SIG2}""",(d('Turner_Russia-Africa-Partnership-That-Delivers.docx'),),notes='AI-discouraged venue; honest disclosure; prior publication disclosed (they republish at their discretion).',url='https://www.pambazuka.org/submit')
em('59-geopolitika','editor@geopolitica.ru',f"Article offer: {ra_title}",offer('Geopolitika.ru',ra_title,U['ra'],'10.5281/zenodo.23836501',"It covers the third Russia-Africa Summit's trade, grain, nuclear, security and education outcomes (about 1,600 words).",1),(d('Turner_Russia-Africa-Partnership-That-Delivers.docx'),),notes='Address from search results only (site blocks automated access); may bounce.',url='https://www.geopolitika.ru/en')
em('60-valdai-club','admin@valdaiclub.com',"Contributor inquiry: William Aaron Turner (Russia-Africa, sanctions, Ukraine)",f"""Dear Valdai Discussion Club,

I would like to ask whether the Club considers opinion or analytical contributions from outside authors for its website. I write on Russia-Africa relations, Western sanctions and the Ukraine conflict. As a sample I attach "{ra_title}" ({U['ra']}; DOI 10.5281/zenodo.23836501), and my CV. I would gladly write an original piece for Valdai on the outcomes of the third Russia-Africa Summit or another subject of your choosing.

About me: {FIRST2} I hold a master's degree.

Best regards,
{SIG2}

{ZEN}""",(d('Turner_Russia-Africa-Partnership-That-Delivers.docx'),d('Turner_CV.pdf')),notes='Only public address is admin@ (contacts page); Valdai normally invites experts.',url='https://valdaiclub.com/about/contacts/')
em('61-indian-punchline','indianpunchline@gmail.com',"From a reader: Russia-Africa summit analysis and In-Q-Tel piece",f"""Dear Ambassador Bhadrakumar,

I'm a regular reader of Indian Punchline. I know it is your own column rather than a site for outside contributors, but I wanted to share two of my recent pieces in case they are useful for your writing or you would ever consider a guest contribution:

- "{ra_title}": {U['ra']}
- "{iqt_title}": {U['iqt']}

About me: {FIRST2}

With respect,
{SIG2}""",notes='Single-author blog; address from the site. Framed as a reader note with a guest-post offer.',url='https://www.indianpunchline.com/')
em('62-offguardian','submissions@off-guardian.org',f"Submission: {iqt_title}",offer('OffGuardian',iqt_title,U['iqt'],'10.5281/zenodo.23836521',IQ_W,1),(d('Turner_In-Q-Tel.docx'),),notes='Submissions address decoded from the About page.',url='https://off-guardian.org/about/')
em('63-21st-century-wire','21stcenturywire@gmail.com',f"Article offer: {art_title}",offer('21st Century Wire',art_title,U['art'],'—',ART_W,1).replace('and is archived open access (DOI —)','as an X Article'),(d('Turner_Art-of-Not-Giving-a-Fck.docx'),),notes='Address published by 21WIRE (older); contact page currently 404.',url='https://21stcenturywire.com/')
em('64-securityweek','press@securityweek.com',"Contributor inquiry: AI in security operations for mid-size organizations",f"""Dear SecurityWeek editors,

I'd like to ask whether SecurityWeek would consider a contributed column, or me as an expert source, on AI in security operations for mid-size organizations. I wrote "Dead Reckoning," a 15,000-word whitepaper on the subject (open access, DOI 10.5281/zenodo.23836365: https://doi.org/10.5281/zenodo.23836365), covering where AI helps defenders, where it becomes a new attack surface, and governance under the NIST AI RMF. Any column would be original and exclusive to SecurityWeek, with no product promotion.

Name, title and company: William Aaron Turner, Founder and CEO, Infinitum Corporation (technology and security consulting; Washington, DC headquarters, Moscow operating location). {FIRST2}

Best regards,
{SIG2}""",notes='No public contributor route; press@ is the published address for pitches.',url='https://advertise.securityweek.com/contact-securityweek')
em('65-herald-zimbabwe','letters@herald.co.zw',f"Opinion: {ra_title}",f"""Dear Editor,

Please consider the opinion article below for The Herald ({words(gt)} words). It is condensed from a longer, fully referenced version first published on my blog ({U['ra']}).

{ra_title.upper()}
{BY}

{gt}

---
{BIO_S}

Best regards,
{SIG2}""",notes='No current op-ed address published; letters@ is the dated listing. May bounce.',url='https://www.heraldonline.co.zw/letters-to-the-editor/')
json.dump(R,open(N+'/rows_b3.json','w'),indent=1)
L=["","## Batch 3 (31 Oct 2026, William: \"Dont ever skip sites!\"; sanctioned outlets sent on his attorney-clearance statement)","| # | Venue | Method | Address/URL | Subject | File | Attachments | Status | Gmail msg id | Notes |","|---|---|---|---|---|---|---|---|---|---|"]
for r in R: L.append(f"| {r['v'][:2]} | {r['v'][3:]} ({r['url']}) | email | {r['addr']} | {r['subj']} | press/submissions/{r['v']}/email.txt | {', '.join(r['atts']) or '—'} | pending-send | — | {r['notes']} |")
open(S+'/index.md','a').write('\n'.join(L)+'\n')
print([(r['v'],r['atts']) for r in R]); print(words(mx), words(md_text(cg)))
