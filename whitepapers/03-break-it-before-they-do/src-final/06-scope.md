
## Part III: Scope like the besieger. See yourself from outside {#part-iii-scope}

A test is only as good as its scope. Scope too narrow, and the report is clean and useless. Scope too broad, and the testers spend their days skimming and you learn little about anything.

CREST's research found that "determining the depth and breadth of coverage of the test" was the first of the top six challenges organizations report, and "agreeing targets and frequency of tests" was another (CREST, 2022). This part is about getting both right.

## Start from the crown, not the contract

Scope usually starts from what is easy to describe: a website, an address range, an office network. That is backward. Start from what you cannot afford to lose.

Name your crown assets. The systems and data whose loss, disclosure or corruption would hurt the organization most. Payroll and finance. Customer records. The operational system your revenue depends on. The identity system that controls access to everything else. Then work outward: what touches them, who administers them, which suppliers connect to them, and what an outsider can see of any of it.

CREST's guide recommends identifying target environments by considering, among other things, "all main internal systems that support your organisation," "their level of criticality to the business," and "details about important third-party suppliers" (CREST, 2022).

## Let the evidence shape the routes

Public data tells you which routes adversaries use most. Use it to set priorities, adjusted for what you know about yourself.

| Route | What the public data says | What to put in scope |
|---|---|---|
| **The edge** | Exploitation of vulnerabilities is now the most common initial access vector in Verizon's dataset, at 31%. Unpatched edge devices explain 29% of the opportunistic SMB ransomware cases it describes (Verizon, 2026) | Internet-facing systems: remote access gateways, firewalls, email and web services, exposed management interfaces |
| **Credentials** | Compromised credentials explain 38% of those SMB cases (Verizon, 2026). Small organizations in Verizon's data experienced a median of seven credential leak events over the year (Verizon, 2026) | Login surfaces, password policy, multifactor coverage, account recovery and help-desk reset processes |
| **People** | Human element in 62% of breaches; pretexting at 6% and phishing at 16% of breaches (Verizon, 2026) | Authorized social engineering tests aimed at processes such as reset verification and payment changes |
| **Suppliers** | Third-party involvement in 48% of breaches (Verizon, 2026). Supply chain compromise the second most common initial attack vector in IBM's study (IBM and Ponemon Institute, 2026) | Supplier connections and accounts, shared platforms (with the owner's written permission), and your own controls over supplier access |
| **Web applications** | The OWASP Top 10:2025 lists Broken Access Control first, followed by Security Misconfiguration and Software Supply Chain Failures (OWASP Top 10, 2025) | Customer portals and internal applications, tested against a recognized methodology |
| **Internal depth** | CISA's red team, in a mature organization, gained persistent access and moved across sites before reaching systems adjacent to sensitive business systems (CISA AA23-059A, 2023) | An assumed-breach test: what an attacker could reach from an ordinary workstation or account |

Verizon's own advice on its statistics is the right attitude. Its report says to use its data "as your starting point, then gather evidence about your specific situation to determine if your risk is higher or lower than that baseline" (Verizon, 2026). In its worked example, a hospital uses its last penetration test results, among other evidence, to adjust its view of its own risk (Verizon, 2026). That is exactly how test results should feed back into planning.

## The outside-in view

Before the test, get the besieger's view. What does the internet see of you? Which domains, addresses, services and cloud resources answer from outside? Compare that list to your asset register. The gaps are the forgotten gates.

This is also the single best use of an opaque, external test. The NCSC notes that closed box testing "more accurately models the risk faced from attackers that are unknown or unaffiliated to the target organisation" (NCSC, 2017/2022). An outsider who finds a system you did not know you had has given you the most valuable finding in the report.

## Assume the wall is crossed

Some of the best scope questions start inside. Suppose an attacker already has one ordinary account and one ordinary laptop. What can they reach? How far is it from there to the crown?

An assumed-breach test answers that question directly, without spending your budget on the initial way in. It makes sense when you already know the way in exists. Verizon's numbers on credentials and edge devices suggest that, for many organizations, it does.

## Depth versus breadth

Every scope trades depth against breadth for a fixed budget. The NCSC's model scoping output states "the timeframe and the amount of effort necessary to deliver the testing - usually given in terms of resource days" (NCSC, 2017/2022). Look at that number critically. Divide it by the number of systems in scope. If the answer is a few hours per system, you are buying a scan with a human signature on it.

My rule of thumb: test fewer things, more deeply, more often, and rotate the scope. A three-year rotation that tests the crown every year and everything else at least once is better than an annual test that touches everything and understands nothing.

## When scope changes mid-test

Testers will find things outside scope. A connected system nobody listed. A supplier link that leads somewhere unexpected. The NCSC says the testing team "may either suggest a change to the scope, which is likely to alter testing time frames and cost, or they may recommend that the exclusion of such components be recorded as a limitation on testing," and that the decision "will generally be down to the risk owner" (NCSC, 2017/2022).

Write that process into the authorization. No tester should ever extend scope on their own initiative. Scope grows only with fresh written approval, and only from someone with authority over the new systems.

## Special handling

Some systems need extra care. Operational technology. Medical devices. Payment systems. Fragile legacy applications. NIST notes that "any time that a test or tester directly interacts with a system or network, the potential exists for unexpected system halts and other denial of service conditions," and that organizations "should determine their acceptable levels of intrusiveness" and may exclude tests "known to create denial of service conditions" (NIST SP 800-115, 2008). Its example is a payroll database "deemed too mission-critical for a particular type of testing" placed on the exclusion list (NIST SP 800-115, 2008).

Exclusion is a decision, not a safe place. If a system is too fragile to test, it may be too fragile to survive a real attacker. Record the exclusion, record who accepted the risk, and find another way to assure it, such as configuration review, architecture review or a test against a faithful copy.

> **The takeaway.** Scope from the crown outward. Follow the routes the evidence says are used. Test fewer things more deeply. Never let scope grow without a signature.

## What to do

- Name your crown assets and map what touches them before writing any scope.
- Compare the outside-in view with your asset register and fix the gaps.
- Build a multi-year rotation: crown every year, edge every year, everything else on a cycle.
- Include at least one assumed-breach objective in your next test.
- Record every exclusion with a named risk owner and an alternative form of assurance.

## What to measure

- Share of crown assets tested in the past 12 months.
- Number of internet-facing assets discovered by testing that were not in the asset register.
- Effort per in-scope system, in tester hours.
- Number of exclusions without an alternative assurance method.
