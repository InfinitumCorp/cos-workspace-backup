## Part VI: Using the frameworks you already have

Here is something I tell every client. You do not need a new framework for AI in security. You need to apply the ones you have, and add a few questions.

### NIST CSF 2.0 as the spine

NIST's Cybersecurity Framework 2.0 is organized around six Functions: Govern, Identify, Protect, Detect, Respond and Recover. The Govern Function is new in version 2.0. It covers the organization's cybersecurity risk management strategy, expectations and policy, and it is designed to tie cybersecurity into the broader enterprise risk management picture (NIST CSF 2.0, 2024). Its categories include organizational context, risk management strategy, roles and responsibilities, policy, oversight, and cybersecurity supply chain risk management. Under Identify, you will find asset management and risk assessment. Under Protect, identity and access control, awareness and training, data security, platform security and infrastructure resilience. Under Detect, continuous monitoring and adverse event analysis. Under Respond, incident management, analysis, reporting and mitigation. Under Recover, recovery plan execution and communication (NIST CSF 2.0, 2024).

I like CSF 2.0 for this paper for a practical reason. It gives executives and practitioners the same vocabulary. And it lets you place AI in two roles at once: as a *tool* that helps you perform the functions, and as an *asset* that must be governed and protected under them.

Here is how I would map it.

| CSF 2.0 Function | AI as a tool | AI as an asset to protect |
|---|---|---|
| **Govern** | Draft policy language and map controls to requirements, with human approval | Assign an accountable owner for AI use; set rules on data, vendors and approvals; include AI vendors in supply chain risk management |
| **Identify** | Help maintain asset and exposure inventories; summarize risk assessments | Inventory every AI tool, model, plug-in and data connection, including the ones staff adopted on their own |
| **Protect** | Support identity and access reviews; draft awareness material; prioritize exposure | Apply identity, access control and data security to AI systems; segment what they can reach |
| **Detect** | Triage alerts; correlate signals; surface anomalies | Monitor AI systems for unusual access, prompts and outputs |
| **Respond** | Summarize incidents; draft timelines and notices; suggest next steps | Include AI incidents in response plans: prompt injection, data exposure through a model, poisoned inputs |
| **Recover** | Help draft recovery runbooks and dependency lists | Make sure you can operate without the AI tools; keep clean copies of configurations and data |

### NIST AI RMF as the AI-specific layer

NIST's AI Risk Management Framework 1.0 organizes AI risk work into four functions: Govern, Map, Measure and Manage. It describes seven characteristics of trustworthy AI systems: valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable, privacy-enhanced, and fair with harmful bias managed (NIST AI RMF, 2023). The framework is voluntary, and NIST describes it as intended for use by organizations designing, developing, deploying or using AI systems.

You do not need to adopt all of it. For a mid-size security team that is *using* AI rather than building it, I would take three ideas.

**Map the context before you deploy.** What is the task, who is affected, what data is involved, and what happens if the system is wrong?

**Measure with evidence you can repeat.** Decide what "working" means before you start. Test against real cases from your own environment, and keep the results.

**Manage with a way to stop.** Know how to turn the system off, and who can do it.

The Generative AI Profile (NIST AI 600-1) then gives you the risk list I covered earlier. Use it as a checklist for every AI-enabled workflow.

### ATT&CK and ATLAS as the common language of behavior

MITRE ATT&CK describes itself as a globally accessible knowledge base of adversary tactics and techniques based on real-world observations, used as a foundation for developing threat models and methodologies (MITRE ATT&CK). The enterprise matrix I reviewed has 15 tactics, from Reconnaissance and Resource Development through Initial Access, Execution, Persistence and so on to Exfiltration and Impact (MITRE ATT&CK).

Why does this matter for the irregular warfare lens? Because ATT&CK lets you organize your defense around behaviors rather than names. As I said earlier, attribution is slippery. Behavior is observable. If your detections, your tests and your incident reports use the same technique vocabulary, then you can tell what coverage you have and what you are missing, regardless of who is on the other side.

