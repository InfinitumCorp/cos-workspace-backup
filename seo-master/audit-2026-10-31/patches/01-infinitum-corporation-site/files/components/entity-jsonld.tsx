import { entityGraph } from "../content/entity";
export function EntityJsonLd() {
  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(entityGraph()) }}
    />
  );
}
