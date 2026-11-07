
# The siege, read by a security analyst {#the-siege}

Before the analysis, the lens. I want to be precise about what the comparison claims and what it does not.

## The framing

Irregular warfare is my analytic lens. Current U.S. joint doctrine, as quoted by the Army's Center for Army Lessons Learned, defines it as "a form of warfare where state and non-state actors campaign to assure or coerce states or other groups through indirect, non-attributable, or asymmetric activities, either as the primary approach or in concert with conventional warfare" (U.S. Army CALL, 2025). The same source says the term "seeks to create dilemmas and increase risk and costs to adversaries to achieve a position of advantage" (U.S. Army CALL, 2025).

Strip away the military context and three ideas are left. Indirect: work around strength rather than through it. Non-attributable: make it hard to know who did it. Asymmetric: spend little, force the other side to spend a lot.

Every one of those describes the people probing your network. They go around your firewall through a supplier or a help desk. They hide behind rented infrastructure and stolen accounts. They spend pennies on scanning and make you spend weeks on recovery.

The siege is the image I use to hold those ideas together. It is a comparison, not a claim. Your organization is not a fortress, and nobody is besieging it in any literal sense. But the logic of a siege maps onto defensive security in ways that are useful for a buyer of testing.

## Five things every siege teaches

**1. The wall is only as strong as its weakest stretch.** A besieger does not attack the strongest gate. It walks the perimeter looking for the crumbling section, the unwatched postern, the culvert nobody thought of. Your attackers do the same with scanners and leaked credentials. Verizon's finding that unpatched edge devices and compromised credentials explain so many opportunistic ransomware cases among smaller businesses is the modern version (Verizon, 2026).

*For testing:* scope must follow the perimeter an adversary sees, not the one your asset register describes.

**2. The besieger has time; the defender has a schedule.** NIST says it plainly: testing "often has a narrow scope because of resource limitations—particularly in the area of time. Malicious attackers, on the other hand, can take whatever time they need" (NIST SP 800-115, 2008). Your test lasts two weeks. The siege does not end.

*For testing:* a single annual test cannot match a continuous adversary. Continuous scanning and scheduled assessment have to carry the load between tests.

**3. Defenders who survive walk their own walls.** The garrison that inspects its own defenses, repairs what it finds and drills its sentries holds longer than the one that trusts the stone. That is authorized testing in one sentence: you find the weak stretch first.

*For testing:* the goal is not a clean report. It is a list of repairs.

**4. Most walls fall from the inside.** History is full of gates opened by someone persuaded, paid or fooled. Verizon puts the human element in 62% of breaches and reports pretexting, a scheme built on a concocted trusted relationship, at 6% of all breaches (Verizon, 2026). IBM reports social engineering such as impersonating help desk staff in 13% of the attacks it studied (IBM and Ponemon Institute, 2026).

*For testing:* people and processes belong in scope, with careful rules, consent from leadership and respect for the staff involved.

**5. Sentries matter as much as stone.** A wall that is breached but watched is a problem. A wall that is breached and unwatched is a catastrophe. IBM's 247-day mean time to identify and contain is the cost of unwatched walls (IBM and Ponemon Institute, 2026).

*For testing:* test detection and response, not only prevention. That is what red teaming is for.

## The adversary's three advantages, and the tester's answer

| Adversary advantage | What it looks like on a network | What authorized testing gives back |
|---|---|---|
| **Indirect approach** | Entry through a supplier, a forgotten system or a person, not through the hardened front door | Scope built around realistic routes, including third parties and social engineering where authorized |
| **Non-attribution** | Activity that blends with normal administration and is hard to distinguish or trace | Exercises that measure whether your monitoring can tell the difference |
| **Asymmetric cost** | Cheap, automated probing against a defense that must be right everywhere | Prioritization that spends your limited effort on what is actually exploited |

The answer to each advantage is not a product. It is information you could not get any other way: a controlled, permitted look at your own defenses through hostile eyes.

## Where the comparison breaks

Every comparison has limits. This one has four.

**A tester is not an enemy.** The whole point of authorized testing is that the tester works for you, under your rules, and stops when you say stop. Treating testers as adversaries, inside the organization or out, poisons the program. They are the scouts you send to the wall, not the army outside it.

**Your systems are not a battlefield.** No one is going to be hurt by a misconfigured server the way people are hurt in war. The comparison is about logic and economics, not about stakes.

**Law and ethics bind you, not them.** Real attackers ignore the law. Your testers cannot and must not. NIST notes that "attackers are not bound by this constraint and use whatever techniques they feel necessary" while organizations "tend to avoid using testing techniques that impact systems or networks" (NIST SP 800-115, 2008). That gap is permanent. Good scoping narrows it. Nothing closes it.

**The paper is not about any real conflict.** I use the siege as a general image. I name no state, no army and no campaign, and I make no claim about any party.

## The device: walk your own walls

The rest of the paper is organized around one habit: walk your own walls before someone else does. That habit has eight parts, covered in the Analysis.

1. Know the difference between the kinds of testing (Part I).
2. Get permission that stands up (Part II).
3. Scope the test the way an adversary would see you (Part III).
4. Demand a method you can audit (Part IV).
5. Turn findings into fixes, and prove they held (Part V).
6. Test the sentries, not just the stone (Part VI).
7. Buy testing like a professional (Part VII).
8. Rehearse with three hypothetical scenarios (Part VIII).
