# Analysis

## Part I: Why an irregular warfare lens

Let me explain why I keep reaching for this framework, and where I stop.

The U.S. Department of Defense's public policy on irregular warfare states that IW is as strategically important as traditional warfare. It describes "irregular" as a deviation from the traditional form of conflict, where actors may use non-traditional methods such as guerrilla warfare, terrorism, sabotage, subversion, criminal activities and insurgency for control of relevant populations (DoDD 3000.07, 2017). The 2020 summary of the Department's Irregular Warfare Annex goes further. It calls IW "a persistent and enduring operational reality," observes that adversaries pursue goals below the threshold of a conventional response, and notes that competitors "have operationalized clandestine criminal activity and predatory economic behavior" (DoD, 2020).

I am not a doctrine scholar, and I am not going to pretend a company's security program is a military campaign. But some of the strategic ideas in those documents transfer cleanly to defending an organization:

- **Adversaries avoid strength and pursue indirect approaches.** The Annex says conventional overmatch pushes adversaries toward indirect approaches that let them achieve objectives without direct confrontation (DoD, 2020). Attackers do exactly this when they skip your hardened core and go through a vendor, a forgotten server, or a help desk.
- **The contest is persistent, not episodic.** The Annex criticizes a "reactive cycle" of investment that rises and falls with crises (DoD, 2020). Security budgets do the same thing after a breach.
- **Unified action is hard and has to be built on purpose.** The Annex states that no single agency has primacy and that "we cannot assume unified action will occur on its own" (DoD, 2020). Inside a company, security, IT, legal, communications and finance often do not act as one unless someone deliberately wires them together.
- **Cost-imposition and denial matter.** The Annex speaks of imposing costs and creating dilemmas for adversaries (DoD, 2020). For a defender, the equivalent is making the easy paths costly and the quick wins disappear.
- **New technology is expected to help.** The Annex says advances in artificial intelligence hold significant potential to transform how information is processed, how trends are understood and how actionable intelligence reaches decision-makers (DoD, 2020). It frames that as part of defeating stealthy, multi-domain campaigns.

That last point is worth pausing on. Even the defense community's own strategy treats AI as a tool for sense-making, meaning faster understanding of a messy environment, rather than as a replacement for judgment. I will take the same approach in this paper.

### What the lens is not

Let me be direct about the guardrails.

- It is not offense. This paper does not describe how to attack anything.
- It is not a license for hype. I will not call a phishing campaign a "war."
- It is not a claim to personal credentials. It is a way of asking better questions.
- It is not a replacement for standard frameworks. I will tie every idea back to NIST, CISA and MITRE, because that is where the common language lives.

With that settled, here are the seven ideas I want to use. For each one I will state the concept, show what the evidence says, and then state what a mid-size defender should do about it.

## Part II: Seven ideas, applied to your security operations

### 1. Persistence: assume the adversary is patient

*Concept.* In irregular contests, the weaker side wins by lasting, not by overwhelming. Time is a weapon.

*Evidence.* The mean time for organizations to identify and contain a breach was 247 days (IBM/Ponemon, 2026). That is eight months. Verizon found KEV vulnerabilities with persistent exploitation detectable on an average of 96% of the days observed, many of them older bugs (Verizon DBIR, 2026). Breaches with lifecycles over 200 days cost USD 5.65 million on average, against USD 4.32 million for shorter ones (IBM/Ponemon, 2026).

*What to do.* Treat dwell time as a first-class metric. Track time-to-detect and time-to-contain the way a finance team tracks cash. And design for the second visit. After you remove an intruder, assume they will test whether you closed the door. Persistence also means the adversary will keep testing the same weaknesses. A KEV-listed vulnerability that sits for 43 days is an invitation that stays open.

*Where AI fits.* Machines do not get tired. They can watch the quiet hours, compare today's behavior to last month's, and surface the one odd login among thousands. That is where AI's staying power can offset the adversary's.

### 2. Deception: expect the message to be the weapon

*Concept.* Irregular adversaries use deception to get others to do the work for them. The goal is to manipulate the target's decisions, not to defeat the target's defenses.

*Evidence.* Verizon found the human element present in 62% of breaches. Social engineering was the third most common breach pattern, at 16% of all breaches. In phishing simulations, successful click rates in mobile-centric vectors, such as voice and text messaging, were 40% higher than via email. Pretexting, where an attacker builds trust through concocted scenarios, reached 6% as an initial access vector in all breaches (Verizon DBIR, 2026). IBM found that voice and SMS phishing was used in 17% of attacks and led to the highest average breach cost among attack vectors, USD 5.29 million, while social engineering such as impersonating help desk staff was used in 13% of attacks and averaged USD 5.23 million (IBM/Ponemon, 2026). IBM also found that AI deepfake or impersonation attacks made up 45% of malicious AI-driven attacks (IBM/Ponemon, 2026).

