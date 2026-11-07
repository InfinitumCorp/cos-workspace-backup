
## Part VII: Buy testing like a professional {#part-vii-buying}

Most mid-size organizations buy their testing. That is sensible. CREST notes that organizations "can carry out penetration testing themselves, sometimes very successfully. More often, they decide to use specialist third-party penetration testing providers" (CREST, 2022). Outside testers bring skills a small team cannot keep on staff, a fresh view, and independence.

Buying well is a skill of its own. CREST's research found organizations reported difficulties in "establishing a business case for a test to be undertaken," "understanding the costs of external services – and determining the true overall cost," and "finding a suitable penetration testing expert when required (e.g. at short notice)" (CREST, 2022).

## The business case

Do not make the business case with fear. Make it with the evidence and your own numbers.

- **The exposure:** Verizon's findings on exploitation as the leading initial access vector, the 26% KEV full-remediation rate and the 43-day median (Verizon, 2026).
- **The cost of being late:** IBM's USD 4.99 million global average, the 247-day lifecycle, and the gap between breaches resolved inside and outside 200 days (IBM and Ponemon Institute, 2026).
- **The association:** IBM's finding that offensive security testing was associated with about USD 211,339 lower average breach cost when measured in isolation (IBM and Ponemon Institute, 2026). Present it honestly. It is a correlation in one study's sample, measured one factor at a time. It does not prove that testing caused lower costs, and it does not predict your result.
- **The trend:** Among breached organizations in IBM's study that planned to increase security investment, the share naming offensive security testing as an area of investment was 26%, down from 32% the year before (IBM and Ponemon Institute, 2026). You can read that as a gap worth closing.
- **Your own data:** Your outside-in view, your KEV backlog, your last test's repeat findings. These persuade more than any industry statistic.

## Choosing a provider

CREST lists supplier selection criteria: the ability to provide a "solid reputation," "history and ethics," "high quality, value-for-money services," "research and development capabilities," "highly competent, technical testers," and "security and risk management, supported by a strong professional accreditation and complaint process" (CREST, 2022). The NCSC says third-party tests "should be performed by qualified and experienced staff only," and recommends that UK government organizations use testers and companies in its CHECK scheme (NCSC, 2017/2022).

Accreditations and certifications are useful signals. They are not guarantees. Ask about the people who will actually do your work.

Questions I would ask any provider, including mine:

1. Which public methodology do you follow, and how do your phases map to it?
2. Who exactly will test, what are their qualifications, and will they be the same people named in the proposal?
3. Show me a redacted sample report. Does it include an executive summary, root causes and limitations?
4. How do you handle data you touch during testing, during and after the engagement?
5. What happens if you find a critical issue mid-test? How fast will I hear?
6. What happens if you find evidence of a real intruder?
7. How do you avoid causing outages, and what is your record of incidents caused by testing?
8. Is a retest included? On what terms?
9. Do you subcontract any part of the work? If so, to whom, and under what controls?
10. What insurance do you carry, and what liability terms do you propose?

A provider who is uncomfortable with any of these questions has told you something.

## Contract terms that matter

NIST's guidance on legal review applies to every testing contract: indemnity or limitation of liability clauses for intrusive testing, nondisclosure obligations, and privacy handling (NIST SP 800-115, 2008). Beyond those, put the following in writing.

| Term | Why |
|---|---|
| Reference to the signed authorization package and rules of engagement | So that scope and rules are binding, not advisory |
| Named testers and approval for substitutions | So you get the skills you paid for |
| Data handling, retention and destruction | NIST lists storage, transmission and "removal of data from systems upon conclusion of the assessment" as plan requirements (NIST SP 800-115, 2008) |
| Critical finding notification within an agreed time | So that a serious flaw does not wait two weeks for a report |
| Report requirements | The NCSC's five items plus your additions (Part IV) |
| Retest included | So "fixed" is verified, not assumed |
| Confidentiality of findings | Findings describe your weaknesses. Treat them as sensitive |
| Stop and real-intruder procedures | So the control decisions in Part II are enforceable |

## Independence and rotation

Long relationships build knowledge. They also build blind spots. Many organizations rotate providers, or at least rotate testers, every few years so that fresh eyes see the wall. That is a common practice, not a rule I can cite to a standard. Weigh it against the value of a provider who knows your estate.

Whatever you decide, keep the testing provider separate from the people whose work it tests. A provider who built your network should not be the only one testing it.

## Building internal capability

Buying testing does not mean outsourcing understanding. The NCSC's model assumes you have "an internal vulnerability assessment and management process" and that "a current vulnerability assessment should be shared with the testers" at scoping (NCSC, 2017/2022). That internal process is yours to own.

For a small team, internal capability means three things. Someone who runs and reads the scans. Someone who owns the remediation register. Someone who can read a test report critically and challenge it. ISC2 reports that 90% of respondents had one or more skills gaps on their cybersecurity teams (ISC2, 2024). If those three roles are not filled, fill them first, with staff, a managed service or a part-time advisor.

## Supplier testing and your supply chain

Your suppliers are part of your wall. Verizon's 48% third-party involvement figure makes that plain (Verizon, 2026). You usually cannot test a supplier's systems. You can:

- Ask key suppliers for evidence of their own independent testing and remediation, under nondisclosure.
- Test your side of every supplier connection: the accounts, the access paths and the controls you own.
- Include supplier scenarios in your tabletop exercises.
- Write testing and notification expectations into supplier contracts at renewal.

The NIST Cybersecurity Framework explicitly includes "security tests and exercises, including those done in coordination with suppliers and relevant third parties" as a source of improvements (NIST CSF 2.0, 2024, ID.IM-02).

## Receiving reports from outsiders

Sometimes the uninvited tester is friendly. A researcher finds a flaw and wants to tell you. The NIST Cybersecurity Framework includes an outcome for this: "Processes for receiving, analyzing, and responding to vulnerability disclosures are established" (NIST CSF 2.0, 2024, ID.RA-08).

A simple, published way to report a vulnerability, a named owner, and a commitment to respond is cheap. It turns some of the people walking your walls into allies. Write it with counsel, so that it is clear what you invite and what you do not.

> **The takeaway.** Buy on evidence, not fear. Ask hard questions of every provider. Contract for the report, the data, the stop and the retest. Keep enough capability in-house to challenge what you are told.

## What to do

- Build the business case from public data and your own exposure numbers, and state the limits of the evidence.
- Use the ten questions and the contract terms above in your next procurement.
- Fill the three internal roles before expanding external testing.
- Publish a simple vulnerability disclosure process.

## What to measure

- Share of engagements with named testers matching the proposal.
- Time from critical finding to notification, against the contract.
- Share of key suppliers that have provided evidence of independent testing.
