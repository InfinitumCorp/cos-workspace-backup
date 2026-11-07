
## Part II: Drones. Cheap mass against your attention {#part-ii-drones}

**What public analysis describes.** The economics come first. CSIS puts them in one line: "If a $500 drone can destroy a multimillion-dollar tank, so, too, can a USV swarm destroy a fleet of ships" (CSIS, 2025a). That is a statement about cost asymmetry, not a measurement of how often it happens. CSIS also says "counter-drone solutions will be decisive on the future battlefield" (CSIS, 2025a), and describes the most marked change as cheap, flexible and highly maneuverable ISR drones (CSIS, 2025a).

Cheap. Many. Flexible. The answer to it is not one exquisite shield. It is a layered, cheap, repeatable defense, and a way to keep from running out of it.

**What it means for you.** Your drones are not aircraft. They are software. Automated scanning for exposed services. Credential stuffing against login pages. Bot traffic. Floods. Commodity phishing kits sold as a service. ENISA describes Phishing-as-a-Service as "automation that paves the way for attackers regardless of their experience" (ENISA, 2025). The same logic as the drone: low cost, low skill, high volume.

The 2026 Verizon DBIR gives a sense of the scale on the flooding side. Its year-in-review timeline records a botnet of 300,000 internet-of-things hosts launching a record 29.7 Tbps DDoS attack, nearly doubling previous peaks (Verizon, 2026). Meanwhile, the median attack size has stayed between 4.2 and 6 Gbps, and half of all attacks last under nine minutes (Verizon, 2026). Both things are true. The peaks grow. The routine stays small and cheap.

For an organization your size, the peak is a vendor problem. The routine is yours.

## The cost exchange

Here is the exchange in plain terms. The left column is the attacker's cheap move. The right column is the defender's cheap answer. This is my summary, built on the sources cited in this part. It is not a measured result.

| Cheap move against you | What it costs you if unanswered | Cheap answer |
|---|---|---|
| Automated login attempts using stolen credentials | Account takeover; investigation time | Multifactor authentication on externally exposed applications and remote access; lockout and rate limits |
| Mass phishing and pretexting | Analyst time per report; a successful click | Phishing-resistant authentication; reporting button; verification rules for payment and identity requests |
| Scans for old, exposed services | One unpatched edge device is a way in | Inventory of the edge; automated patching; remove what you do not use |
| Short flood bursts, repeated | Outage minutes; staff pulled off other work | Upstream DDoS protection; a rehearsed runbook; clear thresholds for escalation |
| AI bot traffic hitting sites and APIs | Bandwidth, content exposure, noise | Rate limits; bot management; robots rules; monitoring |

Notice what is in the right column. No miracle. Authentication, patching, inventory, capacity and a plan.

Verizon's mitigation guidance for exploited vulnerabilities and stolen credentials lines up with the table: require MFA for externally exposed applications and for remote network access, and perform automated operating system and application patch management (Verizon, 2026).

## Plan for the tail, not the average

Verizon gives numbers worth building a runbook around. For the repeatedly attacked DDoS victims in its sample, Verizon reports a median attack duration of 24 minutes. At the higher end of the distribution, it puts duration at around 88 minutes at the 90th percentile and 101 minutes at the 95th (Verizon, 2026).

So design for roughly two hours. Ask three questions.

1. Which customer-facing or revenue-critical services would be unavailable for two hours, and what would that cost?
2. Who decides when to switch to the upstream mitigation or the backup path, and what do they need to know?
3. What does the rest of the team do during a flood? Verizon's own question is the right one: "What would be the impact to your business if your business was affected?" (Verizon, 2026).

One caution, and it is my judgment, not a finding. Treat any flood as a possible distraction. While your eyes are on the loud problem, check the quiet ones. Make sure someone is assigned to do exactly that.

## Counter-drone for the network: four layers

**Absorb.** Put capacity between the flood and your service. For most mid-size organizations, that means buying protection from an upstream provider rather than building it. Ask for written answers on how it works, how fast it engages, and what it costs when attacks run long.

**Filter.** Rate limits, bot management, geo and reputation rules where they make sense, and strong authentication on every login surface. Verizon notes that defenders have to "maintain our footing and use collaboration and partnerships" against growing attacker capability (Verizon, 2026). Sharing with peers and providers counts as a layer.

**Automate.** Cheap and repeatable. Patch automation. Configuration baselines. Alert enrichment. IBM found that security teams extensively using AI and automation shortened breach times by 65 days and lowered average costs by USD 1.93 million compared with those that did not. Only 36% of breached organizations said they used these tools extensively across the security lifecycle (IBM and Ponemon Institute, 2026). That is an association in a benchmark study. It is not proof of what a tool will do for you. But the direction is clear: volume answered by automation.

**Intercept, with a human on the trigger.** Automated response can contain a compromised account or isolate a host faster than a person can. It can also cause an outage faster than any attacker. Start every automated action in recommend-only mode. Widen authority as evidence supports it. Keep a clear off switch and a named owner.

CSIS gives the right caution from the battlefield side: when both sides have AI-enabled systems, "the incentive will lean heavily toward deferring as much as possible to the AI's capability," and "for now, that surely will lead to mistakes" (CSIS, 2025a). Replace "targeting" with "triage" and the warning still holds. Do not let your people turn into a stamp of approval.

## The next turn of the cycle

CSIS offers a forecast, flagged as a forecast. It says sophisticated adversaries will probably find ways to combine AI and cyberattacks, with "offense likely outstripping defense at first," and that AI agents will be able to find vulnerabilities and exploit them "without phoning home and raising alarms" (CSIS, 2025a). Treat that as a planning assumption, not as a fact.

What follows from it? Shorter patch windows on the edge. More weight on detection of behavior over indicators. More automation on your side, built on the same cheap controls.

## What to do

1. **Write the cost-exchange table for your own organization.** Five rows. Their move, your cost, your cheap answer. Fill in the missing right-hand cells and fund the gaps.
2. **Put MFA on every externally exposed login and every remote access path.** Administrators and remote access first.
3. **Automate patching on the edge.** Set a target time for known-exploited vulnerabilities on internet-facing systems, and track it.
4. **Buy absorption, do not build it.** Get upstream flood protection in writing, and run a rehearsal.
5. **Run the two-hour drill.** Simulate a two-hour outage of one customer-facing service and note what breaks.
6. **Start automation in recommend-only mode,** and review overrides weekly.

## What to measure

- Median time to remediate known-exploited vulnerabilities on internet-facing systems (your baseline, not a survey median).
- Share of external login surfaces protected by multifactor authentication.
- Mean time from flood detection to mitigation engagement, in rehearsal.
- Analyst hours spent per week on repetitive triage, and the share handled by automation with human review.
