
## Part VIII: Three scenarios {#part-viii-scenarios}

These three scenarios are **hypothetical**. They are not reports of real incidents, real organizations or real results. They contain no statistics. They exist to show how the fronts interact, and to give your team something to rehearse.

Each scenario is a mid-size organization, roughly a few hundred staff, with a small security team and several outside providers. Use them as prompts for a tabletop exercise. Replace the details with your own.

## Scenario one: The long week

*A regional services company. Monday to Friday.*

**Monday.** The edge. A vendor publishes a notice about a flaw in a remote access appliance. It is on the list of known-exploited vulnerabilities. The company runs that appliance. The patch window is scheduled for the following weekend because of a customer deadline.

**Tuesday.** Drones. A flood hits the customer portal for twenty minutes, stops, then returns an hour later. The on-call engineer spends the afternoon on the upstream mitigation. Meanwhile, a wave of phishing messages reaches finance and the help desk.

**Wednesday.** Sensors. The scanning traffic against the appliance rises. The log source for the appliance has been quiet for days. Nobody noticed, because nobody was asked to watch it.

**Thursday.** Command. A help-desk call, convincingly polite, asks for a password reset for a senior manager who is traveling. The help-desk agent is under pressure and has no verification rule for resets.

**What good looks like.**

- The edge appliance is on the list of tier-1 internet-facing assets. The known-exploited flaw triggers a pre-authorized emergency patch outside the normal window. A named owner decides in hours, not days.
- The flood runbook is rehearsed. The on-call engineer engages upstream protection by the book, and a second person checks the quiet systems while the loud one is being handled.
- A heartbeat check on the appliance's logs fires on Tuesday, not after the fact.
- The help-desk rule requires a call-back to a known number for any reset of a privileged or traveling executive's account. The agent follows the rule, and nobody criticizes the delay.
- By Friday the team has reviewed what happened, changed three things, and rested.

**Questions for your tabletop.** Who can approve an emergency patch outside the window? What do we turn off if the appliance cannot be patched in time? Who is watching the quiet log source?

## Scenario two: The quiet clock

*A professional services firm. A bad afternoon.*

**Situation.** A time source used by several internal systems begins to drift. The drift is small at first. Log timestamps no longer line up between systems. A certificate validation error appears on one internal service, then another. The help desk begins to receive reports of failed sign-ins.

At the same time, someone calls the finance team using a voice that sounds like the managing partner. It asks for an urgent payment to a new account, citing a confidential deal. The caller says not to discuss it by email.

**Pressure points by front.**

- **Electronic warfare, in the sense of Part III.** Time and voice are both signals. Both can be wrong. The two events may be unrelated, or one may be covering for the other. The team does not know.
- **Sensors.** Logs with inconsistent time make it hard to build a timeline. Analysts lose confidence in the data.
- **Command.** Who decides whether to take an authentication service offline to investigate? Who decides whether the payment is real?
- **People.** The finance clerk is junior. The caller is senior.

**What good looks like.**

- Two independent time sources are configured, and an alert fires when they disagree. The team switches to the second source under a runbook, rather than debating which clock is right.
- The finance team has a rule: new payee, urgent request, any channel, requires out-of-band verification through a known number, and a second approver. The clerk follows it. The managing partner, called back on a number from the directory, knows nothing about it.
- Incident notes record the time source and the drift, so the timeline can be rebuilt later.
- Leadership has told the team, in advance, that following the rule is correct even when the person asking is the most senior in the firm.

**Questions for your tabletop.** Which of our systems would fail first if time were wrong? Who can stop a payment at 4:55 p.m. on a Friday? Have we tested this rule against someone who sounds exactly like the boss?

## Scenario three: The vendor goes dark

*A distribution business. A supplier fails.*

**Situation.** A cloud service that handles the company's orders is unavailable. The provider's first notice is vague. Hours pass. Later, the provider states that it is investigating a security incident and that customer data may be affected. Staff cannot take orders. The managed service provider that administers part of the network is also affected, and its support line is overloaded.

**Pressure points by front.**

- **Supply lines.** One provider carries a critical process. There is no second route.
- **Trenches.** The provider's connection into the company's systems uses an account with broad permissions.
- **Command.** The incident has no owner inside the company. Customers are asking questions. The sales team wants to promise dates.
- **People.** Staff have been working through the night. The one person who understands the integration is on leave.

**What good looks like.**

- The supplier is on the tier-1 list. The company holds a recent export of order data in a readable format, and a manual procedure for taking orders by phone and spreadsheet for a limited time. Staff have practiced it once.
- The vendor connection runs through its own segment with its own account, restricted to what the integration needs. The company disables the connection on its own authority while the vendor investigates.
- A named incident owner decides what to tell customers and when. A short holding statement goes out early and is updated at set times.
- The contract with the provider contains incident notification duties, which the company invokes. The company asks the provider written questions and logs the answers.
- A second person has been trained on the integration. The rota gives the first person leave.

**Questions for your tabletop.** If this supplier were gone for a week, what would we do? Who may disable the connection? What would we say to customers in the first two hours?

## What the scenarios share

None of these events is exotic. Each is ordinary pressure applied from several directions. In every one, the organization that does well has done unglamorous work in advance: a list, a rule, a rehearsal, a named owner. The organization that does badly usually has the same tools. It has not decided what to do.

Run one scenario a quarter. Change the details. Write down what you find.
