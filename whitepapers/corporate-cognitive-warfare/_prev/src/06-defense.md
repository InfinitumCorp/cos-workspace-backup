# 6. Defensive Operations and Counter-Influence

Every organization is already on contested terrain, whether or not it chooses to compete there. Competitors, activists, short sellers, fraudsters, disgruntled insiders and opportunists can all try to shape what the organization's audiences believe. Some will use lawful means. Others will use the deceptive tactics this paper excludes from legitimate practice. A cognitive defense capability is therefore as basic as cybersecurity, and the two increasingly overlap.

## 6.1 Threat Taxonomy

The Council of Europe's report on *information disorder* gives a useful vocabulary: mis-information is "when false information is shared, but no harm is meant"; dis-information is "when false information is knowingly shared to cause harm"; and mal-information is "when genuine information is shared to cause harm" (Wardle and Derakhshan 2017). The threats below combine these categories with the techniques of Section 3 turned to illegitimate ends.

- **Coordinated inauthentic behavior (CIB).** Networks of accounts that use false identities to mislead people about who is behind them and what they are doing. Meta's policies and threat reports describe and remove such networks, focusing on the deceptive behavior rather than the content (Meta n.d.).
- **Bot networks and fake engagement.** Automated or purchased accounts that inflate or attack metrics. Platform policies prohibit artificial engagement and coordinated manipulation (X Corp. n.d.; YouTube n.d.), and in the United States the FTC's 2024 rule prohibits the misuse of fake indicators of social media influence (16 CFR § 465.8).
- **Astroturfing.** Campaigns that pose as grassroots opinion while concealing a sponsor: fake petitions, front groups, undisclosed paid commentators, form letters under invented names.
- **Fake reviews and review manipulation.** Fabricated negative reviews of a target, or fabricated positive reviews of a rival, including AI-generated reviews. The FTC's rule addresses fake reviews, purchased reviews, undisclosed insider reviews, company-controlled review sites and review suppression (16 CFR Part 465).
- **Impersonation and deepfakes.** Fake executive accounts, cloned voices, manipulated video and spoofed domains used for fraud, market manipulation or reputational damage.
- **Narrative hijacking.** Taking over a company's hashtag, campaign or event to attach an unrelated or hostile message.
- **Data voids and AI poisoning.** Filling gaps in the information environment—queries for which little reliable content exists—with misleading material that search engines or AI assistants may then surface. The CNA study's observation that militaries may seek to influence perceptions through "manipulation of data and algorithms" has a commercial analogue (Pollpeter and Kerrigan 2021).
- **Malicious leaks (mal-information).** Genuine but selectively released documents, stripped of context to create a false impression.
- **Provocation (reflexive-control style).** Deliberate attempts to bait an organization into a visible overreaction—a hostile legal threat, an angry executive post, a public attack on a critic—that then becomes the real story. The reflexive-control literature describes influence on an opponent's situational assessment and the timing of its decisions (Vasara 2020). Pressure to "respond now" is often the lever.

## 6.2 A Shared Vocabulary: DISARM

Defenders benefit from describing influence campaigns in a common, structured way, as cybersecurity teams do with attack frameworks. The DISARM Foundation describes its open-source DISARM Red Framework as "a common language for documenting influence operations," so that organizations describing what they see "in the same terms" can share intelligence (DISARM Foundation n.d.). Mapping an incident to DISARM helps a company share information with platforms, peers and investigators, and check whether its defenses cover the techniques it is likely to face.

## 6.3 Detection: Narrative Sensing

The Protect phase depends on early warning. A narrative-sensing capability combines tools and human judgment:

- **Monitoring** of brand, executive, product and category terms across social platforms, forums, review sites, news and AI-assistant answers.
- **Baselines** of normal volume, sentiment and source mix, so anomalies stand out.
- **Indicators of coordination:** bursts of similar wording, newly created accounts, synchronized timing, unusual account networks and mismatches between claimed and observed location or language.
- **Triage** that asks three questions: is it false, is it coordinated, and is it gaining traction among audiences that matter?
- **Escalation thresholds** set in advance, so the team does not argue about whether to act while the narrative spreads.

## 6.4 Prebunking and Psychological Inoculation

Inoculation theory, developed by William McGuire in the 1960s, proposes that exposing people to a weakened form of a persuasive attack, together with a refutation, can build resistance to the full attack (McGuire 1964). Recent research has tested this approach against misinformation. Van der Linden and colleagues found that warning people about misleading tactics helped protect accurate beliefs about the scientific consensus on climate change (van der Linden et al. 2017). Roozenbeek and colleagues showed, in studies that included a field experiment on YouTube, that short videos explaining common manipulation techniques improved people's ability to recognize those techniques (Roozenbeek et al. 2022).

