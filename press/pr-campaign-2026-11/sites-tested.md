# Free PR sites: box test results (2026-11-02 ~17:00 MSK, curl from box)
For CMO (browser/account steps) and plan.md. Translations: ./translations/. Never pay/upgrade; free tier only.
Legend: Acct = account needed; Cap = captcha/anti-bot. "Box-HTTPS OK" = free, no account, no captcha.

| Region | Site | Reachable | Free submission URL | Acct | Cap | Pay | Lang | Result |
|---|---|---|---|---|---|---|---|---|
| Global | PRLog | YES (now 200; was unreachable before) | https://www.prlog.org/submit-free-press-release.html -> create free account, login https://www.prlog.org/pub/login.html | Yes | none seen on login | Free tier (unlimited) | EN | Browser: sign up + submit EN releases |
| Global | openPR (.com) | 403 to curl | https://www.openpr.com/news/submit.html | Yes | browser-gated | 1 free / 30 days | EN | Browser (already in log.md) |
| Global | IssueWire | YES | https://www.issuewire.com/signup | Yes | reCAPTCHA | First free release via signup tier; rest paid | EN | Browser; pick free tier only, no card |
| Global | PR.com | YES | https://www.pr.com/press-release-distribution | Yes | ? | Pricing page; free option unclear | EN | Browser check; skip if card required (log reason) |
| Global | 1888PressRelease | - | (handled separately) | - | - | - | EN | Not touched |
| Global | PRFree | - | (handled separately) | - | - | - | EN | Not touched |
| Global | NewswireToday | YES (TLS chain warning) | https://www.newswiretoday.com/login.php?login=editor (register as editor) | Yes | ? | Free basic | EN | Browser |
| German | openPR.de | 403 to curl | https://www.openpr.de/news/submit.html | Yes | browser-gated | Free | DE | Browser, use ccw-de.md |
| German | firmenpresse | YES | https://www.firmenpresse.de/modules.php?name=User_Registration (fields: uname, email, pass, vpass, realname, birth date, url, readrules) | Yes | none seen | Free | DE | Browser/sign-up, use ccw-de.md |
| German | fair-NEWS | YES | https://www.fair-news.de/registrieren (WPForms: name, email, phone, address…) | Yes | reCAPTCHA/hCaptcha/Turnstile | Free tier | DE | Browser, ccw-de.md |
| French | Centre Europe Presse | YES | https://www.centre-europe.com/publier-un-communique-de-presse/ (posts to /communiques/soumettre.php; fields nom, email, entreprise, categorie, titre <=100, contenu >=300, photo required, offre=gratuit, lien empty on free) | No | Cloudflare Turnstile (server rejected curl: "vérification anti-robot a échoué") | Free (0 €) | FR | Browser, ccw-fr.md, 1 attempt made 17:08, rejected by anti-bot |
| French | Actualités Françaises | YES | https://actualitesfrancaises.fr/publier-un-communique/ (name, email, title, tags, category, content, image, arithmetic antispam question) | No | Antispam question | Free, instant | FR | Browser, ccw-fr.md |
| UK | freepressreleases.co.uk | YES | submit@freepressreleases.co.uk (email only; no form, no account) | No | No | Free | EN | Needs an email send (draft in report) |
| Ukrainian | Портал Експеримент | YES | https://md-eksperiment.org/add-news (login form + reCAPTCHA) | Yes | reCAPTCHA | Free (active link paid) | UK | Browser, ccw-uk.md |
| Ukrainian | info-ua.com | YES (via search) | https://www.info-ua.com/press-relizy/add.html -> email releases to the address on that page | No | No | Free | UK/RU | Needs an email send |
| Ukrainian | krb.in.ua (no-registration form) | HTTP 500 | http://krb.in.ua/ | - | - | Free | RU/UK | Blocked: site down (500) |
| Asia | e27 | YES | https://e27.co/contribute/ (contributor account) | Yes | ? | Free (editorial) | EN | Browser; article-style, not raw PR |
| Asia | WeRIndia | YES | no submit form found (aggregator); only https://werindia.com/contact-us | ? | - | ? | EN | Blocked: no free submission path found |
| S. America | INFOREX (Brazil) | YES (JS app) | https://inforex.app.br/ -> "Cadastrar como Assessoria" | Yes | ? | Plan R$0 | PT | Browser, ccw-pt.md |
| S. America / ES | RedPress ES (LatAm coverage) | YES | https://redpress.net/free-press-release-distribution (name, email, phone, company, website, headline, industry, target_market, summary, release_date, press_file PDF/DOCX, boilerplate, spokesperson) | No | Turnstile + captcha_answer | Free (100 journalists) | ES | Browser, ccw-es.md as DOCX/PDF. Note prior 10-26 RedPress submit unconfirmed |
| African | MyPR.co.za | YES | https://mypr.co.za/register/ then https://mypr.co.za/submit/free/ (international: https://mypr.co.za/international/submit) | Yes | reCAPTCHA | Free | EN | Browser |
| African | AfriWallStreet | HTTP 500 | http://www.afriwallstreet.com/ | - | - | - | EN | Blocked: site down (500) |
| African | TechCabal | YES | no PR form; editorial pitch only (contact page) | - | - | - | EN | Blocked for PR: editorial pitch by email only |
| Russian | Atrex.ru | NO (TLS EOF / HTTP 500) | https://atrex.ru/ | - | - | - | RU | Blocked: unreachable from box |
| Russian | P-Reliz.ru | YES | https://p-reliz.ru/add/ (API /api/relizes/; fields title, text, about, categories, user_company_name, user_company_inn*, user_name, user_email, terms) | No (or login) | none | Free, moderated | RU | Blocked: requires Russian INN (tax ID) and corporate-domain email; alt = email to info@p-reliz.ru from corporate domain |
| Russian | Press-release.ru | YES | https://www.press-release.ru/add/?register=yes | Yes | ? | Free basic | RU | Browser, ccw-ru.md / dead-reckoning-ru.md |
| Russian | Re-port.ru | YES | https://re-port.ru/register/ (title, email, username, password, policy, image captcha) | Yes | Image captcha | Free | RU | Browser |
| Russian | VC.ru | YES | https://vc.ru/ (account; post as article/blog) | Yes | ? | Free | RU | Browser; article format |
| Russian | Habr | YES | https://habr.com/ru/ (account; corporate blogs are paid, personal posts moderated) | Yes | ? | Free personal post | RU | Browser; article format, not press release |

Box-HTTPS-submittable (free, no account, no captcha): none found this round.
