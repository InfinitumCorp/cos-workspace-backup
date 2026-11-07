# Patches prepared 2026-10-31 (nothing pushed or deployed)
Why patches: `gh` on the box is not authenticated (`gh auth status`: not logged in), so per instructions no pushes/PRs were made and no files were pushed through connectors.
Decisions applied: 202-729-9509 is the ONLY public phone (681-0120, 980-9300, 614-216-2724/WhatsApp removed wherever edited); legal entity/HQ = Infinitum Corporation, Washington, DC (no California entity references).

## 01-infinitum-corporation-site (Next.js 16 redesign, Vercel project `infinitum-corporation`)
Source of truth is the Vercel CLI deployment (dpl_EtzZQkLZH212tfGqXceefWb2QM1j, created by theinfinitumcorp-4521). The GitHub repo InfinitumCorp/infinitum-corporation-site only holds one content file, so it cannot be built from GitHub. Project root contains app/, components/, content/.
Apply from the project root:
    python3 /path/to/patches/01-infinitum-corporation-site/apply_edits.py .
    npm run typecheck && npm test && npm run build
    vercel deploy            # preview; or `vercel --prod` (still noindex, see below)
What it does:
- New `content/entity.ts` (canonical NAP + profile list), `components/entity-jsonld.tsx` (Organization+ProfessionalService, Person, WebSite graph with @ids shared with the blogs; sameAs = Telegram, Discord, GitHub, Whop, both blogs, Academia; Person sameAs = X @infinitumceo, LinkedIn, williamaaronturner.com, author page). Replaces the old Organization JSON-LD in `app/layout.tsx`.
- Phone -> 202-729-9509 in site.ts, footer `tel:`, contact meta; sweep removes any other 681-0120 / 980-9300; script fails if any banned number, wa.me link, Palo Alto or 5470106 remains.
- Footer: "Mon–Fri 9 AM–9 PM, closed Sat–Sun" + FOLLOW column linking all owned profiles (rel="me").
- Keyword titles/descriptions: layout default, about, capabilities, contact, industries, insights, press.
- New pages: /services and /services/{ai-security-operations, strategic-risk-assessment, defense-technology-advisory, corporate-cognitive-warfare} with Service JSON-LD, internal cross-links; added to sitemap and nav.
- `tests/seo.test.ts` (phone/entity/description-length checks).
- Launch switch already exists: `SITE_INDEXABLE=true` (Production env only) flips robots meta + robots.txt + sitemap at once; previews stay noindex regardless. Leave unset until www.theinfinitumcorporation.com points at Vercel.
Verified here: edit script dry-run on reconstructed files (exit 0), new files pass `tsc --strict` against next 16.4.3, tests 3/3 pass. NOT verified: full `next build` (full source not retrievable: the connector truncates files >~1.5 KB).

## 02-infinitum-survey-flyers
`index.html` (+ `index.html.patch` vs /workspace/survey/index.html) adds robots noindex, title, description; `vercel.json` adds X-Robots-Tag noindex. Deploy: copy both into the project folder and `vercel --prod`.

## 03-InfinitumCorp-profile
`git am` patch for InfinitumCorp/InfinitumCorp (branch seo/entity-nap-2026-10-31, local commit cb951fd in /workspace/repos/InfinitumCorp). README with canonical NAP, services, all owned profiles, research links.

## 04-williamaaronturner-redesign
`git am` patch for InfinitumCorp/williamaaronturner-redesign (branch seo/rebuild-2026-10-31, local commit 804fd18 in /workspace/repos/williamaaronturner-redesign). Replaces the placeholder with a static founder page: H1, bio from boilerplate (no "Private Military Contractor"), Person/Organization JSON-LD, links, contact, robots.txt, sitemap.xml, vercel.json (noindex on *.vercel.app, www->apex 301). Go-live needs DNS for williamaaronturner.com moved off Beacons (William).

## To push once gh is authenticated
    cd /workspace/repos/InfinitumCorp && git push -u origin seo/entity-nap-2026-10-31 && gh pr create --fill
    cd /workspace/repos/williamaaronturner-redesign && git push -u origin seo/rebuild-2026-10-31 && gh pr create --fill