MITRE ATLAS extends the same idea to AI systems (MITRE ATLAS). If you deploy AI in a security role, use ATLAS as a reference for how adversaries might target it, and use it to shape your authorized testing.

### CISA KEV as the priority list

CISA's Known Exploited Vulnerabilities catalog is a public list of vulnerabilities that have been exploited in the wild (CISA KEV catalog). I treat it as the shortest honest priority list in vulnerability management. If a vulnerability is on it, and it is in your environment, it needs an owner and a date. Verizon's data tells us what happens when it does not (Verizon DBIR, 2026).

### What I would not do

I would not buy an "AI security platform" before I had an inventory of what I already own. I would not write a forty-page AI policy that nobody reads. And I would not let a vendor's maturity model substitute for my own measured baseline. Frameworks are scaffolding. The building is your operating practice.

## Part VII: An operating model that fits a mid-size team

A lot of AI advice assumes a security team with dozens of people. Most mid-size organizations have a handful, or a partner, or an IT generalist who also carries security. So let me describe a model that fits.

### Roles

You need five roles. One person can hold several of them in a small organization. What matters is that each one is named.

- **Executive sponsor.** Owns the risk decision and the budget. Usually the CEO, COO or CFO, or the board's designated lead. Accountable for the risk appetite.
- **AI and security owner.** Owns the program day to day. Usually the CISO, head of IT or head of security. Maintains the inventory, the rules and the metrics.
- **Data owner.** Decides what data may be used with which tool. Often the legal, privacy or compliance lead working with business owners.
- **Analyst lead.** Runs the daily operation and decides when an AI-assisted workflow is working. This is the person who sees the false positives first.
- **Communications and legal lead.** Owns the words in an incident. Approves anything that leaves the building.

CSF 2.0's Govern category on roles, responsibilities and authorities exists for exactly this purpose: to make sure someone is accountable (NIST CSF 2.0, 2024).

### Autonomy tiers

Not every AI function deserves the same level of trust. I use four tiers. Start everything at Tier 0 or 1. Promote it only with evidence.

| Tier | What the AI may do | Example | Promotion test |
|---|---|---|---|
| **0: Read and summarize** | Read approved data and produce summaries for a person | Summarize an alert and its context | Analysts rate summaries accurate over a sustained trial |
| **1: Recommend** | Propose a priority or next step; a person decides | Suggest a triage priority; rank open vulnerabilities | Low override rate; errors are understood and rare |
| **2: Act with approval** | Prepare an action; a person approves each one | Draft a ticket, stage a blocklist entry, prepare a message | Each approved action is logged; reversals are rare |
| **3: Act within limits** | Take a narrow, reversible action on its own, inside defined bounds | Quarantine a clearly malicious email from a defined set of senders | Long record at Tier 2; rollback tested; named owner accepts the risk |

For most mid-size organizations, I would stay at Tier 0 to 2 for a long time. Tier 3 should be rare, narrow and reversible. Notice that this ladder answers the resilience question too. If a Tier 3 function fails, you must be able to roll it back and continue without it.

### Data rules

Write a short data rule that anybody can understand. Mine has three classes:

- **Open:** public information. Any approved tool may use it.
- **Internal:** business information that is not public. Only approved tools under contract, with settings that prevent your data from being used to train others' models unless you have decided otherwise.
- **Restricted:** regulated data, credentials, secrets, customer records, and anything where a leak would be a reportable incident. No AI tool unless the data owner and the AI and security owner have both approved it in writing.

Then give people an approved tool. This is the part leaders skip. Verizon found that 67% of users accessing AI services from corporate devices used non-corporate accounts (Verizon DBIR, 2026). If you give people nothing, they will bring something. A sanctioned option is cheaper than a shadow one.

### Identity for AI

