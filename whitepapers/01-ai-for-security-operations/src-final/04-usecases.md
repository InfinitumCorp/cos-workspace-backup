## Part IV: The use cases, one by one {#part-iv}

Not every task suits AI equally.

This part walks through six common security operations use cases. For each, I cover what the work is, what AI can plausibly contribute, what can go wrong, how a person stays in control, and what to measure. I close each with the irregular warfare angle, because it often changes the priority.

First, the summary table. It is Infinitum's practical judgment, informed by the sources in this paper. It is not a measured result.

| Use case | Potential benefit | Main risk | Human oversight |
|---|---|---|---|
| Alert triage | Faster first-pass summaries and grouping of related alerts | Missed or wrongly dismissed true alerts | Analyst confirms every closure; sample reviews of AI decisions |
| Threat-intel enrichment | Context on indicators and techniques, mapped to MITRE ATT&CK | Unverified or outdated claims presented as fact | Analyst checks sources before action |
| Vulnerability prioritization | Ranks fixes using CISA KEV status, exposure and asset value | Over-trusting scores; skipping context | Owners approve patch order and exceptions |
| Log analysis | Plain-language search and pattern spotting across large volumes | Sensitive data sent to unapproved tools | Approved tools only; engineers validate queries |
| Reporting and documentation | Drafts incident notes and status reports faster | Inaccurate or overconfident statements | Named owner edits and signs off |
| Deception and early warning | Helps plan, monitor and summarize decoy activity | Decoys that leak, mislead staff or create legal exposure | Written approval, legal review, tight scope |

### 1. Alert triage

**The work.** Security tools generate alerts. Someone has to look at each one, decide whether it matters, group it with related alerts, and either close it or escalate it. In a mid-size organization, that someone is often one or two people, sometimes part-time.

**What AI can contribute.** A first-pass summary of each alert in plain language. Grouping of related alerts into a single case. A suggested severity with the reasoning shown. A draft of the questions an analyst should answer next. Pulling in context, such as who owns the affected system and whether the user normally does this.

**What can go wrong.** The serious failure is a true alert wrongly dismissed. A model that is right most of the time can still be wrong on the alert that matters. Worse, an analyst who has watched the model be right a hundred times stops checking. That is automation bias, and it is the quiet killer of AI-assisted triage.

The second failure is noise disguised as help: long, fluent summaries that take as long to read as the raw alert.

**How a person stays in control.** AI proposes. A person decides. No alert is closed without a human confirmation, at least during the pilot. Keep a record of every AI suggestion and every analyst override. Each week, pull a sample of AI-recommended closures and have a second analyst review them blind.

**What to measure.** Time from alert to first human decision. Share of AI recommendations that analysts overrode, and why. Number of true incidents that were first suggested for closure. Analyst time per alert before and after.

**The irregular warfare angle.** Alert floods are a form of asymmetric cost imposition, whether intended or not. Every cheap attempt by an attacker costs you analyst minutes. Triage support is where you recover that asymmetry. But remember threshold management: the patient intruder generates few alerts, not many. Do not let triage efficiency become the only goal. A faster queue is worthless if the dangerous event never enters it.

### 2. Threat-intelligence enrichment

**The work.** An alert contains an IP address, a domain, a file hash or a suspicious behavior. Enrichment means finding out what is known about it. Has it been seen before? Is it associated with a known campaign? Which adversary techniques does it suggest?

**What AI can contribute.** Rapid summarization of what internal and approved external sources say about an indicator. Mapping observed behavior to MITRE ATT&CK, the knowledge base of adversary tactics and techniques that helps you map detections and find coverage gaps (MITRE ATT&CK). Drafting a short context note for the analyst. Translating a dense public advisory into the three things your team needs to check today.

**What can go wrong.** Unverified or outdated claims presented as fact. A model may connect an indicator to a named group on thin evidence, or repeat an association that was true years ago. Shared infrastructure makes this worse: an address used by an attacker last year may belong to an innocent tenant today.

**How a person stays in control.** Every enrichment claim cites its source, and the analyst checks the source before acting. Attribution statements are flagged as low confidence by default. Nobody takes action against an external party, and nobody makes an external attribution statement, on the strength of an AI-generated summary.

**What to measure.** Time to context for a new indicator. Share of enrichment claims that could be traced to a source. Number of corrections made by analysts.

**The irregular warfare angle.** This is where the attribution problem lives. Doctrine describes irregular activity as non-attributable, and RAND describes the blurring of attribution as a defining gray-zone tactic (RAND, 2019). An AI tool that produces confident attribution is producing exactly the false certainty that ambiguity is designed to exploit. Use enrichment to understand behavior and likely impact. Treat the question of who as secondary, slow and best left to people and to authorities with the evidence to answer it.

