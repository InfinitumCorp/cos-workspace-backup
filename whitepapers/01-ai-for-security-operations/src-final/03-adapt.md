## Part II: Adversary adaptation {#part-ii}

Irregular actors adapt. That is close to the definition of the term.

They adapt to your defenses, to your politics, to your budget cycle and to your tools. When you close one door, they test the next. When a technique becomes noisy, they replace it with a quieter one.

AI accelerates that loop. To see what adaptation looks like in a real, publicly documented case, let's look at a joint cybersecurity advisory from U.S. and partner agencies.

### A worked example: persistence in critical infrastructure

In February 2024, CISA, the National Security Agency and the FBI, joined by partner agencies, published joint advisory AA24-038A on a persistent-access campaign against critical infrastructure networks (CISA et al., 2024).

I use this advisory as a teaching case because it is public, detailed and authoritative. I use it as a source on techniques only. I do not assess any government or group, and I leave out the advisory's attribution. I will stay at the level of strategy and defense. The advisory itself contains the technical detail defenders need.

Here is what the authoring agencies said, in summary.

They observed indications of the actors "maintaining access and footholds within some victim IT environments for at least five years" (CISA et al., 2024).

And they noted that "some victims are smaller organizations with limited cybersecurity capabilities that provide critical services to larger organizations or key geographic locations" (CISA et al., 2024).

Let that sink in. Five years. Smaller organizations. Exposed because of who and what they connect to.

### Reading the case through the lens

Now apply the six features from Part I.

**Thresholds.** The advisory describes heavy use of living-off-the-land techniques, meaning the use of tools already built into the operating system, together with valid accounts and strong operational security, which combined "allows for long-term undiscovered persistence" (CISA et al., 2024). In some instances, the agencies note, the actors may have avoided using compromised credentials outside normal working hours to avoid triggering alerts. That is threshold management in its purest form.

**Ambiguity.** The advisory notes that conventional indicators of compromise are generally lacking for this kind of activity, which complicates defenders' efforts to identify, track and categorize it (CISA et al., 2024). No malware signature to match. Behavior that looks like administration.

**Proxies.** The advisory reports that the actors used multi-hop proxies, including virtual private servers and end-of-life small office and home office routers, to support their operations (CISA et al., 2024). Borrowed infrastructure. Somebody else's equipment.

**Asymmetry.** The advisory says the actors commonly gained initial access by exploiting known or zero-day vulnerabilities in public-facing network appliances, often using publicly available exploit code for known vulnerabilities (CISA et al., 2024). That is cheap for the attacker and expensive for the defender who has to find and fix every exposed device.

**Resilience.** The incident response guidance in the advisory includes planning for how to keep operating if access to or control of IT or operational technology is lost, and regularly testing manual controls (CISA et al., 2024). The agencies are planning for degraded operations, not just for detection.

### What the defenders were told to do

The advisory's list of actions to take today is short and almost boring (CISA et al., 2024):

1. Apply patches for internet-facing systems, prioritizing critical vulnerabilities in appliances known to be frequently exploited.
2. Implement phishing-resistant multifactor authentication.
3. Ensure logging is turned on for application, access and security logs, and store logs in a central system.
4. Plan "end of life" for technology beyond the manufacturer's supported lifecycle.

Not one of those actions requires AI.

That is the first lesson of this case. Fundamentals beat novelty. An AI program built on top of unpatched edge devices, weak authentication and missing logs is decoration.

The second lesson is subtler. The advisory says many organizations "lack security and network management best practices (such as established baselines) that support detection of malicious LOTL activity," which "makes it difficult for network defenders to discern legitimate behavior from malicious behavior and conduct behavior analytics, anomaly detection, and proactive hunting" (CISA et al., 2024).

That is precisely the kind of problem where AI-assisted analysis may help, if, and only if, the logs exist and someone has defined what normal looks like.

### Sharing as a defensive multiplier

One more lesson from the advisory is easy to overlook. Its incident response guidance includes reporting compromises to the authoring agencies and considering sharing technical information with an authoring agency or a sector-specific information sharing and analysis center (CISA et al., 2024).

That matters for the irregular warfare lens. An adversary operating across many victims sees patterns that no single victim can see. Each defender, alone, sees one fragment. Sharing reverses that asymmetry. When defenders pool what they observe, the adversary's breadth becomes a liability rather than an advantage, because the same behavior seen in many places becomes easier to recognize everywhere.

NATO makes the same point at the alliance level, describing how it "continuously gathers, shares and assesses information in order to detect and attribute any ongoing hybrid activity" (NATO, 2026).

For a mid-size organization, sharing does not require a classified relationship. It can be as simple as membership in a sector information-sharing group, a relationship with a regional law-enforcement contact, and a habit of reading and acting on public advisories. AI can help here too. Summarizing a long advisory into the three checks your team must run this week is exactly the kind of task it handles well, as long as a person verifies the summary against the original.

### Watching your own adaptation

Adaptation runs both ways, and defenders are often slower than they think.

A useful exercise, borrowed from the habit of after-action review in irregular warfare analysis, is to ask after every significant incident or exercise: what did the adversary do that we did not expect, and what will we change because of it? If the honest answer is "nothing," you are not adapting. You are repeating.

Write down the answer. Assign an owner. Check the change was made. That loop, run consistently, is worth more than any single tool.

### How AI changes the adaptation loop

Now add AI to the adversary side.

