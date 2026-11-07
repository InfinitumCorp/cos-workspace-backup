
## Part VI: Test the sentries, not just the stone {#part-vi-detection}

Prevention fails. Every serious framework assumes it. The question is what happens next. Does anyone notice? Does anyone act?

Penetration tests mostly measure the wall. Red and purple exercises measure the sentries.

## The lesson from a mature organization

CISA published the findings of one of its own red team assessments in 2023. It is worth reading in full by anyone who runs a security program, and I will use it here only at the level of lessons, not techniques.

At the request of "a large critical infrastructure organization with multiple geographically separated sites," CISA conducted a red team assessment over a three-month period in 2022. The team "gained persistent access to the organization's network, moved laterally across the organization's multiple geographically separated sites, and eventually gained access to systems adjacent to the organization's sensitive business systems." Multifactor authentication prompts prevented access to one sensitive system (CISA AA23-059A, 2023).

Then the key sentence: "Despite having a mature cyber posture, the organization did not detect the red team's activity throughout the assessment, including when the team attempted to trigger a security response" (CISA AA23-059A, 2023).

Let that sink in. A mature organization, with real strengths, did not see a simulated intruder for months, even when the intruder tried to be seen.

CISA's advisory also lists what worked. "The organization conducts regular, proactive penetration tests and adversarial assessments and invests in hardening their network based on findings." From more than three million external in-scope addresses, the team found no easily exploitable services, which "forced the team to resort to phishing to gain initial access." Strong service account passwords, careful file shares, multifactor authentication on some sensitive systems and strong segmentation all slowed or blocked the team (CISA AA23-059A, 2023).

Two lessons. First, testing and hardening worked: the outer wall held, and the adversary had to go through people instead. Second, the sentries were the weak point. CISA's summary "highlights the importance of collecting and monitoring logs for unusual activity as well as continuous testing and exercises," and encourages organizations to "conduct regular testing within their security operations center" (CISA AA23-059A, 2023). It also recommends treating endpoint management systems, which "provide elevated access to thousands of hosts," as high value assets with additional restrictions and monitoring (CISA AA23-059A, 2023).

## When to red team

Red teaming is a test of maturity. It is wasted on an organization that has not done the basics. My readiness test, in my own judgment, is three yes answers:

1. Scanning and assessment are continuous, and Priority 1 findings are fixed on time.
2. There is a monitoring capability, in-house or managed, with someone accountable for responding around the clock.
3. Leadership is ready to hear that the monitoring missed things, and to fund the fixes.

If any answer is no, spend the budget on the gap instead.

## How to run one safely

The governance of a red team is more demanding than a penetration test, because fewer people know it is happening.

TIBER-EU's structure is a good model. It names five roles: the blue team, "whose prevention, detection and response capabilities are being tested without their foreknowledge"; a threat intelligence provider; the red-team testers; a control team, "a small team within the target entity whose members are the only ones there who know a test is happening and who lead and manage the test"; and, in its regulatory setting, an oversight team at the authority (ECB, TIBER-EU).

A mid-size organization will not have a regulator in the room. It still needs a control group. In my view the minimum is three people: an executive sponsor with authority over the whole scope, a senior security or IT leader who can deconflict in real time, and counsel. The control group holds the authorization, the stop, and the real-intruder clause from Part II.

NIST's guidance on covert testing applies with extra force: the plan must define how test activity detected by security staff is handled, "including as the escalation processes to be followed," so that it "does not trigger reporting of security breaches to external parties" (NIST SP 800-115, 2008). If your monitoring is outsourced, decide in advance whether the provider is in the control group or among the tested, and make sure the contract allows either.

## Purple: learning in the open

For many mid-size organizations, the better first step is a purple exercise. The attackers and defenders agree on a set of behaviors based on threat intelligence. The red side performs each one, safely and within authorization. The blue side records what was logged, what alerted and what was missed. Then both sides fix the gaps together and run it again.

The NCSC describes a related idea: "scenario driven testing of detection and response capability," in which "the aim is to also gauge the detection and response capabilities your organisation has in place" (NCSC, 2017/2022).

The output of a purple exercise is not a report. It is a set of detections that now work, and a list of those that still do not.

## The detection scorecard

Whether you run red or purple, score the sentries on the same five questions for each agreed behavior:

| Question | Outcome to record |
|---|---|
| **Was it logged?** | Yes, partly, or no, and in which system |
| **Did it alert?** | Yes or no, and how long after the activity |
| **Did a person look?** | Yes or no, and how long after the alert |
| **Was the response right?** | Contained, escalated, ignored, or misclassified |
| **What changes?** | The fix to logging, detection, process or staffing |

Track the scorecard over time. Your goal is fewer "no" answers each round. IBM's finding that breach lifecycles over 200 days cost more on average than shorter ones is the business case for every row (IBM and Ponemon Institute, 2026).

## The machine-speed question

The public data hints that testing itself is changing. IBM reports that, among organizations deploying AI agents in their security operations centers, only 18% used them for vulnerability scanning and management, and that in follow-on research more organizations planned to deploy agents for penetration testing (52% against 33%) and for vulnerability scans and management (37% against 18%) (IBM and Ponemon Institute, 2026). These are stated plans, not results.

Automation will make some testing faster and cheaper. It does not change any rule in this paper. An automated test still needs written authorization, a scope, rules of engagement and a stop. A tool that can act needs tighter rules, not looser ones.

> **The takeaway.** A wall nobody watches is only a delay. Test whether the sentries see and act. Start with purple. Red team only when the basics hold.

## What to do

- Score your detection with a purple exercise on three to five behaviors drawn from current threat intelligence.
- Define a control group and covert-test procedures before any red team.
- Treat systems that grant administrative access at scale, such as endpoint management, as crown assets in scope.
- Apply the same authorization rules to any automated or AI-assisted testing.

## What to measure

- Share of agreed behaviors that were logged, alerted and answered, per round.
- Median time from simulated activity to human response.
- Number of detection gaps closed between rounds.
