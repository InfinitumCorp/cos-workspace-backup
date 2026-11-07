# Recommendations {#recommendations}

Here is the plan.

It is not glamorous. It is built around layers, dispersion and redundancy, with no single point that loses the position when it fails. CSIS describes the same logic for communications: dispersed nodes and resilient meshes that keep working "even if multiple nodes go dark" (CSIS, 2025a).

Add capability only when the controls and the evidence are in place. Timelines depend on your team size, your tooling and your risk appetite. The phases below are a sequence first and a schedule second.

## The six steps

**Phase 0: Govern before you buy.** Name one accountable owner for AI in security. Publish an approved-tools list and a plain rule on what data may go into AI services. Use the NIST AI RMF to structure risk decisions. Put role-based access and multifactor authentication on AI models and the data behind them. IBM found that 92% of organizations with an AI-related breach lacked proper AI access controls (IBM and Ponemon Institute, 2026).

**Phase 0: Measure a baseline.** Write down today's numbers: time to triage an alert, time to identify and contain incidents, time to remediate KEV-listed vulnerabilities, analyst hours spent on reporting. No baseline, no proof. It is that simple.

**Phase 1: Pilot with analysts in the loop.** Start small and low-risk: alert summaries, indicator enrichment, report drafts, help writing log queries. AI proposes. A person decides. Keep a record of AI outputs and analyst overrides so you can review quality.

**Phase 2: Point AI at exposure.** Exploitation of vulnerabilities is now the leading way into breaches, so use AI to help prioritize fixes. Combine KEV status, internet exposure and asset importance, and map findings to ATT&CK techniques. System owners keep patch approval. And expect more patches to review, as Verizon does.

**Phase 2: Secure the AI itself.** Review the APIs, plug-ins and cloud settings around every AI workload. IBM's most common root causes were compromised connected apps, APIs or plug-ins and cloud misconfigurations. Inventory the service accounts and keys your AI tools use, and give each one only the access it needs.

**Phase 3: Test it, then widen it.** Commission authorized vulnerability assessments and penetration tests that include your AI-enabled workflows, scoped and approved in writing. IBM lists offensive security testing among factors associated with lower breach costs. Extend automation, such as containment steps, only where tests and metrics show it behaves as intended. Keep an easy way for a person to step in.

> **The takeaway.** Govern first. Measure second. Point AI at the work that shrinks your exposure. Let evidence, not enthusiasm, decide how much autonomy it gets.

## What the battlefield teaches the plan

Each lesson from The modern battlefield maps to a part of the plan. Use this as a check on your own program.

| Battlefield lesson | What it teaches | Where it lands in the plan |
|---|---|---|
| Persistence beats brilliance | Plan a campaign, protect your people, fund year two | 12-month roadmap; staffing and workload metrics; AI for repetitive work only |
| Cheap mass versus exquisite systems | Answer volume with layers and cheap automated controls | KEV-first patching; MFA; email controls; AI triage at volume, human decision |
| You are being watched | Know what is visible, reduce it, build your own sensors | Asset and exposure inventory; logging coverage; attack-surface review |
| Signals can be jammed and spoofed | Verify out of band; keep a second source | Call-back rules; trusted time; cross-checking alerts; model input treated as untrusted |
| Measure, countermeasure, repeat | Controls decay; schedule the re-test | Quarterly detection review; re-baselining; AI tool reviews; exercises |
| The rear area is not safe | Your suppliers and platforms are terrain | Dependency map; vendor evidence; offline copies; manual fallbacks |
| Decentralize decisions, protect the network | Pre-authorize; keep comms that do not depend on what you defend | Written decision rights; out-of-band incident channel; AI as one node, not the spine |

And the dead reckoning check, to run each quarter:

1. **Last known position.** Is your baseline current?
2. **Heading.** Are your top priorities written down and still the right ones?
3. **Speed and time.** Do you know your time to detect, contain and fix, and do you trust your time source?
4. **A second source.** For each critical signal, is there an independent check?
5. **A fix.** When did you last re-verify against reality, and correct course?

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

# Conclusion {#conclusion}

The research agrees on direction.

Attackers are faster. Known vulnerabilities stay open too long. Security teams are short of people and skills. And organizations that use AI and automation extensively report lower costs and faster response.

It agrees on risk, too. AI systems and unsanctioned AI use create new exposure when access control and governance lag behind adoption.

The irregular warfare lens explains why this matters so much. Your opponents, whatever their motive, behave the way doctrine describes. They work indirectly. They avoid attribution. They impose costs asymmetrically. They stay under your thresholds and exploit the seams between your teams, your suppliers and your decisions. AI gives them more speed, scale and intensity.

The public analysis of the modern battlefield points the same way. Persistence. Observation. Cheap mass. Jammed and spoofed signals. Supply lines that are never safe (CSIS, 2025a; CSIS, 2025b). Your organization is not at the front. But it works in the same electromagnetic and informational weather.

You will not win that contest by matching them effort for effort.

When the signal fails, you navigate by dead reckoning. You know your last position. You know your heading. You keep a second source. You correct when you can.

You win it the way resilient institutions have always won it. Protect what matters most. Deny the easy routes. Organize so that decisions are clear and fast. Learn faster than the other side.

So for a mid-size organization, the winning move is neither to avoid AI nor to hand it the keys. Adopt it in stages. Govern, measure, pilot with people in the loop, shrink your exposure, secure the AI itself, and widen automation as the evidence supports it. Done this way, AI stops being another tool to manage and becomes one integrated part of your security program.

That is what practical, integrated security looks like.

Infinitum Corporation helps organizations take these steps in a way that fits their size, systems and risk appetite. I make no promise about the outcome any organization will achieve, and every figure in this paper belongs to the source cited.

Don't take my word for it. Read the sources, then decide.

This is the first paper in a series. The next two are *Trenches and Drones: Network Defense for a War of Attrition* and *Break It Before They Do: Authorized Hacking for Organizations Under Siege*. Both build on the foundation laid here.

Let's stay engaged. Call us at (202) 980-9300, or visit https://www.theinfinitumcorporation.com. Dialogue is key.

<!-- BODY-END -->
