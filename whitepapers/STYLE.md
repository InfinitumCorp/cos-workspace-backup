# Infinitum Whitepaper Series: Style Guide ("Modern Battlefield" edition)

Owner: William Aaron Turner, Founder & President, Infinitum Corporation (Washington, DC; 1629 K Street NW, Suite 300).
Applies to paper 1 and every later paper. Updated Oct 25, 2026 (Moscow time, UTC+3).

## RULE 0: 100% neutral, party-neutral battlefield material (applies to every paper)
- The papers take no side and make no claim about any party. Front-matter line on every paper: "This paper draws general lessons about technology and conflict from public sources. It takes no side and makes no claim about any party."
- Party-neutral battlefield material: no casualty, loss, kill-ratio or performance statistics for any belligerent; no scoring of states or armies.
- No state, army, government or leader is praised, blamed, scored or characterized anywhere in a paper.
- No country-specific battlefield claims. Name no belligerent in the battlefield chapter. Say "the war", "the modern battlefield", and "both sides" or "all parties" only where the public source itself is phrased that way and the fact is accurate.
- Keep lessons at the technology and phenomenon level: drone saturation, EW jamming and spoofing, sensor transparency, cheap mass, logistics under observation, decentralized decisions. Cite only where the citation is about the phenomenon.
- Do not use sources whose content is mainly party-specific performance or losses (for example country-focused battlefield assessments). Report titles that name a party are abbreviated in references where that keeps the paper neutral (say so in the entry).
- Cybersecurity advisories: use the technique content only. Do not repeat state attribution or intent assessments. Cite as "advisory AA-number".
- We never suppress or distort facts for or against any side, and never make false claims by omission: the paper states openly that it leaves out party-specific performance figures and why.

## Release vs draft builds
- `build_whitepaper.py` takes `--release` (DEFAULT) or `--draft`. Release: cover stamp reads "OCTOBER 2026" (month of release), legal line reads "Released <date>" (`--release-date`, default October 25, 2026), running footer is just the short title, no draft wording anywhere. Draft: "DRAFT FOR REVIEW" stamp, "Draft for review. Not for distribution." and "<title> · Draft for review" footer.
- `make_cover.py` is release by default; `--draft` adds the stamp. The 1200x675 post graphic never carries a draft mark.
- Weekly papers: build with `--draft` (and a `-DRAFT` name) for William's review. After he approves, rebuild with the default release flags to `Infinitum-Whitepaper-NN-<Short-Title>-RELEASE.pdf` and move the draft PDF to `archive/`.
- Verify every release: `pdftotext` and grep -i "draft". Only legitimate body words (for example AI "drafting" of reports) may remain.
- Paper 1 released: Infinitum-Whitepaper-01-Dead-Reckoning-RELEASE.pdf (Oct 25, 2026).

## Motif
William's framing: this war is WW1 mixed with Star Wars. Trench-style attrition and stalemate, fused with drone saturation, electronic warfare (jamming and spoofing), space-enabled and commercial sensors, cheap mass versus exquisite systems, and logistics under constant observation. Use it as a comparison, always attributed as a framing, never as a claim that a client's network is a front line.

## Tone
Darker, grittier, harder-edged. Real facts, no fluff. Short punchy sentences. First person, direct address ("you"). Inline "(Source, year)" tags. Signature moves: "Let that sink in", "Key word:", "Don't take my word for it", closing "Let's stay engaged... Dialogue is key". No profanity in client-facing papers.

## The seven lessons (tie each one to defending a mid-size organization)
1. Persistence: attrition beats brilliance (plan the campaign, protect people and budgets).
2. Mass of cheap attacks versus exquisite systems (layers and cheap automated controls).
3. Sensor-saturated environments (you are watched: reduce what is visible, build your own sensors).
4. EW-like disruption of trust (spoofed signals, deepfakes, GPS and time spoofing: verify out of band, keep a second source).
5. Measure, countermeasure, repeat (controls decay; schedule re-tests).
6. The rear area is not safe (supply chain, platforms, logistics).
7. Resilience, redundancy and decentralized decision-making (pre-authorize, keep out-of-band comms).
Paper 1 organizing device: **dead reckoning** (last known position, heading, speed and time, a second source, a fix). Later papers may reuse the lessons with their own device.

