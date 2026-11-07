<!-- BODY-START -->

# Executive summary {#executive-summary}

By William Aaron Turner, Founder and President, Infinitum Corporation.

This is not a hype piece about AI.

It is a practical look at where AI helps a security team, where it hurts, and how a mid-size organization can start without losing control.

I read security problems through one lens: irregular warfare. That is the study of how states, proxies and other groups compete below the threshold of open war, using indirect, deniable and asymmetric means. You don't have to care about military doctrine to benefit from it. You only have to notice that the people attacking your network are behaving exactly the way that doctrine describes.

They probe. They hide in normal activity. They pick the cheapest way in. They wait.

And now they have AI.

Here is the short version. Three findings from recent research stand out.

First, speed. Verizon's 2026 Data Breach Investigations Report (DBIR) found that exploiting software vulnerabilities is now the most common way into a breach, while only 26% of the most critical known-exploited vulnerabilities were fully fixed (Verizon, 2026).

Second, AI works for defenders too. Organizations that used security AI and automation extensively averaged lower breach costs and faster response in IBM's 2026 study (IBM and Ponemon Institute, 2026). Key word: averaged. And most organizations have not adopted these tools widely yet.

Third, AI is also a new attack surface. The research points to plain gaps in access control and governance, not exotic technical failures.

Put those three together and you get the core problem of this paper. Your adversary is getting faster and cheaper. Your team is not getting bigger. AI can close part of that gap. Adopted carelessly, it opens a new one.

The irregular warfare lens adds something the statistics alone do not. It explains why the problem looks the way it does.

Gray-zone actors stay below thresholds. In your environment, that means activity designed to look like normal administration. Hybrid campaigns blur attribution. In your environment, that means you will often not know who is behind an intrusion, and you will have to act anyway. Irregular actors impose costs asymmetrically. In your environment, that means an attacker spends little to make you spend a lot. And the doctrine on countering hybrid threats keeps returning to one answer: resilience. Institutions that can absorb a blow, keep working and recover are much harder to coerce.

That is the standard I hold an AI program to. Does it make your organization more resilient, or does it simply make it busier?

My recommendation is simple and not glamorous: govern first, measure a baseline, pilot with analysts in the loop, point AI at exposure, secure the AI itself, and widen automation only as the evidence earns it. Technology, process and people, working as one system. That is what practical, integrated security looks like.

This paper is organized to support that recommendation.

- **The problem** sets out the pressures: attacker speed, slow remediation, expensive breaches and thin teams.
- **Part I** introduces the irregular warfare lens, with definitions taken from U.S. joint doctrine, CSIS, RAND, NATO and the European Union.
- **Part II** looks at how adversaries adapt, using a public U.S. government advisory as a worked example.
- **Part III** reviews the evidence that AI helps defenders, and where adoption is uneven.
- **Part IV** analyzes six security operations use cases in depth: alert triage, threat-intelligence enrichment, vulnerability prioritization, log analysis, reporting, and deception and early warning.
- **Parts V and VI** cover governance under the NIST AI Risk Management Framework and the job of securing the AI itself.
- **Parts VII and VIII** address people and metrics.
- **Part IX** walks through three illustrative scenarios. They are hypothetical, and labeled that way.
- **Recommendations** give a phased roadmap for the first 90 days and the first 12 months, plus a maturity self-assessment you can run with your team.

A word on sources. Every statistic carries its source. Every definition of doctrine is quoted or paraphrased from a public document I opened and checked. Where I offer judgment, I say so.

All data comes from the public record. All conclusions are mine.

# The problem {#the-problem}

Three pressures are landing on mid-size organizations at once: faster attackers, slower fixes and thin teams.

Let's take them one at a time.

## Attackers are walking in through unfixed software

Verizon found that vulnerability exploitation was the initial access vector in 31% of breaches, up from 20% in the prior year's report. It overtook credential abuse (13%) as the leading vector (Verizon, 2026).

Verizon also reports that AI is helping threat actors speed up the time it takes to exploit known vulnerabilities (Verizon, 2026).

Think about what that means in practice.

A vulnerability is published. A patch is released. The clock starts. On one side, an attacker who can now move from disclosure to working exploitation faster than before. On the other side, your change-management calendar.

The race is not fair. It was never meant to be.

## Fixes are not keeping pace

Only 26% of critical vulnerabilities listed in CISA's Known Exploited Vulnerabilities (KEV) catalog were fully remediated in 2025, down from 38% the year before. The median time to full remediation rose to 43 days from 32 days. The median organization had 16 KEV vulnerabilities to deal with, up from 11 (Verizon, 2026).

Let that sink in.

These are not theoretical weaknesses. KEV is CISA's list of vulnerabilities known to have been exploited in the wild. CISA advises organizations to use the catalog as an input to their vulnerability prioritization framework (CISA, KEV catalog). Yet most of the critical ones were not fully fixed, and the time to fix them got longer.

The direction is wrong on every measure in that paragraph. Fewer fixed. Slower to fix. More to fix.

## Breaches are expensive, and slow to find

IBM's 2026 Cost of a Data Breach Report, conducted by Ponemon Institute, put the global average breach cost at USD 4.99 million, a 12% increase and a record. The mean time to identify and contain a breach was 247 days (IBM and Ponemon Institute, 2026).

Two hundred forty-seven days.

That is roughly eight months in which an intruder may be learning your environment, your people and your habits before you have both found and contained them.

The AI dimension is already showing up in the numbers. More than one in four organizations hit by a malicious attack said it was AI-driven, a 56% increase over the previous year, and AI-driven attacks added an average of USD 1 million to the cost of a malicious breach (IBM and Ponemon Institute, 2026).

## And the people are stretched

The 2024 ISC2 Cybersecurity Workforce Study surveyed 15,852 practitioners and decision-makers. 67% reported a staffing shortage. 90% reported one or more skills gaps. Among organizations with critical or significant skills gaps, 22% reported a material breach, compared with 17% of all respondents who shared that information (ISC2, 2024).

That last comparison matters. Skills gaps are not just an HR problem. In the ISC2 data, they travel with worse security outcomes.

## A caution on the numbers

Now, I know what you're thinking: these studies are global, not mid-size.

You're right.

None of them is limited to mid-size organizations, and they use different samples and different years. Treat the numbers as direction, not as a benchmark for your company. IBM itself notes that its sample is not statistical and leans toward organizations with more mature security programs.

I will keep repeating this point through the paper, because it is the most common way security statistics get misused. A survey average tells you which way the wind is blowing. It does not tell you how strong the wind is at your address.

## Why this is a capacity problem

For a mid-size organization, all of this adds up to a capacity problem.

More vulnerabilities to fix. More alerts to read. More AI-enabled threats to recognize. The same small team.

Mid-size organizations sit in an awkward place. They are big enough to be worth attacking, with real data, real money and real connections to larger partners. They are rarely big enough to staff a full security operations center around the clock, run a dedicated threat-intelligence team, and maintain a separate vulnerability management function.

So the same few people triage alerts in the morning, chase patches in the afternoon and write the board report at night.

That is the opening for AI. It can take some of the reading, sorting, summarizing and drafting off those people.

It is also why adopting it carelessly can make things worse. A tool that produces confident, wrong answers at machine speed does not reduce workload. It moves the workload to cleanup, and it moves the risk to the places nobody is checking.

## The question this paper answers

So the question is not whether to use AI in security operations. Attackers have answered that question for us.

The question is how a mid-size organization adopts it in a way that makes the whole program stronger: more resilient, better prioritized, harder to surprise.

To answer that well, it helps to understand the kind of contest you are in. That is where irregular warfare comes in.

