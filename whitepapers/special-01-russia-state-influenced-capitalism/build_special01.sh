#!/bin/bash
# Build for Special Edition 01: Russia's State-Influenced Capitalism. RELEASE by default; pass --draft for a draft-marked build.
cd /workspace/whitepapers/tools
/workspace/wpvenv/bin/python build_whitepaper.py \
  --src-dir /workspace/whitepapers/special-01-russia-state-influenced-capitalism/src-final \
  --number 3 --edition-label "Special Edition 01" \
  --title "Russia's State-Influenced Capitalism" --title2 "Sanctions-Proof, War-Proof, and Chaos-Proof" \
  --subtitle "A Model the West Loves to Hate" \
  --tagline "Raw results. No lectures." \
  --release-date "October 2026" --date-label "October 2026" \
  --neutrality-note "<strong>Author's position.</strong> This paper presents the author's argued position. Figures are attributed to the sources cited." \
  --scenarios-note "Where sources disagree with each other or with a commonly repeated figure, the paper says so. Scenarios in the Outlook chapter are illustrative and are not predictions." \
  --legal-scope "This paper is an economic analysis written for decision makers. It takes a position, in the author's voice, and it does not address military operations, casualty figures or the conduct of any party in any conflict. Nothing in it is a guide to circumventing sanctions, export controls or any other law, and any use of it should comply with the laws that apply to the reader." \
  --disclaimer "This whitepaper is provided for general information only. It is not legal, investment, regulatory or professional advice for any specific situation, and it does not create a client relationship. Statistics are taken from the public sources cited and remain the property of their publishers. Sources are named in the text and listed in the references, and figures may be revised by their publishers. Infinitum Corporation makes no promise or guarantee about any business, investment or policy outcome." \
  --outdir /workspace/whitepapers/special-01-russia-state-influenced-capitalism \
  --name Infinitum-Whitepaper-Special-01-Russia-State-Influenced-Capitalism-RELEASE "$@"
