
# The problem: they do not need to beat you once {#the-problem}

Here is the uncomfortable math.

An attacker sends ten thousand messages. One person clicks. An attacker scans a million addresses. One appliance is a year behind on patches. An attacker floods a website for nine minutes, then does it again at lunch. None of that costs much. All of it costs you something.

IBM states the imbalance in a sentence: attacks "can be launched for thousands while breaches cost millions" (IBM and Ponemon Institute, 2026). That is the whole problem in a line. The attacker's cost per attempt is low and falling. Your cost per defended attempt is not.

That is attrition. Not a single decisive blow. A steady drain on attention, people, money and nerve, until something gives.

## What the evidence shows

I will keep this section to numbers I can trace to a source I opened. Every figure below belongs to the publisher named.

**Most of the pressure is volume.** ENISA analyzed 4,875 incidents across the European Union between July 2024 and June 2025. DDoS was the dominant incident type, 77% of reported incidents, mostly from hacktivists. Hacktivism represented almost 80% of all incidents, primarily low-impact DDoS campaigns, and only 2% of hacktivism incidents resulted in service disruption (ENISA, 2025).

Read that twice. Almost all of it was noise. Almost none of it broke anything. And ENISA still names ransomware as the most impactful threat in the EU (ENISA, 2025). The loud thing and the dangerous thing are not the same thing, and the loud thing is designed to make you forget it.

**The volume is real, and it comes in bursts.** Verizon's 2026 Data Breach Investigations Report (DBIR) recorded 5,514 denial-of-service incidents. The median attack size has fluctuated between 4.2 and 6 Gbps over recent years, and 50% of attacks lasted less than nine minutes. The largest attacks grew 198% in bits per second and 156% in packets per second compared with the prior year (Verizon, 2026).

Verizon also looked at how often organizations get hit. In a sample of 217 victim organizations, 2% saw periodic, predictable attacks, 40% saw bursts of activity, and 57% saw attacks at seemingly random intervals. The "bursty" victims faced a median of about 17 different attacks over the year, with about one day between attacks. Half of them faced at least 10 different attack types (Verizon, 2026).

Picture the load. Seventeen separate hits, many types, a day apart. That is not an event. It is a posture.

**The way in is usually old and cheap.** ENISA found phishing was the leading intrusion route at about 60%, followed by vulnerability exploitation at 21.3% (ENISA, 2025). Verizon found exploitation of vulnerabilities is now the most prominent initial access vector in its dataset at 31%, up from 20% the year before (Verizon, 2026).

And the vulnerabilities stay open. Verizon reports that only 26% of the vulnerabilities in the CISA Known Exploited Vulnerabilities (KEV) catalog found in its partners' scans were fully remediated, a drop from 38% a year earlier. The median time to fully patch rose to 43 days from 32. The median number of KEV vulnerabilities an organization had to patch in a year rose to 16 from 11 (Verizon, 2026).

**The small and mid-size get hit too.** Verizon found about 96% of ransomware victims, among cases where organization size was known, were small and medium-sized businesses. In its SMB analysis, it describes many of these attacks as opportunistic: victims were chosen because they had compromised credentials (38%) or unpatched vulnerabilities in edge devices (29%) (Verizon, 2026).

**The pain lasts.** IBM puts the global average cost of a breach at a record USD 4.99 million, and the mean time to identify and contain at 247 days. Ransomware showed up in 39% of breached organizations in its sample, up from 34%. The most common tactic shifted: threatening brand reputation was cited by 41% of those hit by ransomware, ahead of encryption at 23% (IBM and Ponemon Institute, 2026).

Pressure on your trust and your public standing, not only on your files.

**And AI is turning the dial.** ENISA reports that AI-supported phishing campaigns reportedly represented more than 80% of observed social engineering activity worldwide by early 2025 (ENISA, 2025). IBM reports more than one in four organizations that experienced a malicious attack said it was AI-driven (IBM and Ponemon Institute, 2026). Verizon reports roughly 15% of non-malicious bot traffic in the third quarter of 2025 was AI bots, and describes security teams scrambling to automate the handling of AI scanning bots and AI-driven traffic (Verizon, 2026).

## The three drains

Attrition drains three things. Name them, because each one needs its own defense.

**Attention.** Every alert, every flood, every phishing report pulls a person's eyes. Attention is finite. Attackers know it. Volume is a way of buying it.

**People.** ISC2's 2024 workforce study found 67% of respondents reported a staffing shortage, and 90% reported one or more skills gaps (ISC2, 2024). Tired people miss things. People who quit take the map with them.

**Money.** Budgets are annual. Campaigns are not. A program built to survive one audit cycle will not survive three years of steady pressure.

## Four ways a mid-size organization loses

I see four failure modes. This is my analysis. It is not a measured result.

1. **Exhaustion.** The team is so busy with the volume that nobody has time for the slow, important things: patching the edge, testing backups, writing the plan.
2. **Blind spots.** You cannot see the whole position. A forgotten appliance. A supplier connection nobody mapped. An old account.
3. **Single points of failure.** One identity provider, one firewall pair, one clock, one administrator who knows how it works. When it goes, everything goes.
4. **Slow adaptation.** The adversary changes a technique in weeks. Your annual policy review does not.

Hold those four in your head. The rest of this paper is a response to them.

## What this paper is, and is not

It is a defensive, practical guide for security and IT leaders in mid-size organizations. It uses the modern battlefield as a lens, and every lesson ends in something you can do.

It is not a weapons paper. It does not describe how to build, buy, aim or defeat any weapon. It contains no targeting content and no training content. When it speaks of testing, it means authorized, scoped testing of your own systems, performed with written permission. It does not recommend striking back at anyone. Responses to attackers belong to law enforcement and to people with authority and evidence.

It is not a vendor list. It makes no promise that any product, or any plan in this paper, will produce a particular result for you.
