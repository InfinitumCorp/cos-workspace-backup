# Notes: Academia AI and Applications submission package (LOCAL ONLY, under embargo)

Prepared 31 Oct 2026 (Moscow time, UTC+3). Nothing has been uploaded, emailed, posted, or submitted.

## Files
- `Turner_LLM-SOC-Triage-Evaluation_TechnicalNote_manuscript.docx`: the manuscript, built on the official Academia Word template
- `Turner_LLM-SOC-Triage-Evaluation_cover-letter.docx`: the cover letter
- `Turner_LLM-SOC-Triage-Evaluation_disclosures.docx`: final disclosures
- `references-check.md`: each citation with its verification URL
- `_official-academia-word-template.docx`: the untouched official template (downloaded from the journal's Style Guide "Word template" link, which redirects to academia-edu-letters.s3.amazonaws.com/submission_templates/word/Academia Word Submission Template.docx)
- `build/`: the source text (content.py, refs.py) and build scripts, so the files can be regenerated after edits

## Sources read
- Author guidelines: https://www.academia.edu/journals/academia-ai-and-applications/about/author-guidelines
- Style guide: https://www.academia.edu/journals/academia-ai-and-applications/about/style-guide
- About/scope: https://www.academia.edu/journals/academia-ai-and-applications/about
- APCs: https://www.academia.edu/journals/about/article-processing-charges (AI and Applications: Type A $2,000/€1,900; Type B $900/€850; Type C $400/€375)

## Article-type recommendation: Technical Note (Type B, US$900)
- **Why not a Research Article or Brief Research Report:** the guidelines require Materials and methods plus Results, meaning primary original studies. We have no dataset, and fabricating experiments is not an option.
- **Why not a Perspective or Opinion ($400):** the guidelines say both are "typically only invited content". An uninvited submission risks desk rejection. Switch to Perspective only if William gets an invitation. In that case the text already fits: it is under 3,000 words with one table.
- **Why a Technical Note fits:** it "describes a specific development, technique, or procedure … or introduces … computational methods". The criteria are "novelty of concepts involved, the validity of the technique, and its potential for practical applications". The manuscript presents a new evaluation procedure: five dimensions, defined measures (closure risk at coverage, deferral suppression, confidence inflation, explanation contamination, escalation inflation), a seven-step protocol, and a reporting card. That is exactly a technique with practical value, and it needs no new data.
- **Length:** the guidelines recommend 2,000–3,000 words. The main text (Introduction through Conclusions, excluding the table and references) is about 2,620 words. The abstract is 250 words. The task brief asked for 150–300 words; the style guide sets no limit.

## Guideline requirements applied
- Official Word template used (A4, DM Sans; the template's own text sizes: 10 pt body, 14 pt headings, 18 pt title). Single spacing, no first-line indent. Header and footer journal name set to "Academia AI and Applications"; Vol/DOI/dates left as XX placeholders for production.
- Article type line: "Technical Note".
- Title: 86 characters, sentence case, no end punctuation, no non-standard abbreviations, and keywords included (search-engine guidance).
- Author byline: corresponding author marked with an asterisk; one corresponding email.
- Affiliation format: "Department, Institute, City, State (USA only), Country", with no postal codes allowed. The manuscript therefore reads "Infinitum Corporation, Washington, DC, USA". The street address (1629 K Street NW, Suite 300) appears only in the cover letter. No phone number appears anywhere.
- Abstract is unstructured, as required for a Technical Note. It has no citations or figure references, and LLM and SOC are defined at first use.
- Keywords: 8, separated by semicolons, with no final period (3–10 allowed).
- Abbreviations are defined at first use in the abstract and again in the main text, and there is no abbreviation list. NIST and OWASP are spelled out at first use.
- Headings are bold and in sentence case: numbered Level 1 (1., 2., …) and Level 2 (3.1., …). Two Level-1 headings contain keywords.
- Table 1: 10 pt, left-aligned, cells vertically centered, 1 pt spacing before and after, 0.5 pt lines, no shading, no empty cells. It is cited in the text before it appears.
- Citations are numbered in square brackets in order of first appearance. References use the modified Vancouver style: up to 6 authors, then "et al."; DOI or URL; ISO 4 abbreviations where known.
- Self-citations: none (limit is 20%). No retracted papers, personal communications, or in-press items.
- Mandatory statements included: Acknowledgments (required because AI was used), Funding, Author contributions, Conflict of interest, and Data availability (the journal's exact "no new data" wording). The template's Publisher's note and Copyright blocks are kept.
- AI use: the style guide requires use beyond language polishing to be disclosed in Materials and methods "or a similar section", so it appears in Section 2 (Approach). The Acknowledgments use the journal's "Language polishing + beyond" statement.
- IRB and Informed consent sections are omitted because they apply only to research with human or animal participants. Supplementary materials are omitted (none).
- Author contributions conflict: the Style Guide and the template say this section is only for multi-author papers, but the Author Guidelines list it as mandatory. It is included as a one-line CRediT statement and can be deleted if the editors ask.
- Template typography caveat: the template's styles use the font name "DM Sans 14pt" (an optical-size variant of DM Sans) inherited from the official file. It renders correctly with DM Sans installed.

## Originality
The framing is new, and no existing Infinitum text was reused (nothing from Dead Reckoning, /workspace/whitepapers, or /workspace/russia-africa). The paper treats the triage pipeline (model, gate, and analyst) as the unit of evaluation, and it treats the gate itself as the attack target. That second idea yields the deferral-suppression, confidence-inflation, and explanation-contamination measures. Two 2026 papers already study prompt injection through log fields: Karanjai et al. at USENIX Security 2026, and Landauer et al. on arXiv. Both are cited, and the note positions itself as complementary to them (Section 6.2) rather than claiming to be first.

## Finalized 31 Oct 2026, 14:40 (Moscow time, UTC+3), after William confirmed the open items
- Funding: "This research received no external funding. Infinitum Corporation did not sponsor or fund this work."
- Conflict of interest: the author is President of Infinitum Corporation, a security consulting firm; there is nothing else to declare.
- AI use: Grok Bot (no version) assisted with drafting and editing; the author reviewed all content and takes responsibility for it. Disclosed in Section 2, in the Acknowledgments, and in the disclosures file.
- All [DRAFT] markers and highlights are removed. The disclosures file was renamed (no _DRAFT).
- The cover letter date is left as a blank line ("Date: ____") to fill in at submission.
- Contact email kept: info@theinfinitumcorporation.com.
- The equation notation was changed from E[C] to E(C), so the only square brackets left are citation numbers.
- APC: Technical Note, US$900. Nothing has been submitted, uploaded, or sent.
