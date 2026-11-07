# Publications SEO pack, 31 Oct 2026
- pubs.csv: every publication/outlet row with status (published / pending / exclusive-hold / under-review / bounced).
- per-post/<slug>.html: Blogger paste blocks (title, search description, JSON-LD, Cite/Also-available footer); header comment has the exact Blogger edit URL.
- blogger-theme-head.xml: Google Scholar Highwire meta tags per post via <b:if data:view.url>, pasted once per blog theme (Blogger cannot put <meta> in a post's head).
- site-schema.html / .json: sitewide Organization + Person graph (DC entity, 202-729-9509, Mon–Fri 09:00–21:00, ORCID, CCW Offer, knowsAbout, subjectOf/workExample).
- zenodo-related-identifiers.md: paste list (no API token on box).
- gsc-urls.txt, indexing.md, live-urls.txt: indexing plan; Wayback + IndexNow status.
- data.py/build.py: regenerate everything after edits (python3 build.py).