For organizations, prebunking means:

- Telling employees, customers and partners in advance about the kinds of scams, impersonations and false claims they may see, and how to verify official communications.
- Publishing a clear list of official accounts, domains and payment procedures.
- Explaining the organization's position on predictable controversies before they arrive, with evidence.
- Training staff to recognize manipulation techniques such as false urgency, fake authority and emotionally loaded framing.

## 6.5 Debunking and Correction

When false information is already circulating, research on correcting misinformation offers practical guidance. Lewandowsky and colleagues review why misinformation persists after correction and recommend, among other things, providing an alternative explanation that fills the gap left by the retracted claim, giving warnings before exposure where possible, and keeping corrections simple and focused on the facts (Lewandowsky et al. 2012). In corporate practice:

- **Lead with the truth** in clear, plain language, and give the audience a coherent account of what actually happened.
- **Show evidence** from sources the audience trusts: independent tests, regulators, customers.
- **Be fast but accurate.** A wrong correction is worse than a slow one. Pre-approved holding statements buy time.
- **Use the channels where the falsehood spread**, not only the company's own website.
- **Report and document** inauthentic activity to platforms under their policies, and preserve evidence for legal review.

## 6.6 Legal and Platform Remedies

Depending on jurisdiction and facts, remedies can include platform reporting under impersonation, CIB and fake-engagement policies; complaints to consumer-protection authorities about fake reviews or deceptive competitor advertising; actions for false advertising under Section 43(a) of the Lanham Act (15 U.S.C. § 1125); trademark and domain-dispute procedures for impersonation; and referrals to law enforcement for fraud. Legal action should be proportionate. An aggressive lawsuit against a critic can turn a minor story into a major one, which is precisely the provocation risk described above.

## 6.7 Decision Hygiene: Defending Against Reflexive Control

If an adversary's aim is to shape your decisions, the last line of defense is the quality of your own decision process. Practices that make an organization harder to steer include:

- **Second sources.** Never act on a single unverified signal, especially one that demands urgency.
- **Red-teaming assumptions.** Before major responses, ask: who benefits if we do this? What would an adversary want us to do now?
- **Pre-commitment.** Decide in calm conditions how the organization will respond to classes of events, so pressure in the moment has less leverage.
- **Pause rules.** For provocations, a short, deliberate delay to verify facts often removes the attacker's advantage.
- **Diverse inputs.** Include people with different information sources in crisis decisions to reduce shared blind spots.

## 6.8 Response Playbook

| Tier | Description | Typical response |
| 1. Watch | Low-reach false or hostile content; no coordination indicators | Log, monitor, prepare facts; no public response |
| 2. Engage | Growing reach among relevant audiences, or inaccurate claims by credible voices | Direct correction to the source; FAQ update; customer-service briefing |
| 3. Respond | Viral spread, coordination indicators, or impersonation | Public statement with evidence; platform reports; journalist briefings; legal review |
| 4. Crisis | Safety, financial or market-integrity impact; executive deepfake or fraud | Crisis team activation; regulators and law enforcement as appropriate; full-channel response; executive communication |

## 6.9 Organizational Resilience

NATO's research report treats resilience—the ability to withstand and recover—as a core function in countering cognitive warfare (NATO STO n.d.). For a company, resilience means a trust reserve built over time, employees who know how to verify and whom to tell, customers who know the official channels, documented processes for payments and approvals that do not rely on recognizing a voice, and leaders who rehearse cognitive-attack scenarios alongside cyber incidents. Organizations that plan for both find that the same people, the same fact base and the same calm process serve both.

## 6.10 Exercising the Defense

Defenses that are never tested decay. Infinitum recommends a regular program of authorized exercises, run with leadership approval and without deceiving the public:

- **Tabletop exercises** that walk the crisis team through a viral falsehood, a fake-review wave, an executive deepfake and a provocation designed to bait an overreaction, using the response tiers above.
- **Verification drills** in which finance and executive-support staff receive simulated urgent requests, clearly scoped and authorized in writing, to test out-of-band verification.
- **Monitoring tests** that check whether the narrative-sensing capability raises alerts on controlled test inputs, such as test mentions on the organization's own accounts or a monitoring vendor's test feed, within the expected time.
- **After-action reviews** that record what worked, what was slow and which pre-approvals were missing, then update the playbook.

The aim is the same as in security testing: find the gaps before an adversary does, under controlled conditions, with written permission.
