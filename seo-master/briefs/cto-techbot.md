# Brief for CTO TechBot (website, survey site, DNS)
From: Infinitum Marketing (CMO), 2026-10-26. Order: William, "SEO plan for everything we own!!! Execute."

## Rules that apply to everything below
- Company facts: Infinitum Corporation, HQ 1629 K Street NW, Suite 300, Washington, DC 20006 (Moscow is an operating location only, never the HQ). Open 24 hours. Phone 202-729-9509 (schema +1-202-729-9509). Email info@theinfinitumcorporation.com. Website https://www.theinfinitumcorporation.com. Telegram https://t.me/infinitumcorporation must appear in copy. Do not use the old phones (202) 681-0120, (202) 980-9300 or (614) 216-2724.
- Use the ready-to-paste copy in `/workspace/seo-master/ready/` (character counts already checked). Full plan: `/workspace/seo-master/master-plan.md`.
- Never post, publish, or announce a NEW public offer without William's direct approval. Already-approved streams (pentest flyer series, Discord webhook) continue as scheduled.
- Buffer: shareNow only, no duplicates, minimal calls. No press releases to Telegram. Stay dormant until your routine fires; do not spend tokens polling.
- No invented numbers: do not state search volumes, rankings or follower goals you did not measure.
- Edits to a profile in William's name (bio, headline, description) are drafts until William says yes; mark each as "approval needed" in your report to Infinitum Marketing (CMO).
- Report back to CMO in one short message: what was done, URL, what is blocked. Silence is fine if nothing changed.

## Your tasks (website https://www.theinfinitumcorporation.com is on the Ueni builder; edits need the builder login, William's approval already exists for these edits)
Findings from live fetch 2026-10-26: title on every page "... | IT Consultant in Washington, D.C."; footer phone (202) 681-0120 (tel: link too); no Telegram/Discord/@infinitumceo links (links to x.com/infinitumusa and Instagram); JSON-LD LocalBusiness telephone +12026810120 and sameAs includes a Google place-ID string that is not a URL; no "open 24 hours" text; sitemap lastmod 2025-01-04; both `www` and non-www return 200 (canonical = non-www); GA4 `G-D4R817TGX6` and GTM `GTM-TG56DMZ` are already in the page source; homepage HTML is about 1.9 MB.
1. Get the builder login from William (via CMO). If you cannot, stop and report.
2. Apply `ready/website-meta-copy.md` (titles <= 60, descriptions <= 160) page by page.
3. Replace phone everywhere with 202-729-9509 (visible text, `tel:` links, JSON-LD). Add visible footer line: "1629 K Street NW, Suite 300, Washington, DC 20006 | 202-729-9509 | Open 24 hours | info@theinfinitumcorporation.com" plus Telegram, X (@infinitumceo), Discord links; replace the infinitumusa link.
4. JSON-LD: paste `ready/website-jsonld.html` into the builder's custom head box. If the builder blocks scripts, inject the same JSON-LD through Google Tag Manager (GTM-TG56DMZ is already installed; publish only after William confirms it is his container). Validate with the free Rich Results Test.
5. Primary domain: set one primary host in the builder (William decides www vs non-www). Make canonical, sitemap and JSON-LD agree with it, and 301 the other host if the builder allows. Tell Blog Bot the final host so blog links match.
6. Add a `/community` (or `/telegram`) page: one paragraph each for Telegram, Discord, X, Whitepapers blog, Whop, with plain links. Add alt text to hero images; use a 1200x630 og:image (current is 915x610).
7. Verify the domain in Google Search Console and Bing Webmaster Tools (William does the login; you add the DNS TXT or HTML-tag token) and submit sitemap.xml. Confirm GA4 `G-D4R817TGX6` belongs to William's property and tell CMO.
8. Test hosting `/llms.txt` (`ready/llms.txt`) at the site root; the builder returned 404 for it today. If not possible, skip.
9. Survey site https://infinitum-survey-flyers.vercel.app: add `<meta name="robots" content="noindex">` (the page is a 131-byte link to the Jotform survey), keep working links. Do not change the survey itself.
10. Check SPF/DKIM/DMARC for the domain and report to CMO/EmailBot.
11. Site wording: leave "advanced surveillance" and "commercial construction" pages untouched until William reviews wording.
Done when: re-fetch of the home page shows the new title, phone, JSON-LD and footer links; report the live URLs.
