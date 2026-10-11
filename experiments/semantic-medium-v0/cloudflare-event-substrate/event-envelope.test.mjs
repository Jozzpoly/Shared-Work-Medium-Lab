// Source-equivalent contract tests with an in-memory SQL mock.
// NOT a Cloudflare Durable Object runtime, storage durability or HTTP deployment test.
import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { runInNewContext } from "node:vm";
import { createHmac, webcrypto } from "node:crypto";

const raw = readFileSync(new URL("./src/index.js", import.meta.url), "utf8");
const transformed = raw
  .replace('import { DurableObject } from "cloudflare:workers";', "")
  .replace("export class ProjectEventLog", "class ProjectEventLog")
  .replace("export default {", "const entry = {");
assert.notEqual(raw, transformed);
const scope = {
  DurableObject: class { constructor() {} },
  crypto: webcrypto, TextEncoder, Uint8Array, Headers, Request, Response, URL,
  Number, JSON, Date, Map, console,
};
runInNewContext(transformed + "\nthis.exports = { entry, ProjectEventLog };", scope);
const { entry, ProjectEventLog } = scope.exports;

class FakeSQL {
  rows = [];
  exec(query, ...values) {
    if (/CREATE TABLE|CREATE INDEX/.test(query)) return {};
    if (query.includes("INSERT OR IGNORE INTO events")) {
      const [delivery_id, github_event, action, received_at, target_url, actor_login, payload_sha256] = values;
      if (!this.rows.some(row => row.delivery_id === delivery_id)) {
        this.rows.push({
          seq: this.rows.length + 1, delivery_id, github_event, action, received_at,
          target_url, actor_login, payload_sha256
        });
      }
      return {};
    }
    if (query.includes("SELECT seq, payload_sha256 FROM events WHERE delivery_id")) {
      return { one: () => this.rows.find(row => row.delivery_id === values[0]) ?? null };
    }
    if (query.includes("FROM events") && query.includes("WHERE seq >")) {
      return { toArray: () => this.rows.filter(row => row.seq > values[0]).slice(0, values[1]) };
    }
    if (query.includes("SELECT COUNT(*)")) {
      return { one: () => ({ count: this.rows.length, latest_cursor: this.rows.at(-1)?.seq ?? null }) };
    }
    throw Error("Test SQL mock does not implement query: " + query.trim().slice(0, 70));
  }
}

const secret = "test-only-key-do-not-deploy";
const project = "Jozzpoly/Shared-Work-Medium-Lab";
function fixture() {
  const sql = new FakeSQL();
  const durableObject = new ProjectEventLog({ storage: { sql } }, {});
  const env = {
    GITHUB_WEBHOOK_SECRET: secret,
    PROJECT_EVENTS: {
      getByName(name) { assert.equal(name, project); return durableObject; }
    }
  };
  async function deliver(payload, id = "delivery-001", options = {}) {
    const body = JSON.stringify(payload);
    const digest = createHmac("sha256", secret).update(body).digest("hex");
    const request = new Request("https://example.invalid/github/webhook", {
      method: "POST", body, headers: {
        "X-Hub-Signature-256": options.invalidSignature ? "sha256:" + "0".repeat(64) : "sha256=" + digest,
        "X-GitHub-Delivery": id,
        "X-GitHub-Event": "issues"
      }
    });
    return entry.fetch(request, env);
  }
  const good = {
    repository: { full_name: project, html_url: "https://github.com/" + project },
    sender: { login: "research-bot" }, action: "opened"
  };
  async function get(path) {
    const response = await entry.fetch(new Request("https://example.invalid" + path), env);
    return { status: response.status, body: await response.json() };
  }
  return { sql, env, deliver, good, get };
}

test("legitimate signed event yields one event and durable cursor API shape", async () => {
  const f = fixture();
  const r = await f.deliver(f.good);
  assert.equal(r.status, 202);
  assert.equal((await r.json()).cursor, 1);
  const batch = await f.get("/events?after=0&limit=50");
  assert.equal(batch.status, 200);
  assert.equal(batch.body.count, 1);
  assert.equal(batch.body.coverage, "verified_webhooks_received_only");
  assert.equal(batch.body.upstream_delivery_completeness, "unverified");
  assert.equal(batch.body.next_cursor, 1);
  assert.equal(batch.body.events[0].target_url, "https://github.com/" + project);
  const empty = await f.get("/events?after=1");
  assert.equal(empty.body.count, 0);
  assert.equal(empty.body.next_cursor, 1);
});

test("a byte-identical redelivery is idempotent", async () => {
  const f = fixture();
  assert.equal((await f.deliver(f.good)).status, 202);
  const duplicate = await f.deliver(f.good);
  assert.equal(duplicate.status, 202);
  assert.equal((await duplicate.json()).cursor, 1);
  assert.equal(f.sql.rows.length, 1);
});

test("a reused delivery ID with different signed payload fails closed", async () => {
  const f = fixture();
  assert.equal((await f.deliver(f.good)).status, 202);
  const conflict = await f.deliver({ ...f.good, action: "closed" });
  assert.equal(conflict.status, 409);
  assert.equal(f.sql.rows.length, 1);
  assert.equal(f.sql.rows[0].action, "opened");
});

test("a correctly signed foreign-repository event cannot contaminate this project", async () => {
  const f = fixture();
  const foreign = { ...f.good, repository: { full_name: "OtherOwner/OtherRepo", html_url: "https://github.com/OtherOwner/OtherRepo" } };
  const r = await f.deliver(foreign);
  assert.equal(r.status, 403);
  assert.equal(f.sql.rows.length, 0);
});

test("invalid signatures cannot create an event", async () => {
  const f = fixture();
  const r = await f.deliver(f.good, "delivery-wrong-sig", { invalidSignature: true });
  assert.equal(r.status, 401);
  assert.equal(f.sql.rows.length, 0);
});

test("oversized webhook envelope is rejected before signature verification", async () => {
  const f = fixture();
  const r = await f.deliver({ ...f.good, note: "X".repeat(131073) }, "delivery-big");
  assert.equal(r.status, 413);
  assert.equal(f.sql.rows.length, 0);
});

test("empty or nonempty log never claims globally complete GitHub history", async () => {
  const f = fixture();
  const before = await f.get("/status");
  assert.equal(before.body.stored_events, 0);
  assert.equal(before.body.upstream_delivery_completeness, "unverified");
  await f.deliver(f.good);
  const after = await f.get("/status");
  assert.equal(after.body.stored_events, 1);
  assert.equal(after.body.coverage, "verified_webhooks_received_only");
  assert.equal(after.body.upstream_delivery_completeness, "unverified");
});

test("cursor log still exists after re-instantiation with the same mock SQL", async () => {
  const f = fixture();
  await f.deliver(f.good);
  const another = new ProjectEventLog({ storage: { sql: f.sql } }, {});
  assert.equal(another.eventsAfter(0, 50).events.length, 1);
  assert.equal(another.status().latest_cursor, 1);
});