*What to do.* Verify identity out of band for any request that moves money, changes credentials, or grants access. Make that a rule everyone can invoke without embarrassment, including when "the CEO" is on the other end. Train for voice and text, not just email. Give your help desk a script and the authority to say no. And remember that the FBI's complaint data lists business email compromise at about USD 3.05 billion in 2025 losses (FBI IC3, 2025). These are not exotic attacks. They are persuasion at scale.

*Where AI fits.* AI helps on the receiving end. It can flag unusual sender patterns, summarize suspicious messages for a busy analyst, and cluster similar phishing reports. But NIST's Generative AI Profile warns that generative AI lowers barriers for offensive cyber capabilities and for large-scale information manipulation (NIST AI 600-1, 2024). Assume the adversary has the same tools for polish and volume. That makes process, not intuition, your defense.

### 3. Influence: protect legitimacy, not only systems

*Concept.* Irregular contests are won or lost on legitimacy and influence. The DoD definition puts it at the center: a struggle for legitimacy and influence over the relevant population (DoDD 3000.07, 2017).

*Evidence.* For a company, the "relevant population" is customers, employees, regulators and partners. IBM found that threats to brand reputation, such as public shaming and media leaks, topped the list of ransomware pressure tactics at 41%, ahead of threats involving employee personal data (35%) and intellectual property (31%) (IBM/Ponemon, 2026). ENISA reported that EU audiences faced Foreign Information Manipulation and Interference alongside cyberespionage (ENISA, 2025). NIST's Generative AI Profile lists "information integrity" among its core risks, defined as a lowered barrier to generating content that may not distinguish fact from fiction or may support large-scale disinformation (NIST AI 600-1, 2024).

*What to do.* Add communications and legal to your incident playbook, with a pre-approved holding statement and a named spokesperson. Decide ahead of time how you will tell customers the truth quickly. Put executive impersonation and brand impersonation in your threat model, and agree how staff verify a "message from the top."

*Where AI fits.* AI can help the communications team draft and tailor notices faster, and it can help monitor for spoofed domains or impersonation attempts. It should not publish anything on its own. A confident but wrong statement during an incident is worse than a late one. NIST's term for the underlying problem is *confabulation*, the confident presentation of erroneous content (NIST AI 600-1, 2024).

### 4. Proxies and criminal ecosystems: map the supply chain of the threat

*Concept.* Adversaries work through intermediaries, including criminal groups, to gain deniability and scale. The Annex says competitors have operationalized clandestine criminal activity as part of their approach (DoD, 2020).

*Evidence.* Ransomware appeared in 48% of breaches in Verizon's dataset, and Verizon observed continued third-party growth, with third-party involvement in 48% of breaches (Verizon DBIR, 2026). ENISA called out Phishing-as-a-Service as an industrialization of phishing and noted convergence in the tactics and tools used by different threat groups (ENISA, 2025). IBM found that supply chain breaches were the most expensive factor in increasing breach costs, adding about USD 227,250 on average, and that supply chain compromises took 258 days on average to identify and contain (IBM/Ponemon, 2026).

*What to do.* Do not just defend your network. Map your dependencies: which vendors can reach your data, which software your business cannot run without, which cloud accounts belong to others. Ask for evidence of multifactor authentication and patch performance in contracts. Remember that in Verizon's data, only 23% of third parties had fully remediated missing or improperly secured MFA on their cloud accounts (Verizon DBIR, 2026). Treat the ecosystem as part of your attack surface.

*Where AI fits.* AI can help read vendor questionnaires, compare contract language and summarize third-party risk reports. It can also help correlate activity across your own environment that matches known criminal tooling patterns. It should not decide whether a vendor is safe.

### 5. Attribution: useful for strategy, rarely useful for containment

*Concept.* In gray-zone contests, ambiguity is a feature. Adversaries try to leave you unsure who is behind a campaign, and unsure whether you have a legal or political right to respond.

*Evidence.* ENISA's finding about "faketivism," a term it uses for intrusions in which state-aligned actors employ hacktivist characteristics, and its note on tool overlap between hacktivists and cybercriminals, show how blurry the lines can get (ENISA, 2025). Verizon's coverage of ransomware ecosystems reflects the same pattern of shared services and shifting affiliations (Verizon DBIR, 2026).

*What to do.* Separate three questions that often get blended. First, what is happening, and how do I contain it? Second, how are they doing it, which is where MITRE ATT&CK helps, because it organizes adversary behavior into tactics and techniques regardless of who is behind them (MITRE ATT&CK). Third, who is it, which matters to law enforcement, insurers and public affairs, but should rarely delay containment. Build your detection around behaviors, not names.

*Where AI fits.* AI is good at mapping observed behavior to technique descriptions and at drafting an incident timeline. It is poor at certainty. Treat any attribution suggested by a model as a hypothesis for an analyst to test.

### 6. Resilience: plan to operate while contested

