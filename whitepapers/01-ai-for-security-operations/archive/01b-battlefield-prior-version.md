# The modern battlefield {#battlefield}

The First World War had trenches, barbed wire, shell craters and stalemate.

This war has all of that. It also has drones overhead, satellites watching, radios jammed, positions spoofed and a six-week cycle of measure and countermeasure.

That is the comparison I keep coming back to. The grind of 1916 with technology that looks like science fiction. I use it as a comparison and nothing more. I am not a war correspondent, and this paper is not a military study. I am a security consultant reading public analysis by people who are, and asking one question: what does this teach the people who defend organizations?

The war I mean is the one in Ukraine. The analysts I rely on are RUSI, CSIS, CNAS and the European institutions that track interference with satellite navigation. I opened each document I cite. Where figures are estimates, I say so. Where sources differ, I say so. And I stay at the strategic level. Nothing here is a tactic, a targeting method or a how-to.

The title of this paper comes from navigation. *Dead reckoning* is what you do when the signal is gone. You know where you were. You know your heading, your speed and how much time has passed. You work out where you are, and you check it against anything else you can trust.

That is the posture I want you to take into security operations. Because the signals you depend on are now being jammed, spoofed and watched.

## Seven lessons

### Lesson 1: Attrition beats brilliance

**What the war shows.** RUSI's assessment of the third year of the war is blunt. Ukraine's approach to defense in depth, and to imposing attrition at longer range, "has made it very costly for Russian forces to make gains," and has limited Russia's ability to build tempo or exploit breaches (RUSI, 2025). RUSI also reports that Russia contracted more than 400,000 additional troops in 2024, and that its forces were often suffering more than 200 personnel killed per day, with over 1,200 casualties per day toward the end of the year (RUSI, 2025). Those are RUSI's figures. They are estimates from one source, and I did not cross-check them against other published estimates. Treat them as indicative.

The shape of it matters more than the number. Neither side can break the other quickly. Both are paying for every meter.

**What it means for you.** Your contest is also a long one. IBM and Ponemon Institute put the mean time to identify and contain a breach at 247 days (IBM and Ponemon Institute, 2026). ISC2 found that 67% of respondents reported a staffing shortage and that budget was the top cause of skills gaps (ISC2, 2024). Attrition hits your side too: tired analysts, thinner budgets, a backlog that does not close.

So plan for a campaign, not an incident. Fund the second year, not just the first quarter. Protect your people from burnout the way you protect systems from failure. A team that is exhausted by month six is a position that will not hold.

**Where AI fits.** AI is a way to spend fewer analyst hours on the repetitive work that wears people down. It does not remove the need to staff the line.

### Lesson 2: Cheap mass versus exquisite systems

**What the war shows.** CNAS found that commercially derived drones are "cheap and plentiful," giving both sides deeper stockpiles of uncrewed aircraft than were previously available (CNAS, 2024). CSIS puts the economics in one line: "If a $500 drone can destroy a multimillion-dollar tank, so, too, can a USV swarm destroy a fleet of ships" (CSIS, 2025a).

Now the caution. RUSI reports that between 60% and 80% of Ukrainian first-person-view drones fail to reach their target, depending on the part of the front and the skill of the operators, and that of those that do, a majority fail to destroy armored vehicles. Yet tactical drones still account for 60 to 70% of damaged and destroyed Russian systems (RUSI, 2025). The officers RUSI spoke to said they still needed artillery, and that drones were most effective in combination with it (RUSI, 2025). CNAS reaches a similar view: drone strikes supplement artillery rather than replace it (CNAS, 2024).

Sources emphasize different things here. CSIS stresses the cost asymmetry. RUSI and CNAS stress that cheap mass works through volume and combination, and that each individual shot often fails. Both can be true.

**What it means for you.** The adversary's cheap mass is phishing kits, automated scanning and commodity ransomware services. ENISA describes Phishing-as-a-Service as automation that "paves the way for attackers regardless of their experience" (ENISA, 2025). IBM puts the imbalance in a sentence: attacks "can be launched for thousands while breaches cost millions" (IBM and Ponemon Institute, 2026).

Most of those attempts fail. A few land. That is the model. You will not stop every attempt. You make the average attempt fail, and you make the successful one small.

Do not answer cheap mass with one exquisite tool. Answer it with layers, and with cheap, repeatable, automated controls that run all day: patching known-exploited vulnerabilities, multifactor authentication, email filtering, segmentation.

**Where AI fits.** This is where AI belongs: cheap mass on your side. Triage, summarization and enrichment at volume, with a person on the decision.

### Lesson 3: You are being watched

**What the war shows.** CNAS concluded that the most consequential mission for drones has been collecting intelligence and obtaining targeting information, not the strikes in the videos (CNAS, 2024). It found that commercial drones make it harder to concentrate forces and achieve surprise, because they give greater visibility into enemy movements beyond the front lines (CNAS, 2024). CSIS says units "must prepare to fight in full view of the enemy," and points to cheap commercial overhead imagery and crowd-sourced intelligence as part of the picture (CSIS, 2025a). RUSI reports that the pervasive threat from fires has pushed units to avoid observation, dig extensively and disperse (RUSI, 2025). CSIS adds that military forces, especially those at fixed sites, "must assume that they will be seen and their movements and emissions detected," which calls for renewed emphasis on operational security, deception and spectrum discipline (CSIS, 2025b). It also says transparency does not guarantee deterrence: despite overwhelming satellite evidence of the buildup, the invasion went ahead (CSIS, 2025b).

