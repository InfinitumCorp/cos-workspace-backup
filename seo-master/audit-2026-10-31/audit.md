# Infinitum Corporation / William Aaron Turner: SEO audit (Phase 1)
Run 2026-10-31 02:13-02:19 MSK (UTC+3). Live crawl with Python requests (Chrome UA) of 61 URLs; raw HTML in `raw/`, per-URL metrics in `crawl.csv` / `crawl.json`, master list in `inventory.csv` (74 rows). Brand SERPs checked with web search. Prior plan `/workspace/seo-master/master-plan.md` (2026-10-26) was re-verified, not redone. Nothing external was edited or published.

## Property count
- 27 distinct web properties: 8 owned sites (Ueni main site, Vercel redesign, Vercel survey page, williamaaronturner.com, 4 Blogger blogs), 15 profiles (X @infinitumceo, X @infinitumusa, Telegram, Discord, Whop, GitHub, Academia, LinkedIn personal, LinkedIn company (unidentified), Google Business Profile, Instagram corp, Instagram personal, HackerOne, Reddit, Medium), 2 inactive (Substack suspended, YouTube removed), 2 third-party (bizprofile.net CA filing, nitter mirror).
- Content items: 15 press releases (11 PressLiftoff Oct 26-31, 3 on 24-7PressRelease 2021/2026, 1 openPR), 15 blog posts across 4 blogs, 13 Academia uploads, 2 whitepapers.

## Brand SERP snapshot (web search, 2026-10-31)
| Query | What ranks | Problem |
|---|---|---|
| "Infinitum Corporation" Washington DC | 1 main site, 2 legal notice, 3 bizprofile.net (Palo Alto CA entity), 4 LinkedIn personal, 5 about page | Old phone (202) 681-0120 shown in snippet; CA entity outranks profiles |
| "William Aaron Turner" Infinitum | 1 williamaaronturner.com (Beacons, 6 words), 2 bizprofile, 3-5 24-7PressRelease (Moscow dateline Aug 2026; 2021 releases with (202) 980-9300) | Founder SERP is owned by legacy/inconsistent pages; no blog/whitepaper/Whop |
| infinitumceo | nitter mirror, PressLiftoff Oct 26, LinkedIn, then unrelated Infinitum brands | x.com profile itself not in top 5 |
| "Infinitum Corp" cybersecurity consulting | main site, 24-7 Aug release, then infinitum-corp.com (Colombian real estate) | Name collision |
| "Ukraine Files" William Aaron Turner | ukrainianfiles.blogspot.com #1 | OK |
| Infinitum whitepaper "Dead Reckoning" AI security operations | none of ours (Dead Reckoning Foundry dominates) | Whitepaper not indexed/ranking |

