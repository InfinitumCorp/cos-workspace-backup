## Part V: Governance and AI risk {#part-v}

You don't have to invent the rulebook.

Public frameworks give you a common language, and they are free. The challenge is not finding guidance. It is applying a small, sensible slice of it consistently.

### The NIST AI Risk Management Framework

The NIST AI Risk Management Framework (AI RMF) was released on January 26, 2023. It is intended for voluntary use and to improve the ability to incorporate trustworthiness considerations into the design, development, use and evaluation of AI products, services and systems (NIST, AI RMF).

Its core is organized around four functions: govern, map, measure and manage. NIST describes governance as a cross-cutting function "infused throughout AI risk management" that enables the other three (NIST, AI RMF Core).

Here is how I translate those four functions for a security team adopting AI tools. The functions are NIST's. The translation is mine.

**Govern.** Who decides, under what rules? NIST's govern function includes outcomes such as mechanisms to inventory AI systems, clear roles and responsibilities, and policies that address risks from third-party software and data (NIST, AI RMF Core). For you, that means: one accountable owner for AI in security, an approved-tools list, a plain rule on what data may go into AI services, and a register of every AI-enabled tool and what it can touch.

**Map.** What is this tool for, and what could go wrong? NIST's map function establishes the context to frame risks, including documenting the system's knowledge limits and how its output will be overseen by humans, and defining processes for human oversight (NIST, AI RMF Core). For you: write one page per AI use case stating its purpose, its inputs, its outputs, who reviews them and what it must never do.

**Measure.** Is it working, and is it safe? NIST calls for AI systems to be tested before deployment and regularly while in operation, and for security and resilience to be evaluated and documented (NIST, AI RMF Core). For you: baseline metrics before the pilot, a log of AI outputs and analyst overrides, and periodic review.

**Manage.** What do we do about what we learned? NIST's manage function includes mechanisms "to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use," and monitoring of pre-trained models used in development (NIST, AI RMF Core). For you: a documented way to switch the tool off, a named person with authority to do it, and a review of every incident involving the tool.

Key word: deactivate. If you cannot turn it off cleanly, you do not control it.

### The Generative AI Profile

On July 26, 2024, NIST released NIST AI 600-1, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*. NIST says the profile can help organizations identify unique risks posed by generative AI and proposes actions for generative AI risk management (NIST, AI RMF).

Most of the AI tools a mid-size security team will touch first are generative: summarizers, assistants, report drafters, query helpers. The profile is the right companion document for those.

NIST also notes on the same page that the AI RMF 1.0 is being revised, and that in April 2026 it released a concept note for an AI RMF profile on trustworthy AI in critical infrastructure (NIST, AI RMF). If you operate in or supply critical infrastructure, watch that work.

### The NIST Cybersecurity Framework 2.0

The NIST Cybersecurity Framework (CSF) 2.0 was released on February 26, 2024. Its core is organized around six functions: Govern, Identify, Protect, Detect, Respond and Recover. Govern was newly added in 2.0 (NIST, 2024).

The CSF gives you a structure for managing risk across the whole program. AI tools are not a separate program. They sit inside it.

A practical way to use the two frameworks together:

| CSF 2.0 function | AI-in-security question to answer |
|---|---|
| Govern | Who owns AI risk in security? Is there an approved-tools list and a data rule? |
| Identify | Do we have an inventory of AI tools, their service accounts and their data access? |
| Protect | Do AI tools and the data behind them have role-based access and multifactor authentication? |
| Detect | Are AI tool activity and AI-generated actions logged and monitored? |
| Respond | Can we disable or roll back an AI tool quickly during an incident? |
| Recover | Do we review AI involvement in every incident and update controls afterwards? |

### Why governance comes first

IBM's numbers make the case on their own. Among organizations with an AI-related breach, 92% lacked proper AI access controls. 68% of breached organizations lacked governance to manage AI or detect shadow AI (IBM and Ponemon Institute, 2026).

Those are not sophisticated failures. They are the absence of basic rules.

From the irregular warfare perspective, ungoverned AI is an unmanaged interface, and Hybrid CoE describes hybrid threats as activities that exploit "the different interfaces" between organizations and domains (Hybrid CoE). Every unapproved AI tool an employee uses is a new interface between your data and someone else's system. An adversary does not need to defeat your controls if your data is already flowing around them.

### A governance minimum for mid-size organizations

If you do nothing else in this part, do these six things. They are my recommendation, aligned with the frameworks above.

1. **Name one accountable owner** for AI in security operations, with authority to approve, pause and retire tools.
2. **Publish an approved-tools list** and a one-page rule on what data may and may not go into AI services.
3. **Inventory every AI-enabled tool**, including features quietly switched on inside existing products, with its service accounts, keys and data access.
4. **Put role-based access and multifactor authentication** on AI tools and the data behind them.
5. **Write a one-page use-case card** for each AI use: purpose, inputs, outputs, human reviewer, prohibited actions, off switch.
6. **Review quarterly**, and after every incident involving an AI tool.

That is not bureaucracy. That is the minimum you need to answer the question every board will eventually ask: what is AI doing in our security program, and who is accountable for it?

## Part VI: Securing the AI itself {#part-vi}

An AI tool in your security operations is not just a helper. It is a system with access, inputs, outputs and dependencies. It can be attacked like any other system, and in some new ways too.

This part describes the main risk categories at a level suited to decision-makers. It is defensive by design. It explains what can go wrong and how to reduce the risk. It does not describe how to carry out attacks.

### Three public references

Three public resources give you the vocabulary.

**OWASP Top 10 for LLM Applications (2025).** The OWASP Gen AI Security Project publishes a list of the top risks for large language model and generative AI applications. The 2025 list includes Prompt Injection, Sensitive Information Disclosure, Supply Chain, Data and Model Poisoning, Improper Output Handling, Excessive Agency, System Prompt Leakage, Vector and Embedding Weaknesses, Misinformation, and Unbounded Consumption (OWASP, 2025).