Observation changes behavior. When everything visible can be hit, you hide, spread out and decide what is worth showing.

**What it means for you.** Your organization is observed too. MITRE ATT&CK lists Reconnaissance as the first tactic in its enterprise matrix, with techniques such as active scanning and gathering information on victim identity and organization (MITRE ATT&CK). That means adversaries study your internet-facing systems, your staff, your suppliers and your business rhythm before they touch anything.

Work out what is visible. Which systems answer on the internet? Which staff names, roles and email formats are public? Which vendors are named on your website? Then reduce what does not need to be there. Concealment has a place in cyber defense: fewer exposed services, fewer stale accounts, fewer forgotten servers.

Then build your own sensors. Logs are your eyes. If you cannot see your own network, you are the one fighting blind.

**Where AI fits.** AI can help you read the sensors you already have, such as logs, alerts and external exposure data. It cannot help you see what you never collected.

### Lesson 4: Signals can be jammed and spoofed

**What the war shows.** CSIS calls electronic warfare one of the most dominant features of the modern battlefield, aimed at eroding the effectiveness of drones and other precision munitions by targeting satellite navigation, communications and surveillance collection. It describes these systems as a "temporary and reversible" way to attack those signals, and notes widespread jamming and spoofing of GPS signals detected in Israel, along Russia's western borders and elsewhere around the globe (CSIS, 2025b). CSIS also records that observers have tracked daily occurrences of GPS jamming and spoofing in regions such as the Baltic Sea, and that regions outside conflict zones will see more electromagnetic interference (CSIS, 2025b). The effect is not limited to the front. A note to the Council of the European Union from Lithuania, Estonia and Finland records that since August 2024 a dramatic increase in jamming and spoofing of satellite navigation signals for aircraft has been recorded in the Baltic region, and that interference with signals received by ships has also been observed more frequently since the beginning of 2025. The note gives counts of cases, for example in Poland from 1,908 in October 2024 to 2,732 in January 2025, by unique ICAO identifier per month. It describes the interference as systematic and deliberate, which is the view of the three states that wrote it (Council of the EU, 2025).

Finland's transport agency warned in June 2025 that disruptions in the Gulf of Finland had "already caused near misses," and that spoofing of the Automatic Identification System, which shows where ships are, had become more frequent. It added that other systems are also used to verify ship location and movement (Traficom, 2025). The EU aviation safety agency and the airline association published a joint plan in June 2025 that includes keeping a backup for satellite navigation, with a minimum operational network of traditional navigation aids (EASA, 2025).

Read the last line again. The remedy for spoofed signals is an independent second source.

**Why this reaches your office.** The same Council note says satellite timing services are used to synchronize telecommunication networks and financial transactions, and to stabilize power grids (Council of the EU, 2025). Time is infrastructure. Position is infrastructure. If your systems trust a signal, someone can try to feed them a false one.

Deception works the same way against people. CSIS records that in March 2022 a deepfake video of the Ukrainian president appearing to surrender was released, and it warns that the next iteration could include deepfake military orders (CSIS, 2025a). IBM found that AI deepfake or impersonation attacks made up 45% of AI-driven attacks, and that voice and SMS phishing led to the highest average breach cost among attack vectors, at USD 5.29 million (IBM and Ponemon Institute, 2026).

**What it means for you.** Do not trust a single signal. Verify out of band. If someone who sounds like your chief executive asks for a payment, call back on a number you already hold. If a log timestamp matters, know where your systems get their time and what happens if it is wrong. If an alert is the only evidence, find a second.

**Where AI fits.** AI can help cross-check signals against each other. It can also be fed bad signals. Treat everything a model reads as untrusted input, and never let one sensor, human or machine, be the only vote.

### Lesson 5: Measure, countermeasure, repeat

**What the war shows.** CSIS quotes RUSI's Nick Reynolds describing a "six week learning cycle on the battlefield." As each side found new ways to jam drone signals, the other found ways around the jamming. CSIS reports drones guided in the final phase of flight to counter jamming, and drones controlled over fiber-optic cables, which are impervious to jamming (CSIS, 2025a). RUSI adds the trade-off: wired control links have downsides, including degraded flight performance, limited range of approximately 10 km and the risk of entanglement (RUSI, 2025). Every fix has a cost, and every fix invites the next move.

**What it means for you.** Controls decay. A detection that worked in spring is evaded by autumn. An AI model tuned on last year's alerts drifts as the environment changes. The joint CISA, NSA and FBI guidance on AI data security lists data drift as one of three major data risks for AI systems (CISA et al., 2025).

So schedule the countermeasure cycle. Re-test your detections. Re-run your tabletop exercises. Re-baseline your metrics. Review the AI tools quarterly and ask what the adversary has changed since the last review.