## Per-property findings
### 1. Main website (theinfinitumcorporation.com, Ueni builder)
- 200 on both `www` and apex, no redirect; canonical = apex, sitemap = apex, while every backlink and our JSON-LD use `www` -> split signals.
- Title on all pages "Infinitum Corporation | IT Consultant in Washington, D.C."; meta descriptions generic/truncated ("Searching for IT Consultancy..."); ethical-hacking page description has boilerplate appended.
- Phone on every page, `tel:` and JSON-LD: (202) 681-0120 (canonical is 202-729-9509). Legal notice also +12026810120. WhatsApp link wa.me/16142162724.
- JSON-LD: LocalBusiness only; `sameAs` = Instagram, x.com/infinitumusa, and a raw GBP place ID (not a URL). No Organization/Person entity, no link to @infinitumceo, Telegram, blogs, Whop.
- Homepage 1.9 MB HTML (inline builder data); 0 internal `<a>` links detected server-side (JS nav) -> crawlability relies on sitemap.
- `/booking`: no H1, 30 words, no OG image. Sitemap lastmod stale (2025-01). robots.txt allows all, lists ueniweb sitemaps.
- No "Corporate Cognitive Warfare", "AI for security operations", "defense technology advisory" or "strategic risk assessment" copy anywhere; legacy service pages (construction, facility mgmt, healthcare IT, procurement) dilute topical focus.
### 2. Vercel redesign (infinitum-corporation.vercel.app, repo InfinitumCorp/infinitum-corporation-site)
- Correctly noindex/nofollow + robots Disallow (staging). Canonicals and sitemap already point to `https://www.theinfinitumcorporation.com/...` paths (`/about`, `/products/*`) that return 404 on the live domain. If the domain is cut over without removing noindex, the whole site deindexes; if not cut over, nothing here counts.
- Still uses (202) 681-0120. Organization JSON-LD present. 15 "product" pages (ORBIS etc.) described as inert prototype concepts.
### 3. Survey page (infinitum-survey-flyers.vercel.app)
- 131 bytes, title "Global Political Survey", no description, indexable. Thin page; noindex it.
### 4. williamaaronturner.com (Beacons)
- Ranks #1 for founder name but is 6 words of crawlable text, no H1; description/JSON-LD say "Private Military Contractor"; links to `http://www.theinfinitumcorporation.com/` (http), HackerOne, Instagram, Reddit, a private Telegram invite. `www.` host returns 500. Redesign repo exists but not deployed.
### 5-8. Blogger blogs
- Ukraine Files (11 posts + pages): strong on-page work already done (unique titles, 130-150 char descriptions, Person/WebSite JSON-LD with +1-202-729-9509, one H1 per post, 750-10,200 words). Gaps: homepage has no H1; two posts still have default slugs (`blog-post_26.html`, `blog-post_85.html`); posts have no in-body `<a>` link to the main website (JSON-LD only); not verified in Search Console.
- Whitepapers (2 posts): good BlogPosting/Organization/Person schema, links to site. Homepage no H1. "Dead Reckoning" not found in search -> indexing not confirmed.
- Russia-Africa Report and Russia-Africa by the Numbers (new, 1 post each): the Russia-Africa Summit article is a 100% duplicate (2,020 words identical) of the Ukraine Files post, both self-canonical -> duplicate content split. Both blogs are thin (1 post).
### 9. Press releases
- 11 PressLiftoff releases in 5 days (10 on Oct 31): all index,follow with NewsArticle schema and links to the site; 10/11 include 202-729-9509. Density on one free wire in one day risks looking like volume posting; Russia-Africa release shows raw markdown.
- 24-7PressRelease: Aug 1 2026 (MOSCOW dateline, "Willian" typo), Dec 2021 x2 ((202) 980-9300, @infinitumusa, Columbus OH contact). These rank for the founder name.
- openPR 4592982: Cloudflare blocks bots; Moscow wording per prior plan.
### 10. Profiles
- X @infinitumceo: indexable, bio has no keywords/link text beyond website; PMC wording. Not in top 5 for its own handle.
- Telegram: 7 subscribers; description says "from Moscow & Washington, D.C." and the "@infinitumceo" link points to `t.me/infinitumceo` (wrong; should be x.com/infinitumceo).
- Whop: good description with NAP and 24h; location label "Milan, IT" contradicts DC; 70 words; JSON-LD Corporation.
- GitHub InfinitumCorp: links to site; 5 public repos.
- Discord: 3 other members, no description.
- Academia.edu, Medium, openPR, LinkedIn: bot walls (403/999) -> need browser check.
- Inactive: Substack (404, suspended for spam), YouTube (removed). Leave dead; do not recreate under same name without William.
### 11. Entity/NAP conflicts in the wild
- Phones live: 202-729-9509 (canonical; blogs, Whop, PressLiftoff), (202) 681-0120 (website, Vercel redesign), (202) 980-9300 (2021 releases, GBP draft), 614-216-2724 (WhatsApp).
- Locations: DC (canonical), Moscow (24-7 Aug, Telegram, openPR), Milan (Whop), Columbus OH (2021 release contact), Palo Alto CA (state filing on bizprofile.net).
- Name collisions: goinfinitum.com (motors), infinitum.org (Web3), infinitum-corp.com (Colombia real estate), LinkedIn "INFINITUM".

## Top 10 issues (ranked by impact)
1. Main site shows wrong phone (202) 681-0120 in text, `tel:`, legal notice and JSON-LD; 4 phone numbers live across the web (NAP conflict -> local-pack and entity trust loss).
2. www vs apex both 200, canonical=apex while all links point at www; no redirect.
3. Main site JSON-LD `sameAs` points to @infinitumusa, Instagram and a non-URL place ID; no Organization/Person graph linking @infinitumceo, Telegram, blogs, Whop, GitHub.
4. Generic titles/meta ("IT Consultant") on every page; none of the boilerplate services (cybersecurity consulting, ethical hacking/vuln assessment, AI for security ops, risk assessment, defense tech advisory, Corporate Cognitive Warfare) are targeted.
5. Founder SERP is dominated by thin Beacons page (6 words, PMC wording) and legacy 24-7 releases with Moscow dateline/old phone.
6. Duplicate content: Russia-Africa Summit article identical on ukrainianfiles and russiaafricareport, both self-canonical.
7. Vercel redesign canonicals/sitemap reference www paths that 404 on the live domain; noindex must be removed only at cut-over.
8. Search Console / Bing Webmaster not verified for any property -> no indexing data; whitepaper not found in search.
9. Location inconsistencies on profiles: Telegram "from Moscow", Whop "Milan, IT", wrong t.me/infinitumceo link in Telegram description.
10. Press velocity: 10 PressLiftoff releases on one day on one free wire (after a Substack spam ban) -> diminishing value and spam-pattern risk; legacy markdown artifacts.
