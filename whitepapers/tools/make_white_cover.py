#!/usr/bin/env python3
"""White (paper) cover variants: full-page cover-white.png (1275x1650) and X Article header xarticle-cover-white.png (1500x500).
Black covers are never touched. Usage: make_white_cover.py  (builds both papers)"""
import os, sys, subprocess, html
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand

def contours(w, h, seed, path, levels=30, lw=1.2, alpha=0.07):
    import matplotlib; matplotlib.use("Agg")
    import matplotlib.pyplot as plt
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
    fig = plt.figure(figsize=(w / 100, h / 100), dpi=100, facecolor="white")
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_facecolor("white"); ax.axis("off")
    ax.contour(x * np.ones_like(y), y * np.ones_like(x), f, levels=levels, colors=[(0, 0, 0, alpha)], linewidths=lw)
    ax.set_xlim(0, w / h); ax.set_ylim(1, 0)
    fig.savefig(path, facecolor="white"); plt.close(fig); return path

E = lambda s: html.escape(s, quote=True)
CONTACT = [brand.PERSON, brand.LOCATION, brand.TELEGRAM_DISPLAY, brand.WEBSITE_DISPLAY, brand.EMAIL]  # no phone

def page_html(p, bg, wide):
    ct = "<br>".join(E(l) for l in CONTACT)
    if not wide:  # 816x1056 CSS px, rendered at 1.5625x -> 1275x1650
        css = """
html,body{margin:0;background:#fff}
.cv{position:relative;width:816px;height:1056px;background:#fff url('%s') center/cover no-repeat;color:#000;font-family:'PoppinsBrand',sans-serif;overflow:hidden}
.top{position:absolute;left:60px;right:60px;top:60px;display:flex;align-items:center}
.wm{font-weight:600;font-size:20px;letter-spacing:.24em;white-space:nowrap}
.rule{flex:1;border-top:1.5px solid #000;margin-left:30px}
.tb{position:absolute;left:60px;right:90px;top:384px}
h1{font-weight:700;font-size:77px;line-height:1.06;letter-spacing:-.01em;margin:0 0 27px}
h2{text-wrap:balance;font-weight:600;font-size:33px;line-height:1.2;margin:-8px 0 21px;color:#000}
.sub{font-weight:300;font-size:25px;line-height:1.35;color:#777;margin:0;max-width:600px}
.tag{font-weight:600;font-size:12.7px;letter-spacing:.3em;text-transform:uppercase;color:#000;margin:36px 0 0;padding-top:13px;border-top:1px solid #999;display:inline-block}
.bot{position:absolute;left:60px;right:60px;bottom:58px;display:flex;justify-content:space-between;align-items:flex-end}
.lab{font-weight:700;font-size:17px}
.lab small{display:block;font-weight:400;font-size:10px;letter-spacing:.22em;color:#777;margin-top:8px;text-transform:uppercase}
.ct{font-size:11.5px;line-height:1.65;color:#444;text-align:right}
"""
    else:  # 1500x500 at 1x
        css = """
html,body{margin:0;background:#fff}
.cv{position:relative;width:1500px;height:500px;background:#fff url('%s') center/cover no-repeat;color:#000;font-family:'PoppinsBrand',sans-serif;overflow:hidden}
.top{position:absolute;left:56px;right:56px;top:40px;display:flex;align-items:center}
.wm{font-weight:600;font-size:22px;letter-spacing:.24em;white-space:nowrap}
.rule{flex:1;border-top:2px solid #000;margin-left:30px}
.tb{position:absolute;left:56px;right:56px;top:100px}
h1{font-weight:700;font-size:__H1W__px;line-height:1.04;letter-spacing:-.01em;margin:0 0 14px}
h2{font-weight:600;font-size:36px;line-height:1.2;margin:0 0 6px;color:#000;white-space:nowrap}
.sub{font-weight:300;font-size:26px;line-height:1.3;color:#777;margin:0}
.tag{font-weight:600;font-size:17px;letter-spacing:.3em;text-transform:uppercase;color:#000;margin:18px 0 0;padding-top:10px;border-top:1px solid #999;display:inline-block}
.bot{position:absolute;left:56px;right:56px;bottom:30px;display:flex;justify-content:space-between;align-items:flex-end}
.lab{font-weight:700;font-size:22px}
.lab small{display:block;font-weight:400;font-size:13px;letter-spacing:.22em;color:#777;margin-top:6px;text-transform:uppercase}
.ct{font-size:16px;line-height:1.45;color:#444;text-align:right}
"""
    css = css.replace("__H1W__", str(p.get("h1w", 92)))
    NB = lambda t: "".join('<span style="white-space:nowrap">%s</span> ' % E(w) for w in t.split("|"))
    body = f"""<div class="cv"><div class="top"><div class="wm">{E(brand.WORDMARK)}</div><div class="rule"></div></div>
<div class="tb"><h1>{E(p['title'])}</h1><h2>{NB(p['title2_nb']) if p.get('title2_nb') and not wide else E(p['title2'])}</h2><p class="sub">{E(p['sub'])}</p><p class="tag">{E(p['tag'])}</p></div>
<div class="bot"><div class="lab">{E(p.get("label") or "Whitepaper \u00a0%02d" % p["n"])}<small>{E(p['stamp'])}</small></div><div class="ct">{ct}</div></div></div>"""
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{brand.font_face_css()}\n{css % ('file://'+bg)}</style></head><body>{body}</body></html>"

