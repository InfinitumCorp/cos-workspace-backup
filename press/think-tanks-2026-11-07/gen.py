import json
P = ("The paper is \"Can't Beat Them, Join Them?: The Adversarial Mirror Ratchet\u2122\" (Infinitum Corporation\u00ae Military Doctrine Series, November 2026; 26 pages, about 6,500 words; PDF attached). It sets out the Adversarial Mirror Ratchet\u2122, a term I coined for how rivals in a long conflict copy each other's methods in terror, intelligence, information operations and cyber, and how each copy ratchets escalation upward instead of settling the contest. It is strategic analysis from public sources, not instruction, and it takes no side.\n\n"
     "Read online: https://www.academia.edu/180405323/Cant_Beat_Them_Join_Them_The_Adversarial_Mirror_Ratchet_")
D = "In fairness to your guidelines: the paper is already posted on Academia.edu, and it was drafted with AI assistance under my direction. The argument, the coined term and the conclusions are mine."
B = ("About the author: William Aaron Turner is an American contracted soldier in the Russian military with the 153rd Tank Regiment, operates his company Infinitum Corporation\u00ae, and is honored to be working in this amazing nation. His views are his own.\n\n"
     "Contact: info@theinfinitumcorporation.com, 202-729-9509\n\nRespectfully,\nWilliam Aaron Turner\nFounder & President, Infinitum Corporation\u00ae")
