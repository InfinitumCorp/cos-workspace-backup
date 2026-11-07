# LinkedIn readiness — preparation/read-only audit
Checked 2026-11-07 02:57 MSK (Europe/Moscow, UTC+3). No external mutations or messages. No credentials accessed. No browser used or recovery assumed.

## Verdict
NOT execution-ready. Local drafts and images exist; personal Buffer queue has no visible campaign rows, but company access, native LinkedIn activity and Sunday routine coverage are incomplete. A missing queue/log entry is NOT proof an asset was never posted.

## Live connector evidence
- Buffer get_channel confirms personal William Aaron Turner / williamaaronturner, channel `6ae0e21f2f1f5ed648eda184`, type `profile`, connected/unlocked; Europe/Moscow; queue not paused. Organization ID `65ff0e17ee308d133504f34e` (organization name not returned).
- Verified externalLink is https://www.linkedin.com/in/williamaaronturner — a MEMBER profile, NOT a company page.
- Buffer list_channels returns only that LinkedIn profile and X `infinitumceo`; no company LinkedIn channel. No verified company page URL/admin role. Old kit slug suggestions are not live verification.
- Buffer list_posts, all statuses, personal channel, Nov 9 00:00 through Nov 22 23:59:59 MSK: 0 edges, hasNextPage=false. Thus zero exact visible personal queue/activity matches for the 18 proposals. Company six rows cannot be checked in Buffer.
- Separate Buffer personal activity query Nov 2 00:00 MSK onward: 3 sent rows, hasNextPage=false: Irregular Warfare Handbook Nov 3 16:42:39 MSK (`6aea2c184c2249b6ae7a52f0`); unrelated excluded legacy promotion Nov 2 23:51:10 MSK; Trenches and Drones Nov 2 17:17:47 MSK (`6ae8da5c2ed49bb945c31409`). TD is historical reuse, not same-date duplicate of company Nov 10/17. Shortened lnkd.in links prevent URL-only canonical resolution; title/log mapping must supplement canonical IDs.
- Postiz postsListTool Nov 2 00:00–Nov 22 23:59:59 MSK: posts=[] (all states). This does not establish whether a company channel is connected there.
- An initial unfiltered Buffer history response was gateway-truncated; it is NOT evidence of exhaustive history. Narrow date queries above are complete per returned pagination.
- No native LinkedIn/browser activity, other organizations, scheduler routines or unseen queues audited. Chrome previously timed out at 30 seconds; no recovery assumed. No live link availability or PDF availability tested.

## Canonical dedupe ledger
Key = Academia numeric asset ID + personal/company + MSK calendar date, independent of time/caption/URL slug. 24 LinkedIn proposals: 18 personal + 6 company; zero duplicate keys inside merged calendar. Different channels remain separate keys.

| MSK date | MSK time | Channel | Canonical Academia ID | Live result |
|---|---|---|---|---|
| 2026-11-09 | 16:30 | personal | 179978972 | No match in Buffer window |
| 2026-11-09 | 17:00 | personal | 179949703 | No match in Buffer window |
| 2026-11-10 | 16:30 | personal | 179949845 | No match in Buffer window |
| 2026-11-10 | 17:00 | company | 180077697 | Company channel unavailable |
| 2026-11-11 | 16:30 | personal | 179950438 | No match in Buffer window |
| 2026-11-11 | 17:00 | personal | 179983771 | No match in Buffer window |
| 2026-11-12 | 16:30 | personal | 179950094 | No match in Buffer window |
| 2026-11-12 | 17:00 | company | 179950438 | Company channel unavailable |
| 2026-11-13 | 16:30 | personal | 179978796 | No match in Buffer window |
| 2026-11-13 | 17:00 | personal | 179950632 | No match in Buffer window |
| 2026-11-13 | 20:00 | company | 179978776 | Company channel unavailable |
| 2026-11-14 | 16:30 | personal | 179978315 | No match in Buffer window |
| 2026-11-16 | 16:30 | personal | 179978454 | No match in Buffer window |
| 2026-11-16 | 17:00 | personal | 179949703 | No match in Buffer window |
| 2026-11-17 | 16:30 | personal | 179978290 | No match in Buffer window |
| 2026-11-17 | 17:00 | company | 180077697 | Company channel unavailable |
| 2026-11-18 | 16:30 | personal | 179950353 | No match in Buffer window |
| 2026-11-18 | 17:00 | personal | 179983771 | No match in Buffer window |
| 2026-11-19 | 16:30 | personal | 179951053 | No match in Buffer window |
| 2026-11-19 | 17:00 | company | 179950438 | Company channel unavailable |
| 2026-11-20 | 16:30 | personal | 179950325 | No match in Buffer window |
| 2026-11-20 | 17:00 | personal | 179950632 | No match in Buffer window |
| 2026-11-20 | 20:00 | company | 179978776 | Company channel unavailable |
| 2026-11-21 | 16:30 | personal | 179977994 | No match in Buffer window |

