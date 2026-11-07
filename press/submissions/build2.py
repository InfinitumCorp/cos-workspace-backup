exec(open('venues2.py').read())
N=S+'/_new'; G=S+'/_gmail'; R=[]
def folder(v): p=f'{S}/{v}'; os.makedirs(p,exist_ok=True); return p
def em(v,to,subj,body,atts=(),notes='',url='',status='ready-to-send'):
    p=folder(v); wr(f'{p}/email.txt',f"TO: {to}\nSUBJECT: {subj}\nATTACHMENTS: {', '.join(os.path.basename(a) for a in atts) or 'none'}\nGUIDELINES: {url}\n\n---BODY---\n{body}")
    wr(f'{G}/{v}.body.txt',body)
    R.append(dict(v=v,method='email',addr=to,subj=subj,file=f'press/submissions/{v}/email.txt',atts=[os.path.basename(a) for a in atts],status=status,notes=notes,url=url))
def fm(v,addr,text,notes='',url='',status='prepared (browser session)',fname='form.txt'):
    p=folder(v); wr(f'{p}/{fname}',text)
    R.append(dict(v=v,method='form/account',addr=addr,subj='—',file=f'press/submissions/{v}/{fname}',atts=[],status=status,notes=notes,url=url))
SH=S+'/_shared'
# new pieces -> docx
sahel=open(N+'/sahel.md').read(); switch=open(N+'/switch.md').read()
md_docx(sahel,N+'/Turner_Sahel-Front_GeopoliticalMonitor.docx'); md_docx(switch,N+'/Turner_Who-Holds-the-Switch_BAR.docx')
sahel_t="The Sahel Front: Ukraine's Drone Teams in Mali and the Cost of Exporting the War"
switch_t="Who Holds the Switch? Russia's Floating Reactors and Africa's Fight for Power"
# Global Times cut
ps=ra_body.split('\n\n'); gt='\n\n'.join(ps[i] for i in [0,1,3,4,6,7,8,9,10,11,13,23,24,34,35,36,37])
open(N+'/globaltimes_cut.txt','w').write(gt); gtw=words(gt)
RA=U['ra']
# 30 Asia Times
em('30-asia-times','shawn.crispin@asiatimes.com',"Pitch: What the Russia-Africa summit actually produced (unpaid; previously published)",
f"""Dear Mr. Crispin,

I'd like to pitch an analysis for Asia Times on the third Russia-Africa Summit in Moscow (28–29 October): what the trade, grain, nuclear and security numbers say about Russia's position on the continent, set against China's and the EU's far larger trade with Africa.

In line with your guidelines, full disclosure: a longer English version, "The Partnership That Delivers: What the Russia-Africa Summit Actually Produced," was published on my blog on 30–31 October ({RA}). I am not seeking payment. If the angle interests you, I will deliver a tightened version of about 1,000 words as a Word file, with every factual claim hyperlinked to its source (TASS, AP, Reuters, BBC, CNN, the Kremlin and others); or, if you prefer an original piece, a new article on the same subject.

About me: {FIRST2}

Best regards,
{SIG2}

{LINKS}""",notes='Pitch first per guidelines; prior publication disclosed; unpaid. Reply only if accepted (2 business days).',url='https://asiatimes.com/write-for-us/')
# 31 Global Times
em('31-global-times','opinion@globaltimes.com.cn',"Opinion submission: The Partnership That Delivers: What the Russia-Africa Summit Actually Produced",
f"""Dear Opinion editors,

Please consider the opinion article below for the Global Times ({gtw} words, within your 800-word limit). For transparency: it is condensed from a longer article first published on my blog on 30 October 2026 ({RA}); the full version with references is available at https://doi.org/10.5281/zenodo.23836501. You are welcome to edit for length and clarity.

THE PARTNERSHIP THAT DELIVERS: WHAT THE RUSSIA-AFRICA SUMMIT ACTUALLY PRODUCED
{BY}

{gt}

---
{BIO_S}

Best regards,
{SIG2}""",notes=f'Text in body, {gtw} words (cut from his article by dropping whole paragraphs; no wording added). Originality not stated by GT; prior publication disclosed.',url='https://www.globaltimes.cn/contact-us/')
# 32 Brave New Europe
em('32-brave-new-europe','info@braveneweurope.com',"Republication offer: Russia's State-Influenced Capitalism (Infinitum whitepaper)",
f"""Dear Brave New Europe editors,

I understand BNE sometimes cross-posts work from contributors' own sites. I'd like to offer my whitepaper "Russia's State-Influenced Capitalism" for republication, in full or as an excerpt with a link back. It examines how Russia's state-guided model of capitalism works and how it has held up under Western sanctions, which I think speaks to BNE's interest in political economy and policy alternatives.

It was first published on Infinitum Whitepapers ({U['sp01']}) and is archived open access (CC BY 4.0) with DOI 10.5281/zenodo.23836439 (https://doi.org/10.5281/zenodo.23836439). The PDF is attached. I'm also happy to offer my article "Useful Idiots: A Guide to the Western Profiteers of the Ukraine War" (https://doi.org/10.5281/zenodo.23836478) if that fits better.

About me: {FIRST2}

Best regards,
{SIG2}

{LINKS}""",atts=(f'{W}/whitepapers/special-01-russia-state-influenced-capitalism/Infinitum-Whitepaper-Special-01-Russia-State-Influenced-Capitalism-RELEASE.pdf',),
notes='BNE says it cross-posts contributor blog pieces; no formal guidelines page. Whitepaper (not an article).',url='https://braveneweurope.com/contacts/')
# 33 Responsible Statecraft
em('33-responsible-statecraft','PitchRS@quincyinst.org',"Pitch: The CIA's venture fund is buying the AI kill chain. Congress isn't watching.",
f"""Dear Responsible Statecraft editors,

Pitch (original, 800–1,200 words): In-Q-Tel, the CIA's nonprofit venture fund, has quietly become one of the most important investors in the AI, data-fusion and targeting technology now flowing into the battlefield, yet its portfolio decisions get almost no public or congressional scrutiny. I'd argue that a taxpayer-funded fund shaping the weapons of the next war should face the same oversight as any other defense program, and set out what minimal transparency would look like.

My longer reported piece on In-Q-Tel ({U['iqt']}) gives me the sourcing; the RS article would be new and written for you, in AP style with embedded links.

About me: {FIRST2}

Best regards,
{SIG2}""",notes='Pitch only (RS prefers pitches; all RS stories original). Exclusive if accepted.',url='https://responsiblestatecraft.org/editorial-submissions-policy/')
# 34 Peoples Dispatch
em('34-peoples-dispatch','contact@peoplesdispatch.org',"Article offer: The Partnership That Delivers: What the Russia-Africa Summit Actually Produced",
f"""Dear Peoples Dispatch editors,

I'd like to offer my analysis "The Partnership That Delivers: What the Russia-Africa Summit Actually Produced" for Peoples Dispatch. It covers the third Russia-Africa Summit in Moscow: 48 African delegations, the grain and fertilizer deliveries, Rosatom's nuclear projects, security agreements and education quotas, and how Western outlets reported it. It was first published on my blog ({RA}); the Word file (about 1,600 words with references) is attached. I'm glad to adapt or shorten it, or to write an original piece for you on Russia-Africa relations or the Global South.

About me: {FIRST2}

Best regards,
{SIG2}

{LINKS}""",atts=(f'{SH}/Turner_Russia-Africa-Partnership-That-Delivers.docx',),notes='Address decoded from the Who We Are page (contact@). No guidelines page.',url='https://peoplesdispatch.org/who-we-are/')
# 35 Modern Ghana
em('35-modern-ghana','editor@modernghana.com',"Opinion submission: The Partnership That Delivers: What the Russia-Africa Summit Actually Produced",
f"""Dear ModernGhana editor,

Please consider the opinion article below for ModernGhana's Opinions section. It is my own work, first published on my blog on 30 October 2026 ({RA}); the Word file with references and a pull-quote image (my own graphic, free to use) are attached.

THE PARTNERSHIP THAT DELIVERS: WHAT THE RUSSIA-AFRICA SUMMIT ACTUALLY PRODUCED
{BY}

{ra_full}

---
{BIO}

Best regards,
{SIG2}""",atts=(f'{SH}/Turner_Russia-Africa-Partnership-That-Delivers.docx',f'{SH}/russia-africa-pull-quote-1080x1350.jpg'),
notes='editor@modernghana.com per search results/contact page (not shown on the policy page). Prior publication disclosed.',url='https://www.modernghana.com/editorial-standards-and-policies')
# 36 ScheerPost
em('36-scheerpost','Mailing@ScheerPost.com',"Pitch: Sweeps and Spies: mine clearance, charity and intelligence",
f"""Dear ScheerPost editors,

Pitch: Humanitarian demining is one of the least scrutinized corners of Western foreign policy. I'd like to write a sourced piece for ScheerPost comparing Russia's military mine-clearance missions in Laos and Syria, cleaning up ordnance largely left by others, with the Western demining-charity model, and asking how far Western-funded mine action overlaps with intelligence and strategic interests.

Sources: published mission data from Russia's International Mine Action Centre and the Vientiane Times; the public history and funding records of the major Western demining NGOs; and reporting already gathered in my longer article "Sweeps and Spies: Russia Clears the Bombs. The West Clears the Data." ({U['sweeps']}). I have not yet contacted the NGOs for comment and would do so before filing.

Previously published: my blogs and 8 long-form X Articles (517,020 views as of 31 Oct 2026), plus open-access archives at Zenodo (https://doi.org/10.5281/zenodo.23836541 for the demining piece).

About me: {FIRST2}

Best regards,
{SIG2}""",notes='Pitch only, "Pitch" in subject per FAQ.',url='https://scheerpost.com/about-us/frequently-asked-questions/')
# 37 Infosecurity Magazine
em('37-infosecurity-magazine','james.coker@rxglobal.com',"Guest article pitch: Mid-size SOCs don't need more AI. They need AI they can audit.",
f"""Dear James,

I'd like to pitch an exclusive guest article (800–1,000 words) for Infosecurity Magazine.

Proposed title: Mid-size SOCs don't need more AI. They need AI they can audit.

Synopsis: Attackers are moving faster: Verizon's 2026 DBIR found vulnerability exploitation is now the most common way into a breach, while only 26% of the most critical known-exploited vulnerabilities were fully fixed. IBM's 2026 breach study found organizations using security AI and automation extensively averaged lower breach costs and faster response, but most mid-size organizations have barely adopted it, and the AI they do adopt becomes a new attack surface. The article argues that mid-size teams should adopt AI in a fixed order: start with triage and enrichment where a human approves every action, log every model decision, put AI tools under the same access control as any privileged account, and measure results against dwell time and analyst workload rather than vendor claims. It will close with a short, practical checklist. No products are named or promoted.

The piece will be written exclusively for Infosecurity. It draws on my research for a longer whitepaper on AI in security operations but will not reuse its text.

Author: William Aaron Turner, Founder and CEO, Infinitum Corporation (technology and security consulting; Washington, DC headquarters, Moscow operating location). {FIRST2} A headshot and short bio are available on request.

Best regards,
{SIG2}""",notes='Pitch (synopsis + title) per op-ed page; exclusive if accepted. Statistics are from the verified Dead Reckoning sources.',url='https://www.infosecurity-magazine.com/op-ed/')
# 38 Help Net Security
em('38-help-net-security','press@helpnetsecurity.com',"Spokesperson suggestion: Building a SOC team that stays / Doing more with flat budgets",
f"""Dear Help Net Security editorial team,

I'd like to suggest myself as a spokesperson for two topics on your Editorial opportunities 2026 page:

- Building a SOC team that stays (deadline 6 November 2026)
- Doing more with flat budgets (deadline 9 November 2026)

Name, title and company: William Aaron Turner, Founder and CEO, Infinitum Corporation (technology and security consulting; headquartered in Washington, DC, with Moscow as an operating location).

Relevant expertise: I lead a security consulting firm and wrote "Dead Reckoning," a 15,000-word whitepaper on AI for security operations at mid-size organizations (open access, DOI 10.5281/zenodo.23836365: https://doi.org/10.5281/zenodo.23836365). It covers automating analyst toil, people and retention, metrics that show whether detection is improving, and governance under the NIST AI RMF, which maps directly to both topics. I read security through an irregular-warfare lens: {FIRST2}

Best regards,
{SIG2}""",notes='Spokesperson offer, details requested by the page (name, title, company, expertise).',url='https://www.helpnetsecurity.com/editorial-opportunities/')
# 39 Black Agenda Report (new original piece)
em('39-black-agenda-report','bareditors@gmail.com',f"Submission Turner {switch_t}",
f"""Dear BAR editors,

Please consider my original opinion article below ({words(md_text(switch))} words). It has not been published anywhere and is submitted only to Black Agenda Report. The Word document with embedded reference links is attached, and the text is copied below.

Suggested headline: {switch_t}
Suggested subhead: At the Moscow summit, Rosatom offered African states electricity from Russian-owned floating nuclear plants. The offer answers a real hunger for power. Whether it serves African sovereignty will be decided in the contract terms.

{md_text(switch).split(chr(10),2)[2].strip()}

---
Bio: {BIO_S} X: @infinitumceo. I don't have a headshot file to hand; I can send one on request.

Best regards,
{SIG2}""",atts=(N+'/Turner_Who-Holds-the-Switch_BAR.docx',),notes='NEW original piece (840 words) written for BAR; exclusive, do not send elsewhere. Headshot not on box (offered on request).',url='https://blackagendareport.com/contact-us')
# 40 RIAC
em('40-riac','editorial@russiancouncil.ru',"Author inquiry: William Aaron Turner (Russia-Africa, sanctions, Ukraine)",
f"""Dear RIAC editors,

I would like to become an author for RIAC's English-language site. I write on Russia-Africa relations, the Ukraine conflict, Western sanctions and the Western defence and intelligence industry.

As a sample I attach "The Partnership That Delivers: What the Russia-Africa Summit Actually Produced," published on my blog on 30 October 2026 ({RA}; DOI 10.5281/zenodo.23836501). I understand you may prefer original material, so I would gladly write a new analytical piece for RIAC; possible subjects include the agreements signed at the third Russia-Africa Summit, Rosatom's floating nuclear plant offer to African states, or the resilience of Russia's economy under sanctions. My CV is attached.

About me: {FIRST2} I hold a master's degree.

Best regards,
{SIG2}

{ZEN}""",atts=(f'{SH}/Turner_Russia-Africa-Partnership-That-Delivers.docx',f'{SH}/Turner_CV.pdf'),notes='Per RIAC "On the wire" page (editorial@). Avoid offering the MGIMO manuscript topic as a full piece while it is under review.',url='https://russiancouncil.ru/en/on-the-wire/')
# 41 Geopolitical Monitor (new original piece, attachment only)
em('41-geopolitical-monitor','editor@geopoliticalmonitor.com',f"Submission (situation report): {sahel_t}",
f"""Dear Editor,

Please find attached my situation report "{sahel_t}" ({words(md_text(sahel))} words, single-spaced Word file, Chicago style, hyperlinked references, no images). It is original, has not been published elsewhere, and is submitted only to Geopolitical Monitor.

Suggested deck: Kyiv's small deployments in northern Mali buy leverage against Russia. They also tie Ukraine to separatists who fight alongside an al-Qaeda affiliate, and they hand the Sahel's military governments a diplomatic weapon.

Disclosure, in line with your guidelines: I am an American serving as a contracted soldier in the Russian military (153rd Tank Regiment, currently in the SVO), and I run Infinitum Corporation (Washington, DC headquarters; Moscow operating location) from Russian soil. The piece relies on CNN and Deutsche Welle reporting and presents both Ukrainian and Russian positions.

Social: X https://x.com/infinitumceo; LinkedIn https://www.linkedin.com/in/william-aaron-t-726076244

Best regards,
{SIG2}""",atts=(N+'/Turner_Sahel-Front_GeopoliticalMonitor.docx',),notes='NEW original piece (988 words) written for GPM; exclusive. Affiliation disclosed (GPM rejects undisclosed state interests).',url='https://www.geopoliticalmonitor.com/write-for-us/')
json.dump(R,open(S+'/_new/rows_email.json','w'),indent=1)
print([ (r['v'],r['atts']) for r in R]); print('gt words',gtw)
