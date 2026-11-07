# Ranked fix list (2026-10-31)
Legend for "How": AUTO = I can apply with an available connector (GitHub-xai / Vercel-xai) without William; BROWSER = needs a logged-in browser session on the box (Blogger, Telegram, Whop, Academia); WILLIAM = needs his login, a decision, or money. Impact: H/M/L. Nothing below has been applied yet.

| # | Fix | Property | Impact | How | Notes |
|---|---|---|---|---|---|
| 1 | Replace (202) 681-0120 with 202-729-9509 in visible text, `tel:` links, legal notice and LocalBusiness JSON-LD | Main site (Ueni) | H | WILLIAM (Ueni login) | Single biggest NAP fix. Keep WhatsApp only if intended. |
| 2 | Pick one host (recommend `www`, matches all backlinks); set builder primary domain so apex 301s to www and canonical/sitemap/JSON-LD use it | Main site | H | WILLIAM (Ueni / DNS) | |
| 3 | Rewrite titles + meta descriptions on home and 4 key service pages per keyword-map.md | Main site | H | WILLIAM (Ueni) | Copy ready in keyword-map.md and `seo-master/ready/website-meta-copy.md` |
| 4 | Replace JSON-LD sameAs (drop @infinitumusa, raw place ID) with Organization+Person graph from `seo-master/ready/website-jsonld.html`; footer links to X @infinitumceo, Telegram, blogs, Whop, GitHub | Main site | H | WILLIAM (Ueni) or GTM-TG56DMZ if he grants GTM access | |
| 5 | Verify Google Search Console + Bing Webmaster for main site and 4 blogs; submit sitemaps; request indexing of whitepapers | All sites | H | WILLIAM (Google login); Blogger verification tag via BROWSER | Without this, no indexing data |
| 6 | Resolve duplicate Russia-Africa Summit article: keep ONE canonical (recommend russiaafricareport, topical match) and on the Ukraine Files copy either delete + Blogger custom redirect, or replace body with a 150-word summary linking to the canonical | UF + RAR blogs | H | BROWSER (Blogger) | 100% identical 2,020-word text today |
| 7 | GBP: phone 202-729-9509 primary, hours 24/7, website www + UTM, description; resolve suspended duplicate listing | GBP | H | WILLIAM (business.google.com unreachable from box) | |
| 8 | Founder SERP: deploy `williamaaronturner-redesign` (or update Beacons) with H1 "William Aaron Turner", 300+ words bio, Person JSON-LD sameAs, https links; fix www 500 | williamaaronturner.com | H | Repo edit AUTO (GitHub); DNS cut-over WILLIAM | |
| 9 | Vercel redesign repo: phone -> 202-729-9509; Organization+Person JSON-LD with full sameAs; per-route titles/descriptions from keyword map; keep noindex + Disallow until cut-over, with a single env flag that flips both at launch; sitemap only lists routes that will exist | infinitum-corporation-site / Vercel | M (H at launch) | AUTO (GitHub-xai push; Vercel redeploy) | Safe: staging is noindex |
| 10 | noindex the survey page (add robots meta + title/description) | infinitum-survey-flyers.vercel.app | L | AUTO (Vercel/GitHub) if source found | Thin page indexed under brand |
| 11 | Add H1 on blog homepages (UF, Whitepapers, both Russia-Africa blogs) | Blogger | M | BROWSER (theme edit) | |
| 12 | Add in-body author/firm link to www main site on every UF post (anchor "Infinitum Corporation, cybersecurity consulting in Washington, DC") | Ukraine Files | M | BROWSER | Currently JSON-LD only |
| 13 | Telegram description: remove "from Moscow" lead, fix `t.me/infinitumceo` -> `https://x.com/infinitumceo`, add https www site | Telegram | M | BROWSER or Telegram bot admin; WILLIAM approved positioning (DC HQ) already in boilerplate | |
| 14 | Whop location label "Milan, IT" -> Washington, DC | Whop | M | BROWSER (no Whop API tool for this) | |
| 15 | X @infinitumceo bio/website; LinkedIn headline "A killer in a suit!" -> keyworded headline (drafts in keyword-map.md) | X, LinkedIn | M | WILLIAM approval of wording, then BROWSER | |
| 16 | Create/claim our LinkedIn company page with unique URL | LinkedIn | M | WILLIAM | |
| 17 | Build 4 missing service pages (AI for security ops, strategic risk assessment, defense technology advisory, Corporate Cognitive Warfare) | Main site / Vercel redesign | M | AUTO on redesign repo; WILLIAM on Ueni | |
| 18 | Press cadence: max 1-2/week, rotate wires, fix raw markdown in Russia-Africa PressLiftoff release via private edit link | Press | M | BROWSER (edit link in published.md) | Reduces spam-pattern risk |
| 19 | Legacy 24-7PressRelease (Moscow dateline, "Willian" typo, old phone): request correction or publish newer DC-dated release that outranks | Press | L-M | WILLIAM (may cost) | |
| 20 | GitHub profile README: add canonical NAP, links to site/blogs/Whop/Academia | GitHub | L | AUTO | |
| 21 | Entity listings: Bing Places, Apple Business Connect, Crunchbase, D-U-N-S, ORCID, TGStat/Telemetr, Clutch, GoodFirms, BBB | Directories | M | WILLIAM (verifications) + BROWSER | Legal-entity decision first (CA close corp 5470106 vs DC) |
| 22 | Academia: confirm each upload's description links to canonical blog URL + site | Academia | L | BROWSER (Cloudflare blocks bots) | |
| 23 | Rename default Blogger slugs (blog-post_26/_85) only if paired with custom redirects | Ukraine Files | L | BROWSER | Optional; low gain |

