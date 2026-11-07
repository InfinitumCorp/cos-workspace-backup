import type { Metadata } from "next";
import Link from "next/link";
import { PageHeading } from "../../components/page-heading";
import { services } from "../../content/services";
export const metadata: Metadata = {
  title: "Security Consulting Services, Washington DC",
  description:
    "Infinitum Corporation services: AI for security operations, strategic risk assessment, defense technology advisory and Corporate Cognitive Warfare. Washington, DC.",
  alternates: { canonical: "/services" },
};
export default function Services() {
  return (
    <>
      <PageHeading
        number="03"
        label="SERVICES"
        title="Security consulting services"
        description="Cybersecurity, risk and technology advisory from Washington, DC. Open Mon–Fri 9 AM–9 PM."
      />
      <section className="section">
        {services.map((s) => (
          <article key={s.slug}>
            <span className="eyebrow">{s.label}</span>
            <h2>
              <Link href={`/services/${s.slug}`}>{s.h1}</Link>
            </h2>
            <p>{s.description}</p>
          </article>
        ))}
      </section>
    </>
  );
}
