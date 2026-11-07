## Part VII: People and the workforce {#part-vii}

Technology does not defend anything by itself. People do.

### The workforce reality

Recall the ISC2 numbers. 67% of respondents reported a staffing shortage. 90% reported one or more skills gaps. Among organizations with critical or significant skills gaps, 22% reported a material breach, compared with 17% of all respondents who shared that information (ISC2, 2024).

And 45% said their teams were already using generative AI in their tools, mostly to augment common operational tasks, write reports and support incident reporting (ISC2, 2024).

So AI is already in the hands of a stretched workforce. The question is whether it is making that workforce stronger or just busier.

### What changes for analysts

When AI enters a security team, the analyst's job changes in three ways.

**From producing to reviewing.** Less time writing the first draft of a report, a query or an alert summary. More time judging whether a draft is right. Reviewing well is a skill. It has to be taught.

**From reading everything to deciding what matters.** Triage support reduces the reading load. That frees time for the judgment calls: is this real, does it matter, what do we do now.

**From operator to supervisor.** As automation widens, analysts become supervisors of systems that act. Supervision requires understanding what the system can do, where it fails, and when to step in.

### The over-reliance trap

The greatest people risk in AI-assisted security is not job loss. It is skill loss.

If junior analysts never investigate an alert from scratch because the assistant always does the first pass, they never build the instincts that let them spot when the assistant is wrong. Five years later, you have a team that can supervise a tool but cannot do the work without it.

That is a resilience problem. And resilience, as Part I showed, is the core of countering irregular pressure.

### What I recommend for people

These are my recommendations, informed by the sources in this paper.

1. **Keep manual skills alive.** Have analysts regularly work cases without AI assistance, and compare their conclusions with the tool's.
2. **Teach review as a skill.** Train analysts to check sources, test queries against known examples and challenge confident language.
3. **Make overrides normal.** An analyst who overrides the AI should be thanked, not questioned. Overrides are your best quality data.
4. **Train for the AI-specific risks.** Every analyst should understand prompt injection, over-reliance and data rules in plain terms.
5. **Rehearse decisions, not just tools.** Run tabletop exercises in which the AI tool is wrong, unavailable or compromised. See whether the team can still function.
6. **Extend awareness beyond the SOC.** Influence operations target everyone. Executives, finance staff and assistants are on the front line of impersonation and fraud. Give them simple verification procedures and the authority to use them.

### Building the bench

Mid-size organizations rarely win bidding wars for experienced security talent. So build it.

Look inside first. System administrators, network engineers and help-desk staff already know your environment, your users and your quirks. That knowledge is exactly what an analyst needs to judge whether an AI-flagged deviation is normal. Pair one of them with your security lead for a few hours a week, and you have started a pipeline.

Use AI as a tutor, not a crutch. An assistant that explains why an alert matters, what an ATT&CK technique means or how a query works can shorten the learning curve. The rule from earlier still applies: the learner must also do the work without it.

Write things down. Every playbook, use-case card and after-action review is training material for the next person. A team that documents well survives turnover. A team that keeps everything in one person's head does not.

And bring in outside help deliberately, for specific gaps and specific periods, with a plan to transfer the knowledge in-house. That is the same principle NATO applies with its tailored support teams: the owner keeps responsibility; specialists help on request.

### Who does what

Clarity of authority is a resilience measure in its own right. Ambiguity about who decides is exactly what hybrid pressure exploits. The table below is a simple allocation of responsibilities I recommend for a mid-size organization adopting AI in security operations. Adjust titles to your structure. Keep the principle: every decision has one owner.

| Role | Responsibilities for AI in security operations |
|---|---|
| Executive sponsor | Accepts residual risk in writing; approves budget; receives quarterly metrics; owns the decision to widen automation |
| Accountable owner for AI in security | Maintains approved-tools list, inventory and use-case cards; approves pilots; holds the off switch |
| Security operations lead | Runs pilots; reviews AI quality weekly; manages analyst training and manual-skill exercises |
| Analysts | Review every AI recommendation; record overrides and reasons; escalate anything uncertain |
| IT and system owners | Approve patch order and exceptions; implement fixes; maintain logging on their systems |
| Legal and privacy | Review data rules, vendor terms, decoy programs and external notifications |
| All staff | Use approved tools only; follow verification procedures for payment and identity requests; report suspicious messages |

### A note on leadership

Leaders set the tone. NIST's govern function includes executive leadership taking responsibility for decisions about risks associated with AI system deployment (NIST, AI RMF Core).

That is not a delegation. A leader who says "the security team handles AI" has not governed it.

Ask your security lead three questions every quarter. What is AI doing in our security program? What did it get wrong? Who checked?

## Part VIII: Metrics that matter {#part-viii}

No baseline, no proof. It is that simple.

Before you pilot anything, write down today's numbers. Then measure the same way after. Without that, every claim of improvement is an opinion.

### Principles

**Measure outcomes, not activity.** The number of alerts processed is activity. The time a real intrusion went unnoticed is an outcome.

**Measure quality alongside speed.** Faster triage that misses true incidents is a regression, not an improvement.

**Measure the AI, not just the team.** Track how often analysts override the tool, and why.

**Compare with yourself.** Survey medians, including the ones in this paper, are context. Your own baseline is the benchmark.

### A starter metric set

The table below is a starter set I recommend for mid-size organizations. Choose a handful. Measure them consistently.

