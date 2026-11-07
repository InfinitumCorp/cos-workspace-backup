
# Recommendations {#recommendations}

Here is the plan.

It is not glamorous. It is a campaign built around depth, cheap layers, second sources, a small signature, a rear that can burn, and decisions that do not wait for permission. The seven parts above each end with their own actions. This section puts them in order.

Add capability only when the controls and the evidence are in place. Timelines depend on your team size, your tooling and your risk appetite. The phases below are a sequence first and a schedule second.

## The seven moves

| # | Move | Front it answers | First proof that it is working |
|---|---|---|---|
| 1 | **Map the ground.** Inventory the edge, crown assets and dependencies. | Sensors; Supply lines | The outside-in list matches your asset register |
| 2 | **Dig in.** Segment, shrink the implicit trust zone, and move administrators onto a separate path. | Trenches | A test from an ordinary workstation cannot reach a crown system |
| 3 | **Close the cheap doors.** MFA on exposed logins, automated patching on the edge, upstream flood protection. | Drones | Known-exploited flaws on the edge are fixed within your target time |
| 4 | **Keep a second source.** Two time sources, out-of-band verification, a heartbeat on every critical log. | Electronic warfare | A drill with the primary source removed shows no surprise |
| 5 | **Reduce your signature.** Shrink what the outside sees, build detection from decisions, and place a few decoys with legal sign-off. | Sensors | Every alert has an owner and a clock |
| 6 | **Plan for the rear to burn.** Tier your suppliers, keep exports and manual procedures, and rehearse the break. | Supply lines | One tier 1 fallback has been run end to end |
| 7 | **Decentralize the decisions.** Write down who may act, keep an out-of-band communications path, and share lessons within days. | Command; People | A pre-authorized action was used and reviewed |

> **The takeaway.** Map first. Dig in second. Close the cheap doors before you buy anything exotic. Keep a second source for every signal you trust. Plan for the rear to burn. Decide before you have to.

## What the battlefield teaches the plan

Each lesson from The modern battlefield maps to a part of the plan. Use this as a check on your own program.

| Battlefield lesson | What it teaches | Where it lands in the plan |
|---|---|---|
| Depth beats a hard shell | Assume the first line is crossed; make every step cost more | Segmentation; per-session access; recovery rehearsals |
| Cheap mass versus exquisite systems | Answer volume with cheap, repeatable, automated layers | MFA; edge patching; upstream flood protection; automation with human review |
| Signals can be jammed and spoofed | Verify out of band; keep a second source | Time sources; call-back rules; heartbeat checks |
| You are being watched | Know your signature; make sense of your own sensors | Outside-in list; decision-led detection; decoys with limits |
| The rear area is not safe | Suppliers and platforms are terrain | Tiered supplier list; exports; manual fallbacks; contract terms |
| Decentralize decisions, protect communications | Pre-authorize; keep a channel that does not depend on what you defend | Decision rights; deputies; out-of-band channel; lessons loop |
| Endurance decides | Staff for year two, not week two | Rotas; cross-training; runbooks; a bench |

And a check to run each quarter. Five questions:

1. **Where are the lines?** Is your trench map current, with strong, partial and absent marked honestly?
2. **What can the outside see?** When did you last compare the outside-in list with your register?
3. **What is the second source?** For time, identity and every critical signal, is there an independent check?
4. **What if the rear burns?** When did you last rehearse a tier 1 supplier failing?
5. **Who may act?** Does everyone on the rota know what they can do without asking?

## The first 90 days

### Days 1 to 30: Map and baseline

- Assemble the outside-in list of everything internet-facing that belongs to you. Reconcile it with the asset register and assign an owner to every item.
- Draw the trench map with five lines. Mark each strong, partial or absent.
- List your top signals (time, identity, names, voice, alerts) and note the second source for each, or the gap.
- Write down today's baseline: time to patch known-exploited flaws on the edge, share of exposed logins with MFA, time to restore a crown system, time from alert to first human action.
- Build the supplier list and tier it.
- Write the pre-authorized action list and name deputies.

### Days 31 to 60: Close the cheap doors

- Patch the edge. Remove services nobody can justify. Put management interfaces behind a separate path.
- Require MFA on every external login and remote access path, starting with administrators.
- Confirm upstream flood protection in writing. Run the two-hour drill.
- Add heartbeat checks to critical log sources.
- Set verification rules for payments, credential resets and access requests. Brief the people who handle them.
- Stand up the out-of-band communications path and test it once.

### Days 61 to 90: Rehearse and decide

- Run one scenario from Part VIII as a tabletop.
- Run a controlled test of removing the primary time source in a change window.
- Test the first fallback for your most important tier 1 supplier.
- Start the lessons log and the weekly review.
- Write the one-page decision rights sheet and have leadership sign it.
- Re-measure the baseline. Report the change to leadership, including what did not move.

## The first 12 months

| Quarter | Focus | What you deliver |
|---|---|---|
| Q1 (days 1 to 90) | Map, close, rehearse | Everything in the 90-day plan |
| Q2 | Dig deeper | Segment your most valuable systems; separate administrator access; extend phishing-resistant authentication to all staff who touch crown assets |
| Q3 | See and decide | Decision-led detection for the six key decisions; first decoys; automation in recommend-only mode, then limited authority; second tabletop with finance, legal and communications |
| Q4 | Survive and adapt | A full tier 1 supplier failure exercise; contract terms updated at renewal; re-run the self-assessment; set next year's targets from your own results |

Throughout the year:

- **Every widening of authority is a decision,** made by a named owner, documented and reversible.
- **Every incident and near miss feeds the lessons log.**
- **Every quarter, report to leadership** on the metrics and on what went wrong.
- **Every year, re-run the self-assessment** below.