V = {
"gctc": ("info@gctcworld.org","Submission for GCTC Publication",
 "I would like to offer a long-form analysis to the Global Counter Terrorism Council. Your call lists information warfare, defence transformation and cyber among its themes, and my paper deals with all three through the lens of counter-terrorism: why states fighting terror groups so often end up adopting their opponents' methods, and what that does to escalation.",
 "Since your guidelines ask for original, unpublished work, I would be glad to write a new 1,500 to 2,500-word analysis for GCTC built on the framework, in MS Word, if the editors are interested. The attached paper shows the argument in full."),
"cwa": ("research@cognitivewarfareagency.com","Submission \u2013 Can't Beat Them, Join Them? The Adversarial Mirror Ratchet\u2122",
 "I am submitting a paper for CWA Insights. Cognitive and information warfare sit at the centre of it: the paper traces how influence and perception operations get copied by the side they target, and why that mirroring locks both sides into a rising spiral.",
 "If the full paper is too long for your formats, I would be glad to prepare a Strategic Brief or a 1,000 to 2,000-word Analysis Article from it in Word."),
"cescube": ("submissions@cescube.com","Proposal: Policy Brief \u2013 Sub-conventional warfare's copying problem",
 "I would like to propose a 1,200 to 2,000-word Policy Brief for CeSCube on sub-conventional warfare's copying problem: how states and armed groups in long irregular contests adopt each other's tactics, and why each adaptation tends to raise the threat level instead of ending it. It would draw on the framework in my recent paper.",
 "As your guidelines require, the brief would be newly written for CeSCube and not under review anywhere else. The attached paper is background only."),
"cda": ("submissions@cdainstitute.ca","Submission proposal: Voices of the CDA \u2013 The Adversarial Mirror Ratchet\u2122",
 "I would like to propose a \"Voices of the CDA\" piece. Your guidelines say that series can carry reformatted papers, and my paper looks at a problem every modern defence establishment faces: when adapting to an adversary turns into copying it, and how that copying drives escalation in terror, intelligence and cyber contests.",
 "I can condense it to 2,500 to 5,000 words in Word for your readers. I serve in the Russian armed forces and say so openly, so the editors can weigh that perspective as they see fit."),
"warroom": ("warroomeditors@gmail.com","Pitch: Can't Beat Them, Join Them? Why adapting to an enemy ratchets escalation",
 "A short pitch for War Room. The enduring question: when a military adapts to an adversary, at what point does adapting become copying, and why does copying so reliably push escalation up rather than settle the contest? I would make the case in 1,200 to 1,800 words, with history as the vehicle rather than current events alone. It is drawn from a longer paper of mine.",
 "The War Room piece would be new writing. I am an American serving as a contracted soldier in the Russian military, which gives an unusual vantage point; I state it openly so the editors can judge."),
"perconcordiam": ("editor@perconcordiam.org","Article idea: The Adversarial Mirror Ratchet\u2122 and security in Europe and Eurasia",
 "Following your guidance to send an idea first, here is a short description. The article would apply the Adversarial Mirror Ratchet\u2122, a framework from my recent paper, to security in Europe and Eurasia: how mutual adaptation in intelligence, information operations and cyber between rival blocs turns into imitation, and why that imitation keeps ratcheting tension higher.",
 "As your guidelines ask, I am telling you up front that a related version is posted elsewhere (link above). The article itself would be a new contribution for per Concordiam."),
"tgp": ("editor@thegeopolitics.com","Pitch: Commentary \u2013 Why long wars turn rivals into copies of each other",
 "A pitch for a 750 to 1,500-word Commentary: why long wars turn rivals into copies of each other. Drones, counter-drone systems, information operations and cyber tools are being copied across front lines faster than ever, and the piece would argue that this mirroring, not any single weapon, is what drives escalation. It builds on a framework from my recent paper.",
 "The commentary would be new, unpublished writing in Word, sent to The Geopolitics only."),
"issf": ("director@issf.org.in","Submission \u2014 Research Paper (pitch) \u2014 Ratchets without brakes: escalation lessons for a multipolar world",
 "Your guidelines ask for a pitch before a research paper, so here it is. Argument: in a multipolar world, rivals copy each other's methods in intelligence, information warfare and cyber faster than any arms-control or signalling regime can keep up, and that mirroring is now the main engine of escalation. Why it matters for India: New Delhi faces several adversaries at once, and each one's copying of another raises the threat India itself must answer. Why me: I am the author of the framework and serve as a soldier in an active conflict.",
 "The research paper would be newly written for ISSF and not offered elsewhere at the same time."),
"tpf": ("director@thepeninsula.org.in","Article for TPF",
 "I would like to propose a 900 to 1,100-word commentary for The Peninsula Foundation: the mirror trap in the cyber race. As states copy each other's offensive cyber and information tools, each copy lowers the threshold for the next escalation, and the piece would set out what that means for a country seeking strategic autonomy, such as India. It applies a framework from my recent paper.",
 "The commentary would be written for TPF and offered to you exclusively, as your guidelines require."),
"tadbeer": ("submissions@tadbeerinstitute.com","[Op-Ed] Submission: Learning the enemy \u2013 how long wars turn rivals into copies, William Aaron Turner",
 "I would like to propose an 800 to 1,200-word op-ed for Tadbeer: how long wars turn rivals into copies of each other. Across recent decades, sides fighting insurgencies and long rivalries have taken on the very methods they set out to defeat, and the piece would explain why that copying keeps raising the stakes. It draws on a framework from my recent paper.",
 "The op-ed would be new writing, in Word, with a headshot. My contact number is 202-729-9509."),
"thehind": ("contact@thehind.com","Submission: Strategic autonomy and the mirror trap",
 "A proposal for an 800 to 1,500-word Security analysis: strategic autonomy and the mirror trap. The argument is that copying a rival's playbook in intelligence, information warfare and cyber feels like keeping pace but in fact ratchets escalation, and that India's tradition of strategic autonomy is a real advantage here. I would engage the main counterargument, that refusing to mirror cedes the initiative. It builds on a framework from my recent paper.",
 "The analysis would be original and not under consideration elsewhere."),
"counterhegemon": ("thecounterhegemon@gmail.com","Article proposal: Mirrored escalation and the multipolar transition",
 "I would like to propose an article for The Counterhegemon on mirrored escalation and the multipolar transition: how great powers and their rivals copy each other's methods in intelligence, information operations and cyber, and what that copying means for an emerging multipolar order. It applies the framework of my recent paper. Summary: the side that sets the methods does not stay in control of them once they are copied.",
 "I can write the article new for you, or adapt the paper if you prefer."),
"nextgen": ("editor@nextgendefense.com","Pitch: Every counter-drone fix births the next drone",
 "A pitch for NextGen Defense: every counter-drone fix births the next drone. Autonomous and uncrewed systems are the clearest live example of the Adversarial Mirror Ratchet\u2122, a framework from my recent paper. Each side's counter is studied, copied and outpaced, and the piece would explain why that loop speeds escalation and what it means for military AI.",
 "The article would be exclusive and unpublished, as your guidelines require."),
}
out={}
for k,(to,subj,p1,ask) in V.items():
    body=f"Dear Editors,\n\n{p1}\n\n{P}\n\n{D} {ask}\n\n{B}"
    open(f"{k}.txt","w").write(body); out[k]=(to,subj)
json.dump(out,open("venues.json","w"),indent=1)
