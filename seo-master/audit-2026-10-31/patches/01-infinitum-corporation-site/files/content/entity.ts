// Canonical brand entity (NAP + profiles). Single source for JSON-LD, footer and contact.
// Only public phone: 202-729-9509 (decided by William Aaron Turner, 2026-10-31).
export const SITE_URL = "https://www.theinfinitumcorporation.com";
export const ORG_ID = `${SITE_URL}/#organization`;
export const PERSON_ID = `${SITE_URL}/#william-aaron-turner`;

export const entity = {
  name: "Infinitum Corporation",
  legalName: "Infinitum Corporation",
  url: SITE_URL,
  email: "info@theinfinitumcorporation.com",
  phone: "202-729-9509",
  phoneE164: "+1-202-729-9509",
  hours: "Mon–Fri 9:00 AM–9:00 PM (closed Sat–Sun)",
  address: {
    streetAddress: "1629 K Street NW, Suite 300",
    addressLocality: "Washington",
    addressRegion: "DC",
    postalCode: "20006",
    addressCountry: "US",
  },
  founder: "William Aaron Turner",
  description:
    "Infinitum Corporation is a technology and security consulting firm headquartered in Washington, DC, with Moscow as an operating location. It provides cybersecurity consulting, network defense, ethical hacking and vulnerability assessment, AI applications for security operations, strategic risk assessment, defense technology advisory and Corporate Cognitive Warfare.",
};

// Owned, live profiles only (checked 2026-10-31). Substack and YouTube are inactive and excluded.
export const orgProfiles = {
  telegram: "https://t.me/infinitumcorporation",
  discord: "https://discord.gg/QVT7dWHUQa",
  github: "https://github.com/InfinitumCorp",
  whop: "https://whop.com/infinitum-corporation/",
  whitepapers: "https://infinitumwhitepapers.blogspot.com/",
  ukraineFiles: "https://ukrainianfiles.blogspot.com/",
  academia: "https://independent.academia.edu/CorporationInfinitum",
};
export const personProfiles = {
  x: "https://x.com/infinitumceo",
  linkedin: "https://www.linkedin.com/in/william-aaron-t-726076244",
  website: "https://williamaaronturner.com/",
  about: "https://ukrainianfiles.blogspot.com/p/about.html",
};

export const footerLinks: ReadonlyArray<readonly [string, string]> = [
  ["X @infinitumceo", personProfiles.x],
  ["Telegram", orgProfiles.telegram],
  ["Discord", orgProfiles.discord],
  ["Whitepapers", orgProfiles.whitepapers],
  ["The Ukraine Files", orgProfiles.ukraineFiles],
  ["Whop", orgProfiles.whop],
  ["GitHub", orgProfiles.github],
  ["Academia.edu", orgProfiles.academia],
];

export const ORCID = "https://orcid.org/0009-0002-1585-5442";

// Publications (31 Oct 2026). Only published items; never exclusives or journal manuscripts under review.
export const publications: ReadonlyArray<{ title: string; url: string; type: string; doi?: string }> = [
  { title: "Useful Idiots: A Guide to the Western Profiteers of the Ukraine War", url: "https://ukrainianfiles.blogspot.com/2026/10/blog-post_85.html", type: "ScholarlyArticle", doi: "10.5281/zenodo.23836478" },
  { title: "WTF Is In-Q-Tel? The CIA's Venture Fund and the Kill Chain It Bankrolled", url: "https://ukrainianfiles.blogspot.com/2026/10/in-q-tel-cia-venture-capital-explained.html", type: "ScholarlyArticle", doi: "10.5281/zenodo.23836521" },
  { title: "Sweeps and Spies: Russia Clears the Bombs. The West Clears the Data.", url: "https://ukrainianfiles.blogspot.com/2026/10/demining-ngos-intelligence-laos-moldova.html", type: "ScholarlyArticle", doi: "10.5281/zenodo.23836541" },
  { title: "The Partnership That Delivers: What the Russia-Africa Summit Actually Produced", url: "https://russiaafricareport.blogspot.com/2026/10/russia-africa-summit-partnership-results.html", type: "ScholarlyArticle", doi: "10.5281/zenodo.23836501" },
  { title: "Dead Reckoning: AI for Security Operations in a Jammed, Spoofed, Watched World", url: "https://infinitumwhitepapers.blogspot.com/2026/10/dead-reckoning-ai-security-operations.html", type: "Report", doi: "10.5281/zenodo.23836365" },
  { title: "Russia's State-Influenced Capitalism: Sanctions-Proof, War-Proof, and Chaos-Proof", url: "https://infinitumwhitepapers.blogspot.com/2026/10/russia-state-influenced-capitalism.html", type: "Report", doi: "10.5281/zenodo.23836439" },
  { title: "Russia-Africa by the Numbers: Trade, Grain, Energy and Security After the Summit", url: "https://russiaafricabythenumbers.blogspot.com/2026/10/russia-africa-by-the-numbers-trade-grain-energy-security.html", type: "Article" },
  { title: "Eastern Economic Forum 2026: Is Russia Isolated?", url: "https://ukrainianfiles.blogspot.com/2026/10/eastern-economic-forum-2026-vladivostok.html", type: "Article" },
  { title: "Russia's Economy Under Sanctions: GDP, Aid, Stalemate", url: "https://ukrainianfiles.blogspot.com/2026/10/russia-economy-sanctions-gdp-aid.html", type: "Article" },
  { title: "Corporate Cognitive Warfare: Irregular Warfare for Market Supremacy (Whitepaper, Expanded Edition)", url: "https://infinitumwhitepapers.blogspot.com/2026/10/corporate-cognitive-warfare-expanded.html", type: "Report", doi: "10.5281/zenodo.23838097" },
  { title: "EchoForm: Modern Applications of Reflexive Control Theory", url: "https://whop.com/infinitum-corporation/echoform-reflexive-control-theory/", type: "ScholarlyArticle" },
];

