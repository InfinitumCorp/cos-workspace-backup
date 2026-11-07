# Zenodo ↔ Academia relations review — Nov 7, 2026 (MSK), local only
No live changes. Zenodo login blocked (CoS notified). Inputs: zenodo-source-check.md, academia-CCW-execution.md, PDFs in /home/box/Downloads.
Method: sha256, pdfinfo pages, pdftotext full text → NFKC, hyphen/dash normalization, line-break hyphen joins, whitespace collapse; word-level diff; then masked ligature glyphs (fi/ff/ffi/ffl/tt/tti and mis-mapped Ï/Ò/Ý).
Semantics note: DataCite `IsIdenticalTo` = same resource in a different form/location (intellectual identity), not required to be byte-identical. A byte mismatch alone does not make a distinct edition.

## DR — zenodo 23836365
- Zenodo PDF: Infinitum-Whitepaper-01-Dead-Reckoning-RELEASE.pdf, 57 pp, sha256 914f88127af4d585…, producer WeasyPrint 70.0.
- Academia PDF: Dead_Reckoning_AI_for_Security_Operation (1).pdf, 57 pp, sha256 14711a0be245e96c…, producer GPL Ghostscript 10.02.1 (re-processed copy).
- Text: 20,930 normalized words each; diff ratio 0.9992; all 16 residual differences are ligature extraction (e.g. staffing/stafÏng); after masking: 0 differences.
- Finding: substantively identical content; files are not byte-identical (Academia copy re-processed through Ghostscript).
- Current relation: "Is identical to" → Blogger post (HTML). NOT verified: Blogger page not compared in this review (no browsing); a blog post may be a summary, not the full text.
- Recommended: (a) Add Academia URL https://www.academia.edu/179949703/Dead_Reckoning_AI_for_Security_Operations as IsIdenticalTo (content-identical PDF; supported). (b) Blogger relation: UNDECIDED. Keep only if the post carries the full paper text (then IsIdenticalTo, as an HTML form, is defensible); if it is a summary/announcement, change to a non-identity relation (e.g. IsDescribedBy / IsReferencedBy, to be chosen after review). Verify Blogger content before any edit.

## TD — zenodo 23887266
- Both PDFs 48 pp, sha256 3343ebde4f34d257… (byte-identical); 17,330 words; diff ratio 1.0.
- Current relation: "Is identical to" → https://www.academia.edu/180077697/ (short URL).
- Recommended: relation correct. Optional cosmetic: replace with canonical https://www.academia.edu/180077697/Trenches_and_Drones_Network_Defense_for_a_War_of_Attrition_Whitepaper_ (only if short URL is judged insufficient; not required).

## CCW — zenodo 23838097
- Zenodo PDF: …EXPANDED-RELEASE.pdf, 38 pp, sha256 78932929e87be40f… (== local RELEASE).
- Academia PDF: Corporate_Cognitive_Warfare_Irregular_Wa.pdf, 38 pp, sha256 b33baebf6f1c65a2… (rebuild; created Oct 31 17:00 vs local 16:52 per academia-CCW-execution.md).
- Text: 16,358 normalized words each; ratio 0.9977; after masking, 21 residuals, all extraction artifacts (tti ligature in Mattis/Antti/setting/letting; bullet glyph position). No substantive wording difference found.
- Current relation: "Is identical to" → Academia URL. Assessment: supported on intellectual identity (same Expanded content, not the 1,222-word original); not byte-identical.
- Recommended: keep. Note: Academia DOI field shows 10.5281/zenodo.23838096 (concept DOI → resolves to record 23838097 per execution log); acceptable, no change needed.

## Summary
| Item | Bytes | Content | Current | Action |
|---|---|---|---|---|
| DR | differ | identical | IsIdenticalTo Blogger | add Academia IsIdenticalTo; Blogger relation UNDECIDED pending content check |
| TD | identical | identical | IsIdenticalTo Academia | keep |
| CCW | differ | identical | IsIdenticalTo Academia | keep |
All actions pending signed-in Zenodo access and approval; nothing applied.
