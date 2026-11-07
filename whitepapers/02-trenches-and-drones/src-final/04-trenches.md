
# Analysis: five fronts and two cross-cutting concerns {#analysis}

The next seven parts take the fronts in turn. Each part follows the same pattern: what public sources describe, what it means for your network, what to do, and what to measure.

## Part I: Trenches. Depth beats a hard shell {#part-i-trenches}

**What public analysis describes.** CSIS says that "defenders who can dig in with effective counter-drone measures will have a significant advantage, and those who must cross open land will be at a significant disadvantage" (CSIS, 2025a). It adds that cover and concealment are of the utmost importance (CSIS, 2025a).

Two ideas there. Depth. And making the attacker cross open ground.

**What it means for you.** For thirty years, many networks were built like a shell. Hard outside. Soft inside. One firewall and a VPN. Get past the wall and you can walk anywhere.

NIST's zero trust guidance describes the problem with a picture from an airport. All passengers pass a security checkpoint, then mill about the terminal, "and all the individuals are considered trusted." That boarding area is what NIST calls the "implicit trust zone." NIST then makes the point that matters: "the implicit trust zone must be as small as possible" for the policy decision point to be as specific as it can be (NIST SP 800-207, 2020).

Shrink the zone where everyone is trusted. That is the whole idea.

NIST defines zero trust as "an evolving set of cybersecurity paradigms that move defenses from static, network-based perimeters to focus on users, assets, and resources." It assumes "no implicit trust granted to assets or user accounts based solely on their physical or network location" (NIST SP 800-207, 2020).

Its tenets read like a field order for a defender who expects to be penetrated:

- All communication is secured regardless of network location. Network location alone does not imply trust.
- Access to individual resources is granted on a per-session basis, with the least privileges needed.
- Access is determined by dynamic policy, including client identity, application and the requesting asset, and may include behavioral and environmental attributes.
- The enterprise monitors and measures the integrity and security posture of all owned and associated assets. No asset is inherently trusted.
- Authentication and authorization are dynamic and strictly enforced before access is allowed.
- The enterprise collects as much information as possible about the current state of assets, network infrastructure and communications, and uses it to improve its security posture (NIST SP 800-207, 2020).

NIST is honest about the limits: these tenets are "the ideal goal," and not all may be fully implemented in their purest form (NIST SP 800-207, 2020).

## Why depth matters in a war of attrition

An attacker with persistence will eventually get a foothold. A phished account. An exposed edge device. A stolen credential. Verizon notes that attackers are "increasingly blending in with normal operations by using the same access paths as legitimate users," such as desktop-sharing tools and virtual private networks (Verizon, 2026). It adds that threat actors seem to be dialing back reliance on traditional tools such as Cobalt Strike as defenders get better at detecting and blocking them (Verizon, 2026).

That is measure and countermeasure in your own logs. The contest moved. Your design has to assume the first line will be crossed.

NIST's cyber resiliency guidance names the design moves. Among its techniques:

- **Coordinated protection.** "Require a threat event to overcome multiple safeguards," increasing the cost to the adversary and the likelihood of detection.
- **Segmentation.** Contain adversary activity to the enclave, segment or facility where it has established a presence, limiting where malware can propagate.
- **Realignment.** Minimize connections between mission-critical and non-critical services, so that a failure in the latter does not reach the former.
- **Privilege restriction.** Make the adversary invest more time and effort obtaining credentials, and curtail what stolen credentials can do.
- **Diversity.** Use heterogeneity to minimize common-mode failures and make the adversary build tools for more than one target type (NIST SP 800-160 Vol. 2 Rev. 1, 2021).

The same document is candid about costs. It notes that "diversity and segmentation can each make analytic monitoring and contextual awareness more difficult," because diverse systems need tools that can handle the variety, and segmentation can limit visibility (NIST SP 800-160 Vol. 2 Rev. 1, 2021).

Depth is not free. Each line you dig has to be manned, watched and maintained. A trench line nobody patrols is a ditch.

## The trench map

Here is a simple way to lay it out. I call these lines. They are my own organizing device, drawn from the NIST and CISA material above. They are not a standard.

| Line | Question it answers | Typical controls | What to watch |
|---|---|---|---|
| 0. The edge | What does the internet touch? | Inventory of internet-facing assets; patching of edge devices; removal of unused services; management interfaces off the internet | Exposure count; time to patch known-exploited flaws |
| 1. Identity | Who or what is asking? | Phishing-resistant multifactor authentication; per-session access; least privilege; service-account inventory | Privileged accounts; dormant accounts; unusual sign-ins |
| 2. Segments | How far can one foothold travel? | Network and application segmentation; separate management network; restricted east-west traffic | Cross-segment flows; new connections between systems that never talk |
| 3. Crown assets | What cannot be lost? | Data classification; stronger controls and logging around critical systems; separate admin paths | Access to crown data; unusual bulk reads |
| 4. Recovery | How do we come back? | Tested, isolated backups; rebuild runbooks; alternate communications | Restore time actually achieved in rehearsal |

Four of those five lines do not stop the attacker. They slow, contain, expose and survive. That is the point. In attrition, nothing is impenetrable. The goal is to make every step cost more than it is worth, and to see it happening.

## A maturity ladder you can borrow

CISA's Zero Trust Maturity Model is written for federal agencies, but its structure helps anyone. It organizes zero trust into five pillars: Identity, Devices, Networks, Applications and Workloads, and Data. It adds three cross-cutting capabilities: Visibility and Analytics, Automation and Orchestration, and Governance. It describes maturity in four stages: Traditional, Initial, Advanced and Optimal. Each pillar can progress at its own pace (CISA ZTMM, 2023).

In the Networks pillar, the model's progression runs from large perimeter or macro-segmentation, through isolation of critical workloads and expanded ingress and egress micro-perimeters, toward micro-segmentation around application profiles (CISA ZTMM, 2023).

For a mid-size organization, treat "Optimal" as a direction, not a deadline. Move each pillar one stage at a time. The stage you are in matters less than whether you know it, and whether you can show movement from quarter to quarter.

## What to do

1. **Draw your real lines.** Take the five lines above and write, for each, what you have today. Be blunt. Mark each as strong, partial or absent.
2. **Shrink the implicit trust zone.** Start with the most valuable segment. Move administrative access onto a separate path. Require phishing-resistant authentication for administrators and remote access first.
3. **Segment before you buy.** Segmentation that exists on a diagram does not count. Test it. Try to reach a crown system from an ordinary workstation, with permission, and write down what happens.
4. **Pay the monitoring cost.** For every line you add, decide what telemetry crosses it and who looks at it.
5. **Keep it boring.** Simple designs that people understand survive staff turnover. Elaborate ones decay.

## What to measure

- Number of segments that contain crown assets, and number of rules allowing traffic into them.
- Share of administrator and remote-access accounts using phishing-resistant authentication.
- Number of systems in the implicit trust zone: those a single compromised workstation can reach.
- Time to restore a crown system from backup, in a rehearsal.

Do not compare your numbers with a survey median. Compare them with your own last quarter.
