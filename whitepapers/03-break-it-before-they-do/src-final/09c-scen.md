
## Part VIII: Three scenarios {#part-viii-scenarios}

These three scenarios are **hypothetical**. They are not reports of real incidents, real organizations or real results. They contain no statistics and no techniques. They exist to show how the parts of this paper interact, and to give your team something to rehearse.

Each scenario is a mid-size organization, roughly a few hundred staff, with a small security team and several outside providers. Use them as prompts for a tabletop exercise. Replace the details with your own.

<div class="scenario" markdown="1">

## Scenario one: The clean report

*A regional professional services firm. One annual penetration test.*

**The setup.** For three years, the firm has bought the same annual external test, scoped to its website and one address range. Each report comes back with a handful of medium findings. Leadership reads "no critical issues" and moves on.

**The turn.** A new IT manager compares the outside-in view with the asset register. She finds a remote access gateway, set up by a contractor two years earlier, that is not in the register and has never been in scope. It is running software with a flaw that appears in the KEV catalog.

**What good looks like.**

- The firm isolates the gateway the same day under a pre-authorized emergency change, then patches it.
- Incident response checks whether anyone used the flaw before the fix. The scope of that check is decided by counsel and the incident response provider, not by the testers.
- The next test is rescoped from the crown outward, with the outside-in view as its starting point.
- Root cause analysis finds the process gap: contractor-built systems were never added to the register. The fix is a change process, not just a patch.

**Questions for your tabletop.** When did we last compare what the internet sees with what our register says? Who can authorize an emergency change? Would our test have found this?

</div>

<div class="scenario" markdown="1">

## Scenario two: The test that found someone else

*A manufacturing company. An internal assumed-breach test.*

**The setup.** The company commissions an assumed-breach test starting from an ordinary employee laptop. The authorization package includes a real-intruder clause.

**The turn.** On day four, the testers notice an account behaving in ways their plan does not explain. It is not them. They stop, as the clause requires, and call the named contact.

**What good looks like.**

- The contact answers within minutes, because the stop drill at kickoff proved the number worked.
- The testers preserve their notes and hand over to the company's incident response provider under the existing plan. They do not investigate further on their own.
- Leadership decides, with counsel, whom to notify. The insurer's requirements were already listed in the authorization.
- Testing resumes two weeks later under a fresh written authorization, with the scope adjusted to what the response found.

**What bad looks like.** No clause, no stop, no contact. The testers keep going, the intruder notices, evidence is lost, and nobody knows who was allowed to do what.

**Questions for your tabletop.** Does our authorization say what happens if testers find a real intruder? Who decides when testing restarts?

</div>

<div class="scenario" markdown="1">

## Scenario three: The help desk call

*A healthcare services provider. An authorized social engineering test.*

**The setup.** Leadership, human resources and counsel approve a limited test of the help desk's password reset process. The rules forbid pretexts involving emergencies, regulators or personal distress. Results will be reported as process findings, not names.

**The turn.** A tester, following the approved pretext, calls the help desk asking for a reset for a senior manager said to be traveling. The agent, under time pressure and with no call-back rule, completes the reset.

**What good looks like.**

- The tester reports the result to the control contact immediately. The account is restored and the reset is reversed within the hour.
- The debrief, with the help desk team present, focuses on the missing verification step. Nobody is blamed.
- The process changes: privileged and executive resets require a call-back to a number already on file, and a second approver.
- A retest a month later, under the same rules, confirms the new step is followed.

**Questions for your tabletop.** How does our help desk verify a reset for a senior or traveling user? Would our staff feel safe reporting that they were fooled?

</div>

## What the scenarios share

Each turns on a decision made before the test. An inventory compared with the outside-in view. A real-intruder clause and a working stop. People safeguards and a no-blame debrief. None depended on a clever tester or an expensive tool. All depended on governance.

Run one scenario a quarter. Change the details. Write down what you find.
