
# Recommendations {#recommendations}

Here is the plan.

It is not glamorous. It is a garrison's routine: know the walls, get permission, look every day, test properly, repair, check the repair, and drill the sentries. The eight parts above each end with their own actions. This section puts them in order.

Timelines depend on your team size, your providers and your risk appetite. The phases below are a sequence first and a schedule second.

## The seven moves

| # | Move | Part it draws on | First proof that it is working |
|---|---|---|---|
| 1 | **Know your walls.** Name crown assets, build the inventory, compare it with the outside-in view. | III | The outside-in list matches the register |
| 2 | **Put permission in writing.** Standard authorization package, third-party consents, legal review, stop and real-intruder clauses. | II | Every test in the past year started with a complete signed package |
| 3 | **Scan continuously, assess regularly.** Daily external scanning, scheduled validated assessment. | I, V | Penetration test findings were mostly already in your register |
| 4 | **Test what an adversary would actually do.** Scope from the crown outward along the routes the evidence says are used. | III, IV | Crown assets and the edge tested in the past 12 months |
| 5 | **Test the watchers, not just the walls.** Purple exercises first, red team when ready. | VI | Detection scorecard improves round over round |
| 6 | **Turn findings into fixes, and prove they held.** Evidence-based priority, one register, root causes, retests. | V | Priority 1 fixes on time and verified by retest |
| 7 | **Buy testing like a professional.** Hard questions, strong contracts, internal capability to challenge results. | VII | Contracts include report, data, stop and retest terms |

> **The takeaway.** Inventory before testing. Permission before action. Evidence before priority. Retest before "fixed."

## What the siege teaches the plan

Each lesson of the siege maps to a part of the plan. Use this as a check on your own program.

| Siege lesson | What it teaches | Where it lands in the plan |
|---|---|---|
| The wall is only as strong as its weakest stretch | Scope to the perimeter an adversary sees | Outside-in view; edge in scope every year |
| The besieger has time; the defender has a schedule | One test a year cannot match a continuous adversary | Continuous scanning; scheduled assessment; rotation |
| Defenders who survive walk their own walls | Find the weak stretch first | Authorized testing as routine, not event |
| Most walls fall from the inside | People and processes are in the path | Authorized social engineering with safeguards |
| Sentries matter as much as stone | Detection and response decide the cost | Purple and red exercises; detection scorecard |

## The first 90 days

### Days 1 to 30: Know the walls and set the rules

- Name an accountable owner for the testing program, with authority to commission tests and to stop them.
- Write the one-page testing policy that defines scanning, assessment, penetration testing, red teaming and purple exercises.
- List crown assets. Build or refresh the inventory of internet-facing systems.
- Start continuous external scanning, or confirm the coverage of what you have. If you are eligible, consider CISA's no-cost Cyber Hygiene services.
- Adopt a standard authorization package based on Part II and NIST SP 800-115 Appendix B.
- List every third-party platform you rely on and record its testing policy or the permission you will need.
- Set up the remediation register and the written prioritization rule from Part V.

### Days 31 to 60: Close the known gaps

- Triage the scan results against the KEV catalog and your exposure. Fix or isolate Priority 1 items.
- Run root cause analysis on the worst ten findings and apply the "where else" question.
- Compare the outside-in view with the register. Add or retire the strays.
- Write the scope for your next penetration test from the crown outward. Include the edge and one assumed-breach objective.
- Procure the test using the questions and contract terms in Part VII. Include a retest.

### Days 61 to 90: Test and learn

- Hold the kickoff. Drill the stop. Confirm the real-intruder clause and contacts.
- Run the test. Require same-day notice of critical findings.
- Hold the debrief with engineering owners present. Load every finding into the register with an owner and date.
- Run one tabletop based on a scenario from Part VIII.
- Report to leadership: what was tested, what was found, what was fixed, what remains, and what it will take.

## The first 12 months

| Period | Focus | Key activities | Gate to move on |
|---|---|---|---|
| **Months 1–3** | Inventory, rules and baseline | Policy; authorization package; continuous scanning; register; first test scoped and run | Signed package for every test; Priority 1 items owned |
| **Months 4–6** | Remediation and retest | Priority 1 and 2 fixes; root cause process changes; retest; disclosure process published | Retest verifies Priority 1 fixes; repeat-finding rate recorded |
| **Months 7–9** | Watch the sentries | First purple exercise on three to five behaviors; detection fixes; supplier evidence requests | Detection scorecard baseline set and first gaps closed |
| **Months 10–12** | Widen and deepen | Web application testing against OWASP guidance; authorized social engineering test of one process; decide on red team readiness | Annual program review; three-year rotation agreed |

A few rules hold across the whole year.

- No test starts without a complete, signed authorization package.
- Every finding has a named owner and a date.
- Nothing is called fixed until it is retested.
- Every quarter, leadership sees the register, the scorecard and what went wrong.
- Every year, re-run the self-assessment below.

## The authorization checklist

Use this before every test. Every box must be ticked.

- [ ] A named executive with authority over every in-scope system has signed.
- [ ] Every third-party owner of in-scope systems has consented in writing, or its published testing policy has been checked and recorded.
- [ ] Systems, applications, address ranges, locations and people in scope are listed specifically.
- [ ] Systems out of scope are listed explicitly.
- [ ] Allowed and forbidden activities are stated in writing, without room for interpretation.
- [ ] Dates, hours, blackout periods and source locations of testing are recorded.
- [ ] Primary and alternate contacts on both sides are named and have been tested.
- [ ] Data handling, retention and destruction terms are agreed.
- [ ] Stop conditions and the person who can call a halt are named.
- [ ] The real-intruder clause says what happens and who decides when testing resumes.
- [ ] Insurers, managed providers and others who must be told have been identified.
- [ ] Counsel has reviewed the package for any intrusive testing.
- [ ] For tests involving people, leadership approval and people safeguards are in place.

