
## Part V: From findings to fixes. Repair the wall, then check the repair {#part-v-findings-to-fixes}

A test that ends with a report has failed. A test that ends with repairs, verified, has succeeded.

NIST puts it directly: "a security test is much more valuable if it also results in a mitigation strategy being developed and implemented." Mitigation recommendations, "including the outcome of the root cause analysis, should be developed for each finding" (NIST SP 800-115, 2008). CREST's research found organizations struggle with "remediating system vulnerabilities effectively" (CREST, 2022). This is where most programs leak value.

## The prioritization problem

You will always have more findings than time. Verizon's data makes that concrete. Even top performers fix only 30% to 40% of KEV instances in the first week after detection, "so choosing the correct ones to patch really is the key strategy" (Verizon, 2026).

So how do you choose? Four public tools help. None is enough alone.

**Severity: CVSS.** The Common Vulnerability Scoring System, maintained by FIRST and now at version 4.0, describes the technical severity of a vulnerability (FIRST CVSS v4.0). Severity tells you how bad a flaw could be. It does not tell you whether anyone is using it.

**Known exploitation: CISA KEV.** CISA says it "maintains the authoritative source of vulnerabilities that have been exploited in the wild" and that organizations "should use the KEV catalog as an input to their vulnerability management prioritization framework" (CISA KEV, 2026). The catalog version dated October 30, 2026 lists 1,766 entries, of which 361 are flagged as known to have been used in ransomware campaigns (CISA KEV, 2026). For U.S. federal civilian agencies, Binding Operational Directive 22-01 set default remediation timelines from 2021: within six months for KEV vulnerabilities with a CVE ID assigned before 2021, and within two weeks for all others (CISA BOD 22-01). On June 10, 2026, CISA revoked it and replaced it with BOD 26-04, *Prioritizing Security Updates Based on Risk*. The new directive sets the urgency of remediation from four variables: whether the asset is publicly exposed, whether the vulnerability is on the KEV catalog, whether an adversary can automate exploitation, and whether exploitation gives partial or total control. CISA says its timeline table is "informed by the SSVC system," and its most urgent tier requires action within three days plus a forensic triage to check whether the system is already compromised (CISA BOD 26-04, 2026). Private organizations are not bound by either directive. The logic of the new one is a useful model: exposure and exploitation first, everything else after.

**Likelihood: EPSS.** FIRST's Exploit Prediction Scoring System "estimates the probability that a published CVE will be exploited in the wild in the next 30 days," published daily for every CVE as a probability between 0 and 1 (FIRST EPSS). It is an estimate from a model. Treat it as a signal, not a verdict.

**Decision: SSVC.** CISA and Carnegie Mellon's Software Engineering Institute developed Stakeholder-Specific Vulnerability Categorization, a methodology that "accounts for a vulnerability's exploitation status, impacts to safety, and prevalence of the affected product." CISA's own decision tree sorts vulnerabilities into four decisions: Track, Track*, Attend and Act (CISA SSVC). The value of SSVC is that it ends in an action, not a number.

## Where the sources point in different directions

The prioritization signals do not always agree, and Verizon's data adds a twist worth knowing.

KEV is a list of things that have been exploited. Verizon calls it "a timestamp and not a timeline": it "marks when a vulnerability reaches a critical mass of exploitation in the wild" (Verizon, 2026). Verizon's modeling of re-exploitation found that "the longer it's been since a vulnerability has been exploited, the less likely it is to be exploited again soon": the probability "drops by roughly half at 30 days, again at 90 days and again by half around nine months" (Verizon, 2026). It suggests that, faced with a choice between an older KEV entry with no recent activity and a non-KEV vulnerability with recent exploitation in your threat intelligence, "focusing on the one with recent activity could be a smarter bet." Verizon also cautions that automation of vulnerability discovery and exploit development by generative AI tooling "could upend" that pattern (Verizon, 2026).

At the same time, Verizon found that 80% of the "Persistent" exploitation category were older vulnerabilities, giving about two years' advance notice (Verizon, 2026). Old does not mean quiet.