## Self-assessment checklist

Use this checklist with your security, IT and leadership teams. Answer honestly. A "no" is not a failure. It is a work item.

Score each item: 0 = not in place, 1 = partly in place, 2 = fully in place and evidenced. The levels at the end are my rough guide, not a formal standard.

### Trenches

- [ ] The trench map exists and is reviewed at least twice a year.
- [ ] Administrators use a separate access path with phishing-resistant authentication.
- [ ] Crown systems sit in segments that an ordinary workstation cannot reach, and this has been tested.
- [ ] A restore of a crown system from isolated backup has been rehearsed in the last year.

### Drones

- [ ] MFA protects every externally exposed login and every remote access path.
- [ ] Known-exploited vulnerabilities on internet-facing systems have a target patch time, and it is measured.
- [ ] Upstream flood protection is in place, with a written runbook and a rehearsal.
- [ ] Automated actions run under a human-in-the-loop rule, with logs and an off switch.

### Electronic warfare

- [ ] Critical systems use at least two independent time sources, and disagreement raises an alert.
- [ ] Requests to move money, reset credentials or grant access follow an out-of-band verification rule.
- [ ] A critical process has been run in degraded mode in the last year.
- [ ] An out-of-band management path exists for the most critical systems.

### Sensors

- [ ] An outside-in list of internet-facing assets exists and has been reconciled with the asset register.
- [ ] Every alert has an owner and a response time.
- [ ] Every critical log source has a heartbeat check.
- [ ] Public repositories, shared links and storage have been reviewed for exposed secrets and files in the last six months.

### Supply lines

- [ ] A supplier list exists, with tiers, owners, data held and access granted.
- [ ] Vendor accounts are limited to what each integration needs, with MFA and logging.
- [ ] Data exports for tier 1 and tier 2 systems are kept where you control them, in formats you can read.
- [ ] A tier 1 supplier failure has been exercised in the last year.
- [ ] Tier 1 contracts contain incident notification and cooperation terms.

### Command

- [ ] A pre-authorized action list exists, with conditions and review dates.
- [ ] Every decision-maker has a named deputy with access and authority.
- [ ] A lessons log is kept, with a weekly review and an owner.
- [ ] An out-of-band communications path exists, and it has been tested in the last quarter.

### People

- [ ] The on-call rota includes recovery time, and load is shared.
- [ ] Every critical function has at least two trained people.
- [ ] Runbooks exist for the ten most likely and five worst failures, and someone other than the author has tested them.
- [ ] An outside bench (retainer, partner or mutual aid) exists, with a tested contact path.
- [ ] Exercises include finance, legal, communications and executives.

### Reading your score

There are 30 items, for a maximum of 60 points.

- **0–19: Foundational.** Map the ground, close the cheap doors, and fix single points of failure before anything else.
- **20–39: Developing.** The basics are partly in place. Prioritize second sources, supplier fallbacks and decision rights.
- **40–60: Established.** Deepen segmentation, automate with care, and keep rehearsing.

Whatever your score, the next step is the same: pick the three lowest items that matter most to your risk, assign owners and dates, and re-score in a quarter.

## A starter scorecard

Report these to leadership each quarter. Compare against your own baseline. Do not compare with a survey median.

| Measure | Front | Direction |
|---|---|---|
| Time to patch known-exploited flaws on the edge | Drones | Down |
| Share of external logins with MFA | Drones | Up |
| Systems in the implicit trust zone | Trenches | Down |
| Time to restore a crown system, in rehearsal | Trenches | Down |
| Independent time sources per critical system | Electronic warfare | Up |
| Internet-facing assets without an owner | Sensors | Down |
| Median time from alert to first human action | Sensors | Down |
| Tier 1 suppliers with a tested fallback | Supply lines | Up |
| Time from detection to first containment action | Command | Down |
| Critical functions with fewer than two trained people | People | Down |

# Conclusion {#conclusion}

The sources agree on direction.

Exploitation of known flaws is still a leading way in. Credentials still get stolen and used. Floods and bots arrive every day. Suppliers carry more of your risk each year. Breaches that run long cost more. Teams are short of people and skills (Verizon, 2026; IBM and Ponemon Institute, 2026; ISC2, 2024).

The public analysis of the modern battlefield points the same way. Depth. Cheap mass. Spoofed and jammed signals. Constant observation. Supply lines that are never safe. Fast cycles of measure and countermeasure (CSIS, 2025a; CSIS, 2025b; CSIS, 2025c). Your organization is not at a front line. But it works in the same electromagnetic and informational weather, and it faces the same economics: cheap pressure against costly defense.

You will not win that by matching them effort for effort. You win it the way resilient institutions do.

Dig in, so the first breach is not the last line. Spread out, so one failure does not take everything. Keep a second source, so a false signal does not steer you. Know what the outside can see, and make sense of what your own sensors tell you. Keep the rear from burning, and know how to fight when it does. Push decisions to the people closest to the problem, and learn faster than the grind wears you down.

Above all, keep going. This is a long contest, and the organizations that do well in it are the ones that are still doing the boring work in year three.

Infinitum Corporation helps organizations take these steps in a way that fits their size, systems and risk appetite. I make no promise about the outcome any organization will achieve, and every figure in this paper belongs to the source cited.

Don't take my word for it. Read the sources, then decide.

This is the second paper in a series. The first is *Dead Reckoning: AI for Security Operations in a Jammed, Spoofed, Watched World*. The next is *Break It Before They Do: Authorized Hacking for Organizations Under Siege*.

Let's stay engaged. Visit https://www.theinfinitumcorporation.com. Dialogue is key.

<!-- BODY-END -->