*Concept.* If the adversary can persist, you need to be able to function anyway. The DoD directive notes that activities before, during and after a conflict can shape the environment and serve to deter or prevent war (DoDD 3000.07, 2017). The business parallel is continuity: the ability to keep delivering your essential services while someone is working against you.

*Evidence.* NIST's Cybersecurity Framework 2.0 organizes outcomes into six functions: Govern, Identify, Protect, Detect, Respond and Recover (NIST CSF 2.0, 2024). IBM found that only 42% of breached organizations reported full recovery, and that fewer than one in 20 recovered in under 50 days (IBM/Ponemon, 2026). Among cost factors, IBM listed key lifecycle management tools, encryption, identity and access management and DevSecOps as associated with lower costs, with DevSecOps showing the largest reduction at about USD 253,805 below the global average (IBM/Ponemon, 2026). It also found that 53% of breached organizations did not encrypt sensitive data at rest and in motion at the time of the breach (IBM/Ponemon, 2026).

*What to do.* Test your recovery, not just your backups. Know your minimum viable operations: which systems must run, which can wait. Keep an offline copy of the things you cannot live without. Practice a manual fallback for critical processes. If your AI-assisted tools fail, or are poisoned or unavailable, the team must still be able to do the job without them.

*Where AI fits.* AI can help with recovery planning, for example by drafting runbooks and flagging dependencies. But resilience requires that no single AI service becomes a hidden single point of failure.

### 7. Defense in depth and deterrence by denial: make the easy paths expensive

*Concept.* You rarely win by being invulnerable. You win by making success costly and uncertain, so adversaries move to easier targets. In the DoD framing, this appears as imposing costs and creating dilemmas (DoD, 2020). In security, we call it defense in depth and, in deterrence terms, deterrence by denial.

*Evidence.* IBM's cost factors give a practical menu. Associated with lower average breach costs: DevSecOps (about USD 253,805), identity and access management (USD 225,622), key lifecycle management (USD 214,923), encryption (USD 213,478), offensive security testing such as red teaming and penetration or vulnerability testing (USD 211,339), SOAR tools (USD 210,771), employee training (USD 196,259), endpoint detection and response (USD 177,710), and managed security services (USD 152,929) (IBM/Ponemon, 2026). Those are associations in a benchmark study, not guarantees. But the shape is instructive: no single control dominates. Layers do.

*What to do.* Stack the layers so that each failure is caught by the next. Prioritize the ones that block the most common entry points: patching known-exploited vulnerabilities, strong identity controls, email and messaging protections, segmentation, and tested recovery. Deterrence by denial is not glamorous. It is a thousand small decisions that raise the adversary's cost per attempt.

*Where AI fits.* AI can raise the speed and consistency of each layer, such as triage, prioritization, and enrichment. It is a force multiplier for layers you already have. It is not a substitute for building them.

## Part III: What the evidence says AI does for defenders

Let me turn from the lens to the data. The strongest quantitative evidence I found comes from IBM and Ponemon Institute's 2026 study.

Organizations that used security AI and automation extensively averaged USD 4.00 million per breach. Those using none averaged USD 5.93 million. That is a USD 1.93 million difference, which IBM describes as a nearly USD 400,000 improvement over the prior year's gap. Limited users fell in the middle at USD 5.05 million, a saving of USD 880,000 compared with those using none (IBM/Ponemon, 2026).

Time showed the same pattern. Extensive users identified and contained breaches in 215 days on average. Limited users took 244 days, and organizations with no use took 280 days. That is 65 days faster for extensive users compared with none (IBM/Ponemon, 2026).

Here is the asterisk. These are associations in a benchmark study of organizations that had already been breached. They are not controlled experiments. Organizations that invest in automation may also be better run in other ways. IBM's methodology section is explicit that the sample is nonstatistical and may lean toward organizations with more mature privacy and security programs (IBM/Ponemon, 2026). I take the direction seriously and the exact dollar figure with a grain of salt.

ISC2's survey provides a practitioner view. Professionals ranked AI and automation as the two technologies they expect to have the greatest impact on their ability to secure their organizations. They expected generative AI to help with threat detection, decision-making and cost, and 71% believed it would let them do their jobs more efficiently. At the same time, they expected the largest return on investment to take two or more years to arrive, and 66% did not know enough about generative AI to know what skills they would need (ISC2, 2024).

Notice what that says about the right posture. Practitioners are optimistic and cautious at the same time. That is a healthy combination.

### Why the benefit is plausible

I do not like to rely on a correlation alone, so let me say why I find the benefit plausible. IBM's breach cost analysis shows that detection and escalation, and lost business, are the largest components of cost (IBM/Ponemon, 2026). Both scale with time. Anything that shortens the time between "something odd happened" and "a person understands it" removes cost. AI is, at its best, a time-compression tool for triage, correlation, summarization and prioritization. It does not make the decisions. It shortens the distance to them.

That is also why human oversight is not a courtesy. It is how you keep a faster process from making faster mistakes.
