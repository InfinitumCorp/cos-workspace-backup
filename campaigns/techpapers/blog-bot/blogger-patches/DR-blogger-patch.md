# Blogger patch spec — DR (Dead Reckoning)

**Status:** LOCAL PREP ONLY. Do not edit the live post until **2026-11-10 10:00 Europe/Moscow (MSK)**.  
**Live post (canonical; verified HTTP 200 on 2026-11-07):** https://infinitumwhitepapers.blogspot.com/2026/10/dead-reckoning-ai-security-operations.html  
**Paper:** Dead Reckoning: AI for Security Operations (Whitepaper No. 1)  
**Owner:** Blog Bot · TechPapers only

## Do / do not
- **Do:** replace the existing `cite-also` footer with `footers/DR-footer.html`; update Search description; verify Academia + DOI anchors; keep body text unchanged.
- **Do not:** invent URLs; touch company/personal websites; upload new assets; add phone, Discord, Substack, product/token/drone pitches, or Paper 3/EchoForm; claim the post was updated before execution day.

## Canonical / authority links (from papers.json + live footer + DataCite)
| Role | URL | Prep check |
|---|---|---|
| Blogger canonical | https://infinitumwhitepapers.blogspot.com/2026/10/dead-reckoning-ai-security-operations.html | HTTP 200; matches DataCite `IsIdenticalTo` |
| Academia | https://www.academia.edu/179949703/Dead_Reckoning_AI_for_Security_Operations | Present on live post; direct fetch 403 (bot wall). Re-verify signed-in on execution day |
| DOI | https://doi.org/10.5281/zenodo.23836365 | DataCite **findable**; title matches RELEASE |
| Zenodo record | https://zenodo.org/records/23836365 | HTML 403 here; DOI/DataCite OK |

## Search description (Blogger Post settings → Search description)
Paste exactly (143 characters; source-faithful to papers.json / RELEASE / DataCite abstract):

```
Mid-size cyber security ops and AI through an irregular-warfare lens: six use cases, NIST AI RMF, and a 90-day roadmap. Infinitum Corporation®.
```

**Why replace live text:** current meta (“90-day AI SOC plan…”) is thinner and more product-like than the paper’s scope (govern first, analysts in the loop, NIST AI RMF, six use cases, maturity self-assessment).

## Image / Open Graph (only where Blogger supports)
| Field | Supported? | Action |
|---|---|---|
| Search description → `meta name=description` + `og:description` | Yes (when search descriptions enabled) | Set text above |
| Featured / first image → `og:image` | Theme-dependent; already emitting og:image | **Flag:** body cover `src` https://raw.githubusercontent.com/InfinitumCorp/ukraine-files-flyers/main/wp-cover-01.jpg returns **HTTP 404**. Do **not** invent a replacement URL. Leave body image tag as-is until a verified Blogger-hosted cover URL exists; alt text may stay. |
| Image alt | Yes (image properties) | Keep existing descriptive alt if present |
| Twitter card meta | Not present / not a native Blogger field | **Unsupported — do not add** custom twitter:* tags unless theme already provides them |
| Custom JSON-LD edits | Theme/HTML already has ScholarlyArticle | Optional later; **out of scope** for this Nov 10 patch unless footer-only |

## Footer HTML
Exact replacement: [`footers/DR-footer.html`](footers/DR-footer.html)

Changes vs live footer:
- Academia + DOI kept exact; Academia anchor text expanded from “paper” to full short title (better backlink context).
- Removed **phone** (campaign: no phone in whitepaper posts).
- Removed **Discord** (campaign exclusion).
- Removed **Wayback** line (archive.org availability API: **no snapshot** for this URL — unsupported).
- Related list limited to verified same-blog DR/TD/CCW peers (no new invented posts).
- Brand: Infinitum Corporation®.

## Body
**Preserve entire existing body.** No paragraph edits in this task.
