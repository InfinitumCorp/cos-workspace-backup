import { test } from "node:test";
import assert from "node:assert/strict";
import { entityGraph, entity } from "../content/entity";
import { services } from "../content/services";

test("only the official phone appears in the entity graph", () => {
  const json = JSON.stringify(entityGraph());
  assert.ok(json.includes("+1-202-729-9509"));
  for (const bad of ["681-0120", "6810120", "980-9300", "9809300", "614", "wa.me"]) {
    assert.ok(!json.includes(bad), `found ${bad}`);
  }
  assert.equal(entity.address.addressRegion, "DC");
});

test("no California entity references", () => {
  const json = JSON.stringify(entityGraph());
  assert.ok(!/Palo Alto|California|5470106/.test(json));
});

test("service meta descriptions are <= 160 chars and slugs unique", () => {
  const slugs = new Set(services.map((s) => s.slug));
  assert.equal(slugs.size, services.length);
  for (const s of services) assert.ok(s.description.length <= 160, s.slug);
});
