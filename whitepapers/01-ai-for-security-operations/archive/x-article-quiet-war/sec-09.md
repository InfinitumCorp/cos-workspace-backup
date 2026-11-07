# Recommendations

Here is the approach I recommend.

Add capability only when the controls and the evidence are in place. Timelines depend on your team size, your tooling and your risk appetite. The phases below are a sequence first and a schedule second.

## The six steps

**Phase 0: Govern before you buy.** Name one accountable owner for AI in security. Publish an approved-tools list and a plain rule on what data may go into AI services. Use the NIST AI RMF to structure risk decisions. Put role-based access and multifactor authentication on AI models and the data behind them. IBM found that 92% of organizations with an AI-related breach lacked proper AI access controls (IBM and Ponemon Institute, 2026).

**Phase 0: Measure a baseline.** Write down today's numbers: time to triage an alert, time to identify and contain incidents, time to remediate KEV-listed vulnerabilities, analyst hours spent on reporting. No baseline, no proof. It is that simple.

**Phase 1: Pilot with analysts in the loop.** Start small and low-risk: alert summaries, indicator enrichment, report drafts, help writing log queries. AI proposes. A person decides. Keep a record of AI outputs and analyst overrides so you can review quality.

**Phase 2: Point AI at exposure.** Exploitation of vulnerabilities is now the leading way into breaches, so use AI to help prioritize fixes. Combine KEV status, internet exposure and asset importance, and map findings to ATT&CK techniques. System owners keep patch approval. And expect more patches to review, as Verizon does.

**Phase 2: Secure the AI itself.** Review the APIs, plug-ins and cloud settings around every AI workload. IBM's most common root causes were compromised connected apps, APIs or plug-ins and cloud misconfigurations. Inventory the service accounts and keys your AI tools use, and give each one only the access it needs.

**Phase 3: Test it, then widen it.** Commission authorized vulnerability assessments and penetration tests that include your AI-enabled workflows, scoped and approved in writing. IBM lists offensive security testing among factors associated with lower breach costs. Extend automation, such as containment steps, only where tests and metrics show it behaves as intended. Keep an easy way for a person to step in.

> **The takeaway.** Govern first. Measure second. Point AI at the work that shrinks your exposure. Let evidence, not enthusiasm, decide how much autonomy it gets.

## The first 90 days

The first 90 days are about foundations and a safe, measured pilot. Here is a realistic plan for a mid-size organization. Adjust the pace to your capacity.

### Days 1 to 30: Govern and baseline

- Name the accountable owner for AI in security operations.
- Inventory AI tools already in use, including AI features switched on inside existing security and productivity products.
- Publish an approved-tools list and a one-page data rule.
- Confirm multifactor authentication and role-based access on every approved AI tool.
- Record baseline metrics from Part VIII: KEV remediation time, open KEV count on internet-facing systems, logging coverage, time to first decision on alerts, reporting hours.
- Fix the obvious: patch internet-facing systems with KEV-listed vulnerabilities; confirm central logging for authentication, VPN and domain controllers; identify end-of-life technology.

### Days 31 to 60: Pilot low-risk use cases

- Choose two pilot use cases. I suggest report drafting and alert-triage summaries.
- Write a use-case card for each: purpose, inputs, outputs, reviewer, prohibited actions, off switch.
- Run in recommend-only mode. No AI-driven closures, no AI-driven changes.
- Log every AI output and every analyst override.
- Hold a weekly fifteen-minute quality review.

### Days 61 to 90: Measure, decide, extend to exposure

- Compare pilot metrics against baseline.
- Decide, in writing, whether each pilot continues, changes or stops.
- Begin AI-assisted vulnerability prioritization in recommend-only mode, with system owners approving patch order.
- Run one tabletop exercise in which an AI tool is wrong or unavailable.
- Brief leadership with three or four metrics and one honest note on what the AI got wrong.

## The first 12 months

After 90 days, the work becomes a cycle: extend carefully, test, measure, adjust.

