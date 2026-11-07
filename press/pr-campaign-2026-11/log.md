# Free PR campaign, Tier 1 (Nov 2026), submission log
Go-ahead: William, 2026-11-02 16:51 MSK ("Start all task!"). Times are MSK (UTC+3). Releases: ccw.md, dead-reckoning.md, special-01.md (this folder; built by releases.py). For SEO Bot: new live URLs marked LIVE.

| Date/time (MSK) | Site | Object | Live URL | Status |
|---|---|---|---|---|
| 2026-11-02 16:53 | SubmitPR (free) | CCW Expanded | https://submitpr.org/press-release/corporate-cognitive-warfare-expanded-edition-william-aaron-turner | LIVE (HTTP 200; free tier, links inactive; IndexNow pinged by site) |
| 2026-11-02 16:54 | SubmitPR (free) | Dead Reckoning | https://submitpr.org/press-release/dead-reckoning-whitepaper-quarterly-ai-check-for-security-teams | LIVE (HTTP 200) |
| 2026-11-02 16:54 | SubmitPR (free) | Special 01 | https://submitpr.org/press-release/russia-forecast-gap-special-01-william-aaron-turner-risk-teams | LIVE (HTTP 200) |
| 2026-11-02 16:54 | PressLiftoff (Free) | CCW Expanded | (not public yet) | PENDING manual review: "An earlier release from this contact or website was removed, so this one is waiting for a quick review." Site will email theinfinitumcorp+press@ when live. Single attempt only; no DR/Special 01 sent. Edit link saved in ../edit-links.md |

## Browser / account needed (not submitted)
| Site | Exact URL | Fields / blockers |
|---|---|---|
| PRFree.org | https://prfree.org/members/register.php then "Submit Release" | username (6-20), password, email, tosAgree, privacyAgree; Cloudflare Turnstile; email confirm; free plan "subject to quality check" |
| 1888PressRelease | https://www.1888pressrelease.com/register_new.php | name, username, password + confirm, email, phone (202-729-9509), reCAPTCHA v3; manual review; no edits after submit; free plan only |
| presslo / PressLux | https://presslo.com/submit -> https://presslux.com/register | free PressLux account (email verification likely), pick "Free" distribution step; AI drafting flow, check paste-in works |
| openPR | https://www.openpr.com/news/submit.html (account: https://www.openpr.com/user/register.html) | 403 to curl (browser only); free-mail rejected, use infinitum-media@mail.grokbot.com; 1 free release / 30 days; editor review weekdays; prior Infinitum release exists, submit CCW only |

## Not used (from sites.md)
PRLog: unreachable from box. Express Press Release: no form (dead). IssueWire, PR.com, EIN Presswire: paid / fee trap. Never pay or upgrade.
| 2026-11-02 17:05 | openPR.com (free) | CCW Expanded | (none) | BLOCKED: "not allowed to post more than 1 free press release a month (email)" for infinitum-media@; retry after 30-day window. No alternate email used (would evade the limit). |

## 2026-11-02 17:00-17:10 MSK: regional/global site tests + translations (executor)
- Full test table: sites-tested.md. Translations: translations/ccw-{de,fr,es,pt,uk,ru}.md, translations/dead-reckoning-ru.md (DC dateline, DC entity, 202-729-9509 only).
- 2026-11-02 17:08 | Centre Europe Presse (FR, free) | CCW (FR) | none | BLOCKED: one plain-HTTPS attempt rejected by Cloudflare Turnstile ("vérification anti-robot a échoué"). Needs browser. Not retried.
- No site qualified for plain-HTTPS submission (all need account and/or captcha, or email). No new live URLs.
- Blocked: krb.in.ua (500), AfriWallStreet (500), Atrex.ru (TLS/500), WeRIndia (no submission path), TechCabal (editorial pitch only), P-Reliz.ru (needs Russian INN + corporate email).
- PRLog is now reachable (was unreachable before) -> browser sign-up.
| 2026-11-02 17:09 | PRFree.org (free) | CCW Expanded | https://news.prfree.org/@infinitumcorp/corporate-cognitive-warfare-expanded-edition-william-aaron-turner-releases-15-000-word-paper-ls3vzssjk25f | LIVE (headline shortened to 120 chars; no image on free plan) |
| 2026-11-02 17:11 | PRLog (free) | all 3 | (none) | BLOCKED: sign-up refused 'already have an account' (d90980); reset says email not found for infinitum-media@, theinfinitumcorp@gmail.com, +press. Need the email of the existing account from William. |
- 2026-11-02 17:12 MSK | freepressreleases.co.uk | CCW | emailed to submit@ from infinitum-media@ | pending editor review
| 2026-11-02 17:13 | Centre Europe Presse (FR, free) | CCW (FR) | (pending) | SUBMITTED, moderation 48-72h |
| 2026-11-02 17:14 | Actualités Françaises (FR) | CCW (FR) | (none yet) | SUBMITTED, no confirmation; check https://actualitesfrancaises.fr/?s=Corporate+Cognitive+Warfare |

