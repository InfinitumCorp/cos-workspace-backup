# The modern battlefield {#battlefield}

Think of the grind of 1916 fused with technology that looks like science fiction.

Persistent observation. Drones overhead. Satellites watching. Radios jammed. Positions spoofed. A cycle of measure and countermeasure that turns in weeks.

That is my shorthand for the modern battlefield. I use it as a comparison and nothing more. I am not a war correspondent, and this paper is not a military study. I am a security consultant reading public analysis, and asking one question: what does this teach the people who defend organizations?

Here are the ground rules.

This paper draws general lessons about technology and conflict from public sources. It takes no side and makes no claim about any party. I do not assess any state, army or leader. I leave out casualty, loss and performance figures for every side, because they are contested, because they are estimates, and because they are not what a security team needs. I keep the lessons at the level of technology and phenomena: drone saturation, electronic jamming and spoofing, sensor transparency, cheap mass, logistics under observation and decentralized decisions.

The main sources are the CSIS report *War and the Modern Battlefield* (2025) and European and aviation authorities that track interference with satellite navigation. I opened each document I cite. Where a source gives an opinion or a forecast, I say so. And I stay strategic. Nothing here is a tactic, a targeting method or a how-to.

The title of this paper comes from navigation. *Dead reckoning* is what you do when the signal is gone. You know where you were. You know your heading, your speed and how much time has passed. You work out where you are, and you check it against anything else you can trust.

That is the posture I want you to take into security operations. Because the signals you depend on are now being jammed, spoofed and watched.

## Seven lessons

### Lesson 1: Persistence beats brilliance

**What public analysis shows.** CSIS observes that persistent coverage from space assets is making the battlefield more transparent and diminishing strategic surprise (CSIS, 2025b). It adds that this transparency does not by itself guarantee restraint or deterrence (CSIS, 2025b).

That is CSIS. Here is my reading of it. When surprise is hard to achieve, contests drag. The side that can sustain effort over time matters more than the side with one clever move.

**What it means for you.** Your contest is also a long one. IBM and Ponemon Institute put the mean time to identify and contain a breach at 247 days (IBM and Ponemon Institute, 2026). ISC2 found that 67% of respondents reported a staffing shortage and that budget was the top cause of skills gaps (ISC2, 2024). Attrition hits your side too: tired analysts, thinner budgets, a backlog that does not close.

So plan for a campaign, not an incident. Fund the second year, not just the first quarter. Protect your people from burnout the way you protect systems from failure. A team that is exhausted by month six is a position that will not hold.

**Where AI fits.** AI is a way to spend fewer analyst hours on the repetitive work that wears people down. It does not remove the need to staff the line.

### Lesson 2: Cheap mass versus exquisite systems

**What public analysis shows.** CSIS puts the economics in one line: "If a $500 drone can destroy a multimillion-dollar tank, so, too, can a USV swarm destroy a fleet of ships" (CSIS, 2025a). That is an illustration of an asymmetry in cost, not a measurement of how often it happens.

CSIS is also clear that no tool is a magic bullet. In its space chapter it says electronic warfare is not a magic bullet against drones or munitions, because technologies and tactics continue to evolve to mitigate its effects (CSIS, 2025b). Cheap mass invites cheap countermeasures, and the contest goes on.

**What it means for you.** The adversary's cheap mass is phishing kits, automated scanning and commodity ransomware services. ENISA describes Phishing-as-a-Service as automation that "paves the way for attackers regardless of their experience" (ENISA, 2025). IBM puts the imbalance in a sentence: attacks "can be launched for thousands while breaches cost millions" (IBM and Ponemon Institute, 2026).

Most of those attempts fail. A few land. That is the model. You will not stop every attempt. You make the average attempt fail, and you make the successful one small.

Do not answer cheap mass with one exquisite tool. Answer it with layers, and with cheap, repeatable, automated controls that run all day: patching known-exploited vulnerabilities, multifactor authentication, email filtering, segmentation.

**Where AI fits.** This is where AI belongs: cheap mass on your side. Triage, summarization and enrichment at volume, with a person on the decision.

### Lesson 3: You are being watched