**MITRE ATLAS.** ATLAS is MITRE's knowledge base of adversary tactics and techniques against AI-enabled systems. Its September 2026 data release lists 16 tactics, 120 techniques, 88 sub-techniques, 40 mitigations and 73 case studies (MITRE ATLAS, 2026). If your team already uses ATT&CK, ATLAS will feel familiar.

**NIST AI 100-2 E2025.** NIST's report *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*, published in March 2025, provides a taxonomy and common terminology for attacks on AI systems and corresponding mitigations (NIST, 2025).

And for organizations deploying AI systems built by others, which is nearly every mid-size organization, the joint guidance *Deploying AI Systems Securely*, published in April 2024 by the NSA's Artificial Intelligence Security Center with CISA, the FBI and allied partners, provides best practices aimed at improving the confidentiality, integrity and availability of AI systems and at protecting, detecting and responding to malicious activity against AI systems and related data and services (NSA AISC et al., 2024).

### Risk 1: Prompt injection

**What it is.** OWASP lists prompt injection as the first risk on its 2025 list (OWASP, 2025). In plain terms, it is when content fed to an AI system alters its behavior in ways its operators did not intend. The content can come from a user directly, or it can be hidden inside material the AI is asked to process, such as an email, a web page, a document or a log entry.

**Why it matters in a SOC.** Security AI tools read hostile content by design. That is their job. A triage assistant summarizes a phishing email. An enrichment tool reads a malicious web page. A log assistant reads whatever an attacker managed to write into a log. Every one of those inputs is potentially adversary-controlled.

**How to reduce the risk.** Treat all content processed by AI as untrusted. Limit what the AI tool is allowed to do based on its output: summarizing is low risk; executing changes is high risk. Keep a person between AI output and any consequential action. Separate tools that read hostile content from tools that hold privileged access.

### Risk 2: Data and model poisoning

**What it is.** OWASP describes data poisoning as occurring when pre-training, fine-tuning or embedding data is manipulated (OWASP, 2025). The effect can be a model that behaves normally in most cases and wrongly in specific ones.

**Why it matters in a SOC.** If a tool learns from your own alert history or analyst feedback, an adversary with long-term access could, in principle, influence what it learns. An intruder who is present for years, as advisory AA24-038A describes, has time to shape what normal looks like.

**How to reduce the risk.** Know where your tools' training and reference data come from. Control who can add to it. Keep versioned copies so you can roll back. Test tools against known examples after every update.

### Risk 3: The model and software supply chain

**What it is.** OWASP lists supply chain as a top risk (OWASP, 2025). AI tools depend on models, libraries, plug-ins, connectors and hosted services from third parties. NIST's govern and manage functions both address risks from third-party software, data and pre-trained models (NIST, AI RMF Core).

**Why it matters.** IBM's most common root causes of AI-related incidents were compromised connected apps, APIs or plug-ins and cloud misconfigurations affecting AI workloads, each at 27% (IBM and Ponemon Institute, 2026). That is a supply chain and configuration problem, not a model problem.

**How to reduce the risk.** Review the APIs, plug-ins and cloud settings around every AI workload. Inventory the service accounts and keys your AI tools use, and give each one only the access it needs. Ask vendors how they secure their models and dependencies, and get the answer in writing.

From the irregular warfare lens, this is the proxy problem again. A compromised supplier is an intermediary. Its access becomes the adversary's access.

### Risk 4: Over-reliance and excessive agency

**What it is.** Two related risks. OWASP lists excessive agency, meaning an AI system granted more ability to act than it needs, and misinformation, meaning output that is wrong but presented credibly (OWASP, 2025). The human counterpart is over-reliance: people trusting AI output without checking it.

**Why it matters in a SOC.** IBM found that among organizations with a SOC that deployed AI agents, 54% used them for automated response and containment (IBM and Ponemon Institute, 2026). Automated response can be valuable. It is also exactly where excessive agency hurts most. A tool that can disable accounts, isolate machines or change firewall rules can cause an outage as easily as it can stop an intrusion.

**How to reduce the risk.** Grant the minimum ability needed. Start every agent in recommend-only mode. Widen its authority only when tests and metrics show it behaves as intended, and keep an easy way for a person to step in. NIST's manage function calls for mechanisms to supersede, disengage or deactivate AI systems that perform inconsistently with intended use (NIST, AI RMF Core). Build that switch before you need it.

### Risk 5: Sensitive information disclosure and shadow AI

**What it is.** OWASP lists sensitive information disclosure as a top risk (OWASP, 2025). In practice, much of the disclosure risk comes not from sanctioned tools but from staff using unapproved ones. IBM reports that the share of incidents involving shadow AI more than doubled to 43% (IBM and Ponemon Institute, 2026).

**How to reduce the risk.** Give people an approved alternative that is good enough to use. Prohibition without an alternative drives usage underground. Pair the approved-tools list with clear data rules and with monitoring for unsanctioned AI services.

### Securing the AI: a short checklist

- Every AI tool is in the inventory, with an owner.
- Every AI tool's service accounts and keys are inventoried and least-privilege.
- Every AI tool that reads untrusted content is separated from tools that can take privileged action.
- Every consequential AI-suggested action passes through a person until evidence supports otherwise.
- Every AI tool can be switched off quickly by a named person.
- Every AI tool is included in authorized security testing.

That last point matters. IBM lists offensive security testing among factors associated with lower breach costs (IBM and Ponemon Institute, 2026). In our terms, that means authorized, scoped, written-permission testing of your own systems, including the AI-enabled workflows. Nothing else.