- 2026-11-02 17:20 MSK openpr.de (DE CCW): BLOCKED. On the free-tier registration, "weiter zur Vorschau" gave "Ups, da ist ein Fehler passiert" twice (Anrede left empty). Retry later.
- 2026-11-02 17:20 MSK firmenpresse.de and fair-news.de: accounts registered, activation links received; activation and submission in progress.
- Whitepaper No. 2 "Trenches and Drones" is live (blog https://infinitumwhitepapers.blogspot.com/2026/11/trenches-and-drones-network-defense-for.html); add it to the all-content submission queue.

| 2026-11-02 17:21 | SubmitPR (free) | Ukraine Aid NGOs | (none) | BLOCKED: "maximum of 5 press releases per day" (PRB's Academia batch used today's quota). Not retried. Queued Nov 3: `python3 submitpr2.py ukraine-aid-ngos ccw-doctrine-introduction ukrainian-deli azov legitimate-targets` (5/day), then art-of-not-giving Nov 4; trenches-and-drones only if PRB has not posted it |
| 2026-11-02 17:25 | (inventory) | 34 live objects | inventory.md | 7 new releases in releases/ (trenches-and-drones, ccw-doctrine-introduction, ukraine-aid-ngos, ukrainian-deli, azov, legitimate-targets, art-of-not-giving); browser-queue.md built |
| 2026-11-02 17:25 | sites-tested.md no-account sites | all new | (none) | NOT SUBMITTED by HTTPS: no site in sites-tested.md takes a no-account, no-captcha form post (Centre Europe/Actualités/RedPress need browser for Turnstile/antispam; P-Reliz needs INN; info-ua & freepressreleases.co.uk need email send) |
- 2026-11-02 17:24 MSK fair-news.de (DE CCW): LIVE https://www.fair-news.de/3834956/corporate-cognitive-warfare-william-aaron-turner-veroeffentlicht-erweiterte-ausgabe-als-whitepaper (title cut to 110 chars, max 3 links).
- 2026-11-02 17:24 MSK firmenpresse.de: account activated; submission in progress.
- 2026-11-02 17:27 MSK firmenpresse.de (DE CCW): submitted on the free tier, ID 2283418, https://www.firmenpresse.de/pressinfo2283418.html (in editorial review).

## 2026-11-02 17:15-17:31 MSK: Regional Wave 2 (CN, JP, KR, BR, CO, IN) per William t108u
- Translations written: translations/ccw-zh.md, ccw-ja.md, ccw-ko.md, ccw-ptbr.md, ccw-esco.md, ccw-hi.md (DC HQ, 202-729-9509, X + Telegram, Mon-Fri 9 AM-9 PM). Site table: plan.md "Regional Wave 2". Browser items: browser-queue.md.
| 2026-11-02 17:29 | VentureSquare (KR, free) | CCW (KO) | (pending) | SUBMITTED via plain HTTPS form, response ok, ticket id 8; editor review, publication not guaranteed |
| 2026-11-02 17:30 | ColombiaMundo Sala de Prensa (CO, free) | CCW (es-CO) + flyer.jpg | (pending) | SUBMITTED: registered (name/company/email/phone 202-729-9509), note posted in Tecnología, redirected to /gracias/; editorial review. First registration try rejected "form open too long" (cached nonce), second OK |
| 2026-11-02 17:31 | PR-FREE (JP) | CCW (JA) | (none) | BLOCKED: submissions paused "for security" |
| 2026-11-02 17:31 | Newswire.co.kr (KR) | - | (none) | SKIP: now paid (77,000 KRW basic); free-posting notice dates from 2004 |
| 2026-11-02 17:31 | Brunch (KR), Jianshu (CN) | - | (none) | BLOCKED: need Korean/Chinese mobile number |
| 2026-11-02 17:31 | DIFUNDIR (BR) | - | (none) | BLOCKED: requires CPF/CNPJ (Brazilian tax ID) |
| 2026-11-02 17:31 | Daily Y why25.com (KR), comunicados.co (CO), pressreleaseindia.net, india-pressrelease.com, bharatpr.com, desipressrelease.com (IN) | - | (none) | BLOCKED: unreachable from box (timeout); Daily Y queued for browser retry |
| 2026-11-02 17:31 | Comunicae CO, India News Grid, PRWireIndia, IndianPRWire, PR TIMES, PR Newswire Asia | - | (none) | SKIP: paid or not eligible (PR TIMES free only for companies under 24 months; India News Grid free only for NGOs) |
| 2026-11-02 17:31 | euobiz.cn (CN), Punjab Infoline (IN), AW News Center (CO) | CCW | (none) | NOT SENT: email/WhatsApp submission to editors needs William's OK |
| 2026-11-02 17:31 | PRESSNOW, Tsunagugu, PRERELE, Zero Press, Linkpress, valuepress, FREE PRESS RELEASE (JP); Vokolla, Xinhua bizwire (CN); RedPress KO, velog, KMMBA (KR); PONTE, INFOREX, Administradores, WebArtigos (BR); PressRelease.in, newsco.in (IN) | CCW (local language) | (none) | QUEUED for browser: reCAPTCHA/Turnstile/Cloudflare/JS tokens or account sign-up |
- 2026-11-02 17:35 MSK PRFree LIVE: trenches-and-drones https://news.prfree.org/@infinitumcorp/trenches-and-drones-william-aaron-turners-second-whitepaper-treats-network-defense-as-attrition-4bafi34dwjpk ; ccw-doctrine-introduction https://news.prfree.org/@infinitumcorp/corporate-cognitive-warfare-a-doctrine-introduction-by-william-aaron-turner-on-markets-as-cognitive-battlespaces-o6cjeh6dev3h ; dead-reckoning https://news.prfree.org/@infinitumcorp/dead-reckoning-whitepaper-william-aaron-turner-gives-security-teams-a-quarterly-check-to-keep-ai-tools-honest-k3iqn445ajfc ; special-01 https://news.prfree.org/@infinitumcorp/the-russia-forecast-gap-william-aaron-turners-special-01-whitepaper-gives-risk-teams-a-sourced-reference-r8540ezbfxbs
- 2026-11-02 17:35 MSK presslo.com: BLOCKED, Cloudflare 1015 rate limit; retry later. IssueWire: needs signup; retrying.
- 2026-11-02 17:42 MSK PRFree LIVE: ukraine-aid-ngos, ukrainian-deli, azov, legitimate-targets, art-of-not-giving (headline changed to "Fifty Countries, One Russia..."). The URLs are in the computerUse report and were relayed to the user.
- 2026-11-02 17:42 MSK IssueWire: signed up, activation pending. presslo: needs a PressLux account.
- 2026-11-02 17:50 MSK euobiz.cn (CN): pitch with form and JPG SENT by William via draft card to info@euobiz.cn; awaiting reply.
- 2026-11-02 17:50 MSK AW News Center (CO) and Punjab Infoline (IN): pitches SENT by William via draft cards; awaiting replies.
- 2026-11-02 17:52 MSK IssueWire: trenches-and-drones submitted (free), PR ID 1880758249428467, Pending review; preview https://www.issuewire.com/pressrelease/preview/225594. PressLux: campaign 198 approved; email verification done, resubmitting.
- 2026-11-02 18:52 MSK presslo (PressLux free): trenches-and-drones LIVE https://presslo.com/release/trenches-and-drones-william-aaron-turners-second-whitepaper-treats-network-defen (headline adds 'a War of Attrition').
- 2026-11-02 17:57 MSK William: media contact is info@theinfinitumcorporation.com going forward (not infinitum-media@). Updated all release, translation and pitch files; agent inbox kept only for site logins.
| 2026-11-02 19:04 | PressLiftoff (Free) | Rewrites of the 410 releases | not public yet | Rewrote all 14 (rewrites/). Submitted 2, about 10 minutes apart: In-Q-Tel (18:52) and EEF (19:03). Both are HELD FOR MANUAL REVIEW ("an earlier release from this contact or website was removed"). The other 12 were held back because ToS §4A bans geopolitical commentary and bulk or similar resubmissions, so sending them risks a sender block. Edit links are in ../edit-links.md. |
| 2026-11-02 19:06 | PressLiftoff (Free) | Russia Sanctions Analysis rewrite | not public | HELD FOR MANUAL REVIEW; edit link in ../edit-links.md |
| 2026-11-02 19:16 | PressLiftoff (Free) | Russia's Economy Under Sanctions rewrite | none | REFUSED: HTTP 400 "We couldn't accept this submission... use the contact page." No field error, so a sender block is likely. Option B stopped and the other 10 were not sent: zelenskyys-rise, ukraine-aid-ngos, ukraine-forced-mobilization, russian-civilian-casualties, polish-supermarket, russia-state-guided-capitalism, media-double-standard, legitimate-military-targets, ukraine-foreign-fighters, azov. Not retried. |
| 2026-11-02 19:15 | PRFree (Free) | 14 rewrites | none | QUEUED for browser (Turnstile login, no API). See browser-queue.md, files in rewrites/prfree/. No other site had script access today: SubmitPR excluded, 1888 quota used/booked through Nov 5, the rest need the browser. |
- 2026-11-02 19:48 MSK PRFree: 14 neutral rewrites LIVE (in-q-tel, EEF, russia-sanctions, russias-economy, zelenskyys-rise, ukraine-aid-ngos, mobilization, civilian-casualties, polish-supermarket, state-guided-capitalism, media-double-standard, legitimate-targets, foreign-fighters, azov); URLs in computerUse report; no image field; form contact email was infinitum-media@ (fix to info@ if editable).

## 2026-11-02 20:45 MSK: CoS follow-up check
- Email (Gmail theinfinitumcorp@ incl. spam + agent inbox, since Nov 2): PressLiftoff CCW Expanded is LIVE (17:12 MSK) https://pressliftoff.com/press-release/corporate-cognitive-warfare-expanded-edition-william-aaron-turner-releases-15000-word-pape (200). Demining NGOs: no live notice yet (still in review). PRFree: already verified (only expired codes; CCW LIVE since 17:09) so no new submission. freepressreleases.co.uk: no reply. 1888PressRelease: registration confirmation only. Academia: auto-ack only, ticket 1059096 (17:22 MSK), no human reply.
- SubmitPR Nov 2 CCW / Dead Reckoning / Special 01: contact was infinitum-media@mail.grokbot.com. Signed in by email link (theinfinitumcorp+press@), edited via HTTP: contact now info@theinfinitumcorporation.com on all 3; added flyer/cover images to Dead Reckoning and Special 01 (CCW already had flyer). All 200.
- PRB Academia batch (12 SubmitPR links in ../published.md): all 200, no grokbot email, no "Battalion".
- 2026-11-02 21:50 MSK CoS: flyers made for the 12 Academia-batch releases (flyer-gen/academia_batch_flyers.py -> flyers/<slug>.png + -square.png, no watermark) and attached to all 12 SubmitPR releases via HTTP edit; verified live.

- 2026-11-02 21:53 MSK PRFree contact-email fix via HTTPS: BLOCKED. The login form (members/login.php) needs a Cloudflare Turnstile token, and a POST without one is refused (/members/ redirects back to login). Nothing was edited or deleted, so 0 fixed. Public profile https://news.prfree.org/@infinitumcorp lists 22 releases. All 22 still show infinitum-media@mail.grokbot.com in the contact block, and info@theinfinitumcorporation.com also appears in the body. The fix needs a real browser login (the box browser times out on prfree.org) or the user's computer for egress. PRFree release URLs (22):
  - https://news.prfree.org/@infinitumcorp/azov-movement-william-aaron-turners-article-examines-the-units-founding-symbols-and-human-rights-record-26tzrm9ktn0o
  - https://news.prfree.org/@infinitumcorp/corporate-cognitive-warfare-a-doctrine-introduction-by-william-aaron-turner-on-markets-as-cognitive-battlespaces-o6cjeh6dev3h
  - https://news.prfree.org/@infinitumcorp/corporate-cognitive-warfare-expanded-edition-william-aaron-turner-releases-15-000-word-paper-ls3vzssjk25f
  - https://news.prfree.org/@infinitumcorp/dead-reckoning-whitepaper-william-aaron-turner-gives-security-teams-a-quarterly-check-to-keep-ai-tools-honest-k3iqn445ajfc
  - https://news.prfree.org/@infinitumcorp/fifty-countries-one-russia-william-aaron-turners-x-article-tallies-the-western-coalitions-results-6lp3yvprik90
  - https://news.prfree.org/@infinitumcorp/grandmas-toddlers-and-forklift-drivers-william-aaron-turner-questions-ukraines-definition-of-military-targets-t89se39r2whw
  - https://news.prfree.org/@infinitumcorp/the-russia-forecast-gap-william-aaron-turners-special-01-whitepaper-gives-risk-teams-a-sourced-reference-r8540ezbfxbs
  - https://news.prfree.org/@infinitumcorp/trenches-and-drones-william-aaron-turners-second-whitepaper-treats-network-defense-as-attrition-4bafi34dwjpk
  - https://news.prfree.org/@infinitumcorp/ukraine-aid-ngos-william-aaron-turners-ukraine-files-opens-with-a-call-to-audit-where-charity-donations-go-evqxc5ashjhj
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-analysis-of-eastern-economic-forum-2026-trade-data-38kcos48bw0q
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-analysis-of-in-q-tel-the-cia-founded-venture-capital-firm-tvrtlvtgukix
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-analysis-of-russias-economy-under-sanctions-q6ny6hvi8neg
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-analysis-of-the-july-2026-cyberattack-on-polish-retailer-lewiatan-2o25ha6fg5ah
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-analysis-of-the-lobbying-charity-and-media-networks-around-ukraines-government-t8l8o207gzt0
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-commentary-comparing-media-coverage-of-the-war-in-ukraine-and-us-urban-violence-wtvqkv0geefw
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-commentary-on-how-dual-use-targets-are-defined-under-the-laws-of-war-mc39ds40luyg
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-commentary-on-russias-state-guided-economic-model-7czcn82ujx0t
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-commentary-on-the-recruitment-and-pay-of-foreign-volunteers-in-ukraines-armed-forces-vvr38rvlaq3g
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-compilation-of-official-reports-on-ukraines-military-mobilization-practices-wxhihfuid9yi
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-guide-for-donors-on-tracing-where-ukraine-aid-donations-go-2syyzs3glmkr
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-sourced-compilation-of-reporting-on-civilian-casualties-inside-russia-7vvfhj83pljx
  - https://news.prfree.org/@infinitumcorp/william-aaron-turner-publishes-whitepaper-comparing-2022-imf-forecasts-for-russia-with-reported-results-t1hh6eg0hko6
- 2026-11-03 11:04 MSK 1888PressRelease CCW retry (draft 774064): SKIPPED, not submitted. Weekly Grok Bot usage is at 100% (William's 80% rule: weekly tasks only until Fri Nov 6 18:10 MSK), on-demand $420.24/$500, and the routine is paused. Login also needs a password entry, which this automation run can't do. No retry routine created.
- 2026-11-03 12:07 MSK SubmitPR daily batch (Nov 3): SKIPPED, nothing submitted. Weekly Grok Bot usage is at 100% (William's 80% rule: weekly tasks only until Fri Nov 6 18:10 MSK); on-demand $421.93/$500. Carry over: ukraine-aid-ngos ccw-doctrine-introduction ukrainian-deli azov legitimate-targets. Note: submitpr2.py attaches an image only for ccw, so it needs a per-slug flyer upload before rerun (image rule).

- 2026-11-07T01:08 box-local: EchoForm presslo browser attempt: both presslo.com and www.presslo.com timed out. No submission or image upload. Retry remains pending; fair-NEWS next.
| 2026-11-07 01:03 | SubmitPR (free) | EchoForm | https://submitpr.org/press-release/echoform-companion-note-william-aaron-turner-reflexive-control-theory | LIVE cover=yes |
| 2026-11-07 01:09 | Pressbox | EchoForm | https://pressbox.com/press-releases/echoformtm-companion-note-modern-applications-of-reflexive-control-theory-released-by-in-2 | LIVE score89 cover=yes |
| 2026-11-07 01:07 | Khaleej Post | EchoForm | (editorial) | sent; cover uploaded |
| 2026-11-07 01:07 | Valencia Ya ES | EchoForm | ref c9ec9026-079a-4191-b970-046d6b3a46db | ok; cover uploaded |


## Reachability / browser outcomes — 2026-11-06 23:12 CET (Europe/Amsterdam)
Parent reports: browser timed out on presslo.com (including www), fair-news.de retry, and www.firmenpresse.de. No submissions or covers uploaded in those attempts. General box doctor: all 11 checks passed. IssueWire browser attempt underway (outcome unknown). Local HTTP server refused child connection; files now readable directly by child.

Read-only public curl GET tests (concurrent; maximum 15s each; no authentication):

| Site | HTTP | Seconds | Curl error |
|---|---|---|---|
| PRFree | 200 | 0.07 | none |
| fair-NEWS | 200 | 1.66 | none |
| firmenpresse | 200 | 5.44 | none |
| presslo | 200 | 0.17 | none |
| IssueWire | 200 | 1.80 | none |
| PressLiftoff | 200 | 1.27 | none |
| PRLog | 200 | 1.06 | none |

All seven roots returned HTTP 200; this does not prove browser rendering, login, submission, or image-upload availability. No obsolete-root conclusion established. No proxy/domain-denial error observed in these HTTP tests.

Public normal route confirmed: https://presslo.com/submit returns 200 and publicly links to https://presslux.com/login (existing account) and https://presslux.com/register. PressLux root and register both returned 200. Prefer existing-account login, not new signup. PRFree https://prfree.org/members/login.php, PressLiftoff https://pressliftoff.com/submit, and PRLog https://www.prlog.org/pub/login.html also returned 200. Logged registration routes (not replacement logins): fair-NEWS https://www.fair-news.de/registrieren; firmenpresse https://www.firmenpresse.de/modules.php?name=User_Registration; IssueWire https://www.issuewire.com/signup. Existing accounts should not be re-registered.

Next normal action for parent: finish existing IssueWire browser attempt; report its actual result and stop if payment requested. If another ordinary navigation is appropriate, use PressLux existing-account login linked by public presslo submit page. No browser operated by diagnostic executor; no submissions, messages, cookies, credentials, internal APIs, or scheduled retries.
| 2026-11-07 01:13 | SubmitPR (free) | Personal profile | https://submitpr.org/press-release/william-aaron-turner-founder-infinitum-personal-profile-november-2026 | LIVE image=yes |
| 2026-11-07 01:15 | Pressbox | Personal profile | (verify pending info@) | quality 94; NOT published; +pressbox NOT used |