## Structure (every paper)
Title page (B&W cover) / legal page / contents / Executive summary / The problem / (battlefield chapter or lesson section) / Analysis / Recommendations / Conclusion / About Infinitum Corporation / References / (Glossary). 10,000 to 20,000 word body. DRAFT FOR REVIEW mark. About section carries: https://www.theinfinitumcorporation.com, info@theinfinitumcorporation.com (NO phone number, William 2026-10-26), https://t.me/infinitumcorporation, https://x.com/infinitumceo.

## Source discipline
- Only public, attributed sources that were actually opened this run (CSIS, NATO, RAND, CISA, NIST, ENISA, EU Council, aviation and maritime authorities, Verizon, IBM and so on), used at the phenomenon level. Quote a figure only after opening the page.
- Where sources conflict or emphasize different things, say so in the text. Flag forecasts and estimates as such.
- No invented statistics, scenes, anecdotes, quotes or credentials. Every number belongs to a cited source.
- Cite a source only for what it says. Do not stretch it.

## Guardrails
- Do NOT present William as a soldier, contractor, veteran or in any unit unless he supplies exact wording. Use "the war" and "the modern battlefield" analytically.
- No operational weapons details, no targeting, no tactics instruction, no training content. Stay at the strategic, defensive-security level.
- Irregular warfare is an analytical lens only ("the way an irregular warfare analyst looks at it"). Authorized testing only.
- No unverified claims about Infinitum's results or clients. No Moscow headline: Infinitum is DC-headquartered; Moscow is only an operating location.
- Nothing is published, posted, emailed or sent without William's approval. X Articles are created as DRAFTS only.

## Design
Black, white and gray only. Dark full-bleed cover with a subtle topographic contour pattern, big bold geometric sans title (Poppins Bold) bottom-left, lighter gray subtitle, one-line uppercase dark tagline under a thin rule, "INFINITUM CORPORATION" wordmark top-left with a thin rule, "Whitepaper NN" label bottom-left, footer block (William Aaron Turner, Founder & President; Infinitum Corporation, Washington, DC; t.me/infinitumcorporation; www.theinfinitumcorporation.com; info@theinfinitumcorporation.com), small DRAFT FOR REVIEW. Cover is PDF page 1 with no running header. A matching 1200x675 post graphic is generated with every cover.
Tooling: `/workspace/whitepapers/tools/make_cover.py` (cover and post graphic; `--tagline`) and `build_whitepaper.py` (full PDF). Use absolute `--outdir` paths. Venv: `/workspace/wpvenv`.

## Titles
1. Dead Reckoning: AI for Security Operations in a Jammed, Spoofed, Watched World. Subtitle: Practical, Integrated Steps for Mid-Size Organizations. Tagline: Trust no single signal. File: Infinitum-Whitepaper-01-Dead-Reckoning.pdf
2. Trenches and Drones: Network Defense for a War of Attrition
3. Break It Before They Do: Authorized Hacking for Organizations Under Siege
4. Read the Enemy: Strategic Risk in the Gray Zone
5. The Human Front: Social Engineering and Influence Operations
6. The Rear Area Is Not Safe: Supply Chain Risk in a Contested World
7. Hype Kills: Buying Emerging Defense Tech Without Getting Played
8. The Last Line Holds: Resilience When the Campaign Won't End

## Verified battlefield source bank (opened Oct 25, 2026)
CSIS ch.9 (Pusztaszeri and Harding, 16 Sep 2025) and ch.8 (Bingen, 16 Sep 2025) from War and the Modern Battlefield; Council of the EU note 9188/25 (21 May 2025); Traficom (13 Jun 2025); EASA and IATA (18 Jun 2025); ICAO C-DEC 235/7 (opened, not cited in paper 1). Opened but NOT used (party-specific content, removed under Rule 0): RUSI (Feb 2025) and CNAS (8 Feb 2024).