const postalAddress = { "@type": "PostalAddress", ...entity.address };

export function entityGraph() {
  return {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": ["Organization", "ProfessionalService"],
        "@id": ORG_ID,
        name: entity.name,
        legalName: entity.legalName,
        url: SITE_URL,
        logo: `${SITE_URL}/infinitum-logo.png`,
        image: `${SITE_URL}/infinitum-logo.png`,
        description: entity.description,
        email: entity.email,
        telephone: entity.phoneE164,
        address: postalAddress,
        location: { "@type": "Place", name: "Infinitum Corporation headquarters", address: postalAddress },
        areaServed: [{ "@type": "City", name: "Washington, DC" }, { "@type": "Country", name: "United States" }],
        openingHoursSpecification: {
          "@type": "OpeningHoursSpecification",
          dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
          opens: "09:00",
          closes: "21:00",
        },
        contactPoint: {
          "@type": "ContactPoint",
          contactType: "customer service",
          telephone: entity.phoneE164,
          email: entity.email,
          areaServed: "US",
          availableLanguage: ["English", "Russian"],
          hoursAvailable: {
            "@type": "OpeningHoursSpecification",
            dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            opens: "09:00",
            closes: "21:00",
          },
        },
        founder: { "@id": PERSON_ID },
        knowsAbout: [
          "Cybersecurity consulting",
          "Network architecture and network defense",
          "Ethical hacking and vulnerability assessment",
          "AI for security operations",
          "Strategic risk assessment",
          "Defense technology advisory",
          "Corporate Cognitive Warfare",
          "cognitive warfare",
          "cognitive dominance",
          "narrative strategy",
          "EchoForm",
          "Reflexive Control Theory",
        ],
        makesOffer: [
          {
            "@type": "Offer",
            itemOffered: {
              "@type": "Service",
              name: "Corporate Cognitive Warfare",
              serviceType: "Corporate Cognitive Warfare consulting",
              description:
                "Corporate Cognitive Warfare, a term coined by William Aaron Turner: narrative strategy, ethical persuasion and search and AI-discovery optimization that help companies win the contest for perception and attention (cognitive dominance), informed by the established discipline of cognitive warfare.",
              provider: { "@id": ORG_ID },
            },
          },
        ],
        subjectOf: publications.map((p) => ({ "@id": `${p.url}#article` })),
        sameAs: Object.values(orgProfiles),
      },
      {
        "@type": "Person",
        "@id": PERSON_ID,
        name: "William Aaron Turner",
        jobTitle: "Founder and President",
        worksFor: { "@id": ORG_ID },
        url: personProfiles.website,
        knowsAbout: ["Cybersecurity", "AI for security operations", "Strategic risk assessment", "Geopolitical analysis", "Corporate Cognitive Warfare", "cognitive warfare", "cognitive dominance", "narrative strategy", "EchoForm", "Reflexive Control Theory"],
        identifier: { "@type": "PropertyValue", propertyID: "ORCID", value: "0009-0002-1585-5442", url: ORCID },
        workExample: publications.map((p) => ({ "@type": p.type, "@id": `${p.url}#article`, name: p.title, url: p.url, ...(p.doi ? { identifier: `https://doi.org/${p.doi}` } : {}) })),
        subjectOf: publications.map((p) => ({ "@id": `${p.url}#article` })),
        sameAs: [ORCID, ...Object.values(personProfiles)],
      },
      {
        "@type": "WebSite",
        "@id": `${SITE_URL}/#website`,
        url: SITE_URL,
        name: entity.name,
        publisher: { "@id": ORG_ID },
        inLanguage: "en-US",
      },
    ],
  };
}
