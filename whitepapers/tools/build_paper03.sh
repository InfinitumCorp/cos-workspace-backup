#!/bin/bash
# Build for Whitepaper 03: Break It Before They Do. RELEASE-mode candidate by default (release date Nov 8, 2026);
# pass --draft for a draft-marked build (and change --name). Body: 03-break-it-before-they-do/src-final.
# Page 1 is replaced with GraphicDesign Bot's full-bleed cover (assets/cover-v2-white.jpg) after the build.
set -e
P=/workspace/whitepapers/03-break-it-before-they-do
NAME=${NAME:-Infinitum-Whitepaper-03-Break-It-Before-They-Do-RELEASE-candidate}
COVER=${COVER:-$P/assets/cover-v2-white.jpg}
cd /workspace/whitepapers/tools
/workspace/wpvenv/bin/python build_whitepaper.py \
  --src-dir $P/src-final \
  --number 3 --title "Break It Before They Do" --title2 "Authorized Hacking for Organizations Under Siege" \
  --subtitle "Practical, Integrated Steps for Mid-Size Organizations" \
  --tagline "Find the weak stretch first." \
  --release-date "November 8, 2026" --date-label "November 2026" \
  --scenarios-note "Scenarios in Part VIII are illustrative and hypothetical. They do not describe any real organization, client or incident." \
  --outdir $P --name $NAME "$@"
/workspace/wpvenv/bin/python - "$P/$NAME" "$COVER" <<'PY'
import sys, io, re, os
from PIL import Image
import pypdf
base, cover = sys.argv[1], sys.argv[2]
# 1) PDF: swap generated page 1 for the full-bleed JPG cover at Letter size (612x792 pt)
im = Image.open(cover).convert("RGB")
buf = io.BytesIO(); im.save(buf, "PDF", resolution=200.0); buf.seek(0)
cov = pypdf.PdfReader(buf).pages[0]
cov.scale_to(612, 792)
r = pypdf.PdfReader(base + ".pdf"); w = pypdf.PdfWriter()
w.add_page(cov)
for p in r.pages[1:]: w.add_page(p)
w.add_metadata(r.metadata or {})
with open(base + ".pdf", "wb") as f: w.write(f)
# 2) HTML: replace generated cover block with the image cover
h = open(base + ".html").read()
rel = os.path.relpath(cover, os.path.dirname(base))
h2 = re.sub(r'<div class="cv">.*?(?=<section class="legal">)', f'<div class="cv"><img src="{rel}" alt="Whitepaper No. 3 cover: Break It Before They Do" style="display:block;width:8.5in;height:11in;object-fit:cover"/></div>', h, count=1, flags=re.S)
open(base + ".html", "w").write(h2)
print("cover swapped:", cover, "pages:", len(w.pages))
PY
