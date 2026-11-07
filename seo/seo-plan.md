# SEO plan: all Infinitum blogs (prepared 2026-10-26, Moscow time)

Blogs: (1) The Ukraine Files: https://ukrainianfiles.blogspot.com (blog id 7176625378576436294; 9 live posts, 4 pages), (2) Infinitum Corporation Whitepapers: https://infinitumwhitepapers.blogspot.com (blog id 1821202937701950238; 2 live posts). /workspace/blog-redesign/ holds only app.js and style.css (a front-end redesign, no posts, no live URL).
Status: NOTHING has been changed live. Everything below is prepared. See "Blockers".

Files: one per post/page in /workspace/seo/posts/*.md (18 files), /workspace/seo/seo-manifest.json, site-wide JSON-LD in /workspace/seo/snippets/, live HTML snapshots in /workspace/seo/live/, generator /workspace/seo/gen.py.
Keyword data rule: no search-volume numbers exist in this plan. Keywords come from the post topics plus SERP observations from WebSearch on 2026-10-26.

## 1. Audit: what is already good (live)
- Every page has a canonical, a meta description, Open Graph tags and Blogger's default BlogPosting JSON-LD.
- Ukraine Files posts also carry a Person + Organization graph (Person sameAs X, GitHub, site).
- Default robots.txt is correct (Disallow /search only) and points at sitemap.xml. sitemap.xml and sitemap-pages.xml both load.
- Title tags are the post titles, mostly under 60 characters. Descriptions are 130-150 characters.
- Internal linking in the series is solid (every post links Hub + About, 4-6 sibling links, Previous/Next).

## 2. Audit: gaps found (ranked by impact)
1. Post 10 (defense advisory) returns 404 live on both blogs, and the press plan (Oct 28) points to it. Needs republishing before any press submission.
2. Companion post "Russian Civilian Casualties..." has an auto permalink (blog-post_26.html), no labels, is missing from the hub page and from Previous/Next navigation, and post 7 does not link back to it.
3. Site-wide structured data is incomplete: Organization lacks the DC address, phone 202-729-9509, 24-hour hours, Telegram and Discord in sameAs; the Whitepapers blog has no Organization at all and Blogger's default publisher says "Blogger". Fix: paste snippets/*-sitewide-jsonld.html into Theme > Edit HTML, in the head (once per blog), then paste each post's BlogPosting+BreadcrumbList from posts/*.md at the end of the post body (HTML view).
4. Missing/empty image alt text on posts 1, 2, 3 (alt is blank); the three whitepaper/other alts are fine but not keyworded.
5. Pages have no og:image (no image in body) and the Contact page has no address or phone.
6. Whitepaper posts have zero internal links (no link to the other paper, to the company site or to the Ukraine Files), hero images are hosted on raw.githubusercontent.com, and the blog title is the page H1 rather than the post title (template).
7. Brand split: the blog is named "Ukrainian Files" but every post, the About page and the X Articles say "The Ukraine Files".
8. Teaser post 1 (309 words) is thin content.
9. Whitepaper 02 title is 80 characters and truncates in results.
10. Fact flags for William (body untouched): EEF post says 80 countries/5,000+ delegates while organizers' final results say 78 countries, 9,300+ participants, 328 agreements, RUB 6.815 trillion; Russia-economy post cites an EC 1.3% growth upgrade while later sources show Russia's own forecast cut to 0.4% (Reuters, May 2026), World Bank 0.8%, IMF 0.9% (October 2026). Stale numbers hurt trust and rich-result eligibility.

## 3. Keyword map (primary per post; full lists in posts/*.md)
| Page | Primary | Notes from SERP |
|---|---|---|
| Home (UF) | The Ukraine Files | brand term |
| Post 1 NGO audit | audit Ukraine aid NGO | consumer charity guides dominate; angle = funders+filings audit |
| Post 2 Russia economy | Russia economy under sanctions | Reuters/World Bank/IMF lead; freshness-driven |
| Post 3 EEF | Eastern Economic Forum 2026 | organizer, TASS, Kommersant, JETRO lead |
| Post 4 In-Q-Tel | In-Q-Tel (target "CIA venture capital arm") | iqt.org, Fortune lead; head term owned by iqt.org |
| Post 5 Organ allegations | Ukraine organ trade allegations | fact-checks (OSCE, VOA, EFE, VoxUkraine) dominate; keep "allegations + denials" framing |
| Post 6 Zelenskyy | Zelensky rise to power | spelling split Zelensky/Zelenskyy |
| Post 7 Mobilization | Ukraine forced mobilization | Ombudsman, Kyiv Independent lead |
| Post 8 Demining | demining NGOs intelligence | halotrust.org, Lao/Russian MFA sources |
| Post 9 Civilian casualties | Russian civilian casualties Ukrainian strikes | BBC leads; event long-tails are open |
| Post 10 Defense advisory | defense technology advisory Washington DC | local DC competitors: Wolverine Group, CADRE, DC Strategic Group |
| Whitepaper 01 | AI for security operations | IBM 2026 Cost of a Data Breach, CISA/NIST PNT pages |
| Special 01 | Russia state-influenced capitalism | PIIE, Carnegie, academic; plain-language gap |

## 4. Blogger settings checklist (needs a signed-in Blogger session as theinfinitumcorp@gmail.com, per blog)
1. Settings > Title: rename "Ukrainian Files" to "The Ukraine Files" (UF blog only).
2. Settings > Description: UF = "Sourced analysis of Ukraine aid NGOs, In-Q-Tel, sanctions and mobilization by William Aaron Turner, President of Infinitum Corporation." WP = "Free security and technology whitepapers from Infinitum Corporation, Washington, DC. Open 24 hours."
3. Settings > Meta tags: enable search description; set the blog description above (150 chars max).
4. Settings > Crawlers and indexing: enable custom robots.txt (snippets/custom-robots.txt); custom robots header tags: Home = all, Archive and Search = noindex, Posts and pages = all (do not noindex posts).
5. Settings > Errors and redirects: add a permanent redirect only if you replace blog-post_26.html with a keyworded permalink.
6. Theme > Edit HTML: paste the matching snippets/*-sitewide-jsonld.html before </head>; make the post title the H1 on post pages (UF template already looks custom; whitepapers template uses the blog title as H1).
7. Per post (Post settings): set Labels, Search description, and for post 9 add labels; paste the post's JSON-LD at the bottom of HTML view; set image alt text (the image Properties dialog or alt attribute in HTML view). Do not touch the body text.
8. Posts per page: show 7 with a jump break so the home page does not duplicate full post bodies.
9. Search Console (needs Google login): add both blogspot properties (URL-prefix), submit sitemap.xml and sitemap-pages.xml, request indexing for new/updated URLs. Bing Webmaster Tools: import from Search Console. IndexNow is not possible on blogspot (no root file hosting).

## 5. Internal linking plan
- Hub page: add post 9 (civilian casualties) to the list and the "Casualties & Human Cost" browse group.
- Post 7 <-> post 9: reciprocal links.
- Post 4 (In-Q-Tel) <-> post 6 (Zelenskyy) <-> post 1 (NGO audit): the intelligence/NGO cluster.
- Post 2 <-> post 3: the sanctions/Asia pivot cluster.
- Both whitepapers: link each other, the company site (anchor "Infinitum Corporation cybersecurity consulting in Washington, DC"), and the Telegram channel in the footer block.
- Cross-blog: Whitepaper 02 (Special 01) -> Ukraine Files posts 2 and 3; Ukraine Files About page -> Whitepapers home.
- Every footer block: Telegram https://t.me/infinitumcorporation, X https://x.com/infinitumceo, Discord https://discord.gg/QVT7dWHUQa, DC HQ, open 24 hours.

## 6. Extra tricks queued (all prepared or free)
- Use question-style H2s on post 5 (already) and post 8; they feed featured snippets.
- FAQPage JSON-LD is NOT recommended: Google no longer shows FAQ rich results for most sites.
- Upload hero images to Blogger instead of GitHub raw hosting; use descriptive filenames (e.g., in-q-tel-explained-cia-venture-capital.jpg) and 1200x630 for social cards.
- Add datePublished/dateModified update notes when figures change (see fact flags).
- External signals: the press-release plan already links the whitepaper URL; add the blog URLs to the Telegram channel description and X bio (needs bot/owner access, not done).
- Google Business Profile: add the Whitepapers blog as a website link/post (blocked earlier by business.google.com timeouts).

## 7. Blockers
- No Blogger API/connector exists in this environment (checked MCP namespaces and Composio: no Blogger toolkit). The earlier publishing path was a signed-in box browser session (theinfinitumcorp@gmail.com, blogger.com), which I (executor) cannot drive: browser control must be delegated to a computer-use subagent. Nothing was applied live.
- Search Console/Bing Webmaster submission needs a signed-in Google session too.
- Post 10 needs republishing (404).
