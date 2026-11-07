#!/usr/bin/env python3
"""Reusable black-and-white cover + social post graphic generator.

Usage:
  /workspace/wpvenv/bin/python make_cover.py \
      --title "Outthink the Quiet War" --title2 "AI for Security Operations" \
      --subtitle "Practical, Integrated Steps for Mid-Size Organizations" \
      --number 1 --outdir /workspace/whitepapers/01-ai-for-security-operations \
      [--draft]  (release is the default)

Outputs in outdir: cover.pdf, cover-preview.png, post-NN.png,
plus cover-bg.png / post-bg.png (contour backgrounds).
Import use: cover_html(...) returns a full-bleed HTML fragment for embedding
as page 1 of the PDF (see build_whitepaper.py).
"""
import argparse, html, os, subprocess, sys, tempfile
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand

# ---------------------------------------------------------------- contours
def make_contours(w, h, seed, path, levels=34, lw=1.3):
    """Grayscale topographic contour lines (white, low alpha) on black."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    rng = np.random.default_rng(seed)
    nx, ny = 420, int(420 * h / w)
    x = np.linspace(0, 1, nx)[None, :] * (w / h)
    y = np.linspace(0, 1, ny)[:, None]
    f = np.zeros((ny, nx))
    for _ in range(9):                       # broad rolling hills
        th = rng.uniform(0, np.pi)
        k = rng.uniform(1.2, 3.6) * 2 * np.pi
        ph = rng.uniform(0, 2 * np.pi)
        f += rng.uniform(0.5, 1.0) * np.sin(k * (np.cos(th) * x + np.sin(th) * y) + ph)
    for _ in range(5):                       # a few peaks/basins
        cx, cy = rng.uniform(0, w / h), rng.uniform(0, 1)
        s = rng.uniform(0.15, 0.35)
        f += rng.choice([-1, 1]) * 2.2 * np.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * s * s))
    fig = plt.figure(figsize=(w / 100, h / 100), dpi=100, facecolor="black")
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor("black"); ax.axis("off")
    ax.contour(x * np.ones_like(y), y * np.ones_like(x), f, levels=levels,
               colors=[(1, 1, 1, 0.13)], linewidths=lw)
    ax.set_xlim(0, w / h); ax.set_ylim(1, 0)
    fig.savefig(path, facecolor="black"); plt.close(fig)
    return path

# ---------------------------------------------------------------- fragments
def _esc(s): return html.escape(s, quote=True)

def _contact_lines(sep_html="<br>"):
    lines = [brand.PERSON, brand.LOCATION, brand.TELEGRAM_DISPLAY, brand.WEBSITE_DISPLAY]
    if brand.EMAIL:
        lines.append(brand.EMAIL)
    return sep_html.join(_esc(l) for l in lines)

COVER_CSS = """
.cv{position:relative;width:8.5in;height:11in;background:#000 url('%(bg)s') center/cover no-repeat;
    color:#fff;font-family:'PoppinsBrand',sans-serif;overflow:hidden;page-break-after:always}
.cv .fade{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(0,0,0,.95) 0,rgba(0,0,0,.0) 38%%,rgba(0,0,0,0) 100%%)}
.cv .top{position:absolute;left:.62in;right:.62in;top:.62in;display:flex;align-items:center}
.cv .wm{font-weight:600;font-size:15pt;letter-spacing:.24em;white-space:nowrap}
.cv .rule{flex:1;height:0;border-top:1.5pt solid #fff;margin-left:.3in}
.cv .tb{position:absolute;left:.62in;right:.9in;top:4.0in}
.cv h1{font-weight:700;font-size:58pt;line-height:1.06;letter-spacing:-.01em;margin:0 0 .28in 0}
.cv h2{text-wrap:balance;font-weight:600;font-size:25pt;line-height:1.2;letter-spacing:-.005em;margin:-.08in 0 .22in 0;color:#fff}
.cv .sub{font-weight:300;font-size:19pt;line-height:1.35;color:#b8b8b8;margin:0;max-width:6.2in;hyphens:none}
.cv .tag{font-weight:600;font-size:9.5pt;letter-spacing:.3em;text-transform:uppercase;color:#fff;margin:.38in 0 0 0;padding-top:.14in;border-top:.75pt solid #6a6a6a;display:inline-block}
.cv .bot{position:absolute;left:.62in;right:.62in;bottom:.6in;display:flex;justify-content:space-between;align-items:flex-end}
.cv .lab{font-weight:700;font-size:13pt}
.cv .lab small{display:block;font-weight:400;font-size:7.5pt;letter-spacing:.22em;color:#8a8a8a;margin-top:6pt;text-transform:uppercase}
.cv .ct{font-weight:400;font-size:8.5pt;line-height:1.65;color:#cfcfcf;text-align:right}
"""

def cover_html(title, subtitle, number, bg_path, draft=False, title2='', tagline='', stamp='October 2026', label=''):
    css = COVER_CSS % {"bg": "file://" + bg_path}
    draft_html = "<small>Draft for review</small>" if draft else (f"<small>{_esc(stamp)}</small>" if stamp else "")
    t2 = f"<h2>{_esc(title2)}</h2>" if title2 else ""
    tg = f'<p class="tag">{_esc(tagline)}</p>' if tagline else ""
    body = f"""
<div class="cv"><div class="fade"></div>
 <div class="top"><div class="wm">{_esc(brand.WORDMARK)}</div><div class="rule"></div></div>
 <div class="tb"><h1>{_esc(title)}</h1>{t2}<p class="sub">{_esc(subtitle)}</p>{tg}</div>
 <div class="bot"><div class="lab">{_esc(label) if label else "Whitepaper &nbsp;%02d" % int(number)}{draft_html}</div>
 <div class="ct">{_contact_lines()}</div></div>
</div>"""
    return css, body

POST_CSS = """
*{box-sizing:border-box}html,body{margin:0;padding:0;background:#000}
.pg{position:relative;width:1200px;height:675px;background:#000 url('%(bg)s') center/cover no-repeat;
    color:#fff;font-family:'PoppinsBrand',sans-serif;overflow:hidden}
.pg .fade{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(0,0,0,.9) 0,rgba(0,0,0,0) 40%%)}
.pg .top{position:absolute;left:64px;right:64px;top:48px;display:flex;align-items:center}
.pg .wm{font-weight:600;font-size:20px;letter-spacing:.24em;white-space:nowrap}
.pg .rule{flex:1;border-top:2px solid #fff;margin-left:28px}
.pg .tb{position:absolute;left:64px;right:100px;top:215px}
.pg h1{font-weight:700;font-size:76px;line-height:1.05;letter-spacing:-.01em;margin:0 0 20px}
.pg h2{font-weight:600;font-size:32px;line-height:1.2;margin:-6px 0 16px;color:#fff;max-width:820px;text-wrap:balance}
.pg .sub{font-weight:300;font-size:25px;line-height:1.35;color:#b8b8b8;margin:0;max-width:880px}
.pg .tag{font-weight:600;font-size:15px;letter-spacing:.3em;text-transform:uppercase;color:#fff;margin:26px 0 0;padding-top:12px;border-top:1px solid #6a6a6a;display:inline-block}
.pg .bot{position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;align-items:flex-end}
.pg .lab{font-weight:700;font-size:18px}
.pg .ct{font-size:14px;line-height:1.6;color:#cfcfcf;text-align:right}
"""

def post_html(title, subtitle, number, bg_path, title2='', tagline='', label=''):
    css = POST_CSS % {"bg": "file://" + bg_path}
    ct = _contact_lines()
    t2 = f"<h2>{_esc(title2)}</h2>" if title2 else ""
    tg = f'<p class="tag">{_esc(tagline)}</p>' if tagline else ""
    body = f"""<div class="pg"><div class="fade"></div>
 <div class="top"><div class="wm">{_esc(brand.WORDMARK)}</div><div class="rule"></div></div>
 <div class="tb"><h1>{_esc(title)}</h1>{t2}<p class="sub">{_esc(subtitle)}</p>{tg}</div>
 <div class="bot"><div class="lab">{_esc(label) if label else "Whitepaper &nbsp;%02d" % int(number)}</div><div class="ct">{ct}</div></div></div>"""
    return css, body

# ---------------------------------------------------------------- renderers
def _doc(css, body, page_css=""):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{brand.font_face_css()}\n{page_css}\n{css}</style></head><body>{body}</body></html>"

def render_cover_pdf(title, subtitle, number, outdir, draft=False, title2='', tagline=''):
    import weasyprint
    outdir = os.path.abspath(outdir)
    brand.warn_if_no_email()
    bg = make_contours(1632, 2112, seed=100 + int(number), path=os.path.join(outdir, "cover-bg.png"))
    css, body = cover_html(title, subtitle, number, bg, draft, title2, tagline)
    doc = _doc(css, body, "@page{size:8.5in 11in;margin:0}html,body{margin:0;background:#000}")
    pdf = os.path.join(outdir, "cover.pdf")
    weasyprint.HTML(string=doc, base_url=outdir).write_pdf(pdf)
    prev = os.path.join(outdir, "cover-preview")
    subprocess.run(["pdftoppm", "-png", "-r", "80", "-singlefile", pdf, prev], check=True)
    return pdf, prev + ".png"

def render_post_png(title, subtitle, number, outdir, title2='', tagline=''):
    outdir = os.path.abspath(outdir)
    brand.warn_if_no_email()
    bg = make_contours(2400, 1350, seed=200 + int(number), path=os.path.join(outdir, "post-bg.png"), lw=2.2)
    css, body = post_html(title, subtitle, number, bg, title2, tagline)
    htmlp = os.path.join(outdir, "post.html")
    open(htmlp, "w").write(_doc(css, body))
    out = os.path.join(outdir, f"post-{int(number):02d}.png")
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", "--allow-file-access-from-files",
                    "--window-size=1200,675", f"--screenshot={out}", "file://" + htmlp],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return out

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--title2", default="", help="optional second headline line (smaller, white)")
    ap.add_argument("--subtitle", required=True)
    ap.add_argument("--tagline", default="", help="optional one-line tagline under the subtitle")
    ap.add_argument("--number", type=int, required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--draft", action="store_true", help="add the DRAFT FOR REVIEW stamp (default is RELEASE: stamp reads the month)")
    ap.add_argument("--no-draft", action="store_true", help="(legacy, ignored: release is the default)")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    print(render_cover_pdf(a.title, a.subtitle, a.number, a.outdir, a.draft, a.title2, a.tagline))
    print(render_post_png(a.title, a.subtitle, a.number, a.outdir, a.title2, a.tagline))
