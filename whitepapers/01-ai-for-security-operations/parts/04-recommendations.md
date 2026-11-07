# Recommendations

Here is the part you came for. Six moves, in order. Each one has a reason, a set of steps, a way to tell whether it is working, and the traps I see most often. After the six moves, I give you a 90-day plan, a short list of metrics, and a list of questions to put to any vendor.

A word on sequence. The order matters. Governance comes before pilots, and securing the AI comes before you widen it. Organizations that start with the exciting part, the pilot, tend to skip the unexciting part, the rules, and then find out about shadow AI the hard way (IBM/Ponemon, 2026).

## Move 1: Govern first

**Why.** IBM found that 68% of breached organizations lacked AI governance to manage AI or detect shadow AI, and only 19% coordinated governance and security teams (IBM/Ponemon, 2026). CSF 2.0 made Govern a Function of its own for a reason (NIST CSF 2.0, 2024). In irregular warfare terms, this is unity of effort. If nobody owns it, nobody defends it.

**What to do.**

1. **Name an accountable owner** for AI use in security, and an executive sponsor. Write the names down.
2. **Write a one-page AI use rule.** It should say what is approved, what is not, what data may go where, who approves new tools, and how to report a problem. One page. If it takes longer to read than a coffee, nobody will read it.
3. **Define your three data classes** (open, internal, restricted) and say which AI tools may touch which class.
4. **Provide a sanctioned tool.** If people have a good approved option, they are less likely to use an unapproved one. Verizon found that 67% of users accessing AI services from corporate devices used non-corporate accounts (Verizon DBIR, 2026).
5. **Put AI vendors under your supply chain risk process.** CSF 2.0 includes a category for cybersecurity supply chain risk management (NIST CSF 2.0, 2024). Ask the questions in the vendor list below.
6. **Set a risk appetite for autonomy.** Use the four tiers from Part VII. Decide now that nothing goes above Tier 2 without the executive sponsor's sign-off.

**How you know it is working.** Anyone on your staff can tell you, in one sentence, which AI tools are approved and what data they may use. Your inventory matches reality within a margin you can state.

**Traps.**

- *The shelf policy.* A policy that nobody follows is worse than none, because it creates false confidence.
- *Ban and hope.* A ban without an alternative pushes the behavior out of sight.
- *Security-only governance.* IBM's finding about coordination is a warning. Bring legal, privacy, HR and the business owners in early.

## Move 2: Measure a baseline

**Why.** You cannot prove AI helped if you do not know where you started. IBM's numbers show that time is where the money goes: lifecycles over 200 days averaged USD 5.65 million, against USD 4.32 million for shorter ones (IBM/Ponemon, 2026). Persistence is the adversary's advantage. Time-to-detect and time-to-contain are your counter.

**What to do.** Record, for the last 90 days or as much history as you have:

- **Mean time to acknowledge** an alert (first human look).
- **Mean time to triage** (decision: benign, suspicious, incident).
- **Mean time to contain** confirmed incidents, however few.
- **Alert volume** per analyst, and the share closed as false positives.
- **Phishing report volume** and time from report to action.
- **KEV exposure:** how many KEV-listed vulnerabilities are present in your environment, and how many days the oldest has been open. Verizon's median was 16 KEV vulnerabilities per organization and 43 days to full remediation (Verizon DBIR, 2026). Compare yourself to that. Do not treat it as a target.
- **Third-party exposure:** how many vendors have access to your data or systems, and how many have given you evidence of multifactor authentication.
- **Recovery:** the last time you restored a critical system from backup, how long it took, and what broke.

If you do not have the data, that is a finding. Start collecting it. Even rough numbers are better than none.

**How you know it is working.** You can put one page in front of the executive sponsor and say, "This is where we are today."

**Traps.**

- *Vanity metrics.* Alerts closed, models deployed, or prompts submitted tell you nothing about risk.
- *Moving the goalposts.* Lock the definitions before the pilot begins, so you do not redefine success after the fact.
- *Measuring only speed.* Track quality, too: errors, overrides, missed items.

## Move 3: Pilot with analysts in the loop

**Why.** IBM found that organizations using security AI and automation extensively had lower breach costs and faster identification and containment, though it was a minority (36%) of breached organizations (IBM/Ponemon, 2026). ISC2's practitioners expect AI to help, and they also expect the biggest payoff to take two years or more (ISC2, 2024). Both are true. Start small and learn quickly.

**What to do.**

1. **Pick one workflow** from the four starting points: phishing report triage, KEV-first vulnerability prioritization, incident and alert summarization, or vendor document review.
2. **Define success before you start.** Choose two or three measures from your baseline. Write them down. For example: reduce time to first triage decision for phishing reports, with no increase in missed malicious messages.
3. **Run it at Tier 0 or 1.** The AI reads and recommends. A person decides. Log every recommendation and every human decision.
4. **Run it in parallel first.** For the first few weeks, have analysts do the work the normal way and compare with the AI's output. This gives you an honest error rate.
5. **Treat all model input as untrusted.** If the tool reads email, tickets or web content, assume an adversary can write some of that content. Do not give the tool the ability to take actions based on instructions inside the content it reads.
6. **Review weekly.** Look at the overrides. Each one is a lesson.
7. **Decide with evidence.** At the end of the pilot, compare with the baseline. Keep, change or stop.

