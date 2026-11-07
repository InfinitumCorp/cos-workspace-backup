#!/usr/bin/env python3
"""Build EchoForm™ RELEASE covers + PDF + DOCX. Overrides brand in-script only."""
import os, sys, re, html, subprocess, io
from pathlib import Path

ROOT = Path('/workspace/whitepapers/echoform')
TOOLS = Path('/workspace/whitepapers/tools')
ASSETS = ROOT / 'assets'
STEM = 'EchoForm-Modern-Applications-of-Reflexive-Control-Theory'
sys.path.insert(0, str(TOOLS))

import brand
# In-script brand overrides (do not edit brand.py)
brand.WORDMARK = 'INFINITUM CORPORATION®'
brand.COMPANY = 'Infinitum Corporation®'
brand.LOCATION = 'Infinitum Corporation®, Washington, DC'

import make_cover
import markdown
import weasyprint
from PIL import Image
import pypdf

TITLE = 'EchoForm™'
TITLE2 = 'Modern Applications of Reflexive Control Theory'
SUBTITLE = "How prepared grounds return as the target's own decision"
TAGLINE = 'A term coined by William Aaron Turner'
LABEL = 'Companion Note'
STAMP = 'November 2026'
SEED = 80  # contour seed per brief

ASSETS.mkdir(exist_ok=True)

# ---------- Black cover PDF + preview ----------
print('== black cover ==')
bg = make_cover.make_contours(1632, 2112, seed=SEED, path=str(ASSETS / 'cover-bg.png'))
css, body = make_cover.cover_html(
    TITLE, SUBTITLE, number=SEED, bg_path=bg, draft=False,
    title2=TITLE2, tagline=TAGLINE, stamp=STAMP, label=LABEL)
doc = make_cover._doc(css, body, "@page{size:8.5in 11in;margin:0}html,body{margin:0;background:#000}")
cover_pdf = ASSETS / 'cover.pdf'
weasyprint.HTML(string=doc, base_url=str(ASSETS)).write_pdf(str(cover_pdf))
subprocess.run(['pdftoppm', '-png', '-r', '80', '-singlefile', str(cover_pdf), str(ASSETS / 'cover-preview')], check=True)
# hi-res cover render
subprocess.run(['pdftoppm', '-png', '-r', '150', '-singlefile', str(cover_pdf), str(ASSETS / 'cover-hi')], check=True)
print('cover.pdf ok')

# ---------- Post 1200x675 ----------
print('== post image ==')
post_bg = make_cover.make_contours(2400, 1350, seed=SEED + 100, path=str(ASSETS / 'post-bg.png'), lw=2.2)
pcss, pbody = make_cover.post_html(TITLE, SUBTITLE, number=SEED, bg_path=post_bg, title2=TITLE2, tagline=TAGLINE, label=LABEL)
htmlp = ASSETS / 'post.html'
htmlp.write_text(make_cover._doc(pcss, pbody))
post_out = ASSETS / 'post-echoform-1200x675.png'
subprocess.run([
    'google-chrome', '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
    '--force-device-scale-factor=1', '--allow-file-access-from-files',
    '--window-size=1200,675', f'--screenshot={post_out}', 'file://' + str(htmlp)
], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print('post ok', post_out.stat().st_size)

# ---------- White cover + X article header ----------
print('== white covers ==')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def contours(w, h, seed, path, levels=30, lw=1.2, alpha=0.07):
    rng = np.random.default_rng(seed)
    nx, ny = 420, int(420 * h / w)
    x = np.linspace(0, 1, nx)[None, :] * (w / h); y = np.linspace(0, 1, ny)[:, None]
    f = np.zeros((ny, nx))
    for _ in range(9):
        th = rng.uniform(0, np.pi); k = rng.uniform(1.2, 3.6) * 2 * np.pi; ph = rng.uniform(0, 2 * np.pi)
        f += rng.uniform(0.5, 1.0) * np.sin(k * (np.cos(th) * x + np.sin(th) * y) + ph)
    for _ in range(5):
        cx, cy = rng.uniform(0, w / h), rng.uniform(0, 1); s = rng.uniform(0.15, 0.35)
        f += rng.choice([-1, 1]) * 2.2 * np.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * s * s))
    fig = plt.figure(figsize=(w / 100, h / 100), dpi=100, facecolor='white')
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor('white'); ax.axis('off')
    ax.contour(x * np.ones_like(y), y * np.ones_like(x), f, levels=levels, colors=[(0, 0, 0, alpha)], linewidths=lw)
    ax.set_xlim(0, w / h); ax.set_ylim(1, 0)
    fig.savefig(path, facecolor='white'); plt.close(fig); return path

