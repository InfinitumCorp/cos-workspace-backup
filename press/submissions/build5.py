exec(open('venues2.py').read())
ui_title="Useful Idiots: A Guide to the Western Profiteers of the Ukraine War"
N=S+'/_new'; SH=S+'/_shared'; R=[]
def fm(v,addr,url,text,notes,status='prepared'):
    p=f'{S}/{v}'; os.makedirs(p,exist_ok=True); wr(f'{p}/form.txt',f"EXACT URL: {addr}\nGUIDELINES: {url}\nNO account has been created. Save any new login in the vault.\n\n{text}"); R.append((v,addr,notes,status))
pp=open(N+'/preprint.md').read()
os.makedirs(f'{S}/67-preprints-org',exist_ok=True)
md_docx(pp,f'{S}/67-preprints-org/Turner_Russia-Africa-Nuclear-Cooperation_ResearchNote.docx')
topdf(f'{S}/67-preprints-org/Turner_Russia-Africa-Nuclear-Cooperation_ResearchNote.docx',f'{S}/67-preprints-org')
fm('66-unz-review','https://www.unz.com/contact/ (contact form; no account)','https://www.unz.com/contact/',
f"""Name: William Aaron Turner | Email: {EMAIL}
Subject: Article offer: {ui_title}
Message: "I'd like to offer my article '{ui_title}' for The Unz Review. It documents, from Western reporting, how members of Congress, retired generals, lobbyists and defense contractors profit from prolonging the Ukraine war. Published at {U['ui']} (open access DOI 10.5281/zenodo.23836478). I can send the Word file. About me: {FIRST2} {PHONE}"
Fallback (directory listing only, unverified): ron@unz.com""",'Contact form only.')
fm('67-preprints-org','https://www.preprints.org/ (free account, Submit)','https://www.preprints.org/instructions-for-authors',
f"""Subject area: Social Sciences > Political Science (or Energy) | Article type: Article / Review
Title: Russia–Africa Nuclear Energy Cooperation after the 2026 Moscow Summit: An Open-Source Review of Projects, Commercial Models and Policy Questions
Author: William Aaron Turner, Infinitum Corporation, Washington, DC; ORCID 0009-0002-1585-5442; email {EMAIL}
Abstract: copy section "Abstract" from the manuscript.
Keywords: Russia; Africa; Rosatom; nuclear energy; floating nuclear power plant; energy access; power purchase agreement
Files: press/submissions/67-preprints-org/Turner_Russia-Africa-Nuclear-Cooperation_ResearchNote.docx (+ .pdf)
AI statement (Methods + Declarations, already in the file): "AI tools assisted with drafting and structuring this note; the author reviewed the text and checked every factual claim against the cited sources."
Conflict of interest (in file): Russian military contract service; CEO of Infinitum Corporation. Funding: none.
Previously published: No (new, unpublished; screened for prior publication).""",'NEW unpublished research note (~1,150 words) written for this venue; must not be posted elsewhere first.')
fm('68-osf-preprints','https://osf.io/preprints/osf (OSF account; Add a preprint)','https://help.osf.io/article/376-preprints-home-page',
f"""Server: OSF Preprints (general). Files (PDF): {SH}/Turner_Useful-Idiots.pdf ; /workspace/whitepapers/special-01-russia-state-influenced-capitalism/Infinitum-Whitepaper-Special-01-Russia-State-Influenced-Capitalism-RELEASE.pdf
Type: Useful Idiots = article (never whitepaper); Special-01 = whitepaper.
License: CC BY 4.0. Link the published DOIs: 10.5281/zenodo.23836478 and 10.5281/zenodo.23836439.
Author: William Aaron Turner, ORCID 0009-0002-1585-5442 (link ORCID to OSF).
Conflict of interest: contracted soldier in the Russian military (153rd Tank Regiment); CEO, Infinitum Corporation.
AI disclosure (paste into the description and the COI/notes field): "This work was drafted with AI assistance and reviewed and verified by the author."
Do NOT post the Preprints.org note, the new exclusive pieces in _new/, or the Academia Technical Note.""",'Account venue; AI disclosure included.')
fm('69-e-international-relations','submissions.e.ir@gmail.com (email; .docx; subject SUBMISSION)','https://www.e-ir.org/p/submissions-guide',
"""NOT SENT. E-IR states: "SUBMISSIONS MUST BE FULLY HUMAN... zero tolerance", and every submission must carry an AI declaration that either no AI was used or that AI was used only in strictly assistive ways that did not generate text. An AI-drafted piece cannot truthfully make either declaration, so no honest submission is possible unless William writes the piece himself.
If he does: Opinion 800–1,500 words, embedded hyperlinks, no headings or footnotes; bio of 20–100 words at the top; title of 80 characters or fewer; send to submissions.e.ir@gmail.com with subject SUBMISSION and the AI declaration in the email.""",'Blocked: honest declaration impossible for AI-drafted text.',status='hold: needs a human-written piece')
L=["","## Batch 3 form/account venues (prepared; no accounts created)","| # | Venue | URL | File | Status | Notes |","|---|---|---|---|---|---|"]
for v,a,n,st in R: L.append(f"| {v[:2]} | {v[3:]} | {a} | press/submissions/{v}/form.txt | {st} | {n} |")
open(S+'/index.md','a').write('\n'.join(L)+'\n'); print('ok')
