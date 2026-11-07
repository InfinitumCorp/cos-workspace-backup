
## Part V: Supply lines. The rear is part of the front {#part-v-supply-lines}

**What public analysis describes.** CSIS says supplying front lines "will be more challenging—and likely deadlier—than ever," and that modern forces "need to anticipate that only a fraction of supplies will get through." Forces will therefore "seek to minimize deliveries to the front lines" and adopt technologies that increase self-sufficiency, such as on-site production of parts (CSIS, 2025a). It also says that as commercial providers take on more of the work, the line between combatants and noncombatants blurs: providers of power, cloud storage and internet connectivity could increasingly be seen as legitimate targets (CSIS, 2025a). Read that as a statement about shared infrastructure. In your world, the shared infrastructure is the cloud and the carrier.

Keep your own parallels in view, and keep them modest. Supply lines are long. They run through other people. They are watched, and they break.

**What it means for you.** Your supply lines are your vendors, your software dependencies, your cloud providers, your connectivity, your managed service providers, your payment processors and your power. Most of it lives outside your walls. You rely on it. You cannot patch it.

## The numbers on dependence

Verizon's 2026 DBIR reports that breaches with third-party involvement increased by 60% from the prior year's dataset, reaching 48% of total breaches (Verizon, 2026). It describes root causes in many cloud-based third-party incidents that "boil down to insecure authentication (absence of MFA, improper credential rotation) or lack of least privilege enforcement for users or service accounts" (Verizon, 2026). In a survival analysis of third-party cloud exposures, only 23% of organizations had fully remediated missing or improperly secured multifactor authentication, though half of findings were resolved within a month (Verizon, 2026).

IBM's 2026 report ranks supply chain compromise as the second most common initial attack vector, and the second slowest to resolve, taking 258 days to identify and contain (IBM and Ponemon Institute, 2026). ENISA observes that attackers abuse cyber dependencies, creating a "ripple effect across the supply chain" (ENISA, 2025).

Read those numbers as direction, not precision. Each study defines "third party" and counts breaches differently. The direction is consistent: the more you rely on others, the more their weaknesses become yours.

## The ordinary mistakes

Most supply line failures are dull.

- **No list.** You cannot defend dependencies you have not named.
- **Trust by contract.** A security questionnaire, filed once, and never looked at again.
- **Flat access.** A vendor account that can reach more than the vendor's job needs.
- **One route.** A single connectivity provider, a single cloud region, a single identity provider, a single payment rail.
- **No exit.** No plan for the day a supplier is breached, suspended or simply gone.

NIST's CSF 2.0 turns this into a category of its own: Cybersecurity Supply Chain Risk Management (GV.SC) under the Govern function. Its outcomes include that "suppliers are known and prioritized by criticality," that requirements are "integrated into contracts and other types of agreements," that supplier risks are "understood, recorded, prioritized, assessed, responded to, and monitored over the course of the relationship," that relevant suppliers are "included in incident planning, response, and recovery activities," and that plans cover what happens "after the conclusion of a partnership or service agreement" (NIST CSF 2.0, 2024).

That list is the best brief I know. Map it onto your own contracts and see which lines are blank.

## Triage the supply line

You cannot treat every supplier alike. Sort them.

| Tier | Who sits here | What you do |
|---|---|---|
| 1. Cannot operate without | Identity provider, core cloud platform, primary connectivity, payment processing, the one software package that runs the business | Written security requirements; incident contact; right to be told; a tested fallback plan; an owner at senior level |
| 2. Painful to lose | Collaboration tools, CRM, HR systems, specialist SaaS | Standard security terms; access limited to what the job needs; a data export you have tested |
| 3. Replaceable | Everything else | Basic review; do not give broad access |

For tier 1, ask hard questions in writing. How would you tell us about an incident, and how fast? What do you do if your own supplier is breached? Where does our data live? How do we leave?

## Keep the rear from burning

CSIS offers a principle you can borrow from logistics: self-sufficiency (CSIS, 2025a). For networks, this means the ability to operate through a failure upstream, for a while.

- **A second route for what matters.** A second connectivity path. A second DNS provider. A backup identity path for administrators. Not for everything.
- **Local copies of what you need.** Data exports of the systems that run the business, kept where you control them, in formats you can read without the vendor.
- **Manual procedures,** printed and tested, for critical operations.
- **Limits on blast radius.** Treat vendor connections as untrusted. Give each its own segment, its own account and its own logging.

NIST's cyber resiliency guidance adds a warning that fits here. Redundancy-supporting approaches such as backup, surplus capacity and replication "are not sufficient to protect against" an advanced persistent threat. A threat actor might choose backup servers as "optimum locations to implant malware" if they are not sufficiently protected, and remote backup servers built with the same architecture as the primary may share its weakness (NIST SP 800-160 Vol. 2 Rev. 1, 2021). A second copy that shares the first copy's weaknesses is the same line drawn twice. That is why diversity appears in the same list.

## Software dependencies

Treat software like any other supply: know what is in it. For critical applications, keep a software bill of materials, track which versions you run, and know who to ask when a component is announced as vulnerable. For the edge, the joint guidance lists "procure secure-by-design devices" among its seven strategies (NSA, 2025). You cannot always do that. When you cannot, the compensating control is to limit and monitor what the product can reach.

## Exercise the break

NIST's guidance on incident response says incidents "occur frequently and cause far more damage," and recovery "often takes weeks or months." It also urges that lessons be shared as soon as they are identified, "not delayed until after recovery concludes" (NIST SP 800-61r3, 2025). For supply lines, that means exercising the day a tier 1 supplier fails or is breached. Who calls whom? What do we switch off? What do we tell customers? How long can we last?

Run it once a year. Invite the supplier if they will come.

## What to do

1. **Build the supplier list.** Name every tier 1 and tier 2 dependency. Record owner, data held, access given and exit path.
2. **Tier them.** Apply different rules to each tier.
3. **Review vendor access.** Remove accounts and permissions that are not needed. Put multifactor authentication and logging on the rest.
4. **Close the dullest gaps first.** A single route, no exit plan, no incident contact.
5. **Test one fallback.** Pick the highest-impact tier 1 supplier and rehearse running without it.
6. **Put incident duties in contracts** at renewal. Notification timelines, cooperation, data return.
7. **Share lessons early.** Hold a short review after any supplier incident, before the dust settles.

## What to measure

- Share of tier 1 suppliers with a named internal owner, a tested fallback and a documented incident contact.
- Number of vendor accounts with access beyond their stated purpose.
- Time to run a critical process in fallback mode, in rehearsal.
- Share of tier 1 and tier 2 contracts that carry incident notification terms.
