<!-- BODY-START -->

# Executive summary {#executive-summary}

By William Aaron Turner, Founder and President, Infinitum Corporation.

Someone is going to test your defenses. The only question is who goes first.

That is the whole argument of this paper. Every organization connected to the internet is already being probed. Scanners knock on every door, every day. Stolen passwords get tried against every login page that will accept them. Old flaws in old appliances get found by people who never had to ask permission. Nobody sends you the report.

So you have a choice. You can wait for the uninvited test, or you can commission an invited one. You can find the breach in your own wall, on your schedule, with your rules, and fix it before anyone else walks through it.

Key word: invited.

This paper is about authorized hacking. That means vulnerability assessment, penetration testing and red teaming done with written permission from the owner of the systems, inside an agreed scope, under rules of engagement, for one purpose: defense. Nothing else qualifies. Testing without permission is not a gray area. It is an attack.

I read security problems through one lens: irregular warfare. Joint doctrine describes it as a form of warfare in which state and non-state actors campaign "through indirect, non-attributable, or asymmetric activities," and says the term "seeks to create dilemmas and increase risk and costs to adversaries to achieve a position of advantage" (JP 1 Vol 1, as quoted in U.S. Army CALL, 2025). That is an analytic lens, nothing more. You do not need to care about doctrine. You only need to notice that the people working against your network behave the way it describes. They probe indirectly. They hide who they are. They spend little and make you spend a lot.

The organizing image for this paper is the siege. A city under siege is not usually taken by one great assault. It is taken because somebody found the one gate that was poorly watched, the stretch of wall that had crumbled, the guard who could be talked into opening a door. Defenders who survived sieges walked their own walls. They looked for the weak stones before the besiegers did. That is a comparison, not a claim that your office is a fortress or that anyone is shooting at it. **This paper draws general lessons about technology and conflict from public sources. It takes no side and makes no claim about any party.** It stays at the level of governance, scoping, rules of engagement, methodology and remediation. It contains no attack instructions, no exploit steps and no targeting content, by design.

## Why now

Three findings from the public record stand out.

**First, the way in has shifted toward the flaws you already know about.** Verizon's 2026 Data Breach Investigations Report (DBIR) found that exploitation of vulnerabilities is now the most common initial access vector for breaches, at 31% of its reporting dataset, while credential abuse, the previous leader, is down to 13% (Verizon, 2026). In its analysis of small and medium-sized businesses, Verizon says many ransomware attacks are opportunistic, and that victims were hit because they had compromised credentials (38%) or unpatched vulnerabilities in edge devices (29%) (Verizon, 2026).

**Second, the fixes are not keeping pace.** Verizon reports that only 26% of the vulnerabilities in CISA's Known Exploited Vulnerabilities (KEV) catalog were fully remediated by organizations in 2025, down from 38% the year before. The median time to full resolution rose to 43 days from 32 (Verizon, 2026). As of the catalog version dated October 30, 2026, the KEV catalog lists 1,766 vulnerabilities with evidence of exploitation in the wild (CISA KEV, 2026).

Let that sink in. These are not theoretical weaknesses. They are flaws somebody has already used. And three out of four were not fully fixed.

**Third, the bill is large and slow to arrive.** IBM and the Ponemon Institute report that the global average cost of a data breach reached a record USD 4.99 million, and that the mean time to identify and contain a breach rose to 247 days. Breaches with lifecycles longer than 200 days cost more on average than shorter ones (USD 5.65 million against USD 4.32 million) (IBM and Ponemon Institute, 2026). In the same study, offensive security testing (red teaming, penetration or vulnerability testing) was one of the factors associated with lower breach costs, about USD 211,339 below the average when each of 30 factors was measured in isolation (IBM and Ponemon Institute, 2026). That is an association in one study's sample, not a promise. It is still worth knowing.

## What authorized testing is, and is not

Testing is not one thing. The four kinds this paper covers answer four different questions.

- **Vulnerability scanning** asks: what known weaknesses can automated tools see? It is cheap, broad and shallow.
- **Vulnerability assessment** asks: of those weaknesses, which are real, and which matter most to us? It adds validation, context and ranking.
- **Penetration testing** asks: could an attacker actually get through, and how far? CREST describes it as "an ethical attack simulation intended to demonstrate or validate the effectiveness of security controls in a particular environment by highlighting risks posed by actual exploitable vulnerabilities" (CREST, 2022).
- **Red teaming** asks: would we notice, and would we respond? It tests the defenders as much as the defenses.

The UK National Cyber Security Centre (NCSC) adds a point most buyers miss. Penetration testing "should be viewed as a method for gaining assurance in your organisation's vulnerability assessment and management processes, not as a primary method for identifying vulnerabilities." It compares a test to a financial audit (NCSC, 2017/2022). In an ideal world, the NCSC says, "you should know what the penetration testers are going to find, before they find it."

Don't take my word for it. That is the government's own guidance.

## The seven moves

The recommendations come in seven moves, sized for a mid-size organization with a small security team.

1. **Know your walls.** Build the inventory first. You cannot authorize a test of systems you cannot name.
2. **Put permission in writing.** Signed authorization, a clear scope, rules of engagement, legal review and a stop condition, before anyone touches a keyboard.
3. **Scan continuously, assess regularly.** Make scanning a daily routine and assessment a scheduled one, so that the penetration test becomes an audit rather than a discovery exercise.
4. **Test what an adversary would actually do.** Scope tests around your crown assets and the routes the public data says are most used: the edge, stolen credentials, people and suppliers.
5. **Test the watchers, not just the walls.** Use red and purple exercises to measure detection and response, not only prevention.
6. **Turn findings into fixes, and prove they held.** Prioritize with exploitation evidence, assign every finding an owner and a date, find the root cause, and retest.
7. **Buy testing like a professional.** Choose qualified providers, contract for data handling and reporting you can use, and keep the program running year after year.

None of these moves needs an exotic product. All of them need discipline: permission before action, evidence before priority, and a retest before anyone says "fixed."

This paper includes a comparison of testing types, an authorization checklist, a rules-of-engagement outline, a 30/60/90-day plan, a 12-month roadmap, a 30-item self-assessment and three scenarios that are hypothetical and say so.

Every figure in this paper belongs to the source cited. I make no claim about the results any organization will achieve. Read the sources, then decide.
