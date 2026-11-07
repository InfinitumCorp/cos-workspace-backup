## Part IV: AI is also terrain

In irregular contests, every new capability you adopt becomes ground that someone else can contest. A new base, a new supply route, a new partner: each one is an asset and an exposure at the same time. AI is no different. If you bring it into your security operations, you have to defend it.

Let me show you what the evidence says about that exposure.

### The numbers on AI incidents

IBM and Ponemon Institute reported that AI-related security incidents, meaning breaches involving an organization's AI models or applications, grew to 21% of the organizations studied, from 13% the year before. That is a 61% increase. Among the organizations that suffered an AI-related breach, 92% lacked proper AI access controls, which IBM defines to include role-based access and multifactor authentication (IBM/Ponemon, 2026).

IBM also broke the incidents down by type. Breaches involving model inversion, where sensitive data is extracted from a model, averaged USD 6.07 million, which is 18% above the global average. Prompt injection, where prompts are maliciously altered to manipulate a model's output, averaged USD 5.89 million. IBM's reading of the prompt injection cost is that corrupting a model can also corrupt every business process that relies on it (IBM/Ponemon, 2026).

Then there is shadow AI, meaning employees using AI tools the organization has not approved. IBM found that incidents involving shadow AI more than doubled, to 43% from 20%. Those incidents cost more on average, USD 5.39 million against USD 4.63 million the prior year, and the consequences included data loss or compromise (49%) and disrupted operations (42%). In about one in five of these incidents, the organization reported paying a regulatory fine (IBM/Ponemon, 2026).

Verizon's data shows the same behavior from the inside. In its data loss prevention dataset, 67% of users who access AI services from corporate devices were using non-corporate accounts, a slight decrease from the prior year. At the same time, 45% of employees were considered regular users of AI, authorized or not, on corporate devices, up from 15% the year before. Shadow AI had become the third most common non-malicious insider action detected, a fourfold increase in percentage from the previous year (Verizon DBIR, 2026).

Look at that governance gap. IBM found that among breached organizations, 68% lacked AI governance to manage AI or detect shadow AI, up from 63% the prior year. Of those with policies, only about a third had strict approval processes for deploying AI. Only 19% of organizations said they coordinated governance and security teams (IBM/Ponemon, 2026).

ISC2's practitioners felt the same pressure from another angle. More than half (54%) had already faced data privacy and security concerns due to their organization's adoption of generative AI, and 65% said their organization needs more regulation on its safe use (ISC2, 2024).

I want to be fair about these numbers. Some of them describe breached organizations, which is a different population than "all organizations." Some come from surveys. They all point the same direction, though. People are adopting AI faster than organizations are governing it.

### The risk catalog

You do not need to invent a list of AI risks. NIST has done much of the work. NIST's Generative AI Profile, a companion to the AI Risk Management Framework, identifies a set of risks that are unique to or exacerbated by generative AI. Several matter to a security team right away (NIST AI 600-1, 2024):

- **Confabulation**: the production of confidently stated but erroneous or false content. In a security setting, that is a fabricated indicator, an invented log line, or a made-up explanation of an alert that sounds right.
- **Information security**: lowered barriers for offensive cyber capabilities, which cuts against you as a defender, and the exposure of the AI system itself to attack.
- **Data privacy**: leakage of sensitive data through prompts, training data or outputs.
- **Value chain and component integration**: the risk that comes with third-party models, data and components that you did not build.
- **Human-AI configuration**: the risk of over-reliance, or of mismatches between what people expect and what the system does.
- **Information integrity**: the lowered barrier to generating content that blurs fact and fiction.

Treat that list as a design input. Before you give a model any role in your security operations, ask which of these risks apply to that role and what you will do about it.

### The data supply chain

A joint Cybersecurity Information Sheet from the NSA's AI Security Center, CISA, the FBI and partner agencies in Australia, New Zealand and the United Kingdom focuses on a point that is easy to miss: the data around an AI system is part of its attack surface. The sheet describes three areas of risk: the data supply chain, maliciously modified or "poisoned" data, and data drift. Its best practices include sourcing reliable data and tracking provenance, verifying integrity in storage and transport, using digital signatures, classifying data and controlling access, encrypting data, storing it securely, and running ongoing data security risk assessments (CISA et al., 2025).

