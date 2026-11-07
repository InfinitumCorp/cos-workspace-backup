# Infinitum Corporation: master SEO plan for every owned property
Prepared 2026-10-26 (Europe/Moscow) by Infinitum Marketing (CMO). Order from William: "SEO plan for everything we own!!! Execute."
Data rule: every number below was observed on 2026-10-26 from a public URL, a search result, or an existing workspace file. There are NO search volumes or rankings in this plan (none are available from free tools without Search Console access). Where something could not be checked it says so.
Nothing in this plan has been posted, submitted, published or edited externally. Ready-to-paste assets are in `/workspace/seo-master/ready/`. Per-bot task lists are in `/workspace/seo-master/briefs/`.

Related files (referenced, not redone): `/workspace/seo/seo-plan.md` and `/workspace/seo-apply/README-checklist.md` (blog SEO, Blog Bot applying), `/workspace/press/seo-plan.md` + `sites.md` (press), `/workspace/infinitum_directories.md` (directories), `/workspace/telegram_seo_plan.md` (Telegram).

## 0. What the live check found (the five facts that drive everything)
1. **Three different phone numbers are live and the official one (202-729-9509) is on none of the core assets.** Website footer, `tel:` links and JSON-LD: (202) 681-0120. `/workspace/infinitum_directories.md` and the Google Business Profile draft: (202) 980-9300. Website builder data also holds a WhatsApp number (614) 216-2724 (not seen as visible text). Only the Ukraine Files blog JSON-LD already carries +1-202-729-9509. Phone is part of NAP, so this is the single biggest local-SEO inconsistency.
2. **The main website says nothing about the brand positioning William chose.** Title on every page is "Infinitum Corporation | IT Consultant in Washington, D.C."; meta description "Searching for IT Consultancy in Washington, D.C.?..."; no Telegram, Discord or `x.com/infinitumceo` links (its JSON-LD and footer link `x.com/infinitumusa` and Instagram); no "open 24 hours" text (the JSON-LD does have 7-day 00:00-23:59 hours); sitemap last updated 2025-01-04 (booking page 2026-07-21); site is built on the Ueni builder (React app, 1.9 MB HTML). Good: HTTPS, canonical, one H1, OG tags, LocalBusiness JSON-LD with the DC address and geo.
3. **Two hostnames both return 200 with no redirect.** `https://theinfinitumcorporation.com/` (declared canonical, used in sitemap and JSON-LD `@id`) and `https://www.theinfinitumcorporation.com/`. All our blog JSON-LD and copy use `www`. Pick one primary domain in the builder so canonical, sitemap and structured data match what we link to.
4. **Google Analytics already appears in the site source**: GA4 ID `G-D4R817TGX6` (builder config key `google_analytics_measurement_id`) plus GTM `GTM-TG56DMZ`. This may be the answer to the "GA4 Measurement ID" blocker. Whether William owns that property cannot be verified without his Google login.
5. **Brand-name collisions and legacy conflicting copy are live.** Search for the brand shows: another "Infinitum" (electric motors, goinfinitum.com, Austin TX; also has the top YouTube result for "Infinitum"), a California close corporation named Infinitum Corporation (Palo Alto, listed on a third-party registry site, with William as agent and our DC address as mailing address), and an unrelated Spanish-language LinkedIn company page "INFINITUM" (62 followers) at `linkedin.com/company/infinitum-corporation`. The 24-7PressRelease piece (Aug 1, 2026) is datelined "MOSCOW, RUSSIA" and says William is "currently engaged in professional work in Russia"; the X bio and personal LinkedIn list DC first but also "Private Military Contractor". Every new asset must therefore pair the brand with "Washington, DC" and "cybersecurity".

## 1. Inventory (status checked 2026-10-26)
Priority: P0 = do this week, P1 = within 30 days, P2 = later/optional. "Blocker" is what stops a bot from doing it alone.