### 3. Vulnerability prioritization

**The work.** Scanners find more vulnerabilities than any team can fix. Someone has to decide what gets fixed first, by whom, and by when, and track whether it actually happened.

**What AI can contribute.** Ranking fixes by combining several signals: whether the vulnerability appears in the CISA KEV catalog, whether the affected system is reachable from the internet, how important the asset is to the business, and whether a compensating control exists. Grouping findings by system owner so that each owner gets one clear list. Drafting change tickets. Mapping findings to ATT&CK techniques so you can see which adversary behaviors a fix would deny. Flagging technology that is past its supported lifecycle.

**What can go wrong.** Over-trusting a score. Skipping context that only the system owner knows, such as a business process that cannot tolerate a reboot this week. Treating the ranked list as the decision rather than as an input to it.

**How a person stays in control.** System owners approve patch order and exceptions. Every exception has a named owner, a reason and an expiry date. Security sets the policy; owners execute; leadership accepts residual risk in writing.

**What to measure.** Time to remediate KEV-listed vulnerabilities on internet-facing systems. Number of open KEV vulnerabilities. Share of exceptions past expiry. Compare your numbers with your own baseline, not with a survey median.

**The irregular warfare angle.** This is the use case I would move to the front of the line for most mid-size organizations, and the evidence supports that view. Verizon finds vulnerability exploitation is now the leading way in, at 31% of breaches (Verizon, 2026). Advisory AA24-038A describes initial access through vulnerabilities in public-facing appliances (CISA et al., 2024). Yet IBM finds only 18% of organizations with SOC agents pointed them at vulnerability management (IBM and Ponemon Institute, 2026).

Denying the opponent the easy route is the most cost-effective move in any irregular contest. Every known-exploited vulnerability you close on an internet-facing system removes a cheap option from the attacker's menu. That is asymmetric cost imposition in your favor.

> **Pull quote.** Detection tells you the adversary is inside. Exposure reduction keeps them out. Most teams have the ratio backward.

### 4. Log analysis

**The work.** Logs record what systems and people did. They are the evidence base for detection, investigation and hunting. They are also enormous, inconsistent and hard to search without specialized query skills.

**What AI can contribute.** Turning a plain-language question into a draft query. Summarizing patterns across large volumes. Highlighting deviations from a baseline: an account active at an unusual hour, a built-in administrative tool used on a server where it is never used, a new connection between two systems that do not normally talk.

**What can go wrong.** Two big risks. First, sensitive data sent to unapproved tools. Logs contain usernames, internal addresses, sometimes personal data. Pasting them into a public AI service is a data leak. Second, a plausible but wrong query that silently misses what you were looking for. A query that returns nothing feels reassuring. It may simply be wrong.

**How a person stays in control.** Approved tools only, with a plain rule about what data may go into them. Engineers validate any AI-drafted query before its results are relied on, and test it against a known example. Keep AI-generated detection logic in version control like any other code.

**What to measure.** Time to answer an investigative question. Number of AI-drafted queries that needed correction. Coverage: share of critical systems sending logs to the central store.

**The irregular warfare angle.** This is the use case that most directly confronts threshold management. Advisory AA24-038A makes the point that defenders who lack established baselines find it difficult to discern legitimate from malicious behavior (CISA et al., 2024). AI-assisted analysis may help build and watch those baselines at a scale a small team cannot manage by hand. But it depends entirely on the logs existing, being centralized and being protected. The same advisory recommends turning logging on and storing logs centrally. Do that first.

### 5. Reporting and documentation

**The work.** Incident notes. Shift handovers. Status reports. Board updates. Regulatory and contractual notifications. After-action reviews. In a stretched team, writing is often the work that slips, and that slippage has real costs: lost context, weak lessons learned, unclear decisions.

**What AI can contribute.** First drafts, faster. Turning a timeline of analyst notes into a readable narrative. Producing different versions of the same facts for different audiences: technical detail for engineers, impact and decisions for executives. This is one of the uses ISC2 respondents most commonly reported (ISC2, 2024).

**What can go wrong.** Inaccurate or overconfident statements. A draft that says the incident is contained when it is not. A report that smooths over uncertainty because fluent prose sounds certain. In a regulatory notification, that can create legal exposure.

**How a person stays in control.** A named owner edits and signs off every external or executive document. Drafts mark facts, estimates and unknowns differently. Nothing leaves the organization without human review.