## Maturity self-assessment

Use this checklist with your security, IT and leadership teams. Answer honestly. A "no" is not a failure. It is a work item.

Score each item: 0 = not in place, 1 = partly in place, 2 = fully in place and evidenced. The levels at the end are my rough guide, not a formal standard.

### Governance

- [ ] A named owner is accountable for the testing program and can commission and stop tests.
- [ ] A written policy defines scanning, assessment, penetration testing, red teaming and purple exercises.
- [ ] A standard authorization package is used for every test.
- [ ] Counsel reviews every intrusive test.
- [ ] Leadership receives a quarterly report on testing, findings and remediation.
- [ ] A vulnerability disclosure process is published and has an owner.

### Inventory and scope

- [ ] Crown assets are named and mapped.
- [ ] The internet-facing inventory is compared with the outside-in view at least quarterly.
- [ ] Third-party platforms in scope have recorded permissions or testing policies.
- [ ] Scope is set from the crown outward, using public data and your own evidence.
- [ ] A multi-year rotation ensures every significant system is tested on a cycle.
- [ ] Every exclusion has a named risk owner and an alternative form of assurance.

### Scanning and assessment

- [ ] Internet-facing assets are scanned continuously.
- [ ] Internal assets are scanned on a defined schedule.
- [ ] Scan results are validated and ranked by a skilled person.
- [ ] KEV status and exploitation likelihood are used in prioritization.
- [ ] A current assessment is shared with penetration testers at scoping.
- [ ] Most findings from the last penetration test were already in the register.

### Testing and method

- [ ] Providers name and follow a recognized public methodology.
- [ ] Critical findings are reported during the test, within an agreed time.
- [ ] Reports include an executive summary, root causes and limitations.
- [ ] Web applications are tested against recognized OWASP guidance.
- [ ] Social engineering tests, if any, follow written people safeguards.
- [ ] Detection and response are tested with purple or red exercises.

### Remediation and improvement

- [ ] Every finding is in one register with a named owner and date.
- [ ] A written prioritization rule sets target times by priority.
- [ ] High-severity findings get root cause analysis and the "where else" question.
- [ ] Priority 1 and 2 fixes are verified by retest.
- [ ] Repeat findings are tracked from test to test.
- [ ] Risk acceptances have an owner, a reason and a review date.

### Reading your score

There are 30 items, for a maximum of 60 points.

- **0–20: Foundational.** Focus on inventory, authorization and continuous scanning before buying deeper tests.
- **21–40: Developing.** Penetration testing is worthwhile. Prioritize remediation, retest and root cause.
- **41–60: Established.** Consider purple exercises and, when ready, red teaming, with continued rotation and review.

Whatever your score, the next step is the same: pick the three lowest items that matter most to your risk, assign owners and dates, and re-score in a quarter.

## The program scorecard

Report these to leadership every quarter. Measure against your own baseline, not anyone else's.

| Measure | Why it matters |
|---|---|
| Internet-facing assets found by testing that were not in the register | Measures whether you know your walls |
| Share of tests with a complete signed authorization package | Measures whether permission comes first |
| Median days to fix Priority 1 findings | Measures speed where it counts |
| Share of findings verified by retest | Measures whether "fixed" is true |
| Repeat-finding rate | Measures whether root causes are being fixed |
| Share of test findings already in your register | Measures whether your own assessment works |
| Detection scorecard: logged, alerted, answered | Measures whether the sentries see and act |

# Conclusion {#conclusion}

The research points one way.

Known flaws are now the most common way in, in Verizon's data. Most of the flaws already known to be exploited are not fully fixed, and the median time to fix them is rising. The opportunists favor smaller organizations, and they get in through the edge and through stolen credentials. Breaches take months to find and contain, and the long ones cost more (Verizon, 2026; IBM and Ponemon Institute, 2026).

The irregular warfare lens explains why this keeps happening. Your adversaries work indirectly, avoid attribution and impose costs asymmetrically. They probe every stretch of the wall because probing is cheap. They do not need permission and they do not share the report.

You cannot stop them probing. You can make sure that when they arrive, the weak stretch has already been found and repaired, by people you invited, under rules you wrote.

That is what authorized testing is. Not a stunt. Not a certificate. A disciplined habit of walking your own walls: knowing what you have, getting permission before anyone touches it, looking every day, testing properly, fixing the cause, checking the fix, and drilling the sentries until they see what they are supposed to see.

The public guidance agrees on the shape. NIST says testing has its greatest value when it ends in mitigation (NIST SP 800-115, 2008). The NCSC says you should know what the testers will find before they find it (NCSC, 2017/2022). CREST says a test is "only a snapshot of a system at a point in time," and counts the assumption that fixing what one test found makes systems "secure" among the top challenges organizations face (CREST, 2022). TIBER-EU says the outcome is not a pass or fail (ECB, TIBER-EU). They are all describing a program, not an event.

Break it before they do. Then fix it. Then check.

Infinitum Corporation helps organizations take these steps in a way that fits their size, systems and risk appetite. Our testing work is always authorized, scoped and approved in writing, and performed for defense. I make no promise about the outcome any organization will achieve, and every figure in this paper belongs to the source cited.

Don't take my word for it. Read the sources, then decide.

This is the third paper in the series. The next is *Read the Enemy: Strategic Risk in the Gray Zone*.

Let's stay engaged. Write to info@theinfinitumcorporation.com, or visit https://www.theinfinitumcorporation.com. Dialogue is key.

<!-- BODY-END -->
