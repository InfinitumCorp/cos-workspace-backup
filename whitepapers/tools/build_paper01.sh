#!/bin/bash
# Build for Whitepaper 01: Dead Reckoning. RELEASE by default; pass --draft for a draft-marked build (and change --name). Body: src-final.
cd /workspace/whitepapers/tools
/workspace/wpvenv/bin/python build_whitepaper.py \
  --src-dir /workspace/whitepapers/01-ai-for-security-operations/src-final --patches paper01_patches.json \
  --number 1 --title "Dead Reckoning" --title2 "AI for Security Operations in a Jammed, Spoofed, Watched World" \
  --subtitle "Practical, Integrated Steps for Mid-Size Organizations" \
  --tagline "Trust no single signal." \
  --outdir /workspace/whitepapers/01-ai-for-security-operations \
  --name Infinitum-Whitepaper-01-Dead-Reckoning-RELEASE "$@"