**What to measure.** Analyst hours spent on reporting, before and after. Time from incident closure to completed after-action review. Number of factual corrections made to AI drafts.

**The irregular warfare angle.** This is where resilience of institutions becomes concrete. The EU framework notes that hybrid threats aim at "generating ambiguity to hinder decision-making processes" (European Commission and High Representative, 2016). Clear, timely, honest reporting is the counter. Leaders who receive accurate information quickly make better decisions under pressure. A reporting process that is fast but unreliable feeds the very ambiguity an adversary wants.

### 6. Deception and early warning

**The work.** Deception, in defensive security, means placing decoy assets, credentials or data inside your own environment so that an intruder who touches them reveals themselves. Early warning more broadly means arranging your defenses so that you learn about an intrusion early in its life rather than late.

MITRE describes its Engage framework as one "for planning and discussing adversary engagement operations." It makes a point worth repeating: "Deception is a process, not a fire-and-forget technology stack." And it frames the logic this way: with traditional cyber defense, "the adversary only needs to be right once," but with adversary engagement, "the adversary only needs to be wrong once" (MITRE Engage).

**What AI can contribute.** Helping plan where decoys would be most informative given your network layout. Monitoring decoy interactions and summarizing them for an analyst. Drafting realistic but fake content so decoys are believable. Correlating a decoy touch with other activity to help an analyst judge whether it is a real intrusion or a misconfigured script.

**What can go wrong.** Decoys that leak into production use or confuse legitimate staff. Decoy data that looks too much like real personal or customer data. Activity that drifts from passive detection toward something that could be seen as interacting with an outside party. Each of these creates operational and legal risk.

**How a person stays in control.** Written approval from leadership. Legal review before deployment. Decoys stay strictly inside your own environment. No decoy ever contains real sensitive data. The program is passive and defensive: it detects and informs. It never reaches outward.

**What to measure.** Number of decoy alerts, and the share that were confirmed as real intrusions versus internal noise. Time from decoy touch to analyst decision.

**The irregular warfare angle.** Deception has a long history in competition below the threshold of war. NATO lists deception among the hybrid methods long used to destabilize adversaries (NATO, 2026). In a defensive setting, the logic flips. You use the adversary's need to explore your environment against them. A patient intruder who stays under every threshold still has to look around. A well-placed decoy turns that exploration into an early warning.

This is also the most specialized use case on the list. For most mid-size organizations, I would sequence it after the basics and after the first four use cases are working. It is a force multiplier, not a foundation.

### Questions to ask before you buy

Most mid-size organizations will not build AI tools. They will buy them, or switch on AI features inside products they already own. Either way, the decision deserves the same scrutiny as any other system that touches sensitive data.

Here are the questions I would put to any vendor, in writing, before a pilot. They follow directly from the risks in this paper and from the frameworks discussed in Parts V and VI.

1. **Data.** What data does the tool send outside our environment? Where is it stored, for how long, and is it used to train models that serve other customers?
2. **Access.** What permissions does the tool need? Can it run in read-only or recommend-only mode? Can we restrict it to specific systems?
3. **Identity.** Does it support our single sign-on, multifactor authentication and role-based access? How are its service accounts and keys managed?
4. **Logging.** Does it log its own inputs, outputs and actions in a form we can send to our central log store?
5. **Off switch.** How quickly can we disable it, and what happens to in-flight actions when we do?
6. **Untrusted content.** How does the tool handle hostile input, such as phishing emails, malicious web pages or attacker-written log entries? What does the vendor do about prompt injection?
7. **Supply chain.** Which third-party models, plug-ins and services does it rely on, and how are they secured and updated?
8. **Evidence.** What independent testing has the product undergone? Will the vendor allow it to be included in our own authorized security testing?
9. **Errors.** How does the tool show uncertainty? How do analysts flag and correct wrong output, and does that feedback improve the product without exposing our data?
10. **Exit.** If we stop using it, how do we get our data back and confirm it has been deleted?

A vendor who cannot answer these clearly is telling you something. Listen.

### Sequencing the use cases

If you take one thing from this part, take the sequence.

1. Start with **reporting and documentation** and **alert triage summaries**. They are low-risk, quick to measure and build trust.
2. Move fast to **vulnerability prioritization**. It addresses the leading way in and is under-used.
3. Add **log analysis** once logging coverage and data rules are in place.
4. Use **threat-intel enrichment** throughout, with strict source discipline.
5. Consider **deception and early warning** once the foundation holds.

That sequence is a judgment, not a law. Your environment may justify a different order. But be suspicious of any plan that starts with autonomous response and ends with patching.