For a mid-size organization that is not training its own models, this matters in a particular way. You will probably use a commercial model or platform, and feed it your own data: logs, tickets, policies, vendor documents. The data you feed it, and the data it retrieves, are your responsibility. If an adversary can influence what your system reads, such as a phishing email that your AI triage tool will summarize, or a document in a shared folder that your assistant will retrieve, then they can try to influence what your system says.

MITRE tracks this class of problem too. ATLAS, its knowledge base of adversary tactics and techniques involving AI systems, described itself at the time of my review as covering 16 tactics, 208 techniques, 40 mitigations and 73 case studies, based on real-world observations and realistic demonstrations by AI red teams (MITRE ATLAS). MITRE ATT&CK's enterprise matrix now includes entries that touch AI as well, such as prompt injection under Execution (MITRE ATT&CK). I mention this to make a simple point. The security community already treats attacks on AI as a documented category, with names and mitigations. You do not have to treat it as science fiction.

### The irregular warfare reading

Let me restate this in the lens we are using. When you adopt AI in your security operations, you are extending your lines. You have a new supply route (data), new partners (model and platform vendors), new points of influence (anything the model reads), and a new class of insider (the assistant itself, with its own permissions). An adversary who prefers indirect approaches will look at exactly those seams.

That leads to a rule I will use in the recommendations: **no AI system gets more access than a new employee in the same role would get, and none gets to act without a human gate until it has earned it.**

## Part V: Where AI helps in a mid-size security operation

Now let me get practical. What does AI actually do for a defender, and where should a small team start?

IBM's research gives one useful hint about where the field is today. Among breached organizations, 77% made limited or extensive use of AI and automation to investigate threats, but only a combined 69% used them for prevention. IBM notes that more than a third of organizations were not using these technologies in their front-line efforts to identify and patch vulnerabilities before they could be exploited. Among the 50% of organizations that have a security operations center and deployed AI agents in it, the majority used the agents for threat hunting and for response and containment. Only 18% used agents for vulnerability scanning and management (IBM/Ponemon, 2026).

Let me connect that to the rest of the data. Verizon found that exploitation of vulnerabilities is now the top way in, and that only 26% of KEV-listed vulnerabilities were fully remediated (Verizon DBIR, 2026). So the place where the adversary most often gets in is the place where the defenders' AI use lags. That is an opportunity. It is also what an irregular warfare analyst would call a seam: a gap between how the defender is organized and where the pressure actually is.

### A workflow view

Here is how I would map AI to a mid-size security operation. For each task I list what AI can do, where the human decision sits, what the typical failure looks like, and what to measure. This is a design aid, not a product list.

| Task | What AI can do | Human decision | Typical failure | What to measure |
|---|---|---|---|---|
| Alert triage | Group related alerts, summarize context, suggest a priority | Analyst accepts, edits or rejects the priority | Confident but wrong summary; missed alert in a "low" bucket | Time to first look; false-positive rate; analyst override rate |
| Alert enrichment | Pull asset, user and vulnerability context into one view | Analyst decides what the context means | Stale or wrong context presented as fact | Analyst minutes per alert |
| Phishing reports | Cluster reports, extract common features, draft a reply to the reporter | Analyst decides to block, purge or escalate | Misses a convincing message that looks routine | Time from report to action; repeat campaign rate |
| Vulnerability prioritization | Rank open findings using KEV status, exposure and asset criticality | Owner decides patch window and exceptions | Over-trusting a score; ignoring context | Days to remediate KEV items; backlog age |
| Detection engineering | Suggest detection logic mapped to ATT&CK techniques; flag gaps | Engineer reviews, tests and approves each rule | Rules that look right and fail in practice | Coverage vs. priority techniques; rule false-positive rate |
| Incident summaries | Draft timelines and status updates from logs and notes | Incident lead verifies before anything is shared | Fabricated detail in a summary that goes to leadership | Time to a verified summary |
| Third-party risk | Read questionnaires and contracts, compare to your requirements | Risk owner decides acceptance | Misses a clause; trusts a vendor claim | Review cycle time; gaps found later |
| Reporting and compliance | Draft control narratives and evidence lists | Control owner signs off | Invented evidence; mismatched control text | Hours per reporting cycle |

A few notes on that table.

