#!/usr/bin/env python3
"""Apply SEO edits to the infinitum-corporation Next.js source (run from repo root).
Exact-string edits; aborts loudly if a target is missing so nothing is half-applied silently."""
import re, sys, shutil, os
from pathlib import Path
ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
HERE = Path(__file__).parent
errors = []

def edit(path, old, new, count=1, regex=False):
    p = ROOT / path
    t = p.read_text()
    n = len(re.findall(old, t)) if regex else t.count(old)
    if n < 1 or (count and n != count):
        errors.append(f"{path}: expected {count or '>=1'} match(es) for {old[:70]!r}, found {n}")
        return
    t = re.sub(old, new, t) if regex else t.replace(old, new)
    p.write_text(t)

# 0. copy new files
for f in (HERE / "files").rglob("*"):
    if f.is_file():
        dst = ROOT / f.relative_to(HERE / "files")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dst)

# 1. site.ts: official phone, nav item for services
edit("content/site.ts", 'phone: "(202) 681-0120",', 'phone: "202-729-9509",\n  phoneE164: "+12027299509",\n  hours: "Mon–Fri 9:00 AM–9:00 PM (closed Sat–Sun)",')
edit("content/site.ts", 'address: "1629 K Street NW, Suite 300, Washington, D.C.",', 'address: "1629 K Street NW, Suite 300, Washington, DC 20006",')
edit("content/site.ts", '["Capabilities", "/capabilities"],', '["Capabilities", "/capabilities"],\n  ["Services", "/services"],\n  ["Publications", "/publications"],')

# 2. layout.tsx: keyword title/description, entity graph replaces old Organization JSON-LD
edit("app/layout.tsx", 'default: "Infinitum Corporation | Intelligence. Technology. Perspective.",',
     'default: "Infinitum Corporation | Cybersecurity Consulting, Washington DC",')
edit("app/layout.tsx", '"Washington, D.C.-based consulting across information technology, security, logistics, and infrastructure.",',
     '"Infinitum Corporation is a Washington, DC cybersecurity and security consulting firm: network defense, ethical hacking, AI for security operations. Open Mon–Fri 9 AM–9 PM. 202-729-9509.",')
edit("app/layout.tsx", r'\n\s*<script\s+type="application/ld\+json"[\s\S]*?\}\}\s*/>', "\n        <EntityJsonLd />", regex=True)
edit("app/layout.tsx", 'import "./globals.css";', 'import { EntityJsonLd } from "../components/entity-jsonld";\nimport "./globals.css";')

# 3. footer: official phone, hours, owned-profile links
edit("components/footer.tsx", '<a href="tel:+12026810120">{site.phone}</a>',
     '<a href={`tel:${site.phoneE164}`}>{site.phone}</a>\n          <p>{site.hours}</p>')
edit("components/footer.tsx", 'import { ClientTicker } from "./client-ticker";',
     'import { ClientTicker } from "./client-ticker";\nimport { footerLinks } from "../content/entity";')
edit("components/footer.tsx", '          <p>{site.address}</p>\n        </div>',
     '          <p>{site.address}</p>\n        </div>\n        <div>\n          <span className="eyebrow">FOLLOW</span>\n          {footerLinks.map(([label, href]) => (\n            <a key={href} href={href} target="_blank" rel="noopener me">\n              {label}\n            </a>\n          ))}\n        </div>')

# 4. page titles / descriptions (keyword map)
meta = {
 "app/about/page.tsx": ('title: "About",', 'title: "About Infinitum Corporation and William Aaron Turner",',
   '"Meet Infinitum Corporation, a Washington, D.C.-based intelligence, security, and technology consultancy.",',
   '"Founded by William Aaron Turner, Infinitum Corporation is a Washington, DC technology and security consulting firm, with Moscow as an operating location.",'),
 "app/capabilities/page.tsx": ('title: "Capabilities",', 'title: "Cybersecurity & IT Consulting Capabilities, Washington DC",',
   '"Explore information technology consulting, security consulting, computer engineering, and project management.",',
   '"Cybersecurity consulting, network defense, ethical hacking and vulnerability assessment, and IT consulting from Infinitum Corporation in Washington, DC.",'),
 "app/contact/page.tsx": ('title: "Contact",', 'title: "Contact Infinitum Corporation, Washington DC",',
   '"Contact Infinitum Corporation at info@theinfinitumcorporation.com or (202) 681-0120 in Washington, D.C.",',
   '"Contact Infinitum Corporation, 1629 K Street NW, Suite 300, Washington, DC 20006. Call 202-729-9509 or email info@theinfinitumcorporation.com. Open Mon–Fri 9 AM–9 PM.",'),
 "app/industries/page.tsx": ('title: "Industries",', 'title: "Industries: Government & Corporate Security Consulting",',
   '"Technology and security consulting contexts for government organizations and private and public corporations.",',
   '"Cybersecurity and security consulting for government organizations and private and public corporations, from Infinitum Corporation in Washington, DC.",'),
 "app/insights/page.tsx": ('title: "Insights",', 'title: "Insights: Security & Geopolitical Research",',
   '"A home for future Infinitum Corporation perspectives on technology, security, and infrastructure.",',
   '"Infinitum Corporation research on cybersecurity, AI for security operations and geopolitics, including whitepapers by William Aaron Turner.",'),
}
for path, (ot, nt, od, nd) in meta.items():
    edit(path, ot, nt); edit(path, od, nd)
edit("app/press/page.tsx", 'title:"Press",description:"Infinitum Corporation press releases and company announcements."',
     'title:"Press Releases and News",description:"Infinitum Corporation press releases and company news from Washington, DC, including announcements by founder William Aaron Turner."')

# 5. sitemap: services
edit("app/sitemap.ts", '    "/capabilities",', '    "/capabilities",\n    "/services",\n    "/services/ai-security-operations",\n    "/services/strategic-risk-assessment",\n    "/services/defense-technology-advisory",\n    "/services/corporate-cognitive-warfare",\n    "/publications",\n    "/publications/echoform",')

# 6. sweep: any leftover non-official numbers anywhere in src
subs = [("(202) 681-0120", "202-729-9509"), ("202-681-0120", "202-729-9509"), ("+12026810120", "+12027299509"),
        ("+1 202-681-0120", "+1 202-729-9509"), ("(202) 980-9300", "202-729-9509"), ("202-980-9300", "202-729-9509"), ("+12029809300", "+12027299509")]
for p in ROOT.rglob("*"):
    if p.suffix in {".ts", ".tsx", ".md", ".mdx"} and p.is_file() and not {"node_modules", ".next", ".git"} & set(p.parts):
        t = p.read_text(errors="ignore"); o = t
        for a, b in subs: t = t.replace(a, b)
        if t != o: p.write_text(t); print("swept", p)
left = []
for p in ROOT.rglob("*"):
    if p.suffix in {".ts", ".tsx"} and p.is_file() and not {"node_modules", ".next", ".git", "tests"} & set(p.parts):
        t = p.read_text(errors="ignore")
        for bad in ["681-0120", "6810120", "980-9300", "9809300", "6142162724", "wa.me/", "Palo Alto", "5470106"]:
            if bad in t: left.append(f"{p}: {bad}")
if left: errors.append("leftover banned strings:\n  " + "\n  ".join(left))
if errors:
    print("ERRORS:\n" + "\n".join(errors)); sys.exit(1)
print("All edits applied. Launch switch: set SITE_INDEXABLE=true on Production only at domain cut-over (already in layout.tsx/robots.ts).")