E = lambda s: html.escape(s, quote=True)
CONTACT = [brand.PERSON, brand.LOCATION, brand.TELEGRAM_DISPLAY, brand.WEBSITE_DISPLAY, brand.EMAIL]

def white_page(bg, wide=False):
    ct = '<br>'.join(E(l) for l in CONTACT)
    if not wide:
        css = f"""
html,body{{margin:0;background:#fff}}
.cv{{position:relative;width:816px;height:1056px;background:#fff url('{bg}') center/cover no-repeat;color:#000;font-family:'PoppinsBrand',sans-serif;overflow:hidden}}
.top{{position:absolute;left:60px;right:60px;top:60px;display:flex;align-items:center}}
.wm{{font-weight:600;font-size:20px;letter-spacing:.24em;white-space:nowrap}}
.rule{{flex:1;border-top:1.5px solid #000;margin-left:30px}}
.tb{{position:absolute;left:60px;right:90px;top:384px}}
h1{{font-weight:700;font-size:77px;line-height:1.06;letter-spacing:-.01em;margin:0 0 27px}}
h2{{text-wrap:balance;font-weight:600;font-size:33px;line-height:1.2;margin:-8px 0 21px;color:#000}}
.sub{{font-weight:300;font-size:25px;line-height:1.35;color:#777;margin:0;max-width:600px}}
.tag{{font-weight:600;font-size:12.7px;letter-spacing:.3em;text-transform:uppercase;color:#000;margin:36px 0 0;padding-top:13px;border-top:1px solid #999;display:inline-block}}
.bot{{position:absolute;left:60px;right:60px;bottom:58px;display:flex;justify-content:space-between;align-items:flex-end}}
.lab{{font-weight:700;font-size:17px}}
.lab small{{display:block;font-weight:400;font-size:10px;letter-spacing:.22em;color:#777;margin-top:8px;text-transform:uppercase}}
.ct{{font-size:11.5px;line-height:1.65;color:#444;text-align:right}}
"""
        h2 = '<span style="white-space:nowrap">Modern Applications of</span> <span style="white-space:nowrap">Reflexive Control Theory</span>'
        body = f"""<div class="cv"><div class="top"><div class="wm">{E(brand.WORDMARK)}</div><div class="rule"></div></div>
<div class="tb"><h1>{E(TITLE)}</h1><h2>{h2}</h2><p class="sub">{E(SUBTITLE)}</p><p class="tag">{E(TAGLINE)}</p></div>
<div class="bot"><div class="lab">{E(LABEL)}<small>{E(STAMP)}</small></div><div class="ct">{ct}</div></div></div>"""
    else:
        css = f"""
html,body{{margin:0;background:#fff}}
.cv{{position:relative;width:1500px;height:500px;background:#fff url('{bg}') center/cover no-repeat;color:#000;font-family:'PoppinsBrand',sans-serif;overflow:hidden}}
.top{{position:absolute;left:56px;right:56px;top:40px;display:flex;align-items:center}}
.wm{{font-weight:600;font-size:22px;letter-spacing:.24em;white-space:nowrap}}
.rule{{flex:1;border-top:2px solid #000;margin-left:30px}}
.tb{{position:absolute;left:56px;right:56px;top:100px}}
h1{{font-weight:700;font-size:72px;line-height:1.04;letter-spacing:-.01em;margin:0 0 14px}}
h2{{font-weight:600;font-size:28px;line-height:1.2;margin:0 0 6px;color:#000}}
.sub{{font-weight:300;font-size:22px;line-height:1.3;color:#777;margin:0;max-width:1100px}}
.tag{{font-weight:600;font-size:15px;letter-spacing:.3em;text-transform:uppercase;color:#000;margin:18px 0 0;padding-top:10px;border-top:1px solid #999;display:inline-block}}
.bot{{position:absolute;left:56px;right:56px;bottom:30px;display:flex;justify-content:space-between;align-items:flex-end}}
.lab{{font-weight:700;font-size:22px}}
.lab small{{display:block;font-weight:400;font-size:13px;letter-spacing:.22em;color:#777;margin-top:6px;text-transform:uppercase}}
.ct{{font-size:16px;line-height:1.45;color:#444;text-align:right}}
"""
        body = f"""<div class="cv"><div class="top"><div class="wm">{E(brand.WORDMARK)}</div><div class="rule"></div></div>
<div class="tb"><h1>{E(TITLE)}</h1><h2>{E(TITLE2)}</h2><p class="sub">{E(SUBTITLE)}</p><p class="tag">{E(TAGLINE)}</p></div>
<div class="bot"><div class="lab">{E(LABEL)}<small>{E(STAMP)}</small></div><div class="ct">{ct}</div></div></div>"""
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{brand.font_face_css()}\n{css}</style></head><body>{body}</body></html>"