**Everything has a human gate.** In every row, the person decides. That is on purpose. NIST's AI Risk Management Framework lists "accountable and transparent" among the characteristics of trustworthy AI, and its MAP function calls for processes for human oversight to be defined, assessed and documented (NIST AI RMF, 2023). In practice, the simplest rule is this: *AI proposes, a person disposes.*

**The metrics matter more than the demo.** A tool that makes a good demo can still add work if analysts spend time checking it. Measure analyst minutes saved, override rates and error types, not impressions.

**Prevention is on the list for a reason.** Two of the rows, vulnerability prioritization and detection engineering, point at exposure and coverage, which are the places where IBM's data says adoption lags and where Verizon's data says the adversary is getting in.

### Four small, safe starting points

If I were advising a mid-size team that has never used AI in its security operations, I would start with these four. Each is bounded, reversible, and measurable.

**1. Phishing report triage.** Your staff already report suspicious messages. An AI-assisted workflow can cluster the reports, extract shared features, and draft a response, while an analyst makes every block-or-purge decision. This is a good first project because the data is yours, the volume is manageable, and the failure mode is visible.

**2. KEV-first vulnerability prioritization.** The CISA KEV catalog is a public list of vulnerabilities known to be exploited in the wild. Match it against your asset inventory, and use AI to help summarize which exposures matter most and to draft remediation tickets for owners. The decision about what to patch first stays with a person. The benefit is aimed directly at the number that worries me most: 43 days (Verizon DBIR, 2026).

**3. Incident and alert summarization.** Use AI to draft summaries that an analyst edits. Never send an AI-drafted summary to leadership or customers without verification. The point is to save the analyst's typing time, not to replace the analyst's judgment.

**4. Policy and vendor document review.** Use AI to compare a vendor's security documentation to your requirements and flag gaps for a person to review. The risk is low, because a person reads the flagged items, and the time saved is real.

None of these four requires giving an AI system the ability to change a firewall rule, disable an account, or send a message to a customer. That comes later, if ever, and only with evidence.

### What AI is not good at

I would be doing you a disservice if I only listed benefits. Here is where I would not rely on AI today.

- **Certainty.** Models produce plausible text. They do not know when they are wrong. NIST's confabulation risk is exactly that (NIST AI 600-1, 2024).
- **Novel situations with little data.** If an event looks unlike anything in the training or reference data, a model may force it into a familiar shape.
- **Adversarial settings without safeguards.** Anything that reads attacker-controlled content, such as an email, a web page or a file, can be influenced by it. Treat model input as untrusted.
- **Accountability.** A model cannot be held responsible. A person must be.
- **Replacing basics.** Verizon's own data suggests that AI is mostly speeding up what adversaries already do, with most AI-assisted tooling tied to well-known techniques (Verizon DBIR, 2026). If so, the best response is to be good at the known basics, and to use AI to help you do so faster. ISC2's practitioners point the same way. They expect AI to help, and they also expect the largest returns to take two or more years to show up (ISC2, 2024).

### Build, buy or partner

A mid-size organization has three ways to get AI into its security operations: build it in-house, buy capabilities embedded in the tools you already use, or partner with a managed provider or consultancy.

Building is rarely the right choice for a mid-size organization. It needs engineering talent, data pipelines and ongoing evaluation that most security teams do not have, and ISC2 shows that skills and budget are already the binding constraints (ISC2, 2024).

Buying embedded capabilities is where most organizations will start. Your endpoint, email, identity and SIEM vendors are adding AI features. Your job is to evaluate them with the same discipline you would use for any new vendor: what data do they see, where does it go, what can the feature do on its own, and how do you turn it off.

Partnering can help fill skill gaps. IBM's analysis lists managed security services among factors associated with lower breach costs (about USD 152,929 below the global average), and found that breaches identified and contained by managed security service providers averaged 230 days, against 209 for internal teams and 247 globally (IBM/Ponemon, 2026). Notice what that says. In IBM's data, internal teams were fastest, and MSSPs were still faster than the global average. A partner is a supplement to your capability, not a substitute for owning your risk.

At Infinitum, this is the space where I think practical, integrated guidance is most useful: helping an organization choose the narrow places where AI adds value, and avoid the broad places where it adds exposure. I will say more about how we approach that in the About section.