## Auto-applicable now (connectors available): #9, #10, #20, and repo-side half of #8 and #17.
## Blocked / needs William: #1-#5, #7, #8 DNS, #15 wording, #16, #19, #21. Bot walls (Cloudflare/LinkedIn 999) prevented automated reads of Academia, Medium, openPR, LinkedIn.

## Status update 2026-10-31 02:35 MSK
- Decisions from William: 202-729-9509 is the only public phone; legal entity/HQ = Infinitum Corporation, Washington, DC (drop the California filing in all schema/listings).
- #9, #10, #17 (redesign side), #20, #8 (repo side): prepared as patches in `patches/` (see patches/README.md). NOT pushed: `gh` not authenticated on the box.
- New risk found: the redesign footer's ClientTicker shows logos (Anthropic, Amazon, AWS, Anduril, Airbnb, AIG, AT&T, Capital One, Affirm, GovTech). If these are not actual clients, that's a false-endorsement/trademark risk and a trust (E-E-A-T) problem. Untouched; William to confirm or remove.

## Added 2026-10-31 12:56 MSK
- Useful Idiots article (hold lifted by William; never hold releases): https://ukrainianfiles.blogspot.com/2026/10/blog-post_85.html plus its Academia.edu copy. Treat like any other article: keyword targeting, internal links from both blogs, the site's research section, and the Person/Organization schema subjectOf lists.
- Hours are now Mon-Fri 9:00-21:00, Sat-Sun closed. Replace "Open 24 hours" in all patches (entity.ts, services/page.tsx, apply_edits.py, both README patches) before pushing.

## Citations status 2026-10-31
- Google Business Profile: phone 202-729-9509, hours, category IT security service (all pending Google review).
- Brownbook: live (business ID 56057714, account theinfinitumcorp+seo@).
- Foursquare: live https://app.foursquare.com/v/infinitum-corporation/6ae5b9c80d7e976db2a43b08
- Hotfrog: account made, submit blocked by human check (form at /admin/add).
- Cylex: Cloudflare block. EZlocal: timed out. ListYourself: needs a call to verify, skipped.