| Period | Focus | Key activities | Gate to move on |
|---|---|---|---|
| Months 1–3 | Govern, baseline, pilot | Owner named; tools inventoried; data rule; baseline metrics; two low-risk pilots; KEV and logging fundamentals | Pilots measured against baseline; written decision on each |
| Months 4–6 | Exposure and log analysis | AI-assisted vulnerability prioritization in production with owner approval; log-analysis assistant with approved data only; enrichment with source discipline | KEV remediation time improving against baseline; query corrections tracked |
| Months 7–9 | Secure and test the AI | Review APIs, plug-ins and cloud settings around AI workloads; least-privilege service accounts; authorized assessment covering AI-enabled workflows | Test findings remediated or accepted in writing |
| Months 10–12 | Selective automation and early warning | Narrow, reversible automation where evidence supports it; consider deception and early-warning program with legal review; annual governance review | Override and error rates acceptable; off switch tested |

A few rules hold across the whole year.

- **Every widening of authority is a decision**, made by the accountable owner, documented, and reversible.
- **Every AI incident triggers a review**, however small.
- **Every quarter, report to leadership** on metrics and on what went wrong.
- **Every year, re-run the maturity self-assessment** below.

## Maturity self-assessment checklist

Use this checklist with your security, IT and leadership teams. Answer honestly. A "no" is not a failure. It is a work item.

Score each item: 0 = not in place, 1 = partly in place, 2 = fully in place and evidenced. The levels at the end are my rough guide, not a formal standard.

### Governance

- [ ] An accountable owner for AI in security operations is named and has authority to pause or retire tools.
- [ ] An approved AI tools list exists and staff know where to find it.
- [ ] A written rule states what data may and may not go into AI services.
- [ ] Every AI-enabled tool is inventoried with an owner, data access and service accounts.
- [ ] Each AI use case has a one-page card with purpose, reviewer, prohibited actions and off switch.
- [ ] AI risk decisions reference the NIST AI RMF and, for generative tools, NIST AI 600-1.

### Fundamentals

- [ ] Internet-facing systems are inventoried.
- [ ] KEV-listed vulnerabilities on internet-facing systems are tracked and prioritized.
- [ ] Phishing-resistant multifactor authentication protects remote access and administrators.
- [ ] Authentication, VPN, domain controller and critical application logs go to a central store.
- [ ] Technology beyond its supported lifecycle is identified with a replacement or isolation plan.
- [ ] Backups of critical systems are tested by actual restoration.

### AI in operations

- [ ] Baseline metrics were recorded before any AI pilot.
- [ ] AI outputs and analyst overrides are logged.
- [ ] No alert is closed and no change is made on AI recommendation alone, unless an evidence-based decision allows it for a narrow case.
- [ ] Vulnerability prioritization uses KEV status, exposure and asset importance, with owner approval.
- [ ] Threat-intel enrichment cites sources, and attribution claims are treated as low confidence by default.

### Securing the AI

- [ ] APIs, plug-ins and cloud settings around AI workloads have been reviewed.
- [ ] AI service accounts and keys follow least privilege.
- [ ] Tools that read untrusted content are separated from tools that take privileged action.
- [ ] Each AI tool can be switched off quickly by a named person, and that has been tested.
- [ ] Authorized security testing includes AI-enabled workflows.
- [ ] Use of unapproved AI services is monitored.

### People and resilience

- [ ] Analysts regularly work cases without AI assistance.
- [ ] Analysts are trained on prompt injection, over-reliance and data rules.
- [ ] A tabletop exercise with an AI-failure injection has been run in the past year.
- [ ] Staff outside security have simple verification procedures for payment and identity requests.
- [ ] Leadership receives quarterly metrics including what the AI got wrong.

### Reading your score

There are 28 items, for a maximum of 56 points.

- **0–19: Foundational.** Focus on fundamentals and governance before expanding AI use.
- **20–39: Developing.** Pilots are reasonable. Prioritize exposure reduction and securing the AI.
- **40–56: Established.** Consider selective automation and early-warning programs, with continued testing.

Whatever your score, the next step is the same: pick the three lowest items that matter most to your risk, assign owners and dates, and re-score in a quarter.