**What public analysis shows.** CSIS says forces "must prepare to fight in full view of the enemy," and points to cheap commercial overhead imagery and crowd-sourced intelligence as part of the picture (CSIS, 2025a). In its space chapter, CSIS says military forces, especially those at fixed sites, "must assume that they will be seen and their movements and emissions detected," which calls for renewed emphasis on operational security, deception and spectrum discipline (CSIS, 2025b).

Observation changes behavior. When everything visible can be seen, you decide what is worth showing.

**What it means for you.** Your organization is observed too. MITRE ATT&CK lists Reconnaissance as the first tactic in its enterprise matrix, with techniques such as active scanning and gathering information on victim identity and organization (MITRE ATT&CK). That means adversaries study your internet-facing systems, your staff, your suppliers and your business rhythm before they touch anything.

Work out what is visible. Which systems answer on the internet? Which staff names, roles and email formats are public? Which vendors are named on your website? Then reduce what does not need to be there. Concealment has a place in cyber defense: fewer exposed services, fewer stale accounts, fewer forgotten servers.

Then build your own sensors. Logs are your eyes. If you cannot see your own network, you are the one fighting blind.

**Where AI fits.** AI can help you read the sensors you already have, such as logs, alerts and external exposure data. It cannot help you see what you never collected.

### Lesson 4: Signals can be jammed and spoofed

**What public analysis shows.** CSIS calls electronic warfare one of the most dominant features of the modern battlefield. It describes these systems as a "temporary and reversible" way to attack satellite navigation, communications and surveillance collection, and notes that jamming and spoofing of GPS signals has been detected in several regions around the globe (CSIS, 2025b). CSIS also records daily occurrences of GPS jamming and spoofing in regions such as the Baltic Sea, and says regions outside conflict zones will see more electromagnetic interference (CSIS, 2025b).

The effect reaches civilians. A note to the Council of the European Union from three member states records a dramatic increase since August 2024 in jamming and spoofing of satellite navigation signals for aircraft in the Baltic region, and more frequent interference with signals received by ships since the beginning of 2025. It gives counts of cases by unique aircraft identifier per month, and describes the problem as a threat to aviation and maritime safety (Council of the EU, 2025).

Finland's transport agency said in June 2025 that disruptions in the Gulf of Finland had "already caused near misses," and that spoofing of the Automatic Identification System, which shows where ships are, had become more frequent. It added that other systems are also used to verify ship location and movement (Traficom, 2025). The EU aviation safety agency and the airline association published a joint plan in June 2025 that includes keeping a backup for satellite navigation, with a minimum operational network of traditional navigation aids (EASA, 2025).

Read the last line again. The remedy for spoofed signals is an independent second source.

**Why this reaches your office.** The same Council note says satellite timing services are used to synchronize telecommunication networks and financial transactions, and to stabilize power grids (Council of the EU, 2025). Time is infrastructure. Position is infrastructure. If your systems trust a signal, someone can try to feed them a false one.

Deception works the same way against people. CSIS notes that deepfake video has already appeared in the war, and warns that the next iteration could include deepfake military orders (CSIS, 2025a). IBM found that AI deepfake or impersonation attacks made up 45% of AI-driven attacks, and that voice and SMS phishing led to the highest average breach cost among attack vectors, at USD 5.29 million (IBM and Ponemon Institute, 2026).

**What it means for you.** Do not trust a single signal. Verify out of band. If someone who sounds like your chief executive asks for a payment, call back on a number you already hold. If a log timestamp matters, know where your systems get their time and what happens if it is wrong. If an alert is the only evidence, find a second.

**Where AI fits.** AI can help cross-check signals against each other. It can also be fed bad signals. Treat everything a model reads as untrusted input, and never let one sensor, human or machine, be the only vote.

### Lesson 5: Measure, countermeasure, repeat

**What public analysis shows.** CSIS quotes an analyst describing a "six week learning cycle on the battlefield." As new ways to jam drone signals appear, so do ways around the jamming. CSIS reports drones guided in the final phase of flight to counter jamming, and drones controlled over fiber-optic cables, which are impervious to jamming (CSIS, 2025a). Its space chapter says drone developers have pushed innovation cycles to weeks rather than months or years, and notes that jammers, when radiating, can be detected and located (CSIS, 2025b). Every fix invites the next move.

**What it means for you.** Controls decay. A detection that worked in spring is evaded by autumn. An AI model tuned on last year's alerts drifts as the environment changes. The joint CISA, NSA and FBI guidance on AI data security lists data drift as one of three major data risks for AI systems (CISA et al., 2025).

