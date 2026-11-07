#!/usr/bin/env python3
"""Reusable whitepaper PDF builder (B&W cover from make_cover.py + body).

Reads section files src/0*.md (BODY: exec summary ... conclusion, then About,
References, Glossary), applies optional in-memory text patches, and writes:
  <outdir>/<name>.pdf, <name>.html, <name>.md (combined markdown)
Usage example: see build_paper01.sh
"""
import argparse, glob, html, os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import markdown, weasyprint
import brand, make_cover

def preprocess(t):
    t = re.sub(r"^> \*\*Pull quote\.\*\* (.+)$", lambda m: f'<blockquote class="pull"><p>{m.group(1)}</p></blockquote>', t, flags=re.M)
    t = re.sub(r"^> \*\*The takeaway\.\*\* (.+)$", lambda m: f'<div class="callout"><p class="callout-lead">The takeaway</p><p>{m.group(1)}</p></div>', t, flags=re.M)
    t = re.sub(r"^\*Source: (.+)\*$", lambda m: f'<p class="source">Source: {m.group(1)}</p>', t, flags=re.M)
    t = re.sub(r"^- \[ \] ", "- ☐&nbsp; ", t, flags=re.M)
    return t

CSS = r"""
:root{--ink:#161616;--muted:#666;--rule:#d9d9d9;--tint:#f2f2f2;--dk:#0d0d0d;--dk2:#2b2b2b;--mid:#777}
@page{size:Letter;margin:.95in .9in .9in .9in;
 @top-left{content:"INFINITUM CORPORATION  ·  %(lab)s";font:600 7.5pt PoppinsBrand;letter-spacing:.14em;color:var(--muted);vertical-align:bottom;padding-bottom:6pt;border-bottom:.5pt solid var(--rule)}
 @top-right{content:string(chapter);font:400 7.5pt PoppinsBrand;color:var(--muted);vertical-align:bottom;padding-bottom:6pt;border-bottom:.5pt solid var(--rule)}
 @bottom-left{content:"%(footer)s";font:400 7.5pt PoppinsBrand;color:var(--muted)}
 @bottom-right{content:counter(page);font:600 8.5pt PoppinsBrand;color:var(--dk)}}
@page cover{size:Letter;margin:0;@top-left{content:none;border:none}@top-right{content:none;border:none}@bottom-left{content:none}@bottom-right{content:none}}
@page front{@top-right{content:""}}
html{font-family:"Source Serif Pro","Source Serif 4",Georgia,serif;font-size:10.6pt;line-height:1.5;color:var(--ink)}
body{margin:0}a{color:var(--dk2);text-decoration:none}
.cv{page:cover}
.cv h1{color:#fff!important;break-before:avoid;padding-top:0;string-set:none;font-family:PoppinsBrand;font-weight:700;font-size:58pt;line-height:1.06;margin:0 0 .28in 0}
.cv h2{color:#fff!important;font-family:PoppinsBrand;margin:-.08in 0 .22in 0;font-size:25pt;font-weight:600}
.cv p{margin:0}
.cv,.cv *{hyphens:none!important}
.legal{page:front;break-after:page;height:8.9in;position:relative}
.legal-inner{position:absolute;bottom:0;font-size:8.6pt;line-height:1.5;color:#333}
.legal-title{font:700 11pt PoppinsBrand;color:var(--dk);margin-bottom:4pt}
.legal-h{font:700 8pt PoppinsBrand;letter-spacing:.15em;text-transform:uppercase;color:var(--dk);margin:14pt 0 2pt 0}
.legal-note{margin-top:16pt;font-style:italic}
.toc{page:front;break-after:page}.toc-title{string-set:none}
.toc-list{list-style:none;padding:0;margin:18pt 0 0 0}.toc-list li{margin:0}
.toc-list li a{color:var(--ink)}.toc-list li a::after{content:leader(dotted) " " target-counter(attr(href),page);color:var(--muted)}
.toc-l1{font:600 10pt PoppinsBrand;margin-top:9pt!important}.toc-l1 a{color:var(--dk)!important}
.toc-l2{font:400 9.6pt "Source Serif Pro";padding-left:16pt;margin-top:3pt!important}
h1{font:700 23pt/1.14 PoppinsBrand;color:var(--dk);letter-spacing:-.01em;margin:0 0 18pt 0;padding-top:6pt;break-before:page;string-set:chapter content()}
main h1::before{content:"";display:block;width:.8in;height:3pt;background:var(--dk);margin-bottom:14pt}
h2{font:600 14.5pt/1.22 PoppinsBrand;color:var(--dk);margin:22pt 0 8pt 0;break-after:avoid}
h3{font:600 11pt/1.25 PoppinsBrand;color:var(--dk2);margin:16pt 0 5pt 0;break-after:avoid}
p{margin:0 0 7pt 0;orphans:2;widows:2;hyphens:auto}
ul,ol{margin:4pt 0 9pt 0;padding-left:18pt}li{margin-bottom:3pt}strong{color:#000}
blockquote{margin:10pt 0 12pt 0;padding:6pt 12pt 6pt 14pt;border-left:2.5pt solid var(--dk2);background:var(--tint);font-style:italic;color:#2b2b2b}
blockquote p{margin:0}
blockquote.pull{hyphens:manual;border:none;background:none;padding:10pt .35in;margin:14pt 0;font:600 14.5pt/1.32 "Source Serif Pro";font-style:italic;color:var(--dk);border-top:.8pt solid var(--dk);border-bottom:.8pt solid var(--dk);break-inside:avoid}
blockquote.pull p::before{content:"“";font:700 30pt/0 PoppinsBrand;color:var(--mid);vertical-align:-10pt;margin-right:4pt}
.callout{background:var(--dk);color:#fff;padding:12pt 16pt;margin:14pt 0;break-inside:avoid}
.callout p{color:#eee;margin:0;font-size:11pt}
.callout-lead{font:600 8pt PoppinsBrand!important;letter-spacing:.2em;text-transform:uppercase;color:#bbb!important;margin-bottom:4pt!important}
table{width:100%;border-collapse:collapse;margin:10pt 0 6pt 0;font:400 8.2pt/1.35 PoppinsBrand;break-inside:auto}
thead{display:table-header-group}
th{background:var(--dk);color:#fff;font-weight:600;text-align:left;padding:5pt 6pt;vertical-align:bottom}
td{padding:5pt 6pt;border-bottom:.5pt solid var(--rule);vertical-align:top}tr{break-inside:avoid}
tbody tr:nth-child(even) td{background:#f6f6f6}
p.source{font:400 8pt PoppinsBrand;color:var(--muted);margin-top:2pt}
h2[id^="part-"]{string-set:chapter content()}
.scenario{border:.8pt solid #ccc;border-left:4pt solid var(--dk);background:#fafafa;padding:10pt 14pt 6pt 14pt;margin:12pt 0 14pt 0}
.scenario-tag{font:600 7.5pt PoppinsBrand;letter-spacing:.2em;text-transform:uppercase;color:#555;margin-bottom:4pt!important}
.scenario p{font-size:9.8pt}
ul.checklist{list-style:none;padding-left:4pt}ul.checklist li{margin-bottom:4pt;font-size:10pt}
#about+p{font-size:11pt}
.refs ol{padding-left:20pt}.refs li{font-size:8.8pt;line-height:1.4;margin-bottom:5pt;overflow-wrap:anywhere}
.glossary p{font-size:9.4pt;margin-bottom:5pt}
"""

