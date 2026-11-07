

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
