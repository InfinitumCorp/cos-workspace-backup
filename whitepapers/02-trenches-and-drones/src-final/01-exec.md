<!-- BODY-START -->

# Executive summary {#executive-summary}

By William Aaron Turner, Founder and President, Infinitum Corporation.

Nobody wins this fight in a day.

That is the first thing to understand about defending a network. The contest is not one big battle. It is a long grind of small, cheap, constant pressure. Scans that never stop. Phishing waves that arrive in bursts. Floods of junk traffic that last nine minutes and come back tomorrow. A device at the edge of your network that has been waiting for a patch for six weeks.

Attrition is the right word for it. Attrition means wearing the other side down. It is a contest of cost, endurance and replacement. The side that can absorb losses, repair, adapt and keep operating outlasts the side that cannot.

This paper is about how a mid-size organization stays in that contest. It is a practical look at network defense when the pressure is persistent, automated and cheap for the people applying it.

I read security problems through one lens: irregular warfare. That is the study of how states and other groups compete through indirect, non-attributable or asymmetric means, and how to counter them. Joint doctrine says irregular warfare "seeks to create dilemmas and increase risk and costs to adversaries" (JP 1 Vol 1, 2023, as quoted in U.S. Army CALL, 2025). You don't need to care about doctrine to benefit from it. You only need to notice that the people working against your network behave the way it describes.

Then add the picture public analysts paint of the modern battlefield. My shorthand for it: trench-style grind fused with science fiction. Defense in depth and dug-in positions. Cheap drones in huge numbers. Jammed and spoofed signals. Sensors everywhere. Supply lines under constant observation (CSIS, 2025a; CSIS, 2025b; CSIS, 2025c).

That is a comparison, not a claim that your network is a front line. Nobody is shooting at your servers. **This paper draws general lessons about technology and conflict from public sources. It takes no side and makes no claim about any party.** It leaves out casualty, loss and performance figures for every side, because they are contested and because a security team does not need them. The lessons sit at the level of technology and phenomena, and each one comes back to a decision you can make on Monday.

## Five fronts, one war

The paper walks through five fronts. Each pairs a feature of the modern battlefield, as public sources describe it, with the same feature on your network.

- **Trenches: depth.** CSIS says defenders who can dig in with effective counter-drone measures hold a significant advantage over those who must cross open land (CSIS, 2025a). On a network, that means segmentation, identity checks at every line, and an implicit trust zone kept "as small as possible" (NIST SP 800-207, 2020).
- **Drones: cheap mass.** CSIS puts the economics in one line: "If a $500 drone can destroy a multimillion-dollar tank, so, too, can a USV swarm destroy a fleet of ships" (CSIS, 2025a). Your version is automated scanning, credential stuffing and flood traffic. In Verizon's data, the median breached entity facing distributed denial of service (DDoS) contended with 17 distinct attacks over a year, and half of all attacks lasted less than nine minutes (Verizon, 2026).
- **Electronic warfare: trust under attack.** Jamming and spoofing target the signals that machines trust. IATA data, cited in a joint release with the European aviation regulator EASA, shows GPS signal loss events up 220% between 2021 and 2024 (EASA and IATA, 2025). Your network has signals too: time sources, name resolution, identities, voices on the phone. NIST lists logging software and certificate management among the things that depend on synchronized time (NIST IR 8323r1, 2023).
- **Sensors: you are watched.** CSIS says forces "must assume that they will be seen and their movements and emissions detected" (CSIS, 2025b). Assume the same about your internet-facing surface. Edge devices act as boundaries, and unsecured, they make it easier for "even unskilled malicious cyber actors" (NSA, 2025).
- **Supply lines: the rear is not safe.** CSIS warns that logistics chains "will be in constant peril" (CSIS, 2025a). IBM found supply chain compromise was the second most common initial attack vector in breaches it studied, and that those breaches took 258 days on average to identify and contain (IBM and Ponemon Institute, 2026).

## What the evidence says

Three findings stand out.

First, the pressure is constant, and mostly cheap. ENISA analyzed 4,875 incidents in the EU over a twelve-month period. DDoS made up 77% of reported incidents. Only 2% of the hacktivism incidents, which were primarily low-impact DDoS, resulted in service disruption (ENISA, 2025). Cheap does not mean harmless, and it does not mean pointless. It means the attacker is spending your attention.

Second, the real damage comes from gaps that stay open. Verizon found only 26% of known-exploited vulnerabilities in its dataset were fully remediated, down from 38% the year before, and the median time to fully patch rose to 43 days from 32 (Verizon, 2026). In its analysis of small and medium-sized businesses, Verizon says many ransomware attacks are opportunistic, and victims were hit because they had compromised credentials (38%) or unpatched vulnerabilities in edge devices (29%) (Verizon, 2026).

Third, endurance is a cost. IBM reports the global average cost of a data breach reached a record USD 4.99 million, and the mean time to identify and contain a breach rose to 247 days. Breaches with lifecycles longer than 200 days cost more on average than shorter ones (USD 5.65 million against USD 4.32 million) (IBM and Ponemon Institute, 2026). Every day an intruder spends inside your lines is a day you pay for.

## What to do

The recommendations come in seven moves, built to be sequenced by a team of a few people.

1. **Map the ground.** Inventory your edge, your crown assets and your dependencies. You cannot defend what you cannot see.
2. **Dig in.** Build depth: segmentation, per-session access, phishing-resistant authentication, and a small implicit trust zone.
3. **Close the cheap doors.** Patch known-exploited vulnerabilities on the edge first. Put DDoS protection and automation where the volume is.
4. **Keep a second source.** Verify out of band. Run more than one trusted time source. Test what happens when the primary fails.
5. **Reduce your signature.** Shrink what the internet can see. Build your own sensors. Place decoys with legal sign-off.
6. **Plan for the rear to burn.** Map suppliers and platforms. Keep offline copies and manual fallbacks that you have actually rehearsed.
7. **Decentralize the decisions.** Write down who may act without asking. Keep a comms channel that does not depend on the network you are defending. Share lessons within hours, not months.

None of these moves needs a miracle product. All of them need a campaign mindset: staffing for year two, measuring against your own baseline, and testing the plan until the plan breaks in a rehearsal instead of a real incident.

This paper includes a 30/60/90-day plan, a 12-month roadmap, a 30-item self-assessment, and three illustrative scenarios that are hypothetical and say so.

Every figure in this paper belongs to the source cited. I make no claim about the results any organization will achieve. Don't take my word for it. Read the sources, then decide.
