
## Part IV: Sensors. Assume you are being watched {#part-iv-sensors}

**What public analysis describes.** CSIS says commercial sensors have changed the battlefield. "All militaries must adapt to a world where movements, emissions, and signatures are constantly monitored." It adds that forces, "especially those at fixed sites and massed in central locations, must assume that they will be seen and their movements and emissions detected." Its prescription is "renewed emphasis on operational security, deception tactics, and electromagnetic spectrum discipline," with exercises that "simulate conditions where adversaries possess near-real-time ISR capabilities" (CSIS, 2025b).

A second CSIS chapter makes the human point. "Information is cheap. Processing it is expensive, and sense-making is exquisite." It also warns that rival services can use video data and a person's "digital dust" to reveal an identity that was meant to stay hidden (CSIS, 2025c).

Two lessons. Your signature is visible. And your own sensors only help if you can make sense of what they tell you.

**What it means for you.** Start from the adversary's side of the glass. MITRE's ATT&CK framework opens its list of tactics with Reconnaissance: "The adversary is trying to gather information they can use to plan future operations." The tactic covers adversaries "actively or passively gathering information that can be used to support targeting," and the information "may include details of the victim organization, infrastructure, or staff/personnel" (MITRE ATT&CK, TA0043). Its technique list includes active scanning of IP blocks and vulnerabilities, gathering host, identity and network information, and searching open websites and technical databases.

You are scanned all day. Most of it is noise. Some of it is a survey.

## Your signature

Your signature is everything an outsider can learn about you without breaking in. Think in five layers.

| Layer | What an outsider can see | The question to ask |
|---|---|---|
| Network | Address ranges, open services, certificate names, old test systems | Does every internet-facing service have an owner and a reason? |
| Software | Product names and versions in banners, headers and file paths | Does the outside need to know which product and version we run? |
| People | Names, roles, email formats, job postings, public social media | What does our public staff information say about who holds the keys? |
| Code and cloud | Public repositories, storage buckets, files left shared | What did we publish by accident, and who checks? |
| Behavior | Working hours, response times, vendor relationships | What does our rhythm tell a patient observer? |

This is not about hiding. Visibility is how business gets done. The goal is to know your signature and make deliberate choices about it, the way a unit chooses where to be seen.

CSIS frames this for militaries as emissions and signature discipline (CSIS, 2025b). Your civilian equivalent is attack surface management. Inventory what is exposed. Remove what is not needed. Patch what must stay. Then look at it again next month, because it will have changed.

## Count what you can see, then cut

The most valuable signature exercise costs almost nothing. Ask your team to produce a list of everything on the internet that is yours, using the same public sources an outsider would. Compare it with your asset register. The gap between the two lists is the work.

Joint guidance on network edge devices, released by CISA, NSA and partner agencies in February 2025, points the same way. NSA lists seven mitigation strategies, starting with "know the edge," and including disabling unneeded features and ports and securing management interfaces (NSA, 2025; CISA, 2025). An NSA expert explains why the edge matters: "if left unsecured, even unskilled malicious cyber actors have an easier time finding and exploiting vulnerabilities in their software or configurations" (NSA, 2025).

## Deception, with limits

NIST's cyber resiliency guidance includes a Deception technique: "Mislead, confuse, hide critical assets from, or expose covertly tainted assets to the adversary." It says deception can lead the adversary to waste effort and reveal tactics, techniques and procedures. It also says deception can complicate analytic monitoring and contextual awareness, and that these techniques "come at a cost to some other cyber resiliency objectives" (NIST SP 800-160 Vol. 2 Rev. 1, 2021).

Remember that when a vendor sells you a deception product. The idea has a long record in adversarial fields. NIST itself notes that Deception, Dynamic Positioning and Unpredictability are cyber adaptations of concepts from adversarial disciplines such as medicine, military and sports (NIST SP 800-160 Vol. 2 Rev. 1, 2021). Used well, a few decoy credentials, files or services that no legitimate user would ever touch give you a near-zero-noise alarm. Used badly, they are one more system to maintain and one more source of confusion.

My advice is modest. Start with a small number of decoys in places that matter. Make sure each one raises an alert that a human will see. Do not build a maze you cannot monitor.

## Your own sensors: the problem of sense-making

Now the other direction. What do you see?

IBM's 2026 study found that the mean time to identify and contain a breach was 247 days (IBM and Ponemon Institute, 2026). That is a sense-making number. The evidence was there. Someone had to find it, read it and decide.

CSIS's line applies exactly: information is cheap, processing it is expensive (CSIS, 2025c). Most mid-size organizations are not short of logs. They are short of attention. Three failure patterns recur:

1. **Everything collected, nothing asked.** Terabytes of logs with no question attached.
2. **Alerts without owners.** Detections that fire into a queue nobody is accountable for.
3. **Sensors without a heartbeat.** A source that quietly stops, and nobody knows.

NIST's incident response guidance (SP 800-61r3) is now written to sit inside the CSF 2.0 functions: Govern, Identify, Protect, Detect, Respond and Recover (NIST SP 800-61r3, 2025; NIST CSF 2.0, 2024). That helps. It puts detection beside governance and recovery in one loop, not in a silo.

## A small-sensor philosophy

Build detection from decisions, not from data.

- Start with the five or six decisions you must make fast in an incident. Isolate a host. Disable an account. Take a service offline. Notify a customer or regulator. Call counsel and law enforcement.
- For each decision, name the signals you need to make it with confidence.
- Collect and retain those signals first. Add more only when a question demands it.
- For each signal, assign an owner, a response time and a heartbeat check.

Fewer sensors, better understood, beat a sprawl nobody can read.

## Keep your own secrets from the wire

CSIS's phrase "digital dust" belongs on a poster in your office. Staff leave trails. Contractors leave trails. Old test systems leave trails. Cloud sharing links live forever unless someone ends them. A few steps pay off quickly:

- Review public repositories, shared drives and storage for exposed secrets and files.
- Set expiry on sharing links and temporary access.
- Rotate any credential that has ever appeared in a ticket, chat or document.
- Give staff clear guidance on what not to post about internal systems.

## What to do

1. **Make the outside-in list.** Everything public that belongs to you. Reconcile with your asset register. Fix the gaps.
2. **Pick your signature rules.** Decide what must be public, what can be reduced, and who approves exceptions.
3. **Define your six decisions** and the signals behind each one. Retire collection that serves no decision.
4. **Give every alert an owner and a clock.**
5. **Add heartbeats** to every critical log source, and test that silence raises an alert.
6. **Start small on decoys,** with legal and privacy sign-off, and only where a human will see the alarm.
7. **Exercise with a watcher in mind.** Run one tabletop a year that assumes the adversary has seen your public footprint for months.

## What to measure

- Number of internet-facing assets without a named owner.
- Gap between the outside-in list and your asset register.
- Median time from alert to first human action.
- Share of critical log sources with a working heartbeat check.
- Share of alerts that lead to a decision, versus alerts closed as noise.