| Area | Metric | Why it matters |
|---|---|---|
| Exposure | Median days to remediate KEV-listed vulnerabilities on internet-facing systems | Exploitation is the leading way in (Verizon, 2026) |
| Exposure | Count of open KEV-listed vulnerabilities | Direct measure of easy routes left open |
| Exposure | Share of technology beyond supported lifecycle, with a plan | End-of-life systems are a recurring weakness (CISA et al., 2024) |
| Detection | Share of critical systems sending logs to a central store | No logs, no detection |
| Detection | Time from alert to first human decision | Speed of the first look |
| Response | Time to identify and contain confirmed incidents | The outcome IBM measures across its sample |
| AI quality | Analyst override rate, with reasons | Shows where the tool is wrong or unclear |
| AI quality | True incidents first suggested for closure | The single most important AI failure metric |
| AI governance | Share of AI tools in inventory with an owner and use-case card | Governance coverage |
| AI governance | Detected use of unapproved AI services | Shadow AI exposure |
| People | Analyst hours spent on reporting | Where AI drafting should help |
| People | Exercises completed with an AI-failure injection | Resilience of the team |

### Reporting metrics upward

Boards do not need twelve metrics. They need three or four, explained plainly, with direction over time.

I suggest: open KEV-listed vulnerabilities on internet-facing systems and time to fix them; time to contain confirmed incidents; AI governance coverage; and one sentence on what the AI got wrong this quarter and what was done about it.

That last item builds trust. A program that reports its own failures is a program leadership can believe.

### Measurement pitfalls

A few traps catch almost every team that starts measuring AI in security operations.

**Measuring only what the tool reports.** Vendors are happy to tell you how many alerts their product handled. That is activity. Measure the outcomes in your own data.

**Changing two things at once.** If you introduce an AI tool and reorganize the team in the same month, you will not know which change caused the result. Stagger changes when you can, and note them when you cannot.

**Ignoring the denominator.** Fewer incidents may mean better defense. It may also mean worse detection. Pair every count with a coverage measure, such as the share of critical systems sending logs.

**Rewarding speed alone.** If analysts are judged only on how fast they close alerts, they will close alerts fast. Pair speed metrics with quality metrics, such as the number of true incidents first suggested for closure.

**Treating survey figures as targets.** The figures from IBM, Verizon and ISC2 in this paper describe their samples. Your goal is steady improvement against your own baseline, not matching a global average.

Measurement done well is a discipline, not a dashboard. It is how a stretched team proves to itself, and to its leadership, that it is getting stronger.

## Part IX: Illustrative scenarios {#part-ix}

The three scenarios below are **illustrative and hypothetical**. They do not describe any real organization, client or incident. No figures in them are measured results. They exist to show how the ideas in this paper fit together in practice.

<div class="scenario" markdown="1">

**Illustrative scenario A (hypothetical): The quiet administrator account**

*Setting.* A regional services company with about 600 staff and a three-person security team. Logs from domain controllers and the VPN are centralized. The team has piloted an AI assistant for log analysis, approved under its governance rules and limited to read-only access.

*What happens.* The assistant's weekly baseline summary notes that an IT administrator account has been signing in through the VPN at consistent times, but from an address range not seen before, and using built-in administrative tools on a file server where that account has not previously been active. No single alert fired. Every action stayed under existing thresholds.

*What the people do.* An analyst reviews the summary, checks the raw logs directly and confirms the pattern. She contacts the administrator by phone, using a number from the staff directory rather than one in an email. The administrator has not been working remotely. The team escalates to incident response, follows its plan, and the incident owner decides on containment steps.

*Lessons.* The assistant did not detect the intrusion. It surfaced a deviation from a baseline that only existed because logging was centralized. The person decided. Verification used an out-of-band channel, an influence-resistant habit. This is the threshold-management problem from Part I, met by baselines and judgment rather than by a single rule.

</div>

<div class="scenario" markdown="1">

**Illustrative scenario B (hypothetical): The patch list nobody trusted**

*Setting.* A mid-size manufacturer with hundreds of open vulnerability findings and a long-standing argument between security and operations about what to patch first.

*What happens.* The security lead pilots AI-assisted prioritization. The tool combines KEV status, internet exposure and asset importance, and produces one ranked list per system owner, with a short explanation for each item. Two internet-facing remote-access appliances with KEV-listed vulnerabilities rise to the top. One is past its supported lifecycle.

*What the people do.* System owners review the lists. Operations flags one server that cannot be rebooted during a production run; the owner documents an exception with a compensating control and an expiry date. The appliances are patched within the week. Leadership approves a replacement plan for the end-of-life device.

*Lessons.* The value was not the score. It was a shared, explained list that owners could accept. The AI ranked; people approved. The team denied the adversary the cheapest route in, the asymmetric move discussed in Parts I and IV. The team now tracks time to remediate KEV-listed vulnerabilities as a board metric.

</div>

<div class="scenario" markdown="1">

**Illustrative scenario C (hypothetical): The helpful assistant that read the wrong email**

*Setting.* A professional services firm uses an AI assistant to summarize reported phishing emails for its small security team. During the pilot, the assistant also had permission to add sender domains to a block list automatically.

*What happens.* A reported email contains hidden text crafted to manipulate any AI system that reads it. The assistant's summary describes the message as benign, and the instructions in the hidden text attempt to steer the assistant's output. Because the block-list permission existed, the team realizes that a similar message could have caused the assistant to take an unwanted action.

*What the people do.* An analyst notices the summary does not match the message's obvious signs of phishing. The team reviews the design under its governance rules, removes the assistant's ability to change the block list, and separates the summarizing function from any function that takes action. They add this case to analyst training and to the scope of their next authorized security test.

*Lessons.* This is prompt injection, the first risk on the OWASP 2025 list, meeting excessive agency. The fix was architectural, not heroic: reduce the tool's authority, keep a person between output and action, and test the workflow. Over-reliance would have missed it. A trained reviewer caught it.

</div>

Across all three scenarios, the pattern is the same. Fundamentals first. AI as an assistant to judgment, not a replacement for it. Clear authority. Measured results.