| # | Property | URL | Status observed live | Owner bot | Top 3 SEO gaps | Actions (summary) | Pri | Blocker |
|---|---|---|---|---|---|---|---|---|
| 1 | Main website | https://www.theinfinitumcorporation.com | 200, builder site, 20 URLs in sitemap, GA4+GTM present, title/meta say "IT Consultant" | CTO TechBot (+CMO copy) | (1) wrong phone (202) 681-0120, no 24-hours text, no Telegram/Discord/X links; (2) generic title/meta, JSON-LD sameAs wrong (infinitumusa, Instagram); (3) www/non-www duplicate, stale sitemap, no GSC/Bing verification | Apply `ready/website-meta-copy.md`, `ready/website-jsonld.html`, footer NAP+links, pick primary host, add `/community` page linking Telegram/Discord/X/blogs, verify GSC+Bing, confirm GA4 ID | P0 | Site-builder login (William); GSC login |
| 2 | Google Business Profile | business.google.com (listing "INFINITUM CORPORATION") | Verified listing edited 2026-10-25, edits pending review; a second suspended listing at the same address exists; box browser cannot reach business.google.com | CMO (browser) / William | (1) phone on listing is the old (202) 980-9300 draft; (2) hours must read open 24 hours; (3) no posts/photos/Q&A; website link and category pending | Set phone 202-729-9509 as primary (keep old numbers as "additional" for 90 days so citations still match), hours 24/7, description from `ready/`, services, UTM website link, add Nov 1 10:00 post if William still wants it | P0 | Browser reach to business.google.com, or William does it |
| 3 | Ukraine Files blog | https://ukrainianfiles.blogspot.com | 200; JSON-LD graph already live with DC address, +1-202-729-9509, 24h hours, sameAs (X, Telegram, Discord, GitHub, both blogs); meta description updated | Blog Bot | Defense advisory post removed (stays down); fact flags (EEF 78 vs 80 countries; Russia growth numbers) pending William; Search Console not verified | Finish `/workspace/seo-apply` checklist (robots, labels, alt text, related links); no links to the removed post | P0 (in progress) | Blogger session; William on fact flags |
| 4 | Whitepapers blog | https://infinitumwhitepapers.blogspot.com | 200; JSON-LD has Organization but no sameAs/Telegram/phone yet; description "Practical, integrated security thinking..."; robots default | Blog Bot | Not yet carrying NAP/sameAs; zero internal links to site; images on raw.githubusercontent.com | Apply seo-apply WP phase; link each paper to the website anchor "cybersecurity consulting in Washington, DC" | P0 (in progress) | Blogger session |
| 5 | X (CEO) | https://x.com/infinitumceo | 200. Bio: "CEO: INFINITUM CORPORATION \| Consultant, Developer, Operator, and (P)rivate (M)ilitary (C)ontractor. \| DC - MEXICO CITY - LONDON - DUBAI - MOSCOW - BEIJING" | X Bot (non-war items only) | (1) bio has no link/keywords/phone; (2) PMC wording conflicts with sanitized listing wording; (3) no pinned post to website | Bio option A/B in `ready/`, website field, pinned non-war post | P1 | William approves bio text; no bot can edit the profile today |
| 6 | X (legacy) | https://x.com/infinitumusa | 200, linked from website footer and JSON-LD. Ownership unknown | William | Website links to an account that is not `@infinitumceo` | Confirm owner; either claim and align, or remove the link from the site | P1 | William |
| 7 | Telegram channel | https://t.me/infinitumcorporation | 200; 6 subscribers; title "Infinitum Corporation \| Geopolitics, Ukraine War, Drones & Crypto"; description starts "from Moscow & Washington, D.C." | Telegram Bot | (1) description conflicts with DC-HQ rule and lacks "open 24 hours"; (2) not in TGStat/Telemetr (as of 10-25 per its plan); (3) no external backlinks | New title/description from `ready/`, pinned post, directory submission, "Share" line weekly | P1 | William approves positioning change |
| 8 | Discord server | https://discord.gg/QVT7dWHUQa (server "Infinitum Corp 1") | Invite valid, never expires, server shows 2 members, no icon or description | Discord Bot | (1) no server description/icon/topic; (2) no pinned welcome with NAP and links; (3) not listed anywhere | Server description, welcome channel, link from site/Telegram/X | P1 | Admin rights (bot has webhook only?) confirm |
| 9 | LinkedIn company page | URL unknown. `linkedin.com/company/infinitum-corporation` is a DIFFERENT Spanish digital-transformation company | No admin access to ours | LinkedIn Bot / William | Cannot be edited, URL not recorded | William gives page URL and admin invite; then use `ready/` About and tagline | P0 | Admin access |
| 10 | LinkedIn personal (William) | https://linkedin.com/in/william-aaron-t-726076244 | 200; public headline reads "A killer in a suit!"; About repeats X bio incl. PMC; 326 followers, 216 connections | LinkedIn Bot (draft only) | (1) headline is not keyworded and not professional; (2) About lacks DC HQ/24h/phone/links; (3) no Featured links | Propose headline in `ready/`, About, Featured: website, whitepapers, Telegram | P1 | William approves each edit; custom URL change optional |
| 11 | Whop store | https://whop.com/infinitum-corporation/ | 200; indexable; description "headquartered in Washington, DC, with operations in Moscow"; shows 1 member, no posts; location label "Milan, IT" | Whop Bot | (1) no 24h/phone/website link/Telegram in description; (2) location label wrong; (3) no posts/reviews; square logo pending | Description from `ready/`, set location, website link, product titles with keywords | P1 | Whop ID verification and square logo (known blockers) |
| 12 | YouTube | Handle `@infinitumcorporation` returns 404; actual channel URL not recorded | Unknown | YouTube Bot | Channel URL/handle not confirmed; unrelated "Infinitum" channel outranks | Confirm channel, set description/links/banner, handle = infinitumcorporation if free | P2 | Channel URL and owner login |
| 13 | Survey site | https://infinitum-survey-flyers.vercel.app | 200, 131-byte page linking the Jotform survey (no description, no noindex); survey https://form.jotform.com/262853312730049 | CTO TechBot | Thin utility page can be indexed under the brand | Add `<meta name="robots" content="noindex">` or redirect to website; keep Jotform noindex-friendly | P2 | Vercel access |
| 14 | Press releases | PressLiftoff 2026-10-26; openPR 4592982; 24-7PressRelease 537353 (2026-08-01); webnewswire/24-7 2021 | Live. Oct 26 PressLiftoff piece: DC HQ, no phone. Aug 1 piece: Moscow dateline | PressRelease Bot | (1) legacy releases say Moscow HQ; (2) boilerplate lacks phone/24h; (3) few releases indexed | Standard boilerplate, DC dateline, keep schedule in `/workspace/press/seo-plan.md` (the two blog-promo releases that linked the removed defense advisory post stay skipped, per William) | P1 | Wire edit fees; no purchases |
| 15 | Email domain | theinfinitumcorporation.com mail, infinitum-media@mail.grokbot.com | Not checked (DNS tools not authorized) | EmailBot / CTO | Signature NAP; SPF/DKIM/DMARC state unknown | Standard signature; ask CTO to check DNS records | P2 | DNS access |
| 16 | Directories/citations | see `/workspace/infinitum_directories.md` | Nothing submitted; file still lists (202) 980-9300 as canonical | CMO + William | Old phone in file; D-U-N-S, Bing, Apple, Crunchbase unclaimed | Update canonical NAP, then claim in order in section 5 | P1 | William (verification, free vs paid) |
| 17 | Other branded profiles of unconfirmed ownership | Instagram `instagram.com/infinitumcorporation` (23K followers, 0 posts per page meta), GitHub `github.com/InfinitumCorp` (3 repos), `williamaaronturner.com` (Beacons link page, bio incl. PMC), Reddit r/Infinitumcorporation (named in Telegram plan, not re-checked) | All 200 except Reddit unchecked | William | Unknown ownership; bio wording inconsistent | William confirms which are his; if yes align bio/links | P2 | William |

