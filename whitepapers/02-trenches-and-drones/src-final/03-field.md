
# The modern battlefield, read by a security analyst {#the-modern-battlefield}

Let me be plain about what I am doing here, and what I am not.

I am reading public analysis of modern conflict for general lessons about technology. I am not assessing any government, army or leader. I make no claim about any party. This paper draws general lessons about technology and conflict from public sources. It takes no side and makes no claim about any party.

I leave out casualty, loss and performance figures for every side. They are contested. They are estimates. And they are not what a security team needs to make a decision. I also leave out the attribution that some sources attach to specific events. That is not because it does not matter. It is because I am not the right author to judge it, and the lesson does not depend on it.

What I keep are the phenomena. Drone saturation. Jamming and spoofing. Sensor transparency. Cheap mass. Logistics under observation. Decentralized decisions.

## The framing

My shorthand: trench-style grind fused with science fiction.

Think of the first world war's long stalemate, the lines of dug-in positions where nothing moved fast. Now add cheap drones overhead, signals jammed and spoofed, satellites and commercial sensors watching the ground, and a cycle of measure and countermeasure that turns over in weeks.

CSIS opens its chapter on technological evolution with the point that new technology drives tactics in unprecedented ways, and that "the party that innovates, procures, and adapts first secures an often insurmountable edge." It gives an example from the first world war: the development of the first rudimentary tank to break the stalemate of trench warfare (CSIS, 2025a).

It then offers the line I keep coming back to: "the next generation of warfare will not be defined solely by who possesses the most advanced technology, but by who can integrate, adapt, and counter it the fastest" (CSIS, 2025a).

Integrate. Adapt. Counter. That is a good description of a security program.

## What public analysis describes

Here are the features I draw on, with the source for each.

**Cheap, flexible sensing and strike.** CSIS says the most marked change has been cheap, flexible and highly maneuverable intelligence, surveillance and reconnaissance (ISR) drones. It says cover and concealment are "of the utmost importance," and that large, highly visible formations are more vulnerable to drone strikes (CSIS, 2025a).

**A cat-and-mouse cycle.** CSIS describes "a highly iterative game of cat and mouse, with advancements in electronic warfare meeting drone advancements step for step" (CSIS, 2025a). It quotes an analyst describing a "six week learning cycle on the battlefield" (CSIS, 2025a).

**Electronic warfare as the norm.** In its chapter on space, CSIS calls the pervasiveness of electronic warfare (EW) "one of the most dominant features of the modern battlefield." It describes EW as a "temporary and reversible way" to target satellite navigation, communications signals and ISR collection, and says "going forward, EW will be the norm" (CSIS, 2025b). It also warns that regions outside conflict zones will experience greater electromagnetic interference, risking harm to civil and commercial transportation and public safety (CSIS, 2025b).

**Transparency.** CSIS says commercial space capabilities have introduced "a new level of transparency" and that "all militaries must adapt to a world where movements, emissions, and signatures are constantly monitored" (CSIS, 2025b). A separate CSIS chapter on intelligence says wars of the future will be fought "in conditions of near transparency," and that "information is cheap. Processing it is expensive, and sense-making is exquisite" (CSIS, 2025c).

**Logistics under pressure.** CSIS says logistics chains "will be in constant peril" and that modern armies "need to anticipate that only a fraction of supplies will get through" (CSIS, 2025a).

**Decentralized units.** CSIS says the future is shifting toward "smaller, highly mobile, adaptable units, where field commanders are empowered to make decisions" while minimizing their communications signature (CSIS, 2025a).

**No clean front line.** CSIS warns that as commercial providers take on greater roles in military operations, the line between combatants and noncombatants will blur, and that civilian service providers such as those supplying power, cloud storage and internet connectivity could increasingly be seen as military targets (CSIS, 2025a). That is CSIS's forecast, and it is contested ground in law and policy. I cite it as a warning about dependency, not as a statement of law.

**Overdependence.** CSIS says militaries "will need to incorporate technology without depending on it," and that "a force multiplier is a high-priority target for an opponent" (CSIS, 2025a).

## Five fronts

I organize the lessons into five fronts, and add two more that cut across all of them: command and people.

| Front | What public analysis describes | The same feature on your network |
|---|---|---|
| Trenches | Defenders who can dig in with effective counter-drone measures hold an advantage; cover and concealment matter | Depth: segmentation, identity at every line, a small trust zone |
| Drones | Cheap, numerous, flexible; economics favor the cheap | Automated scanning, credential stuffing, floods, bots; cheap automated controls in reply |
| Electronic warfare | Jamming and spoofing of signals; EW is the norm | Spoofed identities, time, names and voices; verify out of band; keep a second source |
| Sensors | Near-transparency; assume you are seen | Exposed surface; edge devices; your own telemetry; deception |
| Supply lines | Logistics in constant peril; commercial dependencies | Suppliers, cloud, platforms; offline copies; manual fallbacks |
| Command | Decentralized units; fast learning cycles | Decision rights; out-of-band comms; short lessons-learned loops |
| People | Endurance, integrated technology without overdependence | Staffing, rotation, skill; AI as a helper, not a crutch |

## Where the comparison breaks

I owe you the limits.

A network is not terrain. You cannot dig a trench in an IP range. And you can restore a server from a backup, which is not something a lost position allows.

Your adversaries are not armies. Most of the pressure on a mid-size organization comes from criminals, opportunists and automated tools. Some comes from more capable actors. The lens helps with the shape of the contest. It does not tell you who is on the other end.

Statistics do not transfer. A figure from a battlefield study tells you nothing about your firewall. That is why I use no battlefield statistics at all. My numbers come from breach and incident research, and I cite them to their sources.

Do not mistake analogy for instruction. This paper does not tell you to take any action against any adversary. Offensive action by private organizations raises legal and safety problems, and it is not what this paper recommends.

Finally, a caution about the analogy itself. The point of the lens is not drama. The point is that long, cheap, constant pressure is a different problem from a single dramatic attack, and it needs a different kind of plan.

Now the fronts, one at a time.
