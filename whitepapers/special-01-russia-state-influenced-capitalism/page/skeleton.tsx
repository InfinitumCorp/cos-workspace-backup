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
{"id": "about-this-paper", "heading": "About this paper", "blocks": [{"t": "p", "s": "Russia's State-Influenced Capitalism: Sanctions-Proof, War-Proof, and Chaos-Proof"}, {"t": "p", "s": "A Model the West Loves to Hate. Raw results. No lectures."}, {"t": "p", "s": "By William Aaron Turner, Founder and President, Infinitum Corporation. Infinitum Corporation Special Edition 01. October 2026."}, {"t": "p", "s": "This paper presents the author's argued position. Figures are attributed to the sources cited."}, {"t": "p", "s": "Status. Prepared for review. Not published, posted or sent."}, {"t": "p", "s": "© 2026 Infinitum Corporation. All rights reserved. No part of this publication may be reproduced or distributed without written permission, except for brief quotations with attribution."}, {"t": "p", "s": "Scope. This paper is economic and policy analysis. It is not legal, investment or compliance advice and does not suggest any way to evade sanctions or export controls. Any reader acting on Russia-related business must comply with all applicable sanctions laws, in every jurisdiction that applies to them, and take qualified advice."}, {"t": "p", "s": "Scenarios in the outlook chapter are illustrative and hypothetical. They are not forecasts."}, {"t": "p", "s": "Trademarks and organization names belong to their respective owners. Citation of a source does not imply that its publisher endorses this paper or Infinitum Corporation."}, {"t": "props", "items": [{"label": "Contact", "value": "Infinitum Corporation, Washington, DC, 1629 K Street NW, Suite 300"}, {"label": "Website", "value": "https://www.theinfinitumcorporation.com"}, {"label": "Email", "value": "info@theinfinitumcorporation.com"}, {"label": "Telegram", "value": "https://t.me/infinitumcorporation"}, {"label": "X", "value": "https://x.com/infinitumceo"}]}], "subs": []},
// @@APPEND@@
];

const TOC = [{"label": "About this paper", "id": "about-this-paper"}, {"label": "Executive summary", "id": "executive-summary"}, {"label": "The problem: a consensus that keeps being wrong", "id": "the-problem-a-consensus-that-keeps-being-wrong"}, {"label": "From Yeltsin's Wild 90s to Putin's Order", "id": "from-yeltsin-s-wild-90s-to-putin-s-order"}, {"label": "The model: what \"state-influenced capitalism\" actually is", "id": "the-model-what-state-influenced-capitalism-actually-is"}, {"label": "Sanctions: the largest experiment in economic pressure, and what it produced", "id": "sanctions-the-largest-experiment-in-economic-pressure-and-what-it-produced"}, {"label": "The economy through the war years: the numbers behind \"it should have collapsed\"", "id": "the-economy-through-the-war-years-the-numbers-behind-it-should-have-collapsed"}, {"label": "Safety on the streets: what the data say, and what they do not", "id": "safety-on-the-streets-what-the-data-say-and-what-they-do-not"}, {"label": "Leadership: what a stable center changed", "id": "leadership-what-a-stable-center-changed"}, {"label": "Why the model endures", "id": "why-the-model-endures"}, {"label": "Against its peers: where Russia leads, where it trails", "id": "against-its-peers-where-russia-leads-where-it-trails"}, {"label": "Ten claims, ten checks", "id": "ten-claims-ten-checks"}, {"label": "What the critics get right, and why the thesis still stands", "id": "what-the-critics-get-right-and-why-the-thesis-still-stands"}, {"label": "Outlook: three scenarios and the indicators that tell them apart", "id": "outlook-three-scenarios-and-the-indicators-that-tell-them-apart"}, {"label": "Recommendations: acting on an accurate picture", "id": "recommendations-acting-on-an-accurate-picture"}, {"label": "Method note: how the numbers were gathered", "id": "method-note-how-the-numbers-were-gathered"}, {"label": "Conclusion: the fact that cannot be sanctioned away", "id": "conclusion-the-fact-that-cannot-be-sanctioned-away"}, {"label": "About Infinitum Corporation", "id": "about-infinitum-corporation"}, {"label": "References", "id": "references"}, {"label": "Glossary", "id": "glossary"}];

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
      title="Russia's State-Influenced Capitalism: Sanctions-Proof, War-Proof, and Chaos-Proof"
      summary="A Model the West Loves to Hate. Infinitum Corporation Special Edition 01, by William Aaron Turner, October 2026. This paper presents the author's argued position. Figures are attributed to the sources cited."
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