**Where AI fits.** AI helps you adapt faster, if you measure it. Without measurement, it is only a faster way to be wrong.

### Lesson 6: The rear area is not safe

**What the war shows.** RUSI reports that Ukrainian brigades take approximately 50% of their casualties in the rear, from drones, artillery and glide bombs, and that resupply, rotation and evacuation have all become major challenges because they put people and vehicles in the open (RUSI, 2025). The first adaptation was to minimize the number of rotations. CSIS expects logistics chains to be in "constant peril," says modern armies need to anticipate that only a fraction of supplies will get through, and expects forces to seek self-sufficiency (CSIS, 2025a).

The war's first shot also fell on a commercial network. CSIS records that on February 24, 2022, hours before the ground invasion, a cyberattack on a commercial satellite communications provider took tens of thousands of satellite modems offline across Central and Eastern Europe. It disrupted Ukrainian military communications, and it also knocked out wind turbines and internet access for civilians across Europe (CSIS, 2025b). The target was a commercial provider. The damage reached customers who were nowhere near the war.

CSIS adds a point for any company that sells to governments or depends on commercial infrastructure. It says the line between combatants and noncombatants will blur, and that civilian providers of power, cloud storage and internet connectivity "could increasingly be seen as legitimate military targets" (CSIS, 2025a). That is a forecast by one think tank, not a legal ruling. In its space chapter, CSIS notes that whether commercial satellites used for military purposes become legitimate targets is an area of active debate, and that Russian officials have made statements suggesting they consider such systems valid targets (CSIS, 2025b). Either way, it tells you how analysts see the terrain.

**What it means for you.** Your supply chain is your rear area. Verizon found third-party involvement in 48% of breaches in its 2026 dataset (Verizon, 2026). The CISA advisory on Volt Typhoon observed that victims included smaller organizations that provide critical services to larger ones (CISA et al., 2024).

Map the dependencies. The attack on one satellite provider reached wind turbines. Which vendors can reach your data? Which cloud, network and identity providers does the business stop without? What happens if one is unavailable for a week? Keep offline copies of what you cannot lose. Keep a manual fallback for what you cannot pause.

**Where AI fits.** Every AI tool is a new supply line, with a vendor, a data path and a failure mode. Add it to the map before you depend on it.

### Lesson 7: Decentralize decisions, protect the network

**What the war shows.** CSIS reports that Ukraine adopted a more decentralized communications model, using multiple dispersed radio nodes and smaller radios to reduce the detectability of its signals and make them harder to jam (CSIS, 2025a). It expects future units to be "highly empowered," with field commanders making decisions about cover, concealment and tactics while minimizing their communications signature, and it says units will need resilient mesh networks so that communications continue "even if multiple nodes go dark" (CSIS, 2025a). RUSI reports that one brigade held a 27 km frontage with just four battalions, with low density made up for in depth (RUSI, 2025).

CSIS also names the danger on the other side of the ledger. Israel's technology-heavy border defenses failed on October 7, 2023. In CSIS's words, the attackers "knew how to dismantle static, automated systems" (CSIS, 2025a). And when both sides have AI-enabled processing, CSIS warns, the incentive will lean toward deferring to the machine. "For now, that surely will lead to mistakes" (CSIS, 2025a).

**What it means for you.** A security operation that needs one person's approval for everything, one tool for everything or one channel for everything will break under pressure. Pre-authorize decisions. Write down who may isolate a system at 3 a.m. and under what conditions. Keep a communications path that does not depend on the systems you are defending. If your email is compromised, how does the incident team talk?

And do not build a static, automated wall and call it done. Automation that never changes is a map the adversary can study. People who can improvise, and who know the plan, are the redundancy.

**Where AI fits.** AI is a node. Design the operation so that losing it degrades the team and does not stop it.

## Where the comparison breaks

I owe you the limits.

No one is shooting at your servers. Your adversary is mostly a criminal crew, not an army. The consequences, the law and the ethics are different. Borrowing a lesson is not borrowing a license.

The sources are about one war and the conflicts around it. They are analyses written from interviews, public data and open reporting during an ongoing conflict. Facts change. RUSI's account covers 2024. CSIS's covers events to mid-2025. Casualty and equipment figures are estimates, and the parties dispute them.

The sources also disagree on emphasis. Some stress the revolution in drones. Others stress that artillery and combined arms still matter. I have tried to say which is which.

And I am drawing strategic lessons. I am not offering tactics, and I will not.

## Dead reckoning for security operations

When the signal fails, you navigate from what you know. Five parts.

1. **Last known position.** Your baseline and your inventory. What do you own, and what does normal look like?
2. **Heading.** Your priorities. The few exposures and behaviors that matter most, set in advance.
3. **Speed and time.** Your measures: time to detect, time to contain, time to fix. And a trusted source of time.
4. **A second source.** Independent cross-checks. Out-of-band verification. A backup that does not share the same failure.
5. **A fix when you can get one.** Re-verify against the best signal when it returns, and correct your course.

The rest of this paper is the detail. Part I applies the irregular warfare lens. The recommendations give you the sequence.
