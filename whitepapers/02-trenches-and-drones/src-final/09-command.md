
## Part VI: Command. Decide faster than the grind {#part-vi-command}

**What public analysis describes.** CSIS says the future is "shifting toward smaller, highly mobile, adaptable units, where field commanders are empowered to make decisions about cover, concealment, and tactics while minimizing their communications signature" (CSIS, 2025a). It says fast cycles of adaptation mean fronts may evolve at different paces, "necessitating central nodes to facilitate sharing lessons learned," and that "units will need resilient mesh networks to ensure continuous communication even if multiple nodes go dark" (CSIS, 2025a). It reports a "six week learning cycle" attributed to a RUSI analyst, in which measures and countermeasures follow each other in weeks, not years (CSIS, 2025a). Another chapter says drone developers pushed innovation cycles to "weeks rather than months or years" (CSIS, 2025b).

Three ideas: decisions pushed to the edge, lessons pulled to the center, and communications that survive losing a node.

**What it means for you.** Command is the cross-cutting concern that decides whether all five fronts work together. It is not a rank. It is how decisions are made, how fast, by whom, and what happens when the person who normally decides is unreachable.

## The decision clock

Compare two clocks.

IBM's 2026 study puts the mean time to identify and contain a breach at 247 days (IBM and Ponemon Institute, 2026). Verizon's 2026 DBIR puts the median time to fully patch known-exploited vulnerabilities at 43 days, up from 32 (Verizon, 2026). Attack bursts, as shown in Part II, run in minutes and hours.

An organization whose decisions run on a slower clock than the pressure on it loses ground even when it is doing the right things. The target is not speed at any cost. The target is that no routine decision waits for a meeting.

## Pre-decided authority

In an incident you do not want to discover who can approve what. Decide it in advance.

- **Pre-authorized actions.** A short list of actions that on-call staff may take without asking: disable an account, isolate a host, block an address range, revoke a token. Write down the conditions. Review them after use.
- **Escalation triggers.** Clear lines for when a decision moves up: a crown system, customer data, a regulator notice, a public statement, a payment.
- **Delegation if unreachable.** Every decision-maker has a named deputy with the same authority. The deputy has the numbers, the access, and the standing to act.
- **Intent, not scripts.** State what must be protected and what may be sacrificed. Let those closest to the problem choose the method.

That last point is my own recommendation, drawn from the shape of the CSIS description. It is not a quotation from any doctrine. But the logic is the same as CSIS's: distant, slow, centralized decisions fail under pressure, and local authority must be bounded by clear limits (CSIS, 2025a).

The cost of delegation is mistakes. Accept some. Review them without punishing the people who acted in good faith. Otherwise nobody will act next time.

## Lessons to the center, fast

CSIS says a more widespread battlefield may see fronts evolve at different paces, "necessitating central nodes to facilitate sharing lessons learned" (CSIS, 2025a). NIST SP 800-61r3 says to share lessons "as soon as they are identified, not delayed until after recovery concludes" (NIST SP 800-61r3, 2025).

For you that means:

- **A running log** kept during every incident and every near miss, with a short note on what worked and what did not.
- **A weekly fifteen-minute review** of the log. One owner. Output: at most three changes.
- **A change channel** where findings turn into tickets, with an owner and a date.
- **Outside sources.** Join an information-sharing community in your sector. Verizon's own advice for the growing capability of attackers is to "maintain our footing and use collaboration and partnerships" (Verizon, 2026).

Keep the loop short. A lesson that waits for the quarterly meeting is a lesson that gets forgotten.

## Communications that survive a lost node

CSIS's mesh-network idea has a plain analog: crisis communications that do not depend on the thing that failed (CSIS, 2025a). If email is down, how do you reach each other? If chat is down? If your identity provider is down and nobody can log in?

Build a short communications plan:

1. **A primary channel,** the one you normally use.
2. **An out-of-band channel** that does not depend on your identity provider or primary network. Agree in advance which one, and who has the credentials.
3. **A phone tree** on paper, kept current, with deputies.
4. **A rule** for confirming that a message is real before acting on it, including voice and video, as in Part III.

Test it quarterly. Ask the question: who did not get the message?

## Governance without ceremony

NIST's CSF 2.0 places Govern at the center of its six functions, alongside Identify, Protect, Detect, Respond and Recover (NIST CSF 2.0, 2024). That framing helps in practice. Governance is not paperwork. It is the set of decisions leadership has made, in advance, about what to protect, what to tolerate, and who decides.

For a mid-size organization, a one-page "risk appetite and decision rights" sheet may be the most useful governance document you can write. Name your crown assets. Name the maximum downtime you can accept for each. Name who may approve a deviation. Revisit it every six months.

## What to do

1. **Write the pre-authorized action list.** Five to ten actions. Conditions. Owner. Review date.
2. **Name deputies** for every decision-maker, and give them access and authority.
3. **Draw the escalation triggers** on one page.
4. **Start the lessons log** and the weekly fifteen-minute review.
5. **Build and test the out-of-band communications plan.**
6. **Write the one-page decision rights sheet** and have leadership sign it.

## What to measure

- Time from detection to first containment action, in incidents and exercises.
- Share of incident decisions made within pre-authorized limits.
- Time from a lesson identified to the change deployed.
- Share of the response team reached through the out-of-band channel within ten minutes, in a drill.
