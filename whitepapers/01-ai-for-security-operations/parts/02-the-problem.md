# The Problem

Mid-size organizations are fighting a contest they did not choose, against adversaries they cannot always see, with teams that are smaller than the job. Let's take the pieces one at a time.

## The ground you actually defend

Most security writing is about the dramatic cases: a nation-state campaign, a headline breach, a zero-day with a catchy name. Those exist. But if you run a mid-size company, a law firm, a regional hospital group, a manufacturer or a logistics business, your daily reality is less cinematic and more persistent.

Someone is scanning your internet-facing systems. Someone is sending your staff convincing messages. Someone is looking for an unpatched device, a reused password, a vendor with weak controls. Most of these actors are not after you in particular. They are after anyone who is easy. You are not the target. You are the terrain.

That is why I find the irregular warfare lens useful here. In the U.S. Department of Defense's public strategy summary, irregular warfare is described as a struggle among state and non-state actors to influence populations and affect legitimacy. It favors indirect and asymmetric approaches, and it works to erode an adversary's power, influence and will. The same document notes that state adversaries and their proxies increasingly pursue their objectives in the competitive space "deliberately below the threshold likely to provoke a U.S. conventional response," using campaigns of disinformation, deception, sabotage and economic coercion, as well as proxy and covert operations (DoD, 2020).

I want to be careful. The formal DoD definition of irregular warfare is a violent struggle among state and non-state actors for legitimacy and influence over the relevant population (DoDD 3000.07, 2017). Most of what hits a mid-size company is not violent, and it is not a military contest. I am borrowing the lens, not the label. What the lens gives a defender is a set of questions that conventional "perimeter and patch" thinking tends to skip:

- Is the adversary trying to avoid a fight I can win?
- Is the adversary patient, and what does persistence look like in my logs?
- Who is the adversary working through: a criminal service, a supplier, a compromised partner?
- What is the adversary trying to influence: my staff, my customers, my reputation?
- Can I keep operating while contested?

Keep those five questions in mind. We will come back to each of them in the Analysis.

## Pressure one: the front door is unfixed software

Start with how adversaries get in. Verizon's 2026 report covered incidents from November 2024 through October 2025 and found that exploitation of vulnerabilities was the initial access vector in 31% of breaches in the non-error, non-misuse dataset, up from 20% in the prior year's report. Credential abuse, the previous leader, fell to 13% (Verizon DBIR, 2026).

Now look at what defenders did with that information. Verizon examined vulnerabilities listed in CISA's Known Exploited Vulnerabilities (KEV) catalog, the authoritative list of vulnerabilities exploited in the wild. In 2025, only 26% of KEV-listed vulnerabilities were fully remediated, down from 38% the year before. The median time to full remediation rose to 43 days from 32 days. The median organization had 16 KEV vulnerabilities to deal with, up from 11 (Verizon DBIR, 2026; CISA KEV catalog).

Let that sink in. The things attackers are known to be using, in the median case, take more than six weeks to close.

Verizon also noted that nearly half of the KEV vulnerabilities fall into a "persistent exploitation" category, meaning exploitation activity could be detected on an average of 96% of the days observed, and that only 20% of the vulnerabilities in that persistent group had been registered in the CVE database in 2024 and 2025. For the other 80%, organizations would have had about two years of advance notice in which to patch (Verizon DBIR, 2026). In other words, the adversary does not need novelty. The adversary needs patience and a list.

ENISA's 2025 Threat Landscape, which analyzed 4,875 incidents between July 2024 and June 2025, tells a consistent story from the European side. Phishing was the leading intrusion vector at about 60%, and vulnerability exploitation was second at 21.3%. One caution on ENISA's numbers: its incident set is dominated by hacktivist denial-of-service activity. DDoS made up 77% of reported incidents, and ENISA still identified ransomware as the most impactful threat in the EU (ENISA, 2025). So read the intrusion-vector percentages as a picture of what ENISA observed, not as a measure of what would hit your company.

## Pressure two: the adversary is an ecosystem, not a person

The next pressure is about who you are facing. It is rarely one person in a dark room. It is a supply chain of criminal services.

Verizon found ransomware in 48% of breaches, up from 44%, while the median ransom paid fell to USD 139,875 and 69% of ransomware victims did not pay (Verizon DBIR, 2026). IBM's cost study found that ransomware affected 39% of breached organizations, up from 34%, and that attackers are shifting toward pressure that targets trust: 41% of ransomware incidents included threats to brand reputation (IBM/Ponemon, 2026).

Third parties are part of the picture too. Verizon reported that breaches with third-party involvement reached 48% of total breaches, an increase of 60% from the prior year's dataset. In cloud accounts belonging to third parties, only 23% of organizations had fully remediated missing or improperly secured multifactor authentication, and for weak passwords and permission misconfigurations the time to resolve half of the findings reached almost eight months (Verizon DBIR, 2026).

ENISA describes the same pattern from another angle. It points to the industrialization of phishing through Phishing-as-a-Service kits, which allow adversaries of any skill level to launch campaigns. It also highlights growing abuse of "cyber dependencies" such as the digital supply chain, and a convergence between threat groups: state-aligned actors adopting hacktivist characteristics, and similarities in tools used by hacktivists and cybercriminals (ENISA, 2025).