So schedule the countermeasure cycle. Re-test your detections. Re-run your tabletop exercises. Re-baseline your metrics. Review the AI tools quarterly and ask what the adversary has changed since the last review.

**Where AI fits.** AI helps you adapt faster, if you measure it. Without measurement, it is only a faster way to be wrong.

### Lesson 6: The rear area is not safe

**What public analysis shows.** CSIS expects logistics chains to be in "constant peril," says modern forces need to anticipate that only a fraction of supplies will get through, and expects them to seek self-sufficiency (CSIS, 2025a). CSIS also says the line between combatants and noncombatants will blur, and that civilian providers of power, cloud storage and internet connectivity "could increasingly be seen as legitimate military targets" (CSIS, 2025a). That is a forecast by one think tank, not a legal ruling. In its space chapter, CSIS notes that whether commercial satellites used for military purposes become legitimate targets is an area of active debate (CSIS, 2025b).

The same chapter gives a case of collateral reach. Early in the war, a cyberattack on a commercial satellite communications provider took tens of thousands of satellite modems offline across Central and Eastern Europe. It also knocked out wind turbines and internet access for civilians across Europe (CSIS, 2025b). The target was a commercial provider. The damage reached customers who were nowhere near the fighting.

**What it means for you.** Your supply chain is your rear area. Verizon found third-party involvement in 48% of breaches in its 2026 dataset (Verizon, 2026). The CISA advisory AA24-038A observed that victims included smaller organizations that provide critical services to larger ones (CISA et al., 2024).

Map the dependencies. The attack on one satellite provider reached wind turbines. Which vendors can reach your data? Which cloud, network and identity providers does the business stop without? What happens if one is unavailable for a week? Keep offline copies of what you cannot lose. Keep a manual fallback for what you cannot pause.

**Where AI fits.** Every AI tool is a new supply line, with a vendor, a data path and a failure mode. Add it to the map before you depend on it.

### Lesson 7: Decentralize decisions, protect the network

**What public analysis shows.** CSIS reports that a more decentralized communications model, with multiple dispersed radio nodes and smaller radios, reduces the detectability of signals and makes them harder to jam (CSIS, 2025a). It expects future units to be "highly empowered," with field commanders making decisions about cover, concealment and tactics while minimizing their communications signature, and it says units will need resilient mesh networks so that communications continue "even if multiple nodes go dark" (CSIS, 2025a).

CSIS also names a danger. When both sides have AI-enabled processing, it warns, the incentive will lean toward deferring to the machine. "For now, that surely will lead to mistakes" (CSIS, 2025a).

**What it means for you.** A security operation that needs one person's approval for everything, one tool for everything or one channel for everything will break under pressure. Pre-authorize decisions. Write down who may isolate a system at 3 a.m. and under what conditions. Keep a communications path that does not depend on the systems you are defending. If your email is compromised, how does the incident team talk?

And do not build a static, automated wall and call it done. Automation that never changes is a map the adversary can study. People who can improvise, and who know the plan, are the redundancy.

**Where AI fits.** AI is a node. Design the operation so that losing it degrades the team and does not stop it.

## Where the comparison breaks

I owe you the limits.

No one is shooting at your servers. Your adversary is mostly a criminal crew. The consequences, the law and the ethics are different. Borrowing a lesson is not borrowing a license.

The sources are analyses of an ongoing conflict, written from public data and open reporting. Facts change. The CSIS report was published in September 2025, and the other war-related documents I cite date from 2025. Forecasts are forecasts.

And I am drawing strategic lessons about technology. I am not offering tactics, and I will not.

## Dead reckoning for security operations

When the signal fails, you navigate from what you know. Five parts.

1. **Last known position.** Your baseline and your inventory. What do you own, and what does normal look like?
2. **Heading.** Your priorities. The few exposures and behaviors that matter most, set in advance.
3. **Speed and time.** Your measures: time to detect, time to contain, time to fix. And a trusted source of time.
4. **A second source.** Independent cross-checks. Out-of-band verification. A backup that does not share the same failure.
5. **A fix when you can get one.** Re-verify against the best signal when it returns, and correct your course.

The rest of this paper is the detail. Part I applies the irregular warfare lens. The recommendations give you the sequence.
