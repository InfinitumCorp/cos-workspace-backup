# Indexing actions, 31 Oct 2026

## Sitemaps
- Google sitemap ping (google.com/ping?sitemap=) was retired in 2023 and Bing's in 2022: not used. Submit instead in Search Console > Sitemaps and Bing Webmaster > Sitemaps after verification:
  - https://infinitumwhitepapers.blogspot.com/sitemap.xml (HTTP 200 checked)  + https://infinitumwhitepapers.blogspot.com/sitemap-pages.xml
  - https://russiaafricabythenumbers.blogspot.com/sitemap.xml (HTTP 200 checked)  + https://russiaafricabythenumbers.blogspot.com/sitemap-pages.xml
  - https://russiaafricareport.blogspot.com/sitemap.xml (HTTP 200 checked)  + https://russiaafricareport.blogspot.com/sitemap-pages.xml
  - https://ukrainianfiles.blogspot.com/sitemap.xml (HTTP 200 checked)  + https://ukrainianfiles.blogspot.com/sitemap-pages.xml
- Bing Webmaster can import GSC properties once GSC is verified (fastest path).

## IndexNow (Bing/Yandex/Seznam/Naver)
- NOT submitted. IndexNow requires a key file served from the same host. No host we control has one: Blogger (*.blogspot.com) cannot serve an arbitrary .txt key file; Ueni main site and Beacons (williamaaronturner.com) likewise; zenodo.org / x.com are not ours.
- Enable later: once the Vercel redesign is live on www.theinfinitumcorporation.com, add public/<key>.txt and POST https://api.indexnow.org/indexnow {host,key,urlList}. Blogger URLs: rely on Bing Webmaster URL Submission (10k/day after verification).
- URL list to submit when possible: live-urls.txt (blog posts only for owned hosts).

## Wayback Machine
- NOT saved: web.archive.org refuses TLS from the box (handshake reset; archive.org itself is reachable). Do via browser (computerUse): https://web.archive.org/save, one URL at a time from live-urls.txt, "Save outlinks" off. pubs.csv wayback_url = predicted https://web.archive.org/web/2026/<url> (resolves to nearest snapshot once saved).

## Outlet backlinks to index
- No outlet has published any piece yet (as of 31 Oct). When one does: add its URL to pubs.csv (status published), save to Wayback, add it to the source post's "Also available" list, add `isIdenticalTo`/`isVersionOf` on Zenodo, and request indexing of the source post (GSC) so Google sees the reciprocal link. Never link exclusives (BAR #39, Geopolitical Monitor #41, CGTN #56, Preprints #67, NEO #9) or journal manuscripts until published by the outlet.