My reading: KEV tells you what must be on the list. Exploitation recency and likelihood help you order the list. Your own context decides. Is it on the edge? Does it touch a crown asset? Is there a compensating control?

## A simple ordering rule

For a mid-size team, I suggest a plain rule, adapted from the sources above. It is my synthesis, not a standard.

| Priority | Condition | Target |
|---|---|---|
| **1. Now** | Confirmed exploitable by your tester, or KEV-listed, **and** internet-facing or on a path to a crown asset | Fix or isolate within days, and check whether the system is already compromised. Pre-authorize emergency change |
| **2. Next** | KEV-listed or high exploitation likelihood, internal | Fix within your short service level, measured in days to a few weeks |
| **3. Planned** | High severity, no exploitation evidence, limited exposure | Fix in the normal cycle |
| **4. Accept or track** | Low severity, no exposure, or fully mitigated | Record a risk acceptance with an owner and a review date |

Write the targets down. Publish them to the system owners. Measure against them.

## Root cause: fix the process, not just the server

Individual findings are symptoms. NIST says "identifying the root cause of vulnerabilities is key to improving the organization's overall security posture because a root cause can often be traced to program-level weaknesses," and lists common root causes beginning with "insufficient patch management, such as failing to apply patches in a timely fashion or failing to apply patches to all vulnerable systems" (NIST SP 800-115, 2008). It notes that recommendations may be technical, such as "applying a particular patch," and nontechnical, addressing "the organization's processes," such as "updating the patch management process" (NIST SP 800-115, 2008).

For every high-severity finding, ask three questions:

1. **Why did it exist?** A missing patch, a default setting, an over-privileged account, a process gap.
2. **Why did we not know?** Was it invisible to our scanners, ignored in our queue, or outside our inventory?
3. **Where else does the same cause apply?** If one appliance was missed, which others share its owner, its patch process or its blind spot?

The third question is where a single finding becomes ten fixes.

## The remediation register

Every finding goes into one register, with these fields at minimum:

- Finding, severity as reported, and your own risk rating.
- Affected systems and the crown assets they lead to.
- Root cause and the process change it implies.
- Named owner, not a team.
- Target date, based on your priority rule.
- Status: open, in progress, fixed pending retest, verified, or risk accepted.
- For risk acceptance, who accepted it, why, and when it will be reviewed.

The NIST Cybersecurity Framework expects exactly this loop. Its Improvement category includes "Improvements are identified from security tests and exercises, including those done in coordination with suppliers and relevant third parties" (NIST CSF 2.0, 2024, ID.IM-02).

## Retest: the step most programs skip

"Fixed" is a claim. A retest is the evidence.

Agree a retest in the original contract, so that it is priced and scheduled rather than negotiated later. Retest every Priority 1 and 2 finding. Where root cause analysis produced a process change, test whether the process now works, not just whether the one server was patched.

Then close the loop with the next scan. A finding that reappears in three months tells you the fix did not stick. That is a process failure, and it belongs back in the register.

## Measure the program, not just the findings

The strongest signal of a healthy program is repeat findings falling over time. CREST's guide lists "evaluate penetration testing effectiveness" as a follow-up step (CREST, 2022). The NCSC's ideal, that you know what testers will find before they find it, gives you a direct measure: what share of the test's findings were already in your register (NCSC, 2017/2022)?

> **The takeaway.** Rank with evidence. Fix the cause, not just the symptom. Retest before you say "fixed." Measure whether the same findings come back.

## What to do

- Adopt a written prioritization rule that uses KEV, exploitation likelihood and your own exposure.
- Put every finding in one remediation register with a named owner and date.
- Run root cause analysis on every high-severity finding and apply the "where else" question.
- Contract for retesting up front.

## What to measure

- Median days to fix Priority 1 findings, against your target.
- Share of findings verified by retest.
- Repeat-finding rate from one test to the next.
- Share of test findings already in your own register before the test.
