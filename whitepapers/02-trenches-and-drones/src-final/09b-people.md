
## Part VII: People. Endurance is the strategy {#part-vii-people}

**What public analysis describes.** CSIS notes that new drone units "require a vastly different skill set than traditional infantry" and that recruitment and training programs had to be intensified to build them (CSIS, 2025a). That sentence is generic. It says something every security leader knows: when the nature of the work changes, the people have to change with it, and it takes time.

CSIS also warns of leaning on technology as a crutch: "Using technology as a crutch happens today," and that militaries "must be ready to lose those tools and keep fighting" (CSIS, 2025a). The same chapter says the human tendency to defer to machine recommendations is a hazard in itself (CSIS, 2025a).

**What it means for you.** People are the second cross-cutting concern, and in a war of attrition they are the scarcest resource. Tools can be bought. Experience cannot.

ISC2's 2024 workforce study found 67% of respondents reported a staffing shortage and 90% reported one or more skills gaps (ISC2, 2024). Verizon's analysis of small and medium-sized organizations found that most ransomware victims, among cases where size was known, were small or mid-size (Verizon, 2026). The ones with the smallest teams face the same cheap pressure as the ones with the largest.

I do not cite burnout or turnover statistics here. The sources I opened for this paper do not measure them. I will say only what any security manager can see on their own team: sustained pressure, with no end date, wears people down.

## Design the team for endurance

A short fight can be won with heroics. A long grind cannot. The practical rules are not glamorous.

**Rotate.** Put on-call duty on a rota with real recovery time after a heavy shift. Do not let the same two people carry every incident.

**Cross-train.** For each critical function, name at least two people who can do it. Test it by having the second person do it, with the first person watching, once a quarter.

**Write it down.** Runbooks for the ten things that go wrong most often, and the five that go wrong worst. Plain language. Tested by someone who did not write them.

**Protect attention.** Cut alerts that never lead to action (see Part IV). Automate repetitive triage where you can, with human review (Part II). IBM found that extensive use of AI and automation in security was associated with a shorter breach lifecycle and lower costs (IBM and Ponemon Institute, 2026). Whatever you automate, keep a person accountable.

**Keep a bench.** An incident response retainer, a managed detection provider, or a mutual-aid arrangement with a peer organization. Agree terms before you need them. Know who answers the phone at 3 a.m.

**Train in the open.** Exercises should include non-technical staff. Finance, legal, communications and executive assistants are part of the line. CSIS's guidance on exercises is for militaries, but the principle carries over: simulate conditions where the adversary has good information (CSIS, 2025b). Assume they know your org chart.

## Skills that matter now

The mix of skills changes as the fronts shift. A few that I would grow in a mid-size team:

- **Identity and access.** The craft of making access narrow and short-lived.
- **Cloud and third-party risk.** Reading a provider's responsibility model and finding where it leaves you exposed.
- **Detection engineering.** Turning a decision into a signal (Part IV).
- **Resilience engineering.** Backups, restores, failover and degraded operations (Parts III and V).
- **Communication.** Plain, calm writing and speaking under pressure. Underrated.

You will not hire all of them. Train, contract and partner.

## Humans and machines

CSIS's cautionary note on AI is about judgment: when both sides use AI, the incentive is to defer to it, and for now that will lead to mistakes (CSIS, 2025a). Applied to security operations, it is a rule worth writing down:

- AI recommends. A named human decides, for anything that affects customers, access or money.
- Each automated action has a log, an owner and an off switch.
- People review a sample of automated decisions every week and write down what they find.
- Nobody is judged by how often they agree with the tool.

## Morale is operational

I will keep this short. Say thank you. Name what went well in every post-incident review. Make sure people can take leave. Make sure the person who raised the alarm is thanked, not blamed. Those are cheap. They also decide whether your best people are still there in a year.

## What to do

1. **Build the rota.** Include recovery time. Name deputies.
2. **Map single points of human failure.** For every critical function, name two people.
3. **Write and test ten runbooks.**
4. **Sign a bench.** Retainer, partner or mutual-aid agreement, with a tested contact path.
5. **Run a cross-functional exercise** with finance, legal, communications and executives.
6. **Write the human-in-the-loop rule** for AI and automation, and review a sample every week.

## What to measure

- Number of critical functions with fewer than two trained people.
- Share of runbooks tested by someone other than their author in the last six months.
- Distribution of on-call load across the team.
- Time to reach your outside bench in a test call.
