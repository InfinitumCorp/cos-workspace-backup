# Bing Webmaster Tools plan (Bing index also feeds Yahoo and DuckDuckGo)
1. Go to https://www.bing.com/webmasters → Sign in → Microsoft account, or use "Sign in with Google" with the account that owns the 4 GSC properties.
2. On "Add your site", choose the left panel **Import your sites from GSC** → **Import** → **Continue** → allow Google access → tick ukrainianfiles, russiaafricareport, russiaafricabythenumbers, infinitumwhitepapers (.blogspot.com) → **Import**. These are verified automatically and their sitemaps are imported.
3. For each site, use the site picker (top left) → **Sitemaps** → **Submit sitemap** → `https://<blog>.blogspot.com/sitemap.xml` → **Submit**. Then also submit `/atom.xml?redirect=false&start-index=1&max-results=500`.
4. **URL Submission** (left menu) → **Submit URLs** → paste the URLs for that blog from /workspace/seo-master/publications-2026-10-31/live-urls.txt (27 URLs total; the daily quota is shown on the page) → **Submit**. Add the CCW post https://infinitumwhitepapers.blogspot.com/2026/10/corporate-cognitive-warfare-expanded.html.
5. **URL Inspection** → check one post per blog → **Request indexing** if "not indexed".
6. **Settings → Crawl control**: leave default. **SEO → Site scan**: start a scan per blog and fix missing-alt or meta warnings using images.csv.
7. Images: Bing reads alt, title, figcaption and ImageObject JSON-LD. Apply apply-steps.md first, then resubmit the URLs.
8. DuckDuckGo and Yahoo have no separate submission. Check after 1–2 weeks with `site:<blog>.blogspot.com` on each.
