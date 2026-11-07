
# Analysis: walking your own walls {#analysis}

The analysis has eight parts. Each ends with what to do and what to measure.

## Part I: Know the difference. Four kinds of looking {#part-i-kinds-of-testing}

The most expensive mistake in testing is buying the wrong kind. CREST's research with organizations found that "understanding the difference between vulnerability scanning and penetration testing" was one of the top six challenges they reported, alongside "identifying what type of penetration test is required" (CREST, 2022).

So start with definitions. They are not academic. They decide what you pay for and what you learn.

## Examination and testing

NIST draws the first line. Examinations "primarily involve the review of documents such as policies, procedures, security plans, security requirements, standard operating procedures, architecture diagrams, engineering documentation, asset inventories, system configurations, rulesets, and system logs." Testing "involves hands-on work with systems and networks to identify security vulnerabilities" (NIST SP 800-115, 2008).

Both matter. NIST warns that testing "is less likely than examinations to identify weaknesses related to security policy and configuration," and that "in many cases, combining testing and examination techniques can provide a more accurate view of security" (NIST SP 800-115, 2008). A good program reads the plans and walks the wall.

## Vulnerability scanning

CREST describes vulnerability assessment, "sometimes referred to as 'scanning'," as "the use of automated tools to identify known common vulnerabilities in a system's configuration." Such tools "scan the information systems environment to establish whether security settings have been switched on and consistently applied – and that appropriate security patches have been deployed." It "does not exploit vulnerabilities identified to replicate a real attack, nor does it consider overall security management processes and procedures that support the system" (CREST, 2022).

Scanning is the sentry on the wall. It is cheap, repeatable and broad. It is also noisy and literal. A scanner reports what it can see from where it stands. It does not know which server holds your payroll.

For some organizations, scanning is available at no cost. CISA's Cyber Hygiene services include vulnerability scanning that "continuously monitors and assesses internet-accessible network assets," with weekly reports and ad-hoc alerts on urgent findings, including known exploited vulnerabilities, and web application scanning that covers, among other things, the OWASP Top Ten (CISA Cyber Hygiene). CISA states the services are available to U.S.-based federal, state, local, tribal and territorial governments, and to public and private sector critical infrastructure organizations (CISA Cyber Hygiene). CISA also says enrolled organizations "typically reduce their risk and exposure by 40% within the first 12 months." That is CISA's own claim about its program. I report it as such.

## Vulnerability assessment

In this paper, I separate scanning from assessment, even though some sources use the terms interchangeably. Assessment is what a skilled person does with scan results and everything else: validate them, remove false positives, add business context, and rank what matters. NIST's example of an assessment plan for a vulnerability assessment lists activities "such as port and service identification, vulnerability scanning, security configuration review, and password cracking" against agreed targets (NIST SP 800-115, 2008). The point is judgment, not volume.

The NIST Cybersecurity Framework 2.0 puts the outcome in one line: "Vulnerabilities in assets are identified, validated, and recorded" (NIST CSF 2.0, 2024, ID.RA-01). Identified, validated and recorded. Scanning does the first. Assessment does all three.

## Penetration testing

A penetration test goes a step further. It asks whether a weakness can actually be used, and what follows if it is.

The NCSC defines it as "a method for gaining assurance in the security of an IT system by attempting to breach some or all of that system's security, using the same tools and techniques as an adversary might" (NCSC, 2017/2022). CREST calls it "an ethical attack simulation" built around a manual testing process (CREST, 2022).

NIST divides a penetration test into four phases: planning, discovery, attack and reporting. In the planning phase, "rules are identified, management approval is finalized and documented, and testing goals are set." NIST adds: "No actual testing occurs in this phase" (NIST SP 800-115, 2008). Remember that sentence. A large part of a good test happens before anyone tests anything.

Penetration tests come in different shapes. The NCSC describes a range by how much the testers are told. In transparent or open box testing, "full information about the target is shared with the testers." In opaque or closed box testing, "no information is shared with the testers about the internals of the target," which "more accurately models the risk faced from attackers that are unknown or unaffiliated to the target organisation," but "can also result in vulnerabilities remaining undiscovered in the time allocated for testing" (NCSC, 2017/2022). NIST makes the related distinction between external testing, conducted "from outside the organization's security perimeter," and internal testing (NIST SP 800-115, 2008).

There is a trade. The less you tell the tester, the more realistic the test, and the less of your estate it covers in the time you paid for. For most mid-size organizations, more information produces more value per day. Save the opaque test for the question it answers best: what does an unknown outsider see?

## Red teaming

Red teaming is a different discipline with a different question. CREST quotes the UK Ministry of Defence Red Teaming Guide, which defines a red team as "a team that is formed with the objective of subjecting an organisation's plans, programmes, ideas and assumptions to rigorous analysis and challenge" (CREST, 2022). In security practice, the red team emulates an adversary to test whether the organization's people, processes and technology can detect and respond.

The European TIBER-EU framework, built for the financial sector, describes "threat intelligence-based ethical red-teaming" that mimics "the tactics, techniques and procedures of real-life attackers, based on bespoke threat intelligence." Its key line: "The outcome is not a pass or fail." The test is intended "to reveal the strengths and weaknesses of the cyber resilience measures put in place by the tested entity, with a focus on the learning effect of the test" (ECB, TIBER-EU).

Red teaming is powerful and easy to misuse. It is the last thing a young program needs, not the first. If you cannot keep up with your scan results, you are not ready to learn that your monitoring missed a simulated intruder. You already know.

## Purple teaming

Purple teaming puts the attackers and defenders in the same room, on purpose. The red side runs an agreed activity. The blue side watches what its tools saw and what they missed. Both sides fix the gap together. TIBER-EU publishes separate purple-teaming guidance for how this is managed inside its testing and closure phases (ECB, TIBER-EU).

For a mid-size organization, purple exercises often deliver more learning per dollar than a covert red team, because nothing is wasted on secrecy. The goal is not to catch anyone out. It is to make the sentries better.

## The comparison

| | Scanning | Assessment | Penetration test | Red team | Purple exercise |
|---|---|---|---|---|---|
| **Question** | What known weaknesses are visible? | Which are real and which matter most? | Could an attacker get through, and how far? | Would we notice and respond? | Can we see and stop this specific behavior? |
| **Depth** | Broad, shallow | Broad, validated | Narrow, deep | Objective-driven | Narrow, collaborative |
| **Who knows** | Everyone | Everyone | Usually IT and security | A small control group | Everyone involved |
| **Cadence** | Continuous | Monthly or quarterly | Annually and after major change | When fundamentals are in place | Regularly, by theme |
| **Main output** | Finding list | Ranked, validated findings | Exploitable paths and fixes | Detection and response gaps | Tuned detections |
| **Readiness needed** | An inventory | A remediation process | Assessment under control | Detection and response in place | A team willing to learn in the open |

Treat the cadence column as my judgment, not a standard. Your regulators, customers and risk appetite may require more.

## What to do

- Write a one-page testing policy that defines these five activities in your own words and says who may commission each.
- Start or tighten continuous external scanning before buying a deeper test. If you are eligible, consider CISA's no-cost services.
- Match each test to the question you need answered. Write that question at the top of the scope.
- Do not buy a red team until scanning and assessment are under control.

## What to measure

- Share of internet-facing assets covered by continuous scanning.
- For each test, whether the stated question was answered.
- Share of penetration test findings that your own assessment had already identified. The NCSC's ideal is that you know most of them in advance (NCSC, 2017/2022).
