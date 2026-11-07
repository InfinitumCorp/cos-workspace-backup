
# The problem: the siege is already on {#the-problem}

Here is the uncomfortable truth about testing.

Your systems are tested every day already. Not by you. Automated scanners sweep the internet looking for exposed services. Credential lists harvested from other breaches are replayed against your login pages. Somebody, somewhere, is reading the same vendor advisories your team is reading, and deciding which of them can be turned into a way in.

None of those testers asked permission. None of them will share the findings. And they do not have to be good. They only have to be first.

IBM puts the imbalance in one line: attacks "can be launched for thousands while breaches cost millions" (IBM and Ponemon Institute, 2026). That is the economics of a siege. The besieger can probe a hundred stretches of wall for the price of one breach. The defender has to hold all of them.

## What the evidence shows

I will keep this section to numbers I can trace to a source I opened. Every figure belongs to the publisher named, and describes that publisher's dataset.

**Known flaws are now the main way in.** Verizon's 2026 DBIR says exploitation of vulnerabilities "is now the most common initial access vector for breaches," rising to 31% in its reporting dataset, while credential abuse fell to 13% as an initial access vector (Verizon, 2026). Credentials have not gone away. They have been overtaken.

**The flaws stay open.** Verizon used the CISA KEV catalog as its subset of vulnerabilities that "all organizations are incentivized to patch." Only 26% of KEV vulnerabilities found in organizations' environments had been fully remediated, "a considerable drop from last year's 38%." The share left entirely unremediated rose to 16% from 12%. The median time to full patching rose to 43 days, "almost two weeks longer than last year's 32 days" (Verizon, 2026).

**The pile is growing.** The median number of KEV vulnerabilities an organization had to patch rose to 16 in 2025 from 11 in 2024, which Verizon calls "almost 50% more" (Verizon, 2026). The underlying dataset of vulnerability records grew from 68.7 million in 2022 to 527.3 million in 2025, almost eight times the volume (Verizon, 2026).

**There may be a speed limit.** Verizon found that by Day 7 after detection, somewhere between 60% and 70% of KEV vulnerabilities remain open "regardless of year, volume or organizational maturity." Organizations "at their very best only get to fix 30%–40% of KEV instances in the first week after detection, so choosing the correct ones to patch really is the key strategy" (Verizon, 2026). Verizon itself calls this "an initial measurement," not a law.

Read that twice. Even the best teams cannot fix everything quickly. The winners are the ones who pick the right things to fix first. That is what good assessment is for.

**Old flaws are not safe flaws.** Verizon reports that nearly half of the KEV vulnerabilities with detectable exploitation activity in a research partner's data showed "Persistent" exploitation, meaning activity could be detected on an average of 96% of days. Only 20% of the vulnerabilities in that category were registered in the CVE database in 2024 and 2025. "For the other 80%, organizations would have had about two years' advance notice in which to patch" (Verizon, 2026).

**The opportunists favor the smaller targets.** Of the ransomware cases where Verizon had information on organization size, it found about 96% of victims were small and medium-sized businesses (Verizon, 2026). It describes many of these attacks as opportunistic: victims were chosen because of compromised credentials (38%) or unpatched vulnerabilities in edge devices (29%), "not so much about industry or the revenue of the victims" (Verizon, 2026).

**People remain in the path.** Verizon found the human element present in 62% of breaches. Social Engineering was the third most common breach pattern at 16% of breaches. Pretexting reached 6% of all breaches, and phishing remained at 16% (Verizon, 2026). In phishing simulations, the median click rate in mobile-centric vectors, such as voice and text messaging, was 40% higher than via email (Verizon, 2026).

**Suppliers widen the wall.** Breaches with third-party involvement reached 48% of total breaches in Verizon's dataset, up from 30%, an increase of 60% (Verizon, 2026). IBM found that supply chain compromise was the second most common initial attack vector in the breaches it studied, and that a supply chain breach added about USD 227,250 to the average cost when measured in isolation (IBM and Ponemon Institute, 2026).

**The defenders are stretched.** ISC2 reports that 67% of respondents indicated a staffing shortage, and 90% reported one or more skills gaps on their cybersecurity teams (ISC2, 2024). In IBM's study, a security skills shortage was associated with about USD 179,635 in added breach cost (IBM and Ponemon Institute, 2026).

## Where the sources differ

The sources do not all say the same thing, and I will not pretend they do.

Verizon finds vulnerability exploitation is now the top initial access vector in its dataset (Verizon, 2026). IBM finds phishing was the top attack vector "for the fourth year in a row" in the breaches it studied (IBM and Ponemon Institute, 2026). Those statements are not in conflict. They describe different samples, different methods and different definitions. Verizon analyzes a large body of incidents and breaches contributed by many partners. IBM studies a set of breached organizations in depth and models cost.

The lesson for testing is the same either way. Test the edge, because known flaws are the way in. Test the people and the processes around them, because social engineering is the way in. A program that tests only one is half a program.

## The four failures

Organizations of a few hundred people rarely fail at testing because they never test. They fail in four more ordinary ways.

**They test the wrong thing.** A penetration test is scoped around what was easy to put in a contract, not around what an adversary would want. The crown systems, the supplier connections and the help desk stay out of scope. The report comes back clean. Nobody learned anything.

**They test without permission that would stand up.** The person who signed did not own all the systems in scope. A cloud provider or a managed service provider was never asked. Nobody wrote down what was forbidden. When something breaks, nobody knows who carries the risk.

**They treat the report as the finish line.** CREST lists, among the top six challenges organizations report, "assuming that by fixing vulnerabilities uncovered during a penetration test systems will then be 'secure'" (CREST, 2022). Findings sit in a PDF. A year later, the next test finds the same things.

**They test once and call it assurance.** The NCSC warns that a penetration test "can only validate that your organisation's IT systems are not vulnerable to known issues on the day of the test," and that "it's not uncommon for a year or more to elapse between penetration tests" (NCSC, 2017/2022). A test is a snapshot. The siege is a film.

## The cost of the uninvited test

The uninvited test has a price, and it arrives late. IBM puts the mean time to identify and contain a breach at 247 days (IBM and Ponemon Institute, 2026). In the United States, IBM reports average breach costs exceeded all other countries and regions in its study, at a record USD 11.5 million (IBM and Ponemon Institute, 2026).

Ransom economics are shifting, too. Verizon reports ransomware present in 48% of breaches, up from 44%, while 69% of ransomware victims in its dataset did not pay, and the median ransom paid fell to USD 139,875 from USD 150,000 (Verizon, 2026). Fewer payments do not mean less damage. They mean the damage is being absorbed in downtime, recovery and lost trust instead.

## What this paper is, and is not

This paper is a practical guide to commissioning, governing and using authorized security testing in a mid-size organization. It explains the differences between testing types, how to authorize and scope a test, what good methodology looks like at the level a buyer needs, how to turn findings into fixes, how to test detection and response, and how to choose a provider.

It is not a technical manual. It contains no attack techniques, exploit steps, tool instructions or targeting content. The public standards cited here, such as NIST SP 800-115, PTES, the OWASP testing guide and the CREST guide, are the right places for practitioners to go for methodology. The Penetration Testing Execution Standard itself notes that the standard "does not provide any technical guidelines as far as how to execute an actual pentest" and keeps those separate (PTES). I keep them out entirely.

And it is not a sales pitch dressed as research. Every statistic belongs to the source cited. Where I give my own judgment, I say so.
