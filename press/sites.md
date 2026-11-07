# Free press-release sites reachable from the box (tested 2026-10-26, Europe/Moscow)

Release: /workspace/press/infinitum-release-1.md (.docx). Nothing was submitted. Homepage tests: curl -m 12 with a Chrome UA, following redirects.

## Recommended submission order (7 reachable)

| # | Site | Homepage | Exact submission URL | Account? | Phone? | Ads / paid trap | Email verif? | Captcha | Notes |
|---|------|----------|----------------------|----------|--------|-----------------|--------------|---------|-------|
| 1 | PressLiftoff | 200 | https://pressliftoff.com/submit | No (name and contact email required) | Optional | No ads. Optional $9 "Boost". Pick "Free" in the publish-choice radio. | Not needed. Public and edit links are emailed. | None in form HTML | Instant publish after preview, live links, edit later. Form wants separate dateline city/state/country, lead, body (about 100+ words), quote, boilerplate. Newest and least established. |
| 2 | SubmitPR.org | 200 | https://submitpr.org/submit | No ("No Registration") | Optional | Free tier. Links are inactive unless you add and verify a backlink to submitpr.org or pay $19.95+ in KIN crypto, so skip the upgrade. | No | None (CSRF token only) | Instant publish, Google News RSS, IndexNow. Must tick agree_terms. Fields: title, summary, body, category, company name, website, phone, address, author email. |
| 3 | PRFree.org | 200 | https://prfree.org/members/register.php (sign-up), then "Submit Release" | Yes (username, password, email) | No | Free plan is "subject to quality check". Paid $29/$49 removes ads and adds do-follow links. | Likely (standard sign-up). Untested. | Cloudflare Turnstile on sign-up | Free tier exists. Check the inbox for the confirm link. |
| 4 | 1888PressRelease | 200 | https://www.1888pressrelease.com/register.php (redirects to register_new.php) | Yes (name, username, password, email) | Yes ("Contact Number" field, all fields required) | Ad-supported. Free plan $0. Cannot edit after submit. May be removed after 12 months. Many upsells ($15 to $300). | Likely. Untested. | Google reCAPTCHA v3 (invisible) | Manual review. Use (202) 729-9509 or the company line for the phone. |
| 5 | Express Press Release | 200 | https://express-press-release.net/submit-press-release.php (rules: https://express-press-release.net/free/) | No signup | Form has a phone field | Free queue takes days to weeks. Edits or removals cost $29. No support. Anchor-text links make rejection more likely. Paid $29/$99/$299 for priority. | No | None in HTML | Editor-reviewed, with no guarantee of acceptance. Keep links plain. |
| 6 | presslo (PressLux) | 200 | https://presslo.com/submit, which sends you to a free PressLux account; pick the "Free" distribution step | Yes (free account) | Unknown | Publish and index only. Upsells for 500+ outlets, AP and AI engines. | Likely ("verified author"). | Unknown | Works through PressLux's AI release-drafting flow. Check that it accepts pasted text. |
| 7 | openPR.com | 200 for home; /news/submit.html returns 403 to curl, so use a browser | https://www.openpr.com/news/submit.html | Yes. Free-mail addresses are rejected (a custom domain such as mail.grokbot.com is fine). | Not stated | Free is 1 release per 30 days. Editor review on weekdays. Edit or delete costs 10 EUR. | Not stated | Unknown | Infinitum already has a release on openPR (https://www.openpr.com/news/4592982/...), so this one counts against the 30-day limit and may be flagged as a duplicate. Submit last, or only if the new release is clearly different. |

## Not usable, or not worth it

| Site | Result |
|------|--------|
| PRLog | Homepage times out from the box (000). Unreachable. |
| Free-Press-Release.com, PressReleaseJet, PR9, PRBuzz, OnlinePRNews | Timeout or connection failure (000). |
| Free-Press-Release-Center.info, openPR.de | 403 to curl. |
| RedPress | Reachable, but already attempted. The submission is unconfirmed, with the form timing out. |
| EIN Presswire | Reachable. The "free" release is only by contacting them (/submit-free-press-release); self-serve sign-up (/register?plan=presswire-basic) is paid. Skip unless William wants to email them. |
| IssueWire | Reachable (/signup). It claims "first PR is free", but the page is built around a PayPal checkout, GST, a required 10-digit phone, reCAPTCHA and paid tiers. High fee-trap risk. Skip. |
| PR.com | Reachable. "Create Free Account" exists, but release distribution is paid only. /press-release/submit returns 404. |
| ClickPress | Homepage only links to newsbanq.com, so the original site is effectively dead. |
| PRUnderground ($74.99), NewswireJet, PressReleasePower, 24-7 Press Release, PressAdvantage, ABNewswire, PRLeap, Newswire.com, Send2Press, PitchEngine, Accesswire | Reachable but paid only. |
| FreePressRelease.org, PressReleaseFinder, PR-GB, BigNewsNetwork | Reachable, but no usable free self-serve submit page found. |

## Notes for submitting
- Use the contact email infinitum-media@mail.grokbot.com, with William's Gmail CC'd per his instruction. Phone for forms that need one: 202-729-9509 (given by William for public contact).
- Headquarters wording: Washington, DC (Moscow only as an operating location). Include the Telegram link https://t.me/infinitumcorporation.
- Sites 1, 2 and 5 need no account and no captcha, so they are the cheapest to run fully. Sites 3, 4 and 6 need sign-up and email verification, so check the infinitum-media inbox. Site 3's Turnstile and site 4's reCAPTCHA may block automation, so use the browser desktop.
- Do not buy any upgrade (Boost, KIN, "Starter", prepay credits).

## Update 2026-10-31
- SubmitPR works by plain HTTPS form post from the box (selected_plan=free, CSRF token from /submit); instant publish; account auto-created for theinfinitumcorp+press@gmail.com.
- Express Press Release: /submit-press-release.php has no submission form any more (archive menu ends 2025); treat as dead unless a form reappears.
