import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { PageHeading } from "../../../components/page-heading";
import { getService, services } from "../../../content/services";
import { entity, ORG_ID, SITE_URL } from "../../../content/entity";

export function generateStaticParams() {
  return services.map((s) => ({ slug: s.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug: string }>;
}): Promise<Metadata> {
  const { slug } = await params;
  const s = getService(slug);
  if (!s) return {};
  return {
    title: s.title,
    description: s.description,
    keywords: s.keywords,
    alternates: { canonical: `/services/${s.slug}` },
    openGraph: { title: `${s.title} | ${entity.name}`, description: s.description, url: `/services/${s.slug}` },
  };
}

export default async function ServicePage({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const s = getService(slug);
  if (!s) notFound();
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Service",
    name: s.h1,
    serviceType: s.h1,
    description: s.description,
    url: `${SITE_URL}/services/${s.slug}`,
    provider: { "@id": ORG_ID },
    areaServed: { "@type": "Country", name: "United States" },
  };
  return (
    <>
      <PageHeading number="S" label={s.label} title={s.h1} description={s.intro} />
      <section className="section editorial">
        <span className="eyebrow">{entity.name.toUpperCase()} / WASHINGTON, DC</span>
        <div>
          {s.sections.map((sec) => (
            <div key={sec.heading}>
              <h2>{sec.heading}</h2>
              <p>{sec.body}</p>
            </div>
          ))}
          {s.related &&
            (s.related.href.startsWith("/") ? (
              <Link className="text-link" href={s.related.href}>
                {s.related.label} ↗
              </Link>
            ) : (
              <a className="text-link" href={s.related.href} target="_blank" rel="noopener">
                {s.related.label} ↗
              </a>
            ))}
          <p>
            Talk to us: <a href={`tel:${entity.phoneE164}`}>{entity.phone}</a> ·{" "}
            <a href={`mailto:${entity.email}`}>{entity.email}</a> · {entity.hours}.
          </p>
          <p>
            Other services:{" "}
            {services
              .filter((o) => o.slug !== s.slug)
              .map((o, i) => (
                <span key={o.slug}>
                  {i > 0 && " · "}
                  <Link href={`/services/${o.slug}`}>{o.h1}</Link>
                </span>
              ))}
          </p>
        </div>
      </section>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
    </>
  );
}
