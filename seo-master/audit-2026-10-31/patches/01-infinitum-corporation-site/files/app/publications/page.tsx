import type { Metadata } from "next";
import Link from "next/link";
import { PageHeading } from "../../components/page-heading";
import { entity, publications, SITE_URL } from "../../content/entity";

export const metadata: Metadata = {
  title: "Publications: Research & Whitepapers",
  description:
    "Infinitum Corporation publications by William Aaron Turner: whitepapers and research on Corporate Cognitive Warfare, EchoForm, AI for security operations and geopolitics.",
  alternates: { canonical: "/publications" },
  openGraph: {
    title: `Publications | ${entity.name}`,
    description:
      "Research and whitepapers from Infinitum Corporation, Washington, DC, including Corporate Cognitive Warfare and EchoForm.",
    url: "/publications",
  },
  twitter: {
    card: "summary",
    site: "@infinitumceo",
    title: `Publications | ${entity.name}`,
    description:
      "Research and whitepapers from Infinitum Corporation, including Corporate Cognitive Warfare and EchoForm.",
  },
};

export default function PublicationsPage() {
  return (
    <>
      <PageHeading
        number="P"
        label="Research"
        title="Publications"
        description="Whitepapers and sourced research by William Aaron Turner, Founder & President of Infinitum Corporation (Washington, DC)."
      />
      <section className="section editorial">
        <span className="eyebrow">{entity.name.toUpperCase()} / WASHINGTON, DC</span>
        <ul>
          {publications.map((p) => (
            <li key={p.url}>
              {p.url.startsWith(SITE_URL) ? (
                <Link href={p.url.replace(SITE_URL, "") || "/"}>{p.title}</Link>
              ) : (
                <a href={p.url} target="_blank" rel="noopener">
                  {p.title}
                </a>
              )}{" "}
              <span>({p.type}{p.doi ? `; DOI ${p.doi}` : ""})</span>
            </li>
          ))}
        </ul>
        <p>
          Featured companion note:{" "}
          <Link href="/publications/echoform">EchoForm: Modern Applications of Reflexive Control Theory</Link>
          {" · "}
          <a
            href="https://infinitumwhitepapers.blogspot.com/2026/10/corporate-cognitive-warfare-expanded.html"
            target="_blank"
            rel="noopener"
          >
            Corporate Cognitive Warfare (Expanded Edition)
          </a>
          .
        </p>
      </section>
    </>
  );
}