## Cadence and Sunday collisions
- Six personal dates have two posts only 30 minutes apart: Nov 9/11/13/16/18/20 at 16:30 and 17:00 MSK. Assets differ, so these are cadence conflicts, not exact duplicate keys. Obtain explicit keep/move/suppress decision; do not silently change schedule.
- No new LinkedIn proposals on Sundays Nov 15/22. Existing source plan describes Sunday whitepaper rotation at 20:00 MSK. Neither Sunday has a visible Buffer personal post; Postiz window also empty. Actual routine paper selection and any native queue remain UNKNOWN. Therefore no visible same-date collision, not a cleared rotation. Also avoid repeated asset too close across adjacent dates even though dedupe key differs.
- Company RFH is Nov 13/20 at 20:00 MSK, not Saturdays. Do not run source calendars independently or reinstate old Saturday slots.

## Image availability (local, no uploads)
All 12 retained legacy caption files and matching flyers exist; flyers decode at 1200×627 in `/workspace/academia-promo/flyers/` (numbers 14,02,19,04,15,06,17,07,08,09,10,11). Captions read, not fact-checked against underlying papers.
Seven new campaign cards now exist in BOTH 1200×627 and 1080×1080 PNG sizes under `/workspace/campaigns/techpapers/cards/`:
- dr-dead-reckoning
- td-trenches-and-drones
- ccw-corporate-cognitive-warfare
- bch-battlefield-cyber-hygiene
- cdh-counter-drone-handbook
- rfh-reconnaissance-fusion-handbook
- dd-decentralized-disinformation
Append `-1200x627.png` or `-1080x1080.png` for exact filenames. Dimensions decoded successfully. Landscape contact sheet visually checked: correct Infinitum Corporation® placement, author credit, DC/contact footer, monochrome design; no obvious watermark. Individual full-size/mobile readability and square visuals still need final review. These appeared during the audit after the initial directory scan; availability assessment uses final scan. No distinct variant-B image set verified. Presence does not equal design approval.

## Caption readiness and gaps
- Week-2 variants are NOT missing anymore: `briefs/week-2-variants.md` supplies PERSONAL-DR/CCW/CDH and COMPANY-TD/BCH/RFH (plus seven X drafts outside this execution scope). All six LinkedIn scheduled week-2 variants exist; review/approval pending. Retained legacy captions unchanged, no new variant requirement invented.
- Week-1 company scheduled TD/BCH/RFH lacks Washington, DC opening and concluding discussion question. Proposed source-faithful local additions (not applied): prefix “Washington, DC. ”; TD question “Which aspect of network defense would you examine first?”; BCH “Which digital-hygiene topic deserves more attention in contested environments?”; RFH “Which intelligence-fusion challenge would you discuss first?” Week-2 company drafts already include these.
- Remove “Blog edition: n/a” from company BCH/RFH before final approval (also CDH/DD if later used; those are not scheduled company rows here). Preserve real DOI/Academia/Blogger links; do not invent missing DOI/blog URLs.
- Week-1 personal CCW/CDH generic “leaders who defend real networks” hook is a weak fit. PERSONAL-CDH week-2 repeats its hook in body; optional tighten after review. No product pitches found in TechPapers copy; consulting CTA only.
- Do not import old kit website/Discord/pentest promotion, account edits, launch posts or unverified slugs. Latest campaign restrictions override those older instructions. No personal press on company; all legacy war commentary personal only. Correct name always Infinitum Corporation®; trademarks never added to URLs/emails.

## Smallest next steps / approval scope
1. Review exact 24 merged LinkedIn rows, six cadence conflicts and final caption additions/removals; approve image-to-row mapping and week-2 variants. Source posts are not independently executable calendars.
2. Establish verified company PAGE URL, supported company channel identity/admin publishing access without treating a member profile as a page. Not established here; do not connect/install or use credentials in this task.
3. Before any write, re-read live personal/company queues/activity and Sunday Nov 15/22 selection using supported access; suppress canonical asset+channel+MSK-date duplicates. Native coverage remains a prerequisite, not a presumed empty queue.
4. Required explicit user approval: authorize scheduling/publishing the FINAL enumerated LinkedIn rows from this merged calendar to named personal channel and verified company page, with exact captions, selected images, URLs and MSK dates/times; explicitly accept or revise the six 30-minute personal double-post days; specify whether scheduling or immediate publication. Include uploading only the approved social card images if needed. No blanket approval from another agent is treated as consent.
5. Approval must exclude Paper 3/EchoForm document uploads, personal press to company, product/pentest promotion, Discord, website/account/routine changes, other networks and messages. Company execution remains blocked until identity/access and queue coverage are verified.

## Sources read
`briefs/linkedin-bot.md`, `cmo-calendar.md`, `brief.md`, `papers.json`, `linkedin-personal.md`, `linkedin-company.md`, `briefs/week-2-variants.md`, `briefs/graphicdesign-bot.md`, `/workspace/campaigns/academia-growth-plan.md`, `/workspace/academia-promo/plan.md`, `/workspace/academia-promo/posted-log.md`, all 12 scheduled legacy caption files, `/workspace/linkedin-company/kit.md`; live Buffer get_channel/list_channels/list_posts and Postiz postsListTool schemas/results. No external action taken.
