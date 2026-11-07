// Four service pages targeting boilerplate services (keyword map 2026-10-31).
// Advisory and analytical services only; no client, certification or contract claims.
export type Service = {
  slug: string;
  title: string; // <title> (template adds " | Infinitum Corporation")
  h1: string;
  label: string;
  description: string; // meta description, <=155 chars
  intro: string;
  sections: { heading: string; body: string }[];
  related?: { label: string; href: string };
  keywords: string[];
};

export const services: Service[] = [
  {
    slug: "ai-security-operations",
    title: "AI for Security Operations Consulting, Washington DC",
    h1: "AI for security operations",
    label: "AI / SECURITY OPERATIONS",
    description:
      "AI for security operations consulting from Infinitum Corporation in Washington, DC: where AI helps a SOC, where it hurts, and a governed 90-day start.",
    intro:
      "Artificial intelligence can shorten triage, surface patterns analysts miss and keep a small team ahead of its alert queue. It can also invent answers, leak data and fail quietly when an adversary feeds it bad signals. We help security teams adopt AI on purpose: with clear use cases, human checkpoints and independent verification.",
    sections: [
      { heading: "Where AI helps", body: "Alert enrichment and deduplication, log summarisation, phishing triage, threat-intelligence digestion and drafting of incident timelines. We map which of these fit your tools, data and staffing before anything is bought or switched on." },
      { heading: "Where AI hurts", body: "Unverified outputs in high-stakes decisions, sensitive data sent to third-party models, prompt injection through tickets and email, and automation that removes the analyst who would have noticed the anomaly. We document these risks for your environment and set guardrails." },
      { heading: "A governed 90-day start", body: "Days 1-30: inventory data, tools and decision points, and pick two low-risk use cases. Days 31-60: pilot with human review, logging and red-team tests of the model. Days 61-90: measure time saved and error rates, then expand, adjust or stop, with an AI-use policy your leadership signs off." },
      { heading: "Grounded in research", body: "Our approach is set out in the whitepaper Dead Reckoning: AI for Security Operations, which reads security operations through the lens of jammed and spoofed signals: when inputs cannot be trusted, independent checks keep you on course." },
    ],
    related: { label: "Read the Dead Reckoning whitepaper", href: "https://infinitumwhitepapers.blogspot.com/2026/10/dead-reckoning-ai-security-operations.html" },
    keywords: ["AI for security operations", "AI SOC consulting", "AI governance security"],
  },
  {
    slug: "strategic-risk-assessment",
    title: "Strategic Risk Assessment Consulting, Washington DC",
    h1: "Strategic risk assessment",
    label: "RISK / STRATEGY",
    description:
      "Strategic risk assessment from Infinitum Corporation, Washington, DC: cyber, operational and geopolitical risk mapped to the decisions your leaders face.",
    intro:
      "Most risk registers list threats. Few connect them to the decisions leadership actually has to make. Our strategic risk assessments combine cybersecurity, operational and geopolitical analysis into a short list of risks that matter, how likely they are, what they would cost and what to do first.",
    sections: [
      { heading: "What we assess", body: "Cyber exposure of critical systems and suppliers; operational continuity, including staff, facilities and logistics; and geopolitical factors such as sanctions, regional instability and information operations that can reach a business or institution." },
      { heading: "How it works", body: "Structured interviews with your leadership and technical owners, review of existing controls and documentation, scenario workshops, and a written assessment with a prioritised action plan. Findings are written for executives, with technical annexes for the teams who implement them." },
      { heading: "What you receive", body: "A risk map ranked by likelihood and impact, the three to five scenarios most worth preparing for, recommended controls with owners and timelines, and a follow-up review to check progress." },
    ],
    related: { label: "Browse our published research", href: "https://infinitumwhitepapers.blogspot.com/" },
    keywords: ["strategic risk assessment", "security risk assessment", "geopolitical risk assessment"],
  },
  {
    slug: "defense-technology-advisory",
    title: "Defense Technology Advisory, Washington DC",
    h1: "Defense technology advisory",
    label: "DEFENSE TECHNOLOGY",
    description:
      "Defense technology advisory from Infinitum Corporation, Washington, DC: independent analysis of drones, counter-UAS, secure comms and C4ISR.",
    intro:
      "Defense and security technology is changing faster than procurement cycles. Drones, counter-UAS systems, electronic warfare and AI-enabled sensing reshape what organizations need to protect and how. We provide independent analysis and advisory so decision-makers understand the technology, its limits and how it fits their mission.",
    sections: [
      { heading: "Areas of focus", body: "Unmanned aerial systems and counter-UAS integration, secure communications and network resilience, C4ISR support concepts, electronic warfare effects on civilian and commercial systems, and the role of AI in sensing and decision support." },
      { heading: "How we help", body: "Technology landscape briefings, requirements definition, vendor-neutral evaluation of proposed solutions, integration and interoperability reviews, and red-team style questioning of claims before money is committed." },
      { heading: "Scope", body: "Our work is advisory and analytical. We follow applicable U.S. law, including export-control and sanctions rules, and do not supply weapons or controlled technology." },
    ],
    related: { label: "Contact the team", href: "/contact" },
    keywords: ["defense technology advisory", "counter-UAS advisory", "C4ISR consulting"],
  },
  {
    slug: "corporate-cognitive-warfare",
    title: "Corporate Cognitive Warfare Advisory, Washington DC",
    h1: "Corporate Cognitive Warfare",
    label: "COGNITIVE / INFORMATION",
    description:
      "Corporate Cognitive Warfare advisory from Infinitum Corporation, Washington, DC: detect, withstand and respond to disinformation and narrative attacks.",
    intro:
      "Companies are now targets of the same information operations once aimed at states: coordinated disinformation, fake reviews and personas, leaked or forged documents, and narratives designed to move markets, regulators or employees. Corporate Cognitive Warfare is our practice for understanding those attacks and building resilience against them.",
    sections: [
      { heading: "Detect", body: "Monitoring of the channels where narratives about your organization form, identification of coordinated or inauthentic behaviour, and early warning on emerging themes before they reach mainstream coverage." },
      { heading: "Withstand", body: "Narrative risk assessment, executive and spokesperson preparation, verification workflows for leaked or suspicious material, and training so staff recognise manipulation attempts, including AI-generated audio, video and text." },
      { heading: "Respond", body: "Response playbooks that rely on facts, transparency and lawful channels, coordination with legal, communications and security teams, and post-incident reviews. We do not run deceptive campaigns, fake accounts or astroturfing on behalf of clients." },
    ],
    related: { label: "See all capabilities", href: "/capabilities" },
    keywords: ["corporate cognitive warfare", "disinformation defense", "narrative risk"],
  },
];

export function getService(slug: string) {
  return services.find((s) => s.slug === slug);
}