def legal_html(a):
    legal_status = "Draft for review. Not for distribution." if a.draft else f"Released {a.release_date}"
    em = f"<br/>{html.escape(brand.EMAIL)}" if brand.EMAIL else ""
    return f"""<section class="legal"><div class="legal-inner">
<p class="legal-title">{html.escape(a.title)}: {html.escape(a.title2)}<br/>{html.escape(a.subtitle)}</p>
<p>Infinitum Corporation {a.edition_label or "Whitepaper No. %d" % a.number} &middot; {a.date_label or brand.DATE_LABEL} &middot; <strong>{legal_status}</strong></p>
<p class="neutral">{a.neutrality_note or "<strong>Neutrality statement.</strong> This paper draws general lessons about technology and conflict from public sources. It takes no side and makes no claim about any party."}</p>
<p>&copy; 2026 Infinitum Corporation. All rights reserved. No part of this publication may be reproduced or distributed without written permission, except for brief quotations with attribution.</p>
<p class="legal-h">Disclaimer</p>
<p>{a.disclaimer or "This whitepaper is provided for general information only. It is not legal, regulatory or professional advice for any specific situation, and it does not create a client relationship. Statistics are taken from the public sources cited and remain the property of their publishers; they describe the samples studied by those publishers and are not benchmarks or predictions for any particular organization. Infinitum Corporation makes no promise or guarantee about the security outcome any organization will achieve."}</p>
<p>{a.legal_scope or "This paper is strictly analytical and defensive. References to irregular warfare, gray-zone competition and hybrid threats are used as an analytic lens for defense and resilience. Nothing in this paper is instruction for offensive activity. Any security testing referred to here means authorized, scoped testing performed with the written permission of the system owner."}</p>
<p>{a.scenarios_note}</p>
<p>Trademarks and framework names belong to their respective owners. Citation of a source does not imply that its publisher endorses this paper or Infinitum Corporation.</p>
<p class="legal-h">Contact</p>
<p>{html.escape(brand.LOCATION)} &middot; 1629 K Street NW, Suite 300<br/>{brand.WEBSITE_URL}{em}<br/>Telegram: {brand.TELEGRAM_URL} &middot; X: {brand.X_URL}</p>
<p class="legal-note">All data comes from the public record. All conclusions are mine. &mdash; W.A.T.</p>
</div></section>"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src-dir", required=True)
    ap.add_argument("--patches", help="JSON file: list of [old,new] exact-text replacements")
    ap.add_argument("--number", type=int, required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--title2", default="")
    ap.add_argument("--tagline", default="")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--release", action="store_true", help="RELEASE build: no draft wording anywhere (DEFAULT)")
    g.add_argument("--draft", action="store_true", help="DRAFT build: DRAFT FOR REVIEW stamp, draft legal line and footer")
    ap.add_argument("--release-date", default="October 25, 2026")
    ap.add_argument("--date-label", default="")
    ap.add_argument("--scenarios-note", default="Scenarios in Part IX are illustrative and hypothetical. They do not describe any real organization, client or incident.")
    ap.add_argument("--subtitle", required=True)
    ap.add_argument("--edition-label", default="")
    ap.add_argument("--neutrality-note", default="")
    ap.add_argument("--legal-scope", default="")
    ap.add_argument("--disclaimer", default="")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--name", required=True)
    a = ap.parse_args()
    a.outdir = os.path.abspath(a.outdir)
    os.makedirs(a.outdir, exist_ok=True)
    md_text = "\n\n".join(open(p).read() for p in sorted(glob.glob(os.path.join(a.src_dir, "0*.md"))))
    if a.patches:
        for old, new in json.load(open(a.patches)):
            assert old in md_text, "patch not found: " + old[:60]
            md_text = md_text.replace(old, new)
    open(os.path.join(a.outdir, a.name + ".md"), "w").write(md_text)
    md = markdown.Markdown(extensions=["extra", "toc", "sane_lists", "smarty"], extension_configs={"toc": {"permalink": False}})
    body = md.convert(preprocess(md_text))
    body = body.replace('<div class="scenario">', '<div class="scenario"><p class="scenario-tag">Illustrative &middot; Hypothetical</p>')
    body = re.sub(r"<ul>\s*<li>☐", '<ul class="checklist">\n<li>☐', body)
    items = []
    for m in re.finditer(r'<h([12]) id="([^"]+)">(.*?)</h\1>', body):
        l, i, t = m.groups()
        if l == "2" and not i.startswith("part-"): continue
        items.append(f'<li class="toc-l{l}"><a href="#{i}">{re.sub("<[^>]+>", "", t)}</a></li>')
    toc = f'<section class="toc"><h1 class="toc-title" id="contents">Contents</h1><ul class="toc-list">{"".join(items)}</ul></section>'
    brand.warn_if_no_email()
    assets = os.path.join(a.outdir, "assets"); os.makedirs(assets, exist_ok=True)
    bg = make_cover.make_contours(1632, 2112, seed=100 + a.number, path=os.path.join(assets, "cover-bg.png"))
    ccss, cbody = make_cover.cover_html(a.title, a.subtitle, a.number, bg, a.draft, a.title2, a.tagline, **({'stamp': a.date_label} if a.date_label else {}), label=a.edition_label)
    footer = f"{a.title}  ·  Draft for review" if a.draft else a.title
    css = CSS.replace("%(lab)s", (a.edition_label or f"Whitepaper {a.number:02d}").upper().replace(" ", "  ", 0).replace("WHITEPAPER ", "WHITEPAPER ")).replace("%(footer)s", footer)
    full_title = f"{a.title}: {a.title2}" if a.title2 else a.title
    doc = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/><title>{html.escape(full_title)} | Infinitum {a.edition_label or "Whitepaper %02d" % a.number}</title>
<meta name="author" content="William Aaron Turner"/><meta name="description" content="{html.escape(a.subtitle)}"/>
<style>{brand.font_face_css()}\n{ccss}\n{css}</style></head><body>
{cbody}{legal_html(a)}{toc}<main>{body}</main></body></html>"""
    open(os.path.join(a.outdir, a.name + ".html"), "w").write(doc)
    weasyprint.HTML(string=doc, base_url=a.outdir).write_pdf(os.path.join(a.outdir, a.name + ".pdf"))
    print("built", os.path.join(a.outdir, a.name + ".pdf"))

if __name__ == "__main__":
    main()
