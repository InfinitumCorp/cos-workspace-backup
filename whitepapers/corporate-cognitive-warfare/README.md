# Corporate Cognitive Warfare: Expanded Edition (October 2026)

Status: FINAL; William approved publishing ("Publish CCW", relayed by CoS 2026-10-31). Not yet posted or emailed by WhitePaper Bot. Built 2026-10-31 (Moscow time, UTC+3).

## Deliverables
- Word: `Infinitum-Whitepaper-Corporate-Cognitive-Warfare-EXPANDED.docx`
- PDF: `Infinitum-Whitepaper-Corporate-Cognitive-Warfare-EXPANDED-RELEASE.pdf` (38 pages; grep "draft" = only the ordinary verb "Draft the response playbook" in section 6.8)
- Word count (python-docx): body 14,433 (incl. tables, excl. references); references 1,184; total 15,617 (after QA). Original approved edition was about 1,222 words.
- Cover: full-bleed GraphicDesign Bot v2 cover (`cover.jpg`), white, official mark, no phone. Footer on pages 2–38: "Term coined by William Aaron Turner • Page N".

## Google Drive (folder "Infinitum Whitepapers", private, not shared; owner theinfinitumcorp@gmail.com via connector user-Google-drive)
- Folder: https://drive.google.com/drive/folders/1xpqNkCO1aczz6LADk8U2LL6w8XStgcxB
- CURRENT DOCX (final, v2 cover; uploaded 2026-10-31 16:55 MSK): https://docs.google.com/document/d/1JP6MMshqO9HKNyoBTt-xzwrDYyI5PbTl/edit?usp=drivesdk&ouid=111432877080181597710&rtpof=true&sd=true
- CURRENT PDF (final, 38 pages, v2 cover; uploaded 2026-10-31 16:55 MSK): https://drive.google.com/file/d/1qzboibZDVU4PXWceF5tJvlkXOLFi1oZR/view?usp=drivesdk
- OUTDATED (pre-QA, old cover; kept, not trashed; renamed 2026-10-31 16:58 MSK with prefix "OUTDATED – "): DOCX 1MqPZ0EcyY6geY8on4DSGg21V5rTmAPYq "OUTDATED – Infinitum-Whitepaper-Corporate-Cognitive-Warfare-EXPANDED.docx", PDF 1GVhTQg1x6cVFw0PbKrdqkWYvNFG3fzsC "OUTDATED – Infinitum-Whitepaper-Corporate-Cognitive-Warfare-EXPANDED-RELEASE.pdf". Both still in the Infinitum Whitepapers folder.
- In-place update was not possible: the Drive connector can only overwrite file contents with text, not binary docx/pdf.

## Buffer ideas (org INFINITUM CORP; ideas only, no posts)
6ae5f156bb92470d80b6612b, 6ae5f158f0b1542f87677f8d, 6ae5f15c3784d67df1fb44d8, 6ae5f15ff0b1542f87677fbc, 6ae5f1629a49d19864691d15, 6ae5f1653784d67df1fb45a7 (titles "[CCW-EXP] 1–6"). Eight older "[CCW]" ideas from the original edition are still on the board.

## Release kit (`release-kit/`)
01-blog-summary.md · 02-x-thread.md · 03-linkedin-post.md · 04-newsletter-blurb.md · 05-abstract-keywords.md · 06-flyer-brief-graphicdesign-bot.md. Read links use the [ACADEMIA URL] placeholder.

## Build
`python3 tools/build_docx.py /path/to/original.docx Infinitum-Whitepaper-Corporate-Cognitive-Warfare-EXPANDED.docx` (sources in `src/*.md`), then `soffice --headless --convert-to pdf`.
Source checks: `sources/` (Crossref results, URL checks, downloaded copies).

## QA pass (WhitePaper Bot, 2026-10-31 16:50 MSK)
Rebuilt docx + PDF (38 pages; 15,617 words: body 14,433 incl. tables, references 1,184). Originals in `_prev/`.
Fixes: phone removed (About + release kit); cover attribution line added; Legal Bot terms ("psyops", "psychological operations", "algorithmic manipulation") removed from commercial copy (exec summary, 3.2, 3.3, blog summary); release-kit links -> [ACADEMIA URL]; Telegram/X/web added to kit contacts.
New GraphicDesign Bot cover NOT swapped in: it prints 202-729-9509 and its subtitle ("Winning the Contest for Perception, Attention and Decision-Making") does not match the paper's subtitle; it also says "CEO" rather than "Founder & President".

## Cover swap (2026-10-31 16:52 MSK)
Page 1 replaced with GraphicDesign Bot's full-bleed `/workspace/ccw/design/ccw-whitepaper-cover-v2.jpg` (white, official mark, matching subtitle, Founder & President credit, no phone). First-page header/footer suppressed. Pages 2–38 text unchanged (diffed). Standalone copy: `cover.jpg`. Pre-swap versions: `_prev/pre-cover-v2-1652/`. Note: rebuilding via tools/build_docx.py would restore the old text cover; re-apply the swap if rebuilt.