def shot(htmlp, out, w, h, scale):
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
        f"--force-device-scale-factor={scale}", "--allow-file-access-from-files", f"--window-size={w},{h}",
        f"--screenshot={out}", "file://" + htmlp], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

PAPERS = [
 dict(n=1, dir="/workspace/whitepapers/01-ai-for-security-operations/assets", title="Dead Reckoning",
      title2="AI for Security Operations in a Jammed, Spoofed, Watched World",
      sub="Practical, Integrated Steps for Mid-Size Organizations", tag="Trust no single signal.", stamp="October 2026"),
 dict(n=2, dir="/workspace/whitepapers/02-trenches-and-drones/assets", title="Trenches and Drones",
      title2="Network Defense for a War of Attrition",
      sub="Practical, Integrated Steps for Mid-Size Organizations", tag="Dig in. Spread out. Keep going.", stamp="November 2026"),
 dict(n=3, key="special01", label="Special Edition 01", h1w=64, dir="/workspace/whitepapers/special-01-russia-state-influenced-capitalism/assets",
      title="Russia's State-Influenced Capitalism", title2="Sanctions-Proof, War-Proof, and Chaos-Proof", title2_nb="Sanctions-Proof,|War-Proof,|and Chaos-Proof",
      sub="A Model the West Loves to Hate", tag="Raw results. No lectures.", stamp="October 2026"),
]
if __name__ == "__main__":
    want = sys.argv[1:]
    for p in PAPERS:
        if (want and p.get("key") not in want) or (not want and p.get("key")): continue
        d = p["dir"]; os.makedirs(d, exist_ok=True)
        bg1 = contours(1632, 2112, 100 + p["n"], os.path.join(d, "cover-white-bg.png"))
        open(os.path.join(d, "cover-white.html"), "w").write(page_html(p, bg1, False))
        shot(os.path.join(d, "cover-white.html"), os.path.join(d, "cover-white.png"), 816, 1056, 1.5625)
        bg2 = contours(3000, 1000, 300 + p["n"], os.path.join(d, "xarticle-cover-white-bg.png"), levels=22, lw=1.8)
        open(os.path.join(d, "xarticle-cover-white.html"), "w").write(page_html(p, bg2, True))
        shot(os.path.join(d, "xarticle-cover-white.html"), os.path.join(d, "xarticle-cover-white.png"), 1500, 500, 1)
        print("done", d)
