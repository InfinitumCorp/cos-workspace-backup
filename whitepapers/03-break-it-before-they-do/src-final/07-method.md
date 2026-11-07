
## Part IV: Demand a method you can audit {#part-iv-method}

You do not need to know how to run a penetration test to buy a good one. You do need to know what a good method looks like from the outside, so you can tell a disciplined engagement from an improvised one.

The NCSC warns that, by their nature, "penetration tests cannot be entirely procedural, an exhaustive set of test cases cannot be drawn up. Therefore, the quality of a penetration test is closely linked to the abilities of the penetration testers involved" (NCSC, 2017/2022). Skill matters. A recognized method is what makes skill consistent, repeatable and auditable.

This part stays at the buyer's level. It describes the shape of the major public methodologies and what each should produce for you. It contains no techniques.

## The public standards

**NIST SP 800-115.** NIST's *Technical Guide to Information Security Testing and Assessment* was published in September 2008. Its stated purpose is "to provide guidelines for organizations on planning and conducting technical information security testing and assessments, analyzing findings, and developing mitigation strategies." NIST says it is "not intended to present a comprehensive information security testing or assessment program," but "an overview of the key elements" (NIST SP 800-115, 2008). It is old in technology terms. Its governance guidance, on planning, rules of engagement, legal review, data handling and post-test mitigation, has aged well. It includes a rules-of-engagement template in Appendix B.

**PTES.** The Penetration Testing Execution Standard organizes a test into seven sections: pre-engagement interactions, intelligence gathering, threat modeling, vulnerability analysis, exploitation, post exploitation and reporting (PTES). Its authors describe the arc as running "from the initial communication and reasoning behind a pentest" through "reporting, which captures the entire process, in a manner that makes sense to the customer and provides the most value to it" (PTES). Note what comes first: pre-engagement, the conversations about scope and rules. And note what comes last: a report written for the customer.

**OWASP.** For web applications, the OWASP Web Security Testing Guide (WSTG) describes itself as "the premier cybersecurity testing resource for web application developers and security professionals." Version 4.2 is the current release, with version 5.0 in development (OWASP WSTG). The OWASP Top 10:2025 is "a standard awareness document for developers and web application security" that "represents a broad consensus about the most critical security risks to web applications" (OWASP Top 10, 2025). A test of your web applications should be able to say how it covered each relevant category.

**CREST.** CREST's *A Guide to Penetration Testing* (December 2022) frames testing as a program, not an event: three main stages, preparation, testing and follow up, supported by 22 detailed steps (CREST, 2022). In the testing stage, the steps run from agreeing testing style and type, identifying constraints and producing scope statements, through establishing a management assurance framework and using an effective testing methodology, to reporting key findings (CREST, 2022). Follow up includes remediating weaknesses and evaluating testing effectiveness.

**NCSC.** The NCSC's model engagement follows a simple pattern: "Initial engagement, scoping, testing, reporting and follow up. There should be a severity rating for any issues found" (NCSC, 2017/2022).

**TIBER-EU.** For red teaming in regulated finance, TIBER-EU guidance and templates cover phases "such as initiation, scoping, threat intelligence, red-team testing (planning and reporting), blue team report creation and remediation plan creation" (ECB, TIBER-EU). Even if you are not a bank, the shape is instructive. Intelligence first. Remediation plan last.

## What the methods agree on

Read them side by side and the common shape is obvious.

| Stage | NIST SP 800-115 | PTES | NCSC model | CREST | What you should receive |
|---|---|---|---|---|---|
| **Before** | Planning (no testing occurs) | Pre-engagement interactions | Initial engagement, scoping | Preparation | Signed authorization package, scope, rules of engagement, test plan |
| **Understand** | Discovery | Intelligence gathering, threat modeling | Scoping | Research and planning | A short threat picture explaining why the scope looks the way it does |
| **Test** | Attack | Vulnerability analysis, exploitation, post exploitation | Testing | Identify and exploit vulnerabilities | Immediate notice of critical findings during the test |
| **Report** | Reporting | Reporting | Reporting | Report key findings | A report written for both leadership and engineers |
| **After** | Post-testing activities | — | Follow up | Follow up: remediate, improve | Root causes, remediation plan, retest |

Every serious method begins before testing and ends after it. If a proposal from a provider jumps straight to "testing days" and ends at "report delivered," something is missing.

## What a good report contains

The NCSC lists what a test report should include: "any security issues uncovered," "an assessment by the test team as to the level of risk that each vulnerability exposes the organisation or system to," "a method of resolving each issue found," "an opinion on the accuracy of your organisation's vulnerability assessment," and "advice on how to improve your internal vulnerability assessment process" (NCSC, 2017/2022). It recommends a debrief.

The last two items are the ones most reports leave out, and they are the ones that make a test an audit of your program rather than a list of bugs.

I would add four things a mid-size organization should insist on:

1. **An executive summary in plain language**, one page, saying what was tested, what was found, what it means for the business, and what to do first.
2. **Evidence sufficient to reproduce and verify**, handled under the data rules in your authorization, so your own engineers can confirm each finding and later confirm each fix.
3. **Root causes, not just symptoms.** Which process failure let each finding happen.
4. **A statement of limitations**: what was not tested, what time ran out on, and what scope exclusions were accepted.

## Severity, with judgment

The NCSC notes that testers commonly use the Common Vulnerability Scoring System, and that CHECK reports state risk as high, medium, low or informational. It adds an important caution: other mitigating controls "could minimise the effectiveness of a vulnerability, or the presence of additional vulnerabilities could have a synergistic effect," and "any deviation from associating a vulnerability with its standard rating should be documented and justified" (NCSC, 2017/2022).

Then it says the most important sentence in its guidance for buyers: "risk assessment and decisions on the application of fixes are your responsibility. The test team may not have had access to all details about a specific system or the potential business impact" (NCSC, 2017/2022).

The tester rates. You decide.

## Quality control on your side

You can check method quality without technical depth. Ask these questions of every engagement.

- Was the test plan written and approved before testing started?
- Did the provider tell you about critical findings during the test, or wait for the report?
- Do the findings map to the scope? Are there findings from outside scope? If so, how did that happen?
- Can your engineers reproduce each high-severity finding from the evidence given?
- Does the report state its limitations honestly?
- Did the testers comment on your own vulnerability assessment's accuracy?

> **The takeaway.** You do not need to know how to test. You need to know what a disciplined test looks like from outside: planned before, reported for the business, followed up after.

## What to do

- Require providers to name the public methodology they follow, and map their phases to the table above.
- Write your report requirements into the contract, including the NCSC's five items and the four additions.
- Hold a debrief for every test, with engineering owners in the room.

## What to measure

- Share of reports meeting your report requirements on first delivery.
- Share of high-severity findings your engineers could reproduce from the evidence provided.
- Number of reports with an explicit limitations section. The target is all of them.
