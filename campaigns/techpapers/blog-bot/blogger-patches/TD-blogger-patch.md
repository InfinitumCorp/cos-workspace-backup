# Blogger patch spec — TD (Trenches and Drones)

**Status:** LOCAL PREP ONLY. Do not edit the live post until **2026-11-10 10:00 Europe/Moscow (MSK)**.  
**Live post (canonical; verified HTTP 200 on 2026-11-07):** https://infinitumwhitepapers.blogspot.com/2026/11/trenches-and-drones-network-defense-for.html  
**Paper:** Trenches and Drones: Network Defense for a War of Attrition (Whitepaper No. 2)  
**Owner:** Blog Bot · TechPapers only

## Do / do not
- **Do:** replace `cite-also` with `footers/TD-footer.html`; update Search description; verify Academia + DOI; keep body unchanged.
- **Do not:** invent URLs; website changes; phone/Discord/Substack; product/token/drone sales pitches; execute before the calendar slot.

## Canonical / authority links
| Role | URL | Prep check |
|---|---|---|
| Blogger canonical | https://infinitumwhitepapers.blogspot.com/2026/11/trenches-and-drones-network-defense-for.html | HTTP 200 |
| Academia | https://www.academia.edu/180077697/Trenches_and_Drones_Network_Defense_for_a_War_of_Attrition_Whitepaper_ | On live post; DataCite relatedIdentifier `https://www.academia.edu/180077697/`; direct fetch 403 |
| DOI | https://doi.org/10.5281/zenodo.23887266 | DataCite **findable** |
| Zenodo record | https://zenodo.org/records/23887266 | HTML 403 here; DOI/DataCite OK |

## Search description
Paste exactly (146 characters; aligned to release-abstract.md / DataCite, not the live “drone-war lessons” shorthand):

```
Network defense as attrition: depth, cheap mass, trusted signals, sensors and supply lines—seven moves, 30/60/90-day plan. Infinitum Corporation®.
```

**Why replace live text:** live meta (“drone-war lessons turned into…”) overstates the paper’s careful analogy (comparison, not a claim the network is a front line; no party claims).

## Image / Open Graph
| Field | Supported? | Action |
|---|---|---|
| Search description | Yes | Set text above |
| `og:image` | Already present via Blogger-hosted cover | Keep; cover URL on blogger.googleusercontent checked HTTP 200 |
| Cover alt | Present on live post | Keep |
| Twitter cards | Not native | **Unsupported — skip** |

## Footer HTML
Exact replacement: [`footers/TD-footer.html`](footers/TD-footer.html)

Same hygiene as DR: no phone, no Discord, no unsupported Wayback line, Infinitum Corporation®, Academia/DOI exact.

## Body
**Preserve entire existing body.** No paragraph edits in this task.