Verizon reports that AI is helping threat actors speed up the time it takes to exploit known vulnerabilities (Verizon, 2026). IBM reports that more than one in four organizations hit by a malicious attack said it was AI-driven, and that AI-driven attacks added an average of USD 1 million to the cost of a malicious breach (IBM and Ponemon Institute, 2026).

From an irregular warfare perspective, AI does three things for an adversary.

**It lowers the cost of scale.** Tasks that once took skilled time, such as writing convincing messages in a target's language or sorting stolen data, become cheaper. That widens the asymmetry between attacker cost and defender cost.

**It shortens the cycle.** The gap between disclosure of a vulnerability and its exploitation shrinks. Your remediation calendar, measured in weeks, now competes with an attacker cycle that is getting shorter.

**It improves the disguise.** Influence operations and impersonation become more convincing. The information-environment feature of irregular competition reaches your inbox and your phone.

None of this changes the strategic logic. It intensifies it. NATO's observation about hybrid threats applies here too: the methods are old; the speed, scale and intensity are new (NATO, 2026).

### How defenders should adapt

If the adversary adapts, so must you. But adapt deliberately.

The irregular warfare tradition offers a useful discipline here. Effective counter-irregular strategies do not try to match the opponent everywhere. They protect what matters most, deny the opponent easy wins, build the resilience of the institutions under pressure, and learn faster than the opponent.

Translated to a mid-size security program, that means four things.

1. **Protect what matters most.** Know your critical assets and data flows. You cannot defend everything equally.
2. **Deny easy wins.** Fix the exposed, known-exploited vulnerabilities first. Lock down authentication. Turn on logging.
3. **Build institutional resilience.** Rehearse decisions. Test backups. Clarify authority.
4. **Learn faster.** Measure what happens. Review AI outputs and analyst overrides. Feed every incident back into detection and design.

AI can help with parts of all four. It cannot do any of them for you.

## Part III: The evidence on AI for defenders {#part-iii}

So does AI actually help defenders? The evidence says yes, with an asterisk.

### The good news

IBM compared breached organizations by their use of security AI and automation. Those using it extensively averaged USD 4.00 million per breach. Those using none averaged USD 5.93 million. That is a USD 1.93 million difference. Extensive users also identified and contained breaches in 215 days on average, against 280 days. Limited users landed in between, at USD 5.05 million and 244 days (IBM and Ponemon Institute, 2026).

| Use of security AI and automation | Average breach cost (USD) | Mean time to identify and contain |
|---|---|---|
| Extensive | 4.00 million | 215 days |
| Limited | 5.05 million | 244 days |
| None | 5.93 million | 280 days |

*Source: IBM and Ponemon Institute, Cost of a Data Breach Report 2026.*

### The asterisk

Here's the asterisk. This is an association in a benchmark study, not proof that a tool will do the same for you.

Organizations that invest in automation may simply be better run in other ways. They may have bigger budgets, more mature processes or better-trained staff. The study cannot fully separate those effects.

Still, the direction is hard to ignore: faster, better-prioritized work gives attackers less time inside your environment.

From the irregular warfare perspective, time is the decisive variable. A patient intruder needs time to learn, move and position. Every day you take away from that timeline is a day of advantage taken from them.

### The practitioner view

ISC2 points the same way from the practitioner side. 45% of respondents said their cybersecurity teams were already using generative AI in their tools, mostly to augment common operational tasks, write reports and support incident reporting. They also expected the biggest return on investment to take two or more years (ISC2, 2024).

Plan for a gradual rollout. Anyone promising transformation by next quarter is selling something.

### The uneven rollout

Only 36% of breached organizations used security AI and automation extensively. 25% used none. Among organizations with a SOC that deployed AI agents, the most common uses were threat hunting (56%) and automated response and containment (54%). Only 18% pointed agents at vulnerability scanning and management (IBM and Ponemon Institute, 2026).

Let that sink in.

Verizon says vulnerability exploitation is the leading way in. Yet vulnerability management is where AI agents are least used. Detection is well covered. Exposure reduction is where many teams have the most room to improve.

In irregular warfare terms, many organizations are investing in watching the perimeter and reacting to contact. Fewer are investing in denying the opponent the cheap, easy access route in the first place. That is an imbalance worth correcting.

### The new risks

This is not a one-way street.

IBM reports that 21% of organizations had a security incident involving an AI model or application, up from 13% the year before. The most common causes were compromised connected apps, APIs or plug-ins (27%) and cloud misconfigurations affecting AI workloads (27%). Among organizations with an AI-related breach, 92% lacked proper AI access controls. In IBM's words, these were governance failures, not model risk (IBM and Ponemon Institute, 2026).

Then there is shadow AI, meaning employees using unapproved AI tools. IBM reports that the share of security incidents involving shadow AI more than doubled to 43% from 20%, and that 68% of breached organizations lacked governance to manage AI or detect shadow AI. Verizon reports that frequent use of AI tools by employees rose from 15% to 45% in a year (Verizon, 2026). ISC2 found that 54% of respondents had already faced data privacy and security concerns from their organizations' adoption of generative AI (ISC2, 2024).

This is not an AI problem. It is a basics problem, with AI on top.

Access control. Asset inventory. Approved tools. Configuration management. The same fundamentals that the advisory AA24-038A emphasizes for networks apply, almost word for word, to AI systems.

Hold that thought. We return to it in Parts V and VI.
