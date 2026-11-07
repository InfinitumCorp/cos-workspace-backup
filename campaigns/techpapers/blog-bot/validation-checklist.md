# Blog Bot TechPapers — validation checklist (prep, 2026-11-07 MSK)

Local preparation only. Nothing published, scheduled, uploaded or messaged. No Canvas. No agent contact.

## Sources read
| Source | Path / URL | Used for |
|---|---|---|
| Blog Bot brief | `/workspace/campaigns/techpapers/briefs/blog-bot.md` | Scope, dates, exclusions |
| Merged CMO calendar | `/workspace/campaigns/techpapers/cmo-calendar.md` | Nov 10 / 16 / 18 / 20 slots |
| Site positioning | `/workspace/campaigns/techpapers/briefs/site-positioning.md` | Service-only framing; phone conflict noted |
| papers.json | `/workspace/campaigns/techpapers/papers.json` | Titles, Academia, DOI, Blogger URLs, keywords, short abstracts |
| DR RELEASE | `/workspace/whitepapers/01-ai-for-security-operations/Infinitum-Whitepaper-01-Dead-Reckoning-RELEASE.md` | Content fidelity |
| TD RELEASE + abstract | `/workspace/whitepapers/02-trenches-and-drones/Infinitum-Whitepaper-02-Trenches-and-Drones-RELEASE.md`, `release-abstract.md` | Content fidelity |
| CCW expanded sources | `/workspace/whitepapers/corporate-cognitive-warfare/src/00-front.md`, `09-close.md`, `release-kit/01-blog-summary.md`, `05-abstract-keywords.md`, `README.md` | Content fidelity + caveats |
| Live Blogger HTML | three infinitumwhitepapers.blogspot.com posts (curl) | Existing footers, meta, OG, cover refs |
| DataCite | `api.datacite.org/dois/10.5281/zenodo.{23836365,23887266,23838097}` | DOI findable + titles |

## Live link checks (prep environment)
| Asset | Check | Result |
|---|---|---|
| DR Blogger | GET | **200** — treat as live canonical |
| TD Blogger | GET | **200** |
| CCW Blogger | GET | **200** |
| DR/TD/CCW DOI via DataCite | API | **findable**; titles match RELEASE / papers.json |
| Zenodo HTML pages | GET | **403** (bot wall) — not evidence of absence; DOI/DataCite authoritative here |
| Academia.edu pages | GET | **403** (Cloudflare “Just a moment…”) — **incomplete direct verify**; URLs match papers.json + live Blogger footers; TD/CCW also in DataCite relatedIdentifiers |
| ORCID 0009-0002-1585-5442 | GET | **200** |
| theinfinitumcorporation.com | GET | **200** |
| DR GitHub cover `wp-cover-01.jpg` | GET | **404 — broken** on live DR body image |
| TD/CCW Blogger-hosted covers | GET | **200** |
| Wayback availability for three Blogger URLs | API | **no snapshots** — live footer Wayback links **unsupported** |
| Crossref for Zenodo DOIs | API | 404 expected (DataCite/Zenodo, not Crossref) |

## Campaign rule compliance in drafts
| Rule | Status |
|---|---|
| Infinitum Corporation® (never Infinitum® Corporation) | Applied in patch metas/footers and Medium drafts |
| cyber not IT | Applied (TD Medium uses cyber / network defense) |
| No phone in whitepaper posts | Footers remove phone; Medium drafts have email only |
| No Discord | Removed from proposed footers (present on live posts today) |
| No Substack | Not included; noted BLOCKED |
| No product/token/drone pitches, pentest, Paper3/EchoForm, website changes | Not included |
| CCW not battlefield validation | Explicit in CCW patch + Medium draft |
| Preserve Blogger bodies | Patch specs: footer + search description only |
| Never invent canonical URLs | Only papers.json / live / DataCite URLs used |
| Prep only; do not execute ahead of dates | Stated on every deliverable |
| Do not claim posts live beyond verified Blogger 200s; no agent contact | Observed |

## Unsupported / missing / blockers
1. **Academia direct HTML verification blocked (403)** — re-check signed-in on execution day before asserting page title/PDF availability.
2. **Zenodo HTML 403** — DOI/DataCite sufficient for prep; optional human open on execution day.
3. **DR cover image 404** — live body still points at missing GitHub raw URL; **no invented replacement** in this prep; GraphicDesign/hosting fix is out of scope for Blog Bot patch unless a verified Blogger URL already exists.
4. **Wayback links on live footers unsupported** — removed in proposed footer HTML.
5. **Medium account + canonical feature unverified** — calendar already flags; Nov 16/18/20 are draft prep, not approved publish slots.
6. **Twitter card meta** — not a supported Blogger post setting; flagged skip.
7. **Phone + Discord still on live footers today** — genuine compliance gap until Nov 10 patch executes.
8. **General promotional threads remain stopped** — TechPapers scoped only; do not revive other campaigns.

## Execution dates (MSK)
| When | Task | Artifacts |
|---|---|---|
| Nov 10 10:00 | Blogger SEO/backlink patches DR/TD/CCW | `blogger-patches/*.md` + `footers/*.html` |
| Nov 16 12:00 | DR Medium summary draft (not auto-publish) | `medium-drafts/2026-11-16-DR-medium-summary.md` |
| Nov 18 12:00 | TD Medium summary draft | `medium-drafts/2026-11-18-TD-medium-summary.md` |
| Nov 20 12:00 | CCW Medium summary draft | `medium-drafts/2026-11-20-CCW-medium-summary.md` |

## Medium draft word counts (body after metadata fence; prep recount 2026-11-07)
| File | Approx. words |
|---|---|
| `medium-drafts/2026-11-16-DR-medium-summary.md` | ~671 |
| `medium-drafts/2026-11-18-TD-medium-summary.md` | ~612 |
| `medium-drafts/2026-11-20-CCW-medium-summary.md` | ~593 |