**How you know it is working.** Analysts choose to use it. Time and error numbers improve against the baseline. And when the tool is wrong, someone catches it before it matters.

**Traps.**

- *Pilot theater.* A pilot that is designed to succeed teaches you nothing.
- *Automation bias.* People tend to trust a confident machine. Track the cases where the analyst agreed with a wrong recommendation, and retrain accordingly. NIST's Generative AI Profile flags over-reliance as part of its human-AI configuration risk (NIST AI 600-1, 2024).
- *Scope creep.* Resist adding a second workflow until the first has a result.

## Move 4: Point AI at exposure

**Why.** This is the move that most reflects the irregular warfare lens. Adversaries go where defenders are weakest. Verizon found vulnerability exploitation is now the leading initial access vector at 31%, and that only 26% of KEV-listed vulnerabilities were fully remediated (Verizon DBIR, 2026). IBM found that AI use in security leans toward detection and response, with prevention lagging, and only 18% of organizations with agents in their SOC used them for vulnerability scanning and management (IBM/Ponemon, 2026). Deterrence by denial starts with closing the doors that are known to be used.

**What to do.**

1. **Build your inventory.** You cannot patch what you do not know you have. Start with internet-facing systems, identity systems and anything that holds restricted data. CSF 2.0's asset management category exists for this reason (NIST CSF 2.0, 2024).
2. **Match against KEV.** Make the CISA KEV catalog a standing input to your vulnerability process. For any KEV-listed item in your environment, assign an owner and a date.
3. **Use AI to help prioritize and communicate.** Ask the AI to summarize which exposures combine KEV status, internet exposure and asset importance, and to draft clear remediation requests for system owners. A person validates the list before it goes out.
4. **Tighten identity.** Strong authentication and least privilege reduce what an adversary can do with a stolen credential. IBM lists identity and access management among factors associated with lower breach costs (IBM/Ponemon, 2026).
5. **Look at your edges.** Verizon found third-party involvement in 48% of breaches, and low rates of MFA remediation on third-party cloud accounts (Verizon DBIR, 2026). Ask your most critical vendors for evidence of MFA and patching. Put it in the contract.
6. **Set a service-level target for KEV items.** Choose a number your team can actually meet, such as a target number of days, and track it. Make exceptions visible, with an owner and an expiry date.
7. **Close the loop on people.** Verizon found the human element in 62% of breaches (Verizon DBIR, 2026). Give staff a one-step way to report suspicious messages and a verified call-back rule for any request that moves money or changes access. Train for voice and text as well as email. Mobile-centric vectors had a median success rate 40% higher than email in Verizon's phishing simulations (Verizon DBIR, 2026).

**How you know it is working.** Your KEV backlog shrinks and its oldest item gets younger. Exceptions are rare and documented. A report of a suspicious voice call or text gets as much attention as a report of a suspicious email.

**Traps.**

- *Score worship.* A numeric score is an input, not a decision. Asset context matters.
- *Patching without testing.* Speed matters, but so does not breaking the business. Define a fast path for KEV items with a tested rollback.
- *Forgetting the old.* Verizon found that most persistent exploitation involved older vulnerabilities, with only 20% registered in 2024 and 2025 (Verizon DBIR, 2026). The adversary has a long memory. Your backlog should too.

## Move 5: Secure the AI itself

**Why.** AI is terrain. IBM found AI-related breaches in 21% of organizations studied, with 92% of those lacking proper AI access controls (IBM/Ponemon, 2026). Shadow AI incidents more than doubled to 43% (IBM/Ponemon, 2026). NIST, CISA and MITRE all publish material on this (NIST AI 600-1, 2024; CISA et al., 2025; MITRE ATLAS).

**What to do.**

1. **Inventory every AI tool**, model, plug-in and connection, including those staff adopted on their own. Sources include your single sign-on logs, expense reports, browser and network telemetry, and a simple staff survey. Ask without blame.
2. **Give each AI integration its own identity** with least privilege. No shared accounts. Review the permissions on a schedule.
3. **Control the data path.** Know what data goes into each tool, where it is stored, who at the vendor can see it, and whether it is used to train models. Use your three data classes.
4. **Treat what the model reads as untrusted.** The most important design rule is that content from outside your organization, such as an email, a web page or an uploaded file, must not be able to give the model orders. Separate reading from acting. Keep high-impact actions behind human approval.
5. **Log everything the AI does.** You need an audit trail of prompts, outputs and actions for the same reason you have logs for administrators.
6. **Plan for failure.** Define the manual fallback for every AI-assisted workflow. If the tool is down, wrong or compromised, the team must still be able to do the job.
7. **Extend your incident plan** to cover AI incidents: data exposure through a model, prompt injection, poisoned inputs, an AI account compromise. Add the first-hour steps and the people to call.
8. **Apply the data security basics** from the joint CISA guidance to the data you feed AI: provenance, integrity checks, access control, encryption, and secure storage (CISA et al., 2025).
9. **Use authorized testing.** Have the AI-enabled workflows tested by people you have authorized in writing, with agreed scope and rules of engagement. Use ATLAS and ATT&CK as a vocabulary for what to test.