For a defender, that convergence matters. If the same tools and tactics show up across very different actors, then attributing an attack to a specific group is often slow, uncertain, and not that useful for the person who needs to contain it on Tuesday afternoon.

The financial footprint is large. The FBI's Internet Crime Complaint Center received 1,008,597 complaints in 2025, with reported losses of USD 20.877 billion, a 26% increase from 2024. Business email compromise accounted for roughly USD 3.05 billion of those losses, and the report includes a section on artificial intelligence, with 22,364 AI-related complaints and adjusted losses above USD 893 million (FBI IC3, 2025). These are complaint-based figures from victims who chose to report, so they describe a floor, not a ceiling.

## Pressure three: breaches are slow, expensive and getting more so

IBM and Ponemon Institute's 2026 Cost of a Data Breach Report studied 602 organizations that experienced breaches between March 2025 and February 2026. The global average cost reached a record USD 4.99 million, up 12%. The mean time to identify and contain a breach rose to 247 days, a slight uptick that reversed a five-year decline. Two cost categories, detection and escalation and lost business, drove 63% of the average cost (IBM/Ponemon, 2026).

Time matters in the numbers. Breach lifecycles longer than 200 days averaged USD 5.65 million. Shorter ones averaged USD 4.32 million (IBM/Ponemon, 2026). That is the persistence problem expressed in dollars. The longer an adversary stays inside, the more it costs.

Recovery is slow too. Only 42% of breached organizations reported fully recovering, and fewer than one in 20 recovered in less than 50 days (IBM/Ponemon, 2026).

## Pressure four: the team is smaller than the job

The people problem is the one I hear about the most from leaders, so let me anchor it in data. The 2024 ISC2 Cybersecurity Workforce Study surveyed 15,852 practitioners and decision-makers. Of those, 67% reported a staffing shortage, and 90% reported one or more skills gaps on their teams. Budget was the number one cause cited for both talent and skills gaps. ISC2 estimated the global workforce gap at 4,763,963 people, up 19.1% from the prior year, with a clear note that this measures what organizations say they need and is not a count of open jobs (ISC2, 2024).

The skills gap shows up in outcomes. Of the nearly 7,500 respondents willing to share breach information, 17% said their organization had a material breach in the prior year. Among organizations with skills gaps, the figure was 22% (ISC2, 2024). That is an association from a survey, not proof that skills gaps cause breaches. But it points in the direction you would expect.

IBM's data adds an uncomfortable detail. Its factor analysis identified "security skills shortage" as a factor that increased breach costs, by roughly USD 179,635 on average against the global average, and "inability to prioritize threats against the organization" as another, at USD 188,172 (IBM/Ponemon, 2026).

## Pressure five: AI cuts both ways

Then comes AI, the part everyone wants to talk about.

On the attacker's side, IBM found that more than one in four organizations that experienced a malicious attack reported it was AI-driven, a 56% increase over the prior year. AI deepfake or impersonation attacks drove the highest volume at 45%, followed by AI-enabled malware at 19% and AI-generated phishing at 17%. AI-driven attacks added an average of USD 1 million to the cost of a malicious breach (IBM/Ponemon, 2026). ENISA reported that, by early 2025, AI-supported phishing campaigns reportedly represented more than 80% of observed social engineering activity worldwide, and it flagged a rise in attacks on the AI supply chain (ENISA, 2025).

I want to give you the other half of the evidence, because it keeps this conversation honest. Verizon looked closely at how threat actors are using generative AI. The median threat actor in its dataset researched or used AI assistance in 15 documented techniques. But most of the AI-assisted malware and tooling was associated with well-known, defined techniques, and less than 2.5% of observations involved less-common techniques with one or fewer known malware examples. Of the 793 actors it assessed for risk, fewer than 1% fell into the high or critical category (Verizon DBIR, 2026). My reading of that pattern: AI is speeding up existing attack techniques, and Verizon says it is helping shorten the time to exploit known vulnerabilities, rather than inventing wholly new ones.

On the defender's side, the evidence points to real benefits, which I will cover in detail. But there is a new risk on the defender's own ground. ISC2 found that 45% of respondents' cybersecurity teams had already used generative AI in their tools, that 64% of respondent organizations had implemented it in other departments, and that 54% had faced data privacy and security concerns because of organizational adoption (ISC2, 2024).

## So what is the problem, exactly?

Put the five pressures together and the problem statement is clear.

Adversaries get in through unfixed software, convincing messages and weak third parties. They operate through criminal services that lower their costs and obscure who they are. They are patient, and they use AI to speed up what already works. Defenders are slower to fix, slower to detect and slower to recover, with teams that are short of people and skills.

That is a capacity problem. And capacity is exactly what AI can add, when it is adopted with discipline. It is also exactly what AI can subtract, if it is adopted without discipline, because every shortcut creates something new to defend.

A note on scope before we move on. These studies are global and mixed-size. None of them is limited to mid-size organizations, and they use different samples, different years and different definitions. IBM itself notes that its benchmark sample is nonstatistical and leans toward organizations with more mature security programs (IBM/Ponemon, 2026). Treat the numbers as direction, not as a benchmark for your company. I will flag the limits as we go.