def shot(htmlp, out, w, h, scale):
    subprocess.run(['google-chrome', '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
        f'--force-device-scale-factor={scale}', '--allow-file-access-from-files', f'--window-size={w},{h}',
        f'--screenshot={out}', 'file://' + htmlp], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

bg1 = contours(1632, 2112, SEED, str(ASSETS / 'cover-white-bg.png'))
(ASSETS / 'cover-white.html').write_text(white_page('file://' + bg1, False))
shot(str(ASSETS / 'cover-white.html'), str(ASSETS / 'cover-white.png'), 816, 1056, 1.5625)
bg2 = contours(3000, 1000, SEED + 200, str(ASSETS / 'xarticle-cover-white-bg.png'), levels=22, lw=1.8)
(ASSETS / 'xarticle-cover-white.html').write_text(white_page('file://' + bg2, True))
shot(str(ASSETS / 'xarticle-cover-white.html'), str(ASSETS / 'xarticle-cover-white.png'), 1500, 500, 1)
print('white covers ok')

# ---------- Body PDF via weasyprint ----------
print('== body PDF ==')
md_text = (ROOT / (STEM + '.md')).read_text()

# Extract abstract for meta
am = re.search(r'## Abstract\n\n(.+?)\n\n\*\*Keywords:\*\* (.+?)\n', md_text, re.S)
abstract = am.group(1).strip() if am else SUBTITLE
keywords = am.group(2).strip() if am else 'EchoForm, Reflexive Control Theory'

# Convert body: drop the H1 title line and the short front-matter bullets before Abstract — keep About through References
# We'll structure: legal page from About, then TOC, then content from Abstract onward (About appears again at end in MD)

def preprocess(t):
    t = re.sub(r'^> \*(.+)\*$', lambda m: f'<blockquote class="pull"><p>{m.group(1)}</p></blockquote>', t, flags=re.M)
    t = re.sub(r'^> (.+)$', lambda m: f'<blockquote><p>{m.group(1)}</p></blockquote>', t, flags=re.M)
    return t

# Split off front banner (title through Contents) — use body from Abstract
parts = re.split(r'\n## Abstract\n', md_text, maxsplit=1)
body_md = '## Abstract\n' + parts[1] if len(parts) == 2 else md_text
# Remove duplicate top-level title if present
body_md = re.sub(r'^# .+\n+', '', body_md)

md = markdown.Markdown(extensions=['extra', 'toc', 'sane_lists', 'smarty'],
                       extension_configs={'toc': {'permalink': False}})
body_html = md.convert(preprocess(body_md))

# TOC from h1/h2
items = []
for m in re.finditer(r'<h([12]) id="([^"]+)">(.*?)</h\1>', body_html):
    l, i, t = m.groups()
    items.append(f'<li class="toc-l{l}"><a href="#{i}">{re.sub("<[^>]+>", "", t)}</a></li>')
toc = f'<section class="toc"><h1 class="toc-title" id="contents">Contents</h1><ul class="toc-list">{"".join(items)}</ul></section>'

CSS = make_cover  # noqa - reuse fonts via brand
from importlib import import_module
# Use CSS from build_whitepaper
sys.path.insert(0, str(TOOLS))
import build_whitepaper as bw

footer = 'EchoForm™  ·  Companion Note'
css = bw.CSS.replace('%(lab)s', 'COMPANION NOTE').replace('%(footer)s', footer)

# Legal page
neutrality = ("<strong>Neutrality statement.</strong> This paper draws general lessons from published theory and public sources. "
              "It takes no side, makes no claim about any party, and does not praise, blame, or score any state, army, government, or leader. "
              "Contemporary military discussion concerns mechanisms, not named campaigns or attributions.")
disclaimer = ("This companion note is provided for general information only. It is not legal, operational, regulatory, or professional advice "
              "for any specific situation, and it does not create a client relationship. References identify sources opened for this revision; "
              "a repository or publisher record is not treated as access to an entire book or article. No empirical validation of EchoForm™ is claimed. "
              "Infinitum Corporation® makes no promise or guarantee about outcomes any organization will achieve.")
legal_scope = ("This paper is strictly analytical and defensive. Fake accounts, bot networks, astroturfing, fabricated reviews, and disinformation "
               "appear only as threats to recognize and defend against. This paper gives no instructions for using them. "
               "The analytical language of control does not confer permission to undermine another person's informed choice.")
scenarios = ("All use cases are conceived composite illustrations. They are not accounts of real clients, actual campaigns, or results achieved by Infinitum Corporation®.")

em = f"<br/>{html.escape(brand.EMAIL)}" if brand.EMAIL else ""
legal = f"""<section class="legal"><div class="legal-inner">
<p class="legal-title">{html.escape(TITLE)}: {html.escape(TITLE2)}<br/>{html.escape(SUBTITLE)}</p>
<p>Infinitum Corporation® Companion Conceptual Note &middot; {STAMP} &middot; <strong>Released November 7, 2026</strong></p>
<p class="neutral">{neutrality}</p>
<p>&copy; 2026 Infinitum Corporation®. All rights reserved. No part of this publication may be reproduced or distributed without written permission, except for brief quotations with attribution.</p>
<p class="legal-h">Disclaimer</p>
<p>{disclaimer}</p>
<p>{legal_scope}</p>
<p>{scenarios}</p>
<p>Trademarks and framework names belong to their respective owners. Citation of a source does not imply that its publisher endorses this paper or Infinitum Corporation®. EchoForm™ is a term coined by William Aaron Turner.</p>
<p class="legal-h">Contact</p>
<p>{html.escape(brand.LOCATION)} &middot; 1629 K Street NW, Suite 300<br/>{brand.WEBSITE_URL}{em}<br/>Telegram: {brand.TELEGRAM_URL} &middot; X: {brand.X_URL}</p>
<p class="legal-note">All data comes from the public record. All conclusions are mine. &mdash; W.A.T.</p>
</div></section>"""

# Cover fragment for embedding (then we'll swap with cover.pdf page)
ccss, cbody = make_cover.cover_html(TITLE, SUBTITLE, SEED, bg, False, TITLE2, TAGLINE, stamp=STAMP, label=LABEL)

full_title = f'{TITLE}: {TITLE2}'
meta_desc = abstract[:300].replace('"', "'")
meta_kw = keywords.replace('™', '').replace(';', ',')
doc_html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"/>
<title>{html.escape(full_title)} | Infinitum Corporation® Companion Note</title>
<meta name="author" content="William Aaron Turner"/>
<meta name="description" content="{html.escape(meta_desc)}"/>
<meta name="keywords" content="{html.escape(meta_kw)}"/>
<style>{brand.font_face_css()}\n{ccss}\n{css}
/* companion tweaks */
main h1{{break-before:auto;padding-top:2pt}}
main h1:first-of-type{{break-before:avoid}}
#abstract{{break-before:avoid}}
</style></head><body>
{cbody}{legal}{toc}<main>{body_html}</main></body></html>"""

html_out = ROOT / (STEM + '.html')
html_out.write_text(doc_html)
body_pdf = ROOT / (STEM + '-body.pdf')
weasyprint.HTML(string=doc_html, base_url=str(ROOT)).write_pdf(str(body_pdf))
print('body pdf pages', len(pypdf.PdfReader(str(body_pdf)).pages))

# Merge: cover.pdf as page 1, then body pages from 2 onward (skip generated cover)
print('== merge PDF ==')
cov_reader = pypdf.PdfReader(str(cover_pdf))
body_reader = pypdf.PdfReader(str(body_pdf))
w = pypdf.PdfWriter()
w.add_page(cov_reader.pages[0])
for p in body_reader.pages[1:]:
    w.add_page(p)
# Metadata for SEO
w.add_metadata({
    '/Title': full_title,
    '/Author': 'William Aaron Turner',
    '/Subject': 'EchoForm companion note on modern applications of Reflexive Control Theory; Corporate Cognitive Warfare framework',
    '/Keywords': meta_kw,
    '/Creator': 'Infinitum Corporation',
    '/Producer': 'Infinitum Whitepaper Tools',
})
final_pdf = ROOT / (STEM + '.pdf')
with open(final_pdf, 'wb') as f:
    w.write(f)
print('FINAL PDF', final_pdf, 'pages', len(w.pages), 'bytes', final_pdf.stat().st_size)

# Also copy RELEASE-named alias
release_pdf = ROOT / 'Infinitum-EchoForm-Modern-Applications-of-Reflexive-Control-Theory-RELEASE.pdf'
release_pdf.write_bytes(final_pdf.read_bytes())
print('alias', release_pdf)

# ---------- DOCX ----------
print('== DOCX ==')
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

s = (ROOT / (STEM + '.md')).read_text()
doc = Document()
sec = doc.sections[0]
sec.top_margin = sec.bottom_margin = Inches(.8)
sec.left_margin = sec.right_margin = Inches(.85)
normal = doc.styles['Normal']
normal.font.name = 'Calibri'; normal.font.size = Pt(11)
normal.paragraph_format.space_after = Pt(7)
normal.paragraph_format.line_spacing = 1.1
for h in ['Title', 'Heading 1', 'Heading 2', 'Heading 3']:
    doc.styles[h].font.name = 'Calibri'
    doc.styles[h].font.color.rgb = RGBColor.from_string('19364D')
header = sec.header.paragraphs[0]
header.text = 'INFINITUM CORPORATION®  |  Companion Note  |  November 2026'
header.style = 'Caption'
footer = sec.footer.paragraphs[0]
footer.text = '© 2026 Infinitum Corporation®  |  '
fld = OxmlElement('w:fldSimple'); fld.set(qn('w:instr'), 'PAGE'); footer._p.append(fld)

def inline(p, text):
    for t in re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*)', text):
        if not t:
            continue
        r = p.add_run(t.strip('*') if t.startswith('*') else t)
        if t.startswith('**'):
            r.bold = True
        elif t.startswith('*'):
            r.italic = True

for line in s.splitlines():
    if not line.strip():
        continue
    if line.startswith('# '):
        p = doc.add_paragraph(style='Title'); txt = line[2:]
    elif line.startswith('### '):
        p = doc.add_paragraph(style='Heading 2'); txt = line[4:]
    elif line.startswith('## '):
        txt = line[3:]
        if txt == 'Executive Summary':
            doc.add_page_break()
        p = doc.add_paragraph(style='Heading 1')
    elif line.startswith('> '):
        p = doc.add_paragraph(style='Quote'); txt = line[2:]
    elif line.startswith('- '):
        p = doc.add_paragraph(style='List Bullet'); txt = line[2:]
    else:
        p = doc.add_paragraph(); txt = line
    inline(p, txt)

doc.core_properties.title = full_title
doc.core_properties.author = 'William Aaron Turner, Founder & President, Infinitum Corporation®'
doc.core_properties.subject = 'Released November 2026. Companion conceptual note on EchoForm™ and Reflexive Control Theory.'
doc.core_properties.keywords = meta_kw
docx_path = ROOT / (STEM + '.docx')
doc.save(str(docx_path))
print('DOCX', docx_path, docx_path.stat().st_size)

# Sanity: no draft stamps in outputs
assert 'DRAFT FOR REVIEW' not in s
cov_txt = subprocess.check_output(['pdftotext', str(cover_pdf), '-'], text=True)
assert 'DRAFT' not in cov_txt.upper() or 'DRAFT' not in cov_txt  # November 2026 only
print('cover text sample:\n', cov_txt[:500])
assert 'November 2026' in cov_txt or 'NOVEMBER 2026' in cov_txt.upper()
assert 'DRAFT FOR REVIEW' not in cov_txt
print('ALL BUILD STEPS OK')