**How you know it is working.** Your inventory is complete enough to withstand a surprise. Every AI integration has an owner, a credential, a data class and a fallback. A test of the AI workflow does not result in the tool taking an action it should not.

**Traps.**

- *Treating the vendor as the owner.* The vendor secures its platform. You own your configuration, your data and your permissions.
- *Over-permissioned assistants.* An AI helper that can read everything and send anything is an insider you did not vet.
- *No offline path.* If your response plan depends on a tool that is itself under attack, you have a single point of failure.

## Move 6: Test, then widen

**Why.** Resilience is about performing under pressure, and you only know your performance by testing it. IBM found that only 42% of breached organizations reported full recovery, and that fewer than one in 20 recovered in under 50 days (IBM/Ponemon, 2026). IBM also lists offensive security testing among factors associated with lower breach costs (IBM/Ponemon, 2026). In IW terms, this is rehearsal. You do not want your first meeting with the problem to be the real one.

**What to do.**

1. **Run a tabletop exercise** at least twice a year. A good defensive scenario for this topic: a convincing voice call asks the help desk to reset a senior executive's credentials, while at the same time your AI triage tool summarizes a related phishing report as low priority. Walk through who decides what, how you verify identity, what the AI recommended, and what the human did. Include communications and legal.
2. **Commission authorized testing** of your external exposure and your most critical applications. Set the scope and rules in writing. Use the findings to feed your KEV-style prioritization.
3. **Test recovery.** Restore a critical system from backup in a controlled way. Time it. Write down what failed.
4. **Review the pilots** against the baseline each quarter. Promote an AI function one tier only with evidence, a named owner and a tested rollback.
5. **Widen carefully.** After the first workflow has results, choose the next one. Resist the urge to buy a platform that does everything.
6. **Share what you learn.** Participate in information sharing with your sector, and report relevant incidents to the proper authorities. The DoD Annex observes that no single agency has primacy and unified action must be pursued deliberately (DoD, 2020). The same is true across your sector. No company defends alone.

**How you know it is working.** Your exercises produce action items and you close them. Your recovery time is a number you know, and it is going down. Your autonomy tiers match what you can defend with evidence.

**Traps.**

- *Testing without authorization or scope.* Never test systems you do not own or have not been authorized to test. Make the authorization explicit and in writing.
- *Checkbox exercises.* An exercise that produces no changes was not an exercise.
- *Quietly raising autonomy.* Tier promotion should be a decision, recorded, with a name on it.

## A 90-day plan

This is a starting shape, not a promise. Adjust it to your size and your risk.

| Days | Focus | Key outputs |
|---|---|---|
| **1–15** | Govern and inventory | Named owner and sponsor; one-page AI use rule; three data classes; first AI tool inventory; approved tool list |
| **16–30** | Baseline | One-page baseline of time, volume, KEV exposure, third-party exposure and recovery; agreed definitions |
| **31–60** | Pilot | One workflow at Tier 0 or 1; parallel run; weekly review; log of overrides and errors |
| **61–75** | Exposure | KEV process with owners and dates; vendor evidence requests sent; identity review for AI integrations |
| **76–90** | Test and decide | Tabletop exercise; recovery test; pilot review against baseline; keep, change or stop; plan for the next quarter |

## Metrics for the executive sponsor

Keep the dashboard short. These are the measures I would put in front of an executive sponsor each quarter:

1. **Time to first look and time to contain**, against baseline.
2. **KEV backlog:** count, and age of the oldest item.
3. **AI inventory coverage:** share of AI tools with an owner, identity, data class and fallback.
4. **Pilot quality:** analyst override rate and error categories.
5. **Recovery time** for your most critical system, as last tested.
6. **Exercise follow-through:** share of action items closed.
7. **Third-party evidence:** share of critical vendors who have provided MFA and patching evidence.

## Questions to put to any vendor

Whether you are buying a new AI security product or evaluating AI features in a tool you own, ask:

1. What data does the feature see, where is it processed and stored, and who at your company can access it?
2. Is our data used to train or improve models for others? Can we turn that off, and is it in the contract?
3. What actions can the feature take on its own? Can we restrict it to read-only or recommend-only?
4. How does the feature treat content from outside our organization, such as emails, web pages and files? What protections exist against that content manipulating it?
5. What logs do we get? Can we see prompts, outputs and actions?
6. How do we turn it off, and what happens to our workflow when we do?
7. How is the feature tested, and what is its known failure behavior? Can you share evidence?
8. Which frameworks do you map to, such as NIST AI RMF or MITRE ATLAS? Can you show how?
9. What happens in the event of your own security incident? How and when will we be told?
10. What does exit look like? Can we get our data and configurations out?

A vendor who welcomes these questions is a vendor to talk to. A vendor who deflects them has told you something too.