## 2. Unified keyword map (no volumes; based on page content, services, and SERP observations from this session)
Rule: one primary phrase per page; always pair the brand with "Washington, DC" or "cybersecurity" because of the collisions in section 0.

| Cluster | Primary phrase | Supporting phrases | Lives on |
|---|---|---|---|
| Brand | Infinitum Corporation Washington DC | Infinitum Corporation cybersecurity; William Aaron Turner Infinitum | Home, GBP, LinkedIn company, all profiles, JSON-LD `name` |
| Local services | cybersecurity consulting Washington DC | security consulting DC; IT consulting Washington DC; open 24 hours cybersecurity | Home, Security consulting page, GBP, Bing Places |
| Pen testing (approved free offer, flyers only) | ethical hacking Washington DC | vulnerability assessment; penetration testing services | Ethical hacking page, flyers (already approved channels), whitepapers |
| Defense tech | defense technology advisory Washington DC | counter-UAS integration advisory; C4ISR support consulting | Press releases (the two blog-promo releases that linked the removed defense advisory post stay skipped, per William), Whop, whitepapers |
| AI | AI for security operations | AI applications for security operations | Whitepaper 01, press Day 3, Whop |
| Risk | strategic risk assessment | security risk assessment for government | Press Day 6, services page |
| Thought leadership (blog only) | The Ukraine Files | audit Ukraine aid NGO; In-Q-Tel; Russia economy under sanctions (per `/workspace/seo/seo-plan.md` section 3) | Ukraine Files blog only. Not on X, not on the website, not in X Bot copy |
| Community | Infinitum Corporation Telegram | Infinitum Discord | Telegram, Discord, website `/community` |

