import type { Metadata } from "next";
import Link from "next/link";
import { PageHeading } from "../../../components/page-heading";
import { entity, ORCID, ORG_ID, PERSON_ID, SITE_URL } from "../../../content/entity";

const CANONICAL = "/publications/echoform";
const ABS = `${SITE_URL}${CANONICAL}`;
const TITLE = "EchoForm: Modern Applications of Reflexive Control Theory";
const SEO_TITLE = "EchoForm: Modern Applications of Reflexive Control Theory | Infinitum Corporation";
const DESC =
  "EchoForm names how prepared decision grounds return through networks as the target's own conclusion. Companion to Corporate Cognitive Warfare.";
const KEYWORDS = [
  "EchoForm",
  "Reflexive Control Theory",
  "decision grounds",
  "recursive reasoning",
  "algorithmic amplification",
  "Corporate Cognitive Warfare",
  "information integrity",
  "organizational resilience",
];
const CCW_BLOG =
  "https://infinitumwhitepapers.blogspot.com/2026/10/corporate-cognitive-warfare-expanded.html";
const CCW_DOI = "https://doi.org/10.5281/zenodo.23838097";
const CCW_ZENODO = "https://zenodo.org/records/23838097";
// Placeholders until each live copy is published:
const PLACEHOLDER_DOI = "[DOI PENDING]";
const PLACEHOLDER_ACADEMIA = "[ACADEMIA URL]";
const PLACEHOLDER_BLOG = "[BLOG URL]";
const LIVE_WHOP = "https://whop.com/infinitum-corporation/echoform-reflexive-control-theory/";

export const metadata: Metadata = {
  title: TITLE,
  description: DESC,
  keywords: KEYWORDS,
  authors: [{ name: "William Aaron Turner", url: "https://williamaaronturner.com/" }],
  alternates: { canonical: CANONICAL },
  openGraph: {
    type: "article",
    title: SEO_TITLE,
    description: DESC,
    url: CANONICAL,
    siteName: entity.name,
  },
  twitter: {
    card: "summary",
    site: "@infinitumceo",
    title: SEO_TITLE,
    description: DESC,
  },
  other: {
    "citation_title": TITLE,
    "citation_author": "Turner, William Aaron",
    "citation_author_orcid": ORCID,
    "citation_publication_date": "2026/11/07",
    "citation_publisher": "Infinitum Corporation",
    "citation_technical_report_institution": "Infinitum Corporation",
    "citation_language": "en",
    "citation_abstract_html_url": ABS,
  },
};

export default function EchoFormPage() {
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "ScholarlyArticle",
    "@id": `${ABS}#article`,
    headline: TITLE,
    name: TITLE,
    description: DESC,
    url: ABS,
    mainEntityOfPage: ABS,
    datePublished: "2026-11-07",
    inLanguage: "en",
    keywords: KEYWORDS.join(", "),
    author: {
      "@type": "Person",
      "@id": PERSON_ID,
      name: "William Aaron Turner",
      identifier: {
        "@type": "PropertyValue",
        propertyID: "ORCID",
        value: "0009-0002-1585-5442",
        url: ORCID,
      },
      url: "https://williamaaronturner.com/",
      jobTitle: "Founder and President",
      worksFor: { "@id": ORG_ID },
    },
    publisher: {
      "@type": "Organization",
      "@id": ORG_ID,
      name: "Infinitum Corporation",
      url: SITE_URL,
      address: {
        "@type": "PostalAddress",
        streetAddress: "1629 K Street NW, Suite 300",
        addressLocality: "Washington",
        addressRegion: "DC",
        postalCode: "20006",
        addressCountry: "US",
      },
    },
    about: KEYWORDS.map((name) => ({ "@type": "Thing", name })),
    isBasedOn: {
      "@type": "Report",
      name: "Corporate Cognitive Warfare: Irregular Warfare for Market Supremacy (Whitepaper, Expanded Edition)",
      url: CCW_BLOG,
      identifier: CCW_DOI,
    },
    sameAs: [LIVE_WHOP, CCW_BLOG, CCW_DOI, CCW_ZENODO],
    isPartOf: { "@type": "WebPage", url: LIVE_WHOP, name: "EchoForm on Whop" },
    genre: "Whitepaper",
    additionalType: "https://schema.org/Report",
  };

  return (
    <>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <PageHeading
        number="P"
        label="Companion note"
        title={TITLE}
        description="How prepared grounds return as the target's own decision — a companion conceptual note to Corporate Cognitive Warfare."
      />
      <section className="section editorial">
        <span className="eyebrow">{entity.name.toUpperCase()} / WASHINGTON, DC</span>
        <p>
          By{" "}
          <a href="https://williamaaronturner.com/" rel="author">
            William Aaron Turner
          </a>{" "}
          (ORCID{" "}
          <a href={ORCID}>0009-0002-1585-5442</a>), Founder &amp; President, Infinitum Corporation,
          Washington, DC. Released 7 November 2026.
        </p>
        <p>{DESC}</p>
        <h2>Also available / placeholders</h2>
        <ul>
          <li>
            Companion whitepaper (live):{" "}
            <a href={CCW_BLOG} target="_blank" rel="noopener">
              Corporate Cognitive Warfare (Expanded Edition)
            </a>{" "}
            · DOI <a href={CCW_DOI}>{CCW_DOI.replace("https://doi.org/", "")}</a> ·{" "}
            <a href={CCW_ZENODO} target="_blank" rel="noopener">
              Zenodo
            </a>
          </li>
          <li>
            Live copy (Whop):{" "}
            <a href={LIVE_WHOP} target="_blank" rel="noopener">
              {LIVE_WHOP}
            </a>
          </li>
          <li>EchoForm Zenodo DOI: {PLACEHOLDER_DOI}</li>
          <li>EchoForm Academia.edu: {PLACEHOLDER_ACADEMIA}</li>
          <li>EchoForm blog (infinitumwhitepapers.blogspot.com): {PLACEHOLDER_BLOG}</li>
          <li>
            Author page:{" "}
            <a href="https://williamaaronturner.com/publications/echoform">
              williamaaronturner.com/publications/echoform
            </a>
          </li>
        </ul>
        <p>
          <Link href="/publications">All publications</Link>
          {" · "}
          <a href="https://infinitumwhitepapers.blogspot.com/" target="_blank" rel="noopener">
            Whitepapers blog
          </a>
          {" · "}
          Media: <a href={`mailto:${entity.email}`}>{entity.email}</a>
        </p>
      </section>
    </>
  );
}
