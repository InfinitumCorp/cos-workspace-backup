#!/bin/bash
# Build for Whitepaper 02: Trenches and Drones. RELEASE by default; pass --draft for a draft-marked build (and change --name). Body: src-final.
cd /workspace/whitepapers/tools
/workspace/wpvenv/bin/python build_whitepaper.py \
  --src-dir /workspace/whitepapers/02-trenches-and-drones/src-final \
  --number 2 --title "Trenches and Drones" --title2 "Network Defense for a War of Attrition" \
  --subtitle "Practical, Integrated Steps for Mid-Size Organizations" \
  --tagline "Dig in. Spread out. Keep going." \
  --release-date "November 1, 2026" --date-label "November 2026" \
  --scenarios-note "Scenarios in Part VIII are illustrative and hypothetical. They do not describe any real organization, client or incident." \
  --outdir /workspace/whitepapers/02-trenches-and-drones \
  --name Infinitum-Whitepaper-02-Trenches-and-Drones-RELEASE "$@"