Competitive observations (real, from earlier session SERP checks in `/workspace/seo/seo-plan.md`): DC defense-advisory results are held by Wolverine Group, CADRE, DC Strategic Group. These are named so the page copy can differentiate; no ranking claims are made.

## 3. NAP consistency checklist (canonical record: `ready/nap-canonical.json`)
Canonical: **Infinitum Corporation** | **1629 K Street NW, Suite 300, Washington, DC 20006** | **202-729-9509** (schema +1-202-729-9509) | info@theinfinitumcorporation.com | https://www.theinfinitumcorporation.com | **Open 24 hours** | Founder William Aaron Turner | HQ Washington, DC (Moscow operating location only).
Checklist (mark when done; owner in brackets):
- [ ] Website footer, contact block, `tel:` links, JSON-LD: (202) 681-0120 -> 202-729-9509 [CTO]
- [ ] Website text says "Open 24 hours" (JSON-LD already 24/7) [CTO]
- [ ] GBP primary phone -> 202-729-9509; old numbers as additional [CMO/William]
- [ ] Remove or rewrite "(202) 980-9300" in `/workspace/infinitum_directories.md` (done in section 5 of this plan; file not edited so the original record stays) [CMO]
- [ ] Ukraine Files blog JSON-LD: already correct (verified live) [Blog Bot]
- [ ] Whitepapers blog JSON-LD + footer: not yet [Blog Bot]
- [ ] X bio, LinkedIn company/personal, Telegram description, Discord, Whop, YouTube: copy in `ready/profile-and-directory-copy.md` [each bot]
- [ ] Press boilerplate: add phone, "open 24 hours", DC HQ [PressRelease Bot]
- [ ] Email signature [EmailBot]
- [ ] Legacy mismatches to either leave or request edits: 24-7PressRelease Aug 1 (Moscow dateline), openPR 4592982 (Moscow), 2021 releases. These need William's call; wire edits may cost money [William]
- [ ] Legal entity check: third-party registry data shows a California close corporation with this name filed 2023-01-26 and Palo Alto principal address, DC mailing address. Before D&B, SAM.gov, Apple or Bing verification, William should confirm which legal entity owns the DC office and brand (I cannot verify from public sources) [William]
Formatting rules: "Infinitum Corporation" in prose; "INFINITUM CORPORATION" only where the registry/GBP requires; "1629 K Street NW, Suite 300" (never "K St" or "Ste"); phone as 202-729-9509; no Moscow address anywhere; always the same email.

## 4. Backlink and internal cross-linking plan
Hub and spoke: the website is the hub; every other property links to it with the same anchor family and the website links back to all of them.

