import { Page, Section, Text, BulletList, NumberedList, Table, Quote, LinkCards, Properties, TableOfContents, Fragment } from "grok/canvas";

type Blk =
  | { t: "p"; s: string }
  | { t: "quote"; s: string }
  | { t: "ul"; items: string[] }
  | { t: "ol"; items: string[] }
  | { t: "table"; cols: string[]; rows: string[][] }
  | { t: "links"; links: { title: string; href: string }[] }
  | { t: "props"; items: { label: string; value: string }[] };
type Sub = { heading: string; blocks: Blk[] };
type Sec = { id: string; heading: string; blocks: Blk[]; subs: Sub[] };

const SECTIONS: Sec[] = [
{"id":"about-this-paper","heading":"About this paper","blocks":[{"t":"p","s":"Dead Reckoning: AI for Security Operations in a Jammed, Spoofed, Watched World"},{"t":"p","s":"Practical, Integrated Steps for Mid-Size Organizations"},{"t":"p","s":"By William Aaron Turner, Founder and President, Infinitum Corporation. Infinitum Corporation Whitepaper No. 1. October 2026. Released October 25, 2026."},{"t":"p","s":"Neutrality statement. This paper draws general lessons about technology and conflict from public sources. It takes no side and makes no claim about any party."},{"t":"p","s":"© 2026 Infinitum Corporation. All rights reserved. No part of this publication may be reproduced or distributed without written permission, except for brief quotations with attribution."},{"t":"p","s":"Disclaimer. This whitepaper is provided for general information only. It is not legal, regulatory or professional advice for any specific situation, and it does not create a client relationship. Statistics are taken from the public sources cited and remain the property of their publishers; they describe the samples studied by those publishers and are not benchmarks or predictions for any particular organization. Infinitum Corporation makes no promise or guarantee about the security outcome any organization will achieve."},{"t":"p","s":"This paper is strictly analytical and defensive. References to irregular warfare, gray-zone competition and hybrid threats are used as an analytic lens for defense and resilience. Nothing in this paper is instruction for offensive activity. Any security testing referred to here means authorized, scoped testing performed with the written permission of the system owner."},{"t":"p","s":"Scenarios in Part IX are illustrative and hypothetical. They do not describe any real organization, client or incident."},{"t":"p","s":"Trademarks and framework names belong to their respective owners. Citation of a source does not imply that its publisher endorses this paper or Infinitum Corporation."},{"t":"props","items":[{"label":"Contact","value":"Infinitum Corporation, Washington, DC, 1629 K Street NW, Suite 300"},{"label":"Phone","value":"(202) 980-9300"},{"label":"Website","value":"https://www.theinfinitumcorporation.com"},{"label":"Email","value":"info@theinfinitumcorporation.com"},{"label":"Telegram","value":"https://t.me/infinitumcorporation"},{"label":"X","value":"https://x.com/infinitumceo"}]},{"t":"p","s":"All data comes from the public record. All conclusions are mine. W.A.T."}],"subs":[]},
// @@APPEND@@
];

const TOC = [{"label":"About this paper","id":"about-this-paper"},{"label":"Executive summary","id":"executive-summary"},{"label":"The problem","id":"the-problem"},{"label":"Attackers are walking in through unfixed software","id":"attackers-are-walking-in-through-unfixed-software"},{"label":"Fixes are not keeping pace","id":"fixes-are-not-keeping-pace"},{"label":"Breaches are expensive, and slow to find","id":"breaches-are-expensive-and-slow-to-find"},{"label":"And the people are stretched","id":"and-the-people-are-stretched"},{"label":"A caution on the numbers","id":"a-caution-on-the-numbers"},{"label":"Why this is a capacity problem","id":"why-this-is-a-capacity-problem"},{"label":"The question this paper answers","id":"the-question-this-paper-answers"},{"label":"The modern battlefield","id":"the-modern-battlefield"},{"label":"Seven lessons","id":"seven-lessons"},{"label":"Where the comparison breaks","id":"where-the-comparison-breaks"},{"label":"Dead reckoning for security operations","id":"dead-reckoning-for-security-operations"},{"label":"Analysis","id":"analysis"},{"label":"Part I: The irregular warfare lens","id":"part-i-the-irregular-warfare-lens"},{"label":"Part II: Adversary adaptation","id":"part-ii-adversary-adaptation"},{"label":"Part III: The evidence on AI for defenders","id":"part-iii-the-evidence-on-ai-for-defenders"},{"label":"Part IV: The use cases, one by one","id":"part-iv-the-use-cases-one-by-one"},{"label":"Part V: Governance and AI risk","id":"part-v-governance-and-ai-risk"},{"label":"Part VI: Securing the AI itself","id":"part-vi-securing-the-ai-itself"},{"label":"Part VII: People and the workforce","id":"part-vii-people-and-the-workforce"},{"label":"Part VIII: Metrics that matter","id":"part-viii-metrics-that-matter"},{"label":"Part IX: Illustrative scenarios","id":"part-ix-illustrative-scenarios"},{"label":"Recommendations","id":"recommendations"},{"label":"The six steps","id":"the-six-steps"},{"label":"What the battlefield teaches the plan","id":"what-the-battlefield-teaches-the-plan"},{"label":"The first 90 days","id":"the-first-90-days"},{"label":"The first 12 months","id":"the-first-12-months"},{"label":"Maturity self-assessment checklist","id":"maturity-self-assessment-checklist"},{"label":"Conclusion","id":"conclusion"},{"label":"About Infinitum Corporation","id":"about-infinitum-corporation"},{"label":"References","id":"references"},{"label":"Glossary","id":"glossary"}];

function renderBlock(b: Blk) {
  switch (b.t) {
    case "p":
      return <Text>{b.s}</Text>;
    case "quote":
      return <Quote>{b.s}</Quote>;
    case "ul":
      return <BulletList items={b.items} />;
    case "ol":
      return <NumberedList items={b.items} />;
    case "table":
      return <Table columns={b.cols} rows={b.rows} />;
    case "links":
      return <LinkCards links={b.links.map((l) => ({ title: l.title, href: l.href }))} numbered />;
    case "props":
      return <Properties items={b.items.map((p) => ({ label: p.label, value: p.value }))} />;
  }
}

export default function App() {
  return (
    <Page
      title="Dead Reckoning: AI for Security Operations in a Jammed, Spoofed, Watched World"
      summary="Practical, Integrated Steps for Mid-Size Organizations. Infinitum Corporation Whitepaper No. 1, by William Aaron Turner. Released October 25, 2026."
      width="column"
    >
      <TableOfContents items={TOC} />
      {SECTIONS.map((sec) => (
        <Section key={sec.id} id={sec.id} heading={sec.heading}>
          {sec.blocks.map((b, i) => (
            <Fragment key={i}>{renderBlock(b)}</Fragment>
          ))}
          {sec.subs.map((sub, j) => (
            <Section key={j} heading={sub.heading}>
              {sub.blocks.map((b, k) => (
                <Fragment key={k}>{renderBlock(b)}</Fragment>
              ))}
            </Section>
          ))}
        </Section>
      ))}
    </Page>
  );
}
