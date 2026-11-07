
## Part II: Permission first. Authority that stands up {#part-ii-authority}

This is the part of the paper I care about most.

Without permission, there is no such thing as ethical hacking. There is only hacking. The difference between a security test and a crime is a signature, a scope and a set of rules, made before the work starts, by people with the authority to make them.

NIST's glossary defines rules of engagement as "detailed guidelines and constraints regarding the execution of information security testing," established before the start of a test, that give the test team "authority to conduct defined activities without the need for additional permissions" (NIST SP 800-115, 2008). Read the last phrase again. Authority to conduct defined activities. Not any activities. Defined ones.

## Who may say yes

Permission has to come from someone who actually owns the risk and the systems. That sounds obvious. It is where many programs go wrong.

NIST says that if an organization "does not control part or all of its network, such as having a portion of its systems housed on a third party's network, the owner of the other network usually must also consent in writing to the assessment plan." It gives the example of shared systems, such as virtual machine platforms that serve several organizations. "By signing the assessment plan, all parties acknowledge and approve of the assessment" (NIST SP 800-115, 2008).

In a modern mid-size organization, that list of owners is long. Cloud platforms. Software-as-a-service providers. Managed service providers. Hosting companies. Payment processors. Each has its own terms on what customers may test and how. Some publish testing policies. Some require notice. Some forbid certain activities outright. Your contract with the tester does not override your contract with them.

My rule: if you do not own it outright, you get written permission from whoever does, or it is out of scope.

## The law is part of scope

NIST recommends that legal advisors "always be involved for intrusive tests such as penetration testing." Legal departments "may assist in reviewing the assessment plan and providing indemnity or limitation of liability clauses into contracts," may require nondisclosure agreements, and "should also address any privacy concerns" (NIST SP 800-115, 2008). NIST notes that captured data "may include sensitive data that does not belong to the organization—or personal employee data, which may create privacy concerns" (NIST SP 800-115, 2008).

In the United States, the federal computer crime statute turns on authorization. When the Department of Justice revised its charging policy under the Computer Fraud and Abuse Act in 2022, it said that, for the first time, the policy "directs that good-faith security research should not be charged." It also said that "claiming to be conducting security research is not a free pass for those acting in bad faith," and that the policy focuses on cases where a defendant "is either not authorized at all to access a computer or was authorized to access one part of a computer" and accessed a part beyond it (DOJ, 2022).

That is a prosecutorial policy, not a safe harbor, and it is not legal advice. I cite it to make one point: authorization is the legal hinge. Testing inside it is defense. Testing outside it may be a crime, whatever the intent. Other countries have their own laws, and testing across borders raises its own questions. Ask counsel in every jurisdiction involved.

## The authorization package

NIST describes an assessment plan, rules of engagement, or both, and suggests a short memorandum that testers can show to staff "as authorization to gain access to particular systems" (NIST SP 800-115, 2008). Whatever you call the documents, the package should answer these questions in writing.

| Question | What the document must say |
|---|---|
| **Who authorizes?** | Named executive owner with authority over every system in scope, plus written consent from any third-party owners |
| **Who tests?** | The provider, the named testers, their qualifications, and any background checks your policies require |
| **What is in scope?** | Systems, applications, address ranges, locations and people, listed specifically |
| **What is out of scope?** | An explicit exclusion list. NIST says the plan "should also list specific systems ... that are not authorized to be examined or tested" (NIST SP 800-115, 2008) |
| **What is allowed?** | Types and level of testing, at a level of detail that describes "the type of testing, approach, and tools" (NIST SP 800-115, 2008) |
| **What is forbidden?** | Prohibited activities stated "in a way that leaves no room for interpretation" (NIST SP 800-115, 2008) |
| **When?** | Dates, hours, blackout periods and change freezes |
| **From where?** | Source addresses and locations of testing, so administrators can tell testing from attack (NIST SP 800-115, 2008) |
| **Who is on call?** | Primary and alternate contacts on both sides, available at short notice, and an escalation path |
| **What about data?** | Storage, encryption, transmission, retention and destruction of any data the testers touch |
| **What if something breaks?** | Stop conditions, who can call a halt, and how service is restored |
| **What if they find a real intruder?** | Whether testing stops, who is told, and who decides when it resumes |
| **Who else must know?** | Requirements to inform parent organizations, insurers, regulators or incident response providers |

That last row matters more than it looks. NIST says the plan should identify any requirements "to inform parent organizations, law enforcement, and a computer incident response team" and, for covert testing, define how detected test activity is handled, so that "assessment activity does not trigger reporting of security breaches to external parties" (NIST SP 800-115, 2008). Think about your cyber insurer and your managed security provider. A test that triggers a false breach notification is a test that went badly.

## The real intruder clause

This one deserves its own heading. Testers sometimes find evidence that someone else got there first.

NIST asks the right questions: "if the assessors discover an actual intruder or an intruder's footprints within the network, should testing stop? If so, when can testing recommence—and by whose authority?" It says the plan "should provide clear-cut instructions" (NIST SP 800-115, 2008).

Decide in advance. In my view the default should be: stop the test, preserve what was seen, hand over to incident response under your existing plan, and restart only with fresh written authority. A test that keeps running over a live intrusion can destroy evidence and confuse the response.

## People in scope

Social engineering tests touch real people. They deserve more care, not less.

The NCSC's description of scenario-driven testing and CREST's note that a penetration test "plays only a small part (despite often including social engineering tests) in reviewing the people element" both treat people as part of the picture (NCSC, 2017/2022; CREST, 2022). If people are in scope, add these to the package:

- Explicit leadership approval and, where your policies or law require it, review by human resources and counsel.
- A rule that results are reported as patterns and process gaps, not as names to be disciplined.
- A ban on pretexts that would cause real distress, exploit personal circumstances or impersonate emergency services, regulators or law enforcement.
- A debrief plan, so that the people involved learn something and are not simply embarrassed.

The purpose of testing people is to fix processes, such as how the help desk verifies a reset or how finance confirms a payment change. A test that makes staff afraid to report mistakes has made you weaker.

## Stop means stop

Every authorization needs a stop. Name who can call it on each side, how it is communicated, and how fast testers must cease. Test the stop at the kickoff meeting. It takes two minutes and it will tell you whether the contacts actually answer.

> **The takeaway.** Permission is not paperwork. It is the line between defense and attack. Get it from every owner, in writing, before anyone touches anything.

## What to do

- Adopt a standard authorization template based on the table above and NIST's rules-of-engagement outline in SP 800-115 Appendix B.
- List every third-party platform in scope and record the written permission or published testing policy for each.
- Involve counsel for every intrusive test. Decide the real-intruder clause and the stop procedure before kickoff.
- For any test involving people, add the people safeguards above.

## What to measure

- Share of tests with a complete, signed authorization package before the start date.
- Number of third-party systems tested without recorded permission. The target is zero.
- Time from "stop" to cessation in the kickoff drill.
