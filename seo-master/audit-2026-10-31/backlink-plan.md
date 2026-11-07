# Backlink and entity plan (white-hat only), 2026-10-31
Hard rules: no PBNs, no link farms, no paid/sponsored links without rel="sponsored", no comment/forum spam, no mass auto-posting, no duplicate text across sites, no links from the ~85 sibling Vercel projects (capital-chronicles news sites, PR brands) to Infinitum: interlinking them would look like a private network. One brand-entity record (`/workspace/seo-master/ready/nap-canonical.json`) used everywhere.

## Tier 0: fix our own link graph first (hub and spoke, free, immediate)
| From | To | Placement | Status / who |
|---|---|---|---|
| Main site footer + JSON-LD sameAs | x.com/infinitumceo, Telegram, Discord, both main blogs, Whop, GitHub, williamaaronturner.com, Academia | footer icons + sameAs | Needs Ueni login (William) or GTM injection |
| Every Ukraine Files post | Main site | one in-body "About the author" line: "William Aaron Turner is founder of Infinitum Corporation, a cybersecurity consulting firm in Washington, DC" linked to www site | Blog Bot (Blogger session) |
| Whitepaper posts | Main site service pages (once they exist) | in-body contextual link | Blog Bot |
| Russia-Africa blogs | Ukraine Files canonical post + main site | header/footer | Blog Bot |
| williamaaronturner.com | https://www (not http) main site, blogs, X, Academia, Whop | links | William (Beacons) or deploy redesign repo |
| X, LinkedIn, Telegram, Discord, GitHub README, Whop | main site (UTM per `ready/utm-links.md`) | bio/website field | per bot, William approval for bios |
| Academia uploads | canonical blog URL + main site | abstract/description | Academia bot (browser) |

## Tier 1: entity listings (genuinely eligible, free)
| Listing | Why | Requirement / blocker |
|---|---|---|
| Google Business Profile | Local pack, knowledge panel | Fix phone to 202-729-9509, hours 24/7, website www; merge/remove suspended duplicate; William login |
| Bing Places (import GBP) | Bing/ChatGPT/Copilot local | After GBP fixed |
| Apple Business Connect | Apple Maps/Siri | Verification; William |
| Google Search Console + Bing Webmaster (all 5 sites) | Indexing, sitemaps, link data | William Google login; Blogger can add meta tag |
| Wikidata item | Knowledge-graph entity | Only if notability via independent sources exists. Currently only self-published + free wires -> likely deleted. Hold until 2+ independent press mentions. |
| Crunchbase | Entity + founder profile | Company-domain email; free |
| D-U-N-S | Prerequisite for SAM.gov, Apple | Legal-entity decision (CA close corp vs DC) |
| LinkedIn company page | Brand SERP slot | Create/claim ours with unique vanity URL e.g. /company/infinitum-corporation-dc |
| OpenCorporates / state registry | Already public (CA 5470106) | Make sure DC mailing address matches |
| ORCID iD for William | Research identity tying Academia/whitepapers | Free; William creates |
| Zenodo DOI for whitepapers | Citable, indexed by Google Scholar | Free; must be original research and same canonical text; William approval |

## Tier 2: quality directories (one each, manual, unique description)
Clutch (basic), GoodFirms, DesignRush (free listing), BBB (free profile), DC Chamber (paid: ask), UpCity, Manta, Hotfrog, Yelp (business owner), Foursquare. TGStat + Telemetr for Telegram. Max 2-3 per week, each with canonical NAP and a distinct description. Skip any requiring payment without William.

## Tier 3: earned links (highest value)
- Expert-source platforms: Qwoted, Featured.com, Help a B2B Writer, SourceBottle: William answers cybersecurity / AI-in-SOC / risk queries with his real expertise -> editorial links.
- Guest/contributed articles from whitepaper material (rewritten, not copied): HackerNoon, Dark Reading contributor, Security Boulevard (syndication allowed with canonical), Infosecurity Magazine opinion, LinkedIn articles (canonical back).
- Podcasts on cybersecurity/geopolitics (guest pitches) -> show-notes links.
- Original data assets: "Russia-Africa by the Numbers" style data briefs are citable; pitch to journalists covering the topic.
- Press: max 1-2 releases per week, each with real news, rotate wires (PressLiftoff, SubmitPR, openPR monthly, EIN only if William pays). DC dateline, canonical boilerplate, plain URLs. Stop 10-per-day bursts.
- Unlinked brand mentions: monitor (Google Alerts "Infinitum Corporation", "William Aaron Turner") and request a link politely.

## Do not do
Buy links/"guest post packages", Fiverr backlink gigs, GSA/automated directory blasts, Web 2.0 link wheels, cross-linking the sibling Vercel news sites or Blogger spin-off blogs purely for links, recreate Substack, re-upload the removed YouTube channel, publish identical articles on multiple blogs without canonical.
