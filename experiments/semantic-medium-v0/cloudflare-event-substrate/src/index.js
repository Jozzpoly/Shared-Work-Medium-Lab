import { DurableObject } from "cloudflare:workers";

const PROJECT_NAME = "Jozzpoly/Shared-Work-Medium-Lab";

function hexToBytes(hex) {
  const clean = hex.toLowerCase();
  if (clean.length % 2 !== 0 || !/^[0-9a-f]+$/.test(clean)) return null;
  const bytes = new Uint8Array(clean.length / 2);
  for (let i = 0; i < bytes.length; i++) {
    bytes[i] = Number.parseInt(clean.slice(i * 2, i * 2 + 2), 16);
  }
  return bytes;
}

async function verifyGithubSignature(secret, rawBody, signatureHeader) {
  if (!secret || !signatureHeader?.startsWith("sha256=")) return false;
  const signature = hexToBytes(signatureHeader.slice("sha256=".length));
  if (!signature) return false;

  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["verify"]
  );

  return crypto.subtle.verify(
    "HMAC",
    key,
    signature,
    new TextEncoder().encode(rawBody)
  );
}

async function sha256Hex(value) {
  const digest = await crypto.subtle.digest(
    "SHA-256",
    new TextEncoder().encode(value)
  );
  return [...new Uint8Array(digest)]
    .map(byte => byte.toString(16).padStart(2, "0"))
    .join("");
}

function normalizeWebhook({ deliveryId, eventType, payload, payloadDigest }) {
  return {
    delivery_id: deliveryId,
    github_event: eventType,
    action: payload.action ?? null,
    received_at: new Date().toISOString(),
    target_url:
      payload.issue?.html_url ??
      payload.pull_request?.html_url ??
      payload.repository?.html_url ??
      null,
    actor_login:
      payload.sender?.login ??
      payload.actor?.login ??
      null,
    payload_sha256: payloadDigest
  };
}

export class ProjectEventLog extends DurableObject {
  constructor(ctx, env) {
    super(ctx, env);
    this.sql = ctx.storage.sql;

    this.sql.exec(`
      CREATE TABLE IF NOT EXISTS events (
        seq INTEGER PRIMARY KEY AUTOINCREMENT,
        delivery_id TEXT NOT NULL UNIQUE,
        github_event TEXT NOT NULL,
        action TEXT,
        received_at TEXT NOT NULL,
        target_url TEXT,
        actor_login TEXT,
        payload_sha256 TEXT NOT NULL
      );

      CREATE INDEX IF NOT EXISTS events_received_at_idx
        ON events(received_at);
    `);
  }

  record(event) {
    this.sql.exec(
      `
        INSERT OR IGNORE INTO events (
          delivery_id,
          github_event,
          action,
          received_at,
          target_url,
          actor_login,
          payload_sha256
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
      `,
      event.delivery_id,
      event.github_event,
      event.action,
      event.received_at,
      event.target_url,
      event.actor_login,
      event.payload_sha256
    );

    const row = this.sql.exec(
      "SELECT seq, payload_sha256 FROM events WHERE delivery_id = ?",
      event.delivery_id
    ).one();

    if (row.payload_sha256 !== event.payload_sha256) {
      return { accepted: false, conflict: true, cursor: row.seq };
    }

    return { accepted: true, cursor: row.seq };
  }

  eventsAfter(after = 0, limit = 50) {
    const safeAfter = Number.isFinite(Number(after))
      ? Math.max(0, Number(after))
      : 0;

    const safeLimit = Number.isFinite(Number(limit))
      ? Math.min(100, Math.max(1, Number(limit)))
      : 50;

    const rows = this.sql.exec(
      `
        SELECT
          seq,
          delivery_id,
          github_event,
          action,
          received_at,
          target_url,
          actor_login,
          payload_sha256
        FROM events
        WHERE seq > ?
        ORDER BY seq ASC
        LIMIT ?
      `,
      safeAfter,
      safeLimit
    ).toArray();

    return {
      project: PROJECT_NAME,
      coverage: "verified_webhooks_received_only",
      upstream_delivery_completeness: "unverified",
      after: safeAfter,
      count: rows.length,
      events: rows,
      next_cursor: rows.length
        ? rows[rows.length - 1].seq
        : safeAfter
    };
  }

  status() {
    const row = this.sql.exec(
      "SELECT COUNT(*) AS count, MAX(seq) AS latest_cursor FROM events"
    ).one();

    return {
      project: PROJECT_NAME,
      coverage: "verified_webhooks_received_only",
      upstream_delivery_completeness: "unverified",
      stored_events: Number(row.count ?? 0),
      latest_cursor: Number(row.latest_cursor ?? 0)
    };
  }
}

function json(data, init = {}) {
  const headers = new Headers(init.headers || {});
  headers.set("Content-Type", "application/json; charset=utf-8");
  headers.set("Cache-Control", "no-store");
  return new Response(JSON.stringify(data, null, 2), {
    ...init,
    headers
  });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const stub = env.PROJECT_EVENTS.getByName(PROJECT_NAME);

    if (request.method === "POST" && url.pathname === "/github/webhook") {
      const rawBody = await request.text();
      const signature = request.headers.get("X-Hub-Signature-256");
      const deliveryId = request.headers.get("X-GitHub-Delivery");
      const eventType = request.headers.get("X-GitHub-Event");

      if (!deliveryId || !eventType || deliveryId.length > 128 || !/^[a-z_]{1,64}$/.test(eventType)) {
        return json({ error: "missing GitHub delivery metadata" }, { status: 400 });
      }

      // Bounded post-read envelope check; streaming limits remain a future deployment gate.
      if (new TextEncoder().encode(rawBody).byteLength > 131072) {
        return json({ error: "webhook payload exceeds research envelope" }, { status: 413 });
      }

      const valid = await verifyGithubSignature(
        env.GITHUB_WEBHOOK_SECRET,
        rawBody,
        signature
      );

      if (!valid) {
        return json({ error: "invalid GitHub webhook signature" }, { status: 401 });
      }

      let payload;
      try {
        payload = JSON.parse(rawBody);
      } catch {
        return json({ error: "invalid JSON payload" }, { status: 400 });
      }

      if (payload?.repository?.full_name !== PROJECT_NAME) {
        return json({ error: "webhook repository outside declared project scope" }, { status: 403 });
      }

      const payloadDigest = await sha256Hex(rawBody);
      const event = normalizeWebhook({
        deliveryId,
        eventType,
        payload,
        payloadDigest
      });

      const result = await stub.record(event);
      if (!result.accepted) {
        return json({ error: "delivery ID reused with different payload" }, { status: 409 });
      }

      return json({
        ok: true,
        ...result
      }, { status: 202 });
    }

    if (request.method === "GET" && url.pathname === "/events") {
      const after = Number(url.searchParams.get("after") || 0);
      const limit = Number(url.searchParams.get("limit") || 50);
      return json(await stub.eventsAfter(after, limit));
    }

    if (request.method === "GET" && url.pathname === "/status") {
      return json(await stub.status());
    }

    return json({
      service: "swm-cloudflare-event-substrate-v0",
      routes: {
        webhook: "POST /github/webhook",
        events: "GET /events?after=<cursor>&limit=<1..100>",
        status: "GET /status"
      }
    });
  }
};