| From | To | Anchor/placement | Owner |
|---|---|---|---|
| Website footer + new `/community` page | Telegram, X (@infinitumceo), Discord, both blogs, Whop, GitHub | "Telegram channel", "Whitepapers", etc. | CTO |
| Both blogs (footer, About, Contact, each paper) | Website | "Infinitum Corporation, cybersecurity consulting in Washington, DC" | Blog Bot |
| Whitepapers blog | Telegram, Discord, Whop | footer block | Blog Bot |
| Ukraine Files blog | Website, Telegram, Discord, X, Whitepapers | footer block (already in JSON-LD) | Blog Bot |
| Telegram description + pinned post | Website, X, Discord, Whitepapers | plain URLs | Telegram Bot |
| X bio/website field/pinned post | Website (UTM), Telegram, Whitepaper 01 | no Ukraine/war links | X Bot |
| LinkedIn company/personal Featured | Website, Whitepapers, Telegram | | LinkedIn Bot |
| Discord welcome | Website, Telegram, X, Whitepapers | | Discord Bot |
| Whop description + each product | Website, Telegram | | Whop Bot |
| YouTube channel + each video | Website, Telegram | first line of description | YouTube Bot |
| Press releases | Website, Telegram (in the release text only; never post the release to Telegram), X, Discord | plain URL, no anchor text games (wires reject them) | PressRelease Bot |
| GBP | Website with UTM, `/booking` as appointment link | | CMO/William |
| Email signature | Website, Telegram | | EmailBot |
Earned/third-party backlinks, in priority order (all free; paid items need William): Bing Places, Apple Business Connect, D-U-N-S, Crunchbase, LinkedIn page, BBB free profile, Clutch Basic, GoodFirms, TGStat/Telemetr, HackerNoon article from whitepaper excerpt, Qwoted/Featured expert profile. Details and verification notes: `/workspace/infinitum_directories.md` (use this plan's phone, not the phone in that file).
Rule: no more than one placement of the same text per site; no duplicate press text across wires; no purchased links.

## 5. Directory order (free first, details in `/workspace/infinitum_directories.md`)
1 Fix NAP on GBP and website. 2 Bing Places (import from GBP). 3 D-U-N-S lookup/claim (start now: up to 30 business days). 4 Apple Business Connect (needs 2 verifications). 5 LinkedIn company page claim. 6 Crunchbase (needs a company-domain email). 7 BBB free profile. 8 Clutch Basic, GoodFirms. 9 TGStat, Telemetr for the Telegram channel. 10 SAM.gov only if William wants federal work. Stop and ask William before any dues or paid tier (DC Chamber, NVTC, AFCEA, NDIA, Clutch Verified).
Decisions already known to be needed: whether Suite 300 is a real office (virtual-office rejection risk on Bing/DC CBE), and which legal entity name to use.

## 6. Schema / sameAs plan
One entity graph, same `@id` everywhere: `https://www.theinfinitumcorporation.com/#organization` (type Organization + ProfessionalService), person `.../#william-aaron-turner`. Already live on the Ukraine Files blog with its own person `@id`; WP blog gets the same.
`sameAs` list (only profiles the company controls and has verified): X https://x.com/infinitumceo, Telegram https://t.me/infinitumcorporation, Discord https://discord.gg/QVT7dWHUQa, Whitepapers blog, Ukraine Files blog, Whop store, GitHub org. Add the LinkedIn company page and YouTube URL when confirmed; remove `x.com/infinitumusa` and the GBP place-ID string "ChIJGdA6L8UdjKwRFOJoG7YqzvA" (currently inside website sameAs, which is not a URL). Instagram only if William confirms it is his.
Ready file: `ready/website-jsonld.html` (valid JSON, parsed by script). Whether the Ueni builder accepts custom `<script>` is unverified (flagged in the file and in the CTO brief). Fallback: Google Tag Manager (GTM-TG56DMZ is already on the site) can inject the same JSON-LD without touching the builder.
Not recommended: FAQPage markup (Google no longer shows FAQ rich results for most sites), fake review/aggregateRating markup (policy violation), anything claiming awards or clients.
Other machine-readable aids: `ready/llms.txt` (an emerging convention; no confirmed ranking effect, harmless; needs root hosting the Ueni builder may not allow, so a fallback is hosting it at a path on a property we control and linking it); keep the builder's robots.txt (it allows all and lists sitemaps).

## 7. 30-day calendar (Oct 27 to Nov 25, 2026; times Europe/Moscow; DST in US ends Nov 1: 5 PM ET moves from 00:00 to 01:00 Moscow time)
| Date | Task | Owner |
|---|---|---|
| Oct 27 | William decisions batch (section 9). CTO/William: builder login, confirm GA4 ID `G-D4R817TGX6`. Blog Bot continues seo-apply (UF then WP). | William, CTO, Blog Bot |
| Oct 27-28 | GBP: phone, hours, description (if browser reaches; else William). Blog Bot finishes UF. PressRelease Day 1 (PressLiftoff) with new boilerplate. | CMO, Blog Bot, PressRelease |
| Oct 28-29 | Website: title/meta, footer NAP, links, JSON-LD (builder login needed). Telegram description/title (after approval). WP blog SEO phase. | CTO, Telegram Bot, Blog Bot |
| Oct 30 | Verify Search Console: website (domain), both blogs (HTML tag); submit sitemaps; Bing WMT import. | William (login), Blog Bot adds tags |
| Oct 31 | Bing Places claim (import from GBP). D-U-N-S lookup/application. Discord description and welcome post. | William/CMO, Discord Bot |
| Nov 1 | GBP post 10:00 if William still wants it (not scheduled yet). Whop description and location label. X bio and pinned post (if approved). | CMO, Whop Bot, X Bot |
| Nov 2-4 | LinkedIn company page claim and About; personal profile proposals reviewed. Apple Business Connect. TGStat + Telemetr submission. Press Days 2-4 per `/workspace/press/seo-plan.md`. | William, LinkedIn Bot, Telegram Bot, PressRelease |
| Nov 5-8 | Crunchbase (company email), BBB free profile, Clutch Basic, GoodFirms. Internal link audit. First GSC data check. | CMO/William |
| Nov 9-15 | Content: one new whitepaper-derived page on the website `/resources` (needs builder) or HackerNoon article. YouTube channel setup if URL confirmed. Re-crawl all properties and diff against this plan. | CTO, Blog Bot, YouTube Bot |
| Nov 16-22 | Fix whatever the re-crawl/GSC Coverage report shows; request indexing for changed URLs. Telegram directory listings check. | CMO, bots |
| Nov 23-25 | 30-day KPI report (section 8) to William; decide on paid items (none assumed). | CMO |
No new public offers or posts go out from this calendar without William's approval. Approved posting streams (pentest flyer series; Discord webhook) continue under their own schedules.

## 8. KPIs, free tools only (baseline = observed 2026-10-26)
| KPI | Tool | Baseline | 30-day target |
|---|---|---|---|
| Website indexed pages | Google Search Console (needs William's verification), `site:` query | not measurable yet (GSC not verified) | all 20 sitemap URLs indexed |
| Brand-query impressions/clicks ("infinitum corporation", "infinitum corporation washington dc") | GSC Performance | not measurable yet | set baseline in week 2 |
| NAP consistency | Manual checklist in section 3 plus `curl` crawl | website 1 of 3 NAP elements right (address yes, phone no, hours JSON-LD only) | 100% of owned profiles |
| Structured data valid | Rich Results Test / Schema validator (free) | website: LocalBusiness only; UF blog: Organization+Person; WP: Organization | all three on the same entity graph |
| GBP views, calls, direction requests | GBP Performance | listing edits pending | first 30 days logged |
| Telegram subscribers / post views | Telegram channel stats, TGStat | 6 subscribers | set by Telegram Bot; no number promised |
| Discord members | Server settings | 2 | tracked weekly |
| X followers, profile visits | X analytics | not read (fetcher blocks counts) | tracked weekly |
| LinkedIn personal followers | LinkedIn analytics | 326 followers (public SERP data) | tracked weekly |
| Whop store visits | Whop dashboard | 1 member | tracked |
| Referring domains / backlinks | GSC Links report, free backlink checker | unknown | count new profiles/directories live |
| Website sessions by source (UTM) | GA4 (ID found `G-D4R817TGX6`, ownership unconfirmed) | unknown | per-source report from `ready/utm-links.md` |
| Press pages indexed | `site:` + exact title search | per `/workspace/press/seo-plan.md` | >= 3 indexed (that plan's own target) |
Weekly manual brand SERP check: search "Infinitum Corporation Washington DC" and "William Aaron Turner Infinitum" and log which of our properties appear.

## 9. Blockers and decisions that need William
1. Site-builder (Ueni) login for the CTO, or approval to do it himself. Confirm GA4 `G-D4R817TGX6` is his property (or give the correct ID).
2. Search Console and Bing Webmaster verification (his Google login) for the website and both blogs.
3. Primary domain: `www` or non-www (builder currently canonical = non-www).
4. Approve: Telegram title/description change; X bio (option A or B in `ready/`); LinkedIn personal headline/About; removal of "Private Military Contractor" and "A killer in a suit!" wording across profiles (all optional; he must say yes).
5. LinkedIn company page: URL and admin invite (the guessed URL belongs to another company).
6. Google Business Profile: reach business.google.com (egress) or edit phone/hours himself; keep or drop the Nov 1 10:00 post.
7. Which of these are his: Instagram @infinitumcorporation (23K followers), x.com/infinitumusa, GitHub InfinitumCorp, williamaaronturner.com, Reddit r/Infinitumcorporation, YouTube channel URL, and whether Whop's "Milan, IT" location is intended.
8. Legal entity name/address to use for D&B, Apple, Bing, SAM.gov, and whether Suite 300 is a staffed office.
9. Legacy "Moscow" press copy (24-7PressRelease Aug 1 2026, openPR 4592982): leave, or request edits (may cost money).
10. Blog fact flags from `/workspace/seo/seo-plan.md` (EEF figures, Russia growth figures) and the Useful Idiots legal read; unchanged and unresolved.
