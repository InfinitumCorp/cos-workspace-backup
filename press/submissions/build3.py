exec(open('venues2.py').read())
iqt_title="WTF Is In-Q-Tel? The CIA's Venture Fund and the Kill Chain It Bankrolled"; art_title="The Art of Not Giving a F*ck: 50 Countries, One Russia, Zero Results"; sw_title="Sweeps and Spies: Russia Clears the Bombs. The West Clears the Data."; ui_title="Useful Idiots: A Guide to the Western Profiteers of the Ukraine War"; ra_title="The Partnership That Delivers: What the Russia-Africa Summit Actually Produced"
R=[]
def fm(v,addr,url,text,notes):
    p=f'{S}/{v}'; os.makedirs(p,exist_ok=True); wr(f'{p}/form.txt',f"EXACT URL: {addr}\nGUIDELINES: {url}\nNO account has been created. Log any login in the vault.\n\n{text}")
    R.append((v,addr,url,notes))
A=f'{S}/_shared'
fm('42-opednews','https://www.opednews.com/ (free member account, then Submit Content > Article)','https://mail.opednews.com/populum/writersguidelines.php',
f"""OpEdNews accepts reprints and simultaneous submissions; the author must hold the rights (he does).
Submit one article per entry, each with "Originally published at <URL>" in the first line:
1. {ui_title}  | source {U['ui']} | file {A}/Turner_Useful-Idiots.docx | DOI 10.5281/zenodo.23836478
2. {iqt_title} | source {U['iqt']} | file {A}/Turner_In-Q-Tel.docx | DOI 10.5281/zenodo.23836521
3. {ra_title}  | source {U['ra']} | file {A}/Turner_Russia-Africa-Partnership-That-Delivers.docx | DOI 10.5281/zenodo.23836501
4. {sw_title}  | source {U['sweeps']} | file {A}/Turner_Sweeps-and-Spies.docx | DOI 10.5281/zenodo.23836541
5. {art_title} | source {U['art']} | file {A}/Turner_Art-of-Not-Giving-a-Fck.docx
Account fields: name William Aaron Turner; email theinfinitumcorp+opednews@gmail.com; bio below.
Bio: {BIO}
Do NOT post the two new exclusive pieces (_new/) or the Academia Technical Note.""",'Reprints OK; account needed. Highest reach of the form venues.')
fm('43-hackernoon','https://app.hackernoon.com/ (free account, New Story)','https://help.hackernoon.com/republishing-guide',
f"""Story: {iqt_title}. Paste text from {A}/Turner_In-Q-Tel.docx.
Story Settings > "First seen at": {U['iqt']} (blogspot is not eligible for canonical, so use First seen at).
Turn ON the "AI-Assisted" credibility indicator and add one intro line: "AI tools assisted with research and editing; the author reviewed every claim."
Tags: cybersecurity, ai, intelligence, venture-capital, defense-tech.
Bio: {BIO_S}
Optional second story: Dead Reckoning summary linking to https://doi.org/10.5281/zenodo.23836365.""",'HackerNoon discourages AI-written text; requires AI-Assisted disclosure. Medium-low priority.')
fm('44-dev-to','https://dev.to/enter (free account, Create Post)','https://dev.to/guidelines-for-ai-assisted-articles-on-dev',
f"""Post: "Dead Reckoning: AI for Security Operations at Mid-Size Organizations (summary)".
Body: the whitepaper's executive summary from /workspace/whitepapers/01-ai-for-security-operations.md (section "Executive summary"), then link to {U['wp01']} and https://doi.org/10.5281/zenodo.23836365.
Front matter: canonical_url: {U['wp01']} ; tags: security, ai, devops, career
AI disclosure: set to "some AI" (assisted) per DEV guidelines.
Do NOT use the Academia Technical Note (under journal review).""",'canonical_url supported; AI-assisted allowed with disclosure.')
fm('45-internet-archive','https://web.archive.org/save (no account needed)','https://help.archive.org/help/using-the-wayback-machine/',
"Save Page Now, one URL at a time (tick 'Save outlinks' off):\n"+'\n'.join(list(U.values())+['https://zenodo.org/records/'+x for x in ['23836365','23836439','23836478','23836501','23836521','23836541']]),
'Preservation copies of the blog originals and Zenodo records. No account, low effort.')
fm('46-mr-online','https://www.jotform.com/form/220455692635056 (MR Online submit / contact form)','https://www.jotform.com/form/220455692635056',
f"""MR Online accepts ORIGINAL articles only (not published online before), up to 2,000 words. None of his existing pieces qualify, and the two new pieces are exclusive elsewhere.
Use the form's "Contact the editors" option with this message:
"I write on Russia-Africa relations, sanctions and Western defence-industry influence. I'd like to propose an original article for MR Online on the political economy of the Russia-Africa trade relationship after the October 2026 Moscow summit. Samples: {U['ra']} ; {U['ui']}. Bio: {BIO_S} Contact: {EMAIL}, {PHONE}."
If they say yes: needs-new-piece.""",'Original-only; pitch via the contact option. needs-new-piece if accepted.')
fm('47-the-grayzone','https://thegrayzone.com/contact/ (contact form)','https://thegrayzone.com/contact/',
f"""Name: William Aaron Turner | Email: {EMAIL}
Subject: Pitch: Ukraine's drone war in the Sahel / In-Q-Tel and the AI kill chain
Message: "I'm an American serving as a contracted soldier in the Russian military (153rd Tank Regiment, currently in the SVO) and CEO of Infinitum Corporation. I'd like to pitch an original piece on In-Q-Tel, the CIA's venture fund, and the AI targeting technology it has financed, building on my published piece {U['iqt']}. Happy to discuss angles. {PHONE}"
NOTE: do not pitch the Sahel angle; that piece is exclusive to Geopolitical Monitor.""",'Pitches via form only.')
fm('48-figshare','https://figshare.com/account/register (free account)','https://help.figshare.com/',
"Optional mirror of the 6 Zenodo records (same PDFs as press/submissions/24-zenodo/upload.md). Low value: Zenodo DOIs already exist; if used, cite the Zenodo DOI in each Figshare description rather than minting duplicates.",
'Lowest priority; duplicates Zenodo.')
L=["","## Batch 2 form/account venues (prepared, not submitted; no accounts created)","| # | Venue | URL | File | Status | Notes |","|---|---|---|---|---|---|"]
for v,a,u,n in R: L.append(f"| {v[:2]} | {v[3:]} | {a} | press/submissions/{v}/form.txt | prepared | {n} |")
L+=["","## Batch 2 researched and skipped","| Venue | Reason |","|---|---|",
"| Oriental Review (or@orientalreview.su) | OFAC-designated 3 Mar 2022 (E.O. 14024, Treasury jy0628); attorney clearance covered only SCF and NEO |",
"| Katehon | OFAC SDN (Analiticheski Tsentr Katekhon); no public submission route |",
"| RT / Sputnik op-ed | ANO TV-Novosti and Rossiya Segodnya are US-sanctioned; no public op-ed route |",
"| Press TV / Tehran Times | Iran sanctions (IRIB is an SDN); not attorney-cleared |",
"| Geopolitika.ru | Dugin-linked; no public submission contact |",
"| Valdai Club, Indian Punchline | Invited experts only / single-author blog |",
"| Unz Review, OffGuardian, 21st Century Wire | No public submission route found |",
"| Preprints.org | Rejects previously published work |",
"| E-International Relations | Original, unpublished academic work only |",
"| The Herald (Zimbabwe) | Only a dated letters@ address; site timed out |",
"| SecurityWeek | Contributor columns are by invitation; not pursued |",
"| OSF Preprints (general) | Same OSF platform as SocArXiv (on hold for the AI question) |",
"","## Batch 2 AI-ban venues (need a piece William wrote himself)","| Venue | Policy |","|---|---|",
"| Mises Wire (mises.org/submissions) | \"Do not use AI to compose or translate articles\"; permanent-ban risk |",
"| CGTN Opinion (opinions@cgtn.com) | Does not accept AI-generated op-eds; original and exclusive, 800 words |",
"| The American Conservative (submissions@) | Avoid AI-generated writing; no simultaneous submissions |",
"| Pambazuka News (submissions@pambazuka.org) | Advises against LLM-generated text; also no republishing unless requested |"]
open(f'{S}/index.md','a').write('\n'.join(L)+'\n')