Every AI tool that touches your systems needs an identity, and that identity needs the least privilege that lets it do its job. IBM found that, among organizations with AI-related breaches, 92% lacked proper AI access controls (IBM/Ponemon, 2026). Give each integration its own credentials. Avoid shared accounts. Log what each one does. Rotate secrets. Review permissions on a schedule. This is the same identity discipline you already apply to employees and contractors, applied to a new kind of worker.

### Cadence

A simple rhythm keeps the program alive:

- **Weekly:** analyst lead reviews AI-assisted workflow metrics, overrides and errors.
- **Monthly:** AI and security owner reviews inventory changes, new tools and incidents, and updates the data owner.
- **Quarterly:** executive sponsor reviews the baseline metrics, the risk register and the tier promotions. Run an exercise at least once a quarter.
- **Annually:** review the whole program against CSF 2.0 and refresh the plan.

This is not heavy. But it makes the work continuous. That matters because of persistence: the adversary does not take a quarter off, so the defender's practice cannot either.

## Part VIII: Honest limits and counterarguments

I would not trust a paper that only told me what I wanted to hear, so let me argue against myself.

**"The IBM numbers prove AI saves money."** They do not. They show an association among organizations that were breached, in a nonstatistical sample (IBM/Ponemon, 2026). Organizations that use security AI extensively may also have better tooling, better staff and better processes. The direction is encouraging. The exact figure is not a forecast.

**"AI will make attackers unstoppable."** The evidence I reviewed does not support that. IBM reports a real rise in AI-driven attacks and their costs. But Verizon's analysis of actors using AI found that most AI-assisted tooling was tied to well-known techniques, with a median of 55 existing malware examples performing the same functions, and that the share of phishing as an initial access vector had barely moved over the past few years (Verizon DBIR, 2026). Both organizations are describing something real. The honest summary is that attackers are getting faster and cheaper at what they already do, and defenders who are slow on basics are the ones who feel it.

**"Our team is too small for this."** Maybe. But the small team is exactly where the capacity gap bites. ISC2 found that budget was the number one cause of both talent and skills gaps, and 67% of respondents reported a staffing shortage (ISC2, 2024). The answer is not to skip the work. It is to choose a narrow starting point, measure it, and use partners where it makes sense.

**"Why not wait until AI matures?"** Because your staff are already using it. Verizon found 45% of employees were regular users of AI on corporate devices (Verizon DBIR, 2026). Waiting does not mean you have no AI. It means you have ungoverned AI.

**"This is all too defensive."** Fair challenge, and one an irregular warfare analyst would raise. Defense alone cedes the initiative. But for a company, the legitimate version of "taking the initiative" is not offense. It is authorized testing, threat-informed defense, and exercises that find your weaknesses before somebody else does. IBM's data lists offensive security testing, such as red teaming and penetration or vulnerability testing, among the factors associated with lower breach costs (IBM/Ponemon, 2026). I will return to that in the recommendations.

**"You borrowed a military framework for a business problem."** I did, and I said so up front. The formal DoD definition is about violent struggle (DoDD 3000.07, 2017), and a phishing email is not that. What I borrowed is the habit of thinking about indirect adversaries, persistence, proxies, influence and resilience. If the lens helps, use it. If it does not, the recommendations stand on the NIST, CISA and MITRE material alone.

### What this paper cannot tell you

A few limits are worth stating plainly.

- The studies I used are global and mixed-size. None isolates mid-size organizations.
- They use different periods, definitions and sample methods, so numbers from different sources should not be added or compared directly.
- IBM's data is from breached organizations. Verizon's is incident-based. ISC2's is a survey of practitioners. ENISA's reflects incidents it observed in the EU, and is dominated by hacktivist denial-of-service activity. FBI IC3's figures come from complaints that victims chose to file.
- I did not run any test of any tool. I make no claim about what any particular product does.
- Infinitum has not published results from client engagements in this paper, and this paper does not claim any.
