const REPO = "Jozzpoly/Shared-Work-Medium-Lab";
const API = `https://api.github.com/repos/${REPO}`;

function githubHeaders(env) {
  const headers = new Headers({
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2026-03-10",
    "User-Agent": "swm-observation-gateway-v0"
  });

  if (env.GITHUB_TOKEN) {
    headers.set("Authorization", `Bearer ${env.GITHUB_TOKEN}`);
  }

  return headers;
}

async function githubJson(path, env) {
  const response = await fetch(API + path, {
    headers: githubHeaders(env)
  });

  const rate = {
    limit: numberOrNull(response.headers.get("x-ratelimit-limit")),
    remaining: numberOrNull(response.headers.get("x-ratelimit-remaining")),
    used: numberOrNull(response.headers.get("x-ratelimit-used")),
    reset: numberOrNull(response.headers.get("x-ratelimit-reset")),
    resource: response.headers.get("x-ratelimit-resource"),
    etag: response.headers.get("etag")
  };

  const text = await response.text();

  if (!response.ok) {
    const error = new Error(`GitHub ${response.status} for ${path}`);
    error.status = response.status;
    error.rate = rate;
    error.body = text.slice(0, 1000);
    throw error;
  }

  return {
    data: JSON.parse(text),
    rate
  };
}

function numberOrNull(value) {
  if (value == null || value === "") return null;
  const number = Number(value);
  return Number.isFinite(number) ? number : null;
}

function decodeBase64Utf8(value) {
  const binary = atob((value || "").replace(/\s/g, ""));
  const bytes = Uint8Array.from(binary, char => char.charCodeAt(0));
  return new TextDecoder("utf-8").decode(bytes);
}

function stripLightMarkdown(value) {
  return (value || "")
    .replace(/\*\*/g, "")
    .replace(/`/g, "")
    .replace(/^>\s?/gm, "")
    .trim();
}

function parseDeclaredState(markdown) {
  const status = stripLightMarkdown(
    markdown.match(/\*\*Status:\*\*\s*(.+)/i)?.[1]
  ) || "unknown";

  const updated = stripLightMarkdown(
    markdown.match(/\*\*Last material update:\*\*\s*(.+)/i)?.[1]
  ) || "unknown";

  const frontierSection = markdown.split(/\n## Current frontier\s*\n/i)[1] || "";
  const frontierBlock = frontierSection.split(/\n#{2,6}\s+/)[0] || "";
  const frontier = frontierBlock
    .split(/\n+/)
    .map(line => line.replace(/^>\s?/, "").trim())
    .filter(line => line && !line.startsWith("#"))
    .slice(0, 5)
    .join(" ");

  const links = [...frontierBlock.matchAll(/\[[^\]]+\]\((https?:\/\/[^)]+)\)/g)]
    .map(match => match[1]);

  return {
    status,
    last_material_update: updated,
    frontier: stripLightMarkdown(frontier) || "unknown",
    frontier_links: links
  };
}

function minRemaining(parts) {
  const values = parts
    .map(part => part.rate?.remaining)
    .filter(value => Number.isFinite(value));

  return values.length ? Math.min(...values) : null;
}

function chooseTtlSeconds({ authenticated, remaining, limit }) {
  // Conservative public mode: 5 GitHub reads per cache miss.
  // 600s => at most ~30 GitHub reads/hour for a continuously requested cache key.
  let ttl = authenticated ? 60 : 600;

  if (Number.isFinite(remaining) && Number.isFinite(limit) && limit > 0) {
    const fraction = remaining / limit;

    if (remaining <= 5 || fraction <= 0.10) ttl = Math.max(ttl, 1800);
    else if (remaining <= 15 || fraction <= 0.25) ttl = Math.max(ttl, 900);
    else if (remaining <= 30 || fraction <= 0.50) ttl = Math.max(ttl, 600);
  }

  return ttl;
}

async function observeProject(env) {
  const observedAt = new Date().toISOString();

  const [repo, stateFile, issues, pulls, commits] = await Promise.all([
    githubJson("", env),
    githubJson("/contents/docs/RESEARCH_STATE.md?ref=main", env),
    githubJson("/issues?state=open&sort=updated&direction=desc&per_page=8", env),
    githubJson("/pulls?state=open&sort=updated&direction=desc&per_page=8", env),
    githubJson("/commits?per_page=8", env)
  ]);

  const stateMarkdown = decodeBase64Utf8(stateFile.data.content);
  const declared = parseDeclaredState(stateMarkdown);
  const pureIssues = issues.data.filter(item => !item.pull_request);

  const parts = [repo, stateFile, issues, pulls, commits];
  const remaining = minRemaining(parts);
  const limit = parts
    .map(part => part.rate?.limit)
    .find(value => Number.isFinite(value)) ?? null;

  const ttlSeconds = chooseTtlSeconds({
    authenticated: Boolean(env.GITHUB_TOKEN),
    remaining,
    limit
  });

  return {
    schema: "swm.project-observation.v0",
    project: {
      name: REPO,
      source_url: `https://github.com/${REPO}`
    },
    projection: {
      observed_at: observedAt,
      source: "github-rest",
      source_auth: env.GITHUB_TOKEN ? "worker-secret" : "unauthenticated-public",
      recommended_cache_ttl_seconds: ttlSeconds,
      source_budget: {
        limit,
        remaining,
        minimum_remaining_seen: remaining
      }
    },
    declared,
    observed: {
      default_branch: repo.data.default_branch,
      default_branch_pushed_at: repo.data.pushed_at,
      open_issues: pureIssues.map(issue => ({
        number: issue.number,
        title: issue.title,
        url: issue.html_url,
        updated_at: issue.updated_at
      })),
      open_pull_requests: pulls.data.map(pull => ({
        number: pull.number,
        title: pull.title,
        url: pull.html_url,
        updated_at: pull.updated_at,
        draft: Boolean(pull.draft)
      })),
      recent_commits: commits.data.map(commit => ({
        sha: commit.sha,
        title: (commit.commit?.message || "commit").split("\n")[0],
        url: commit.html_url,
        committed_at:
          commit.commit?.committer?.date ||
          commit.commit?.author?.date ||
          null
      }))
    },
    provenance: {
      declared_state: {
        url: stateFile.data.html_url,
        blob_sha: stateFile.data.sha,
        etag: stateFile.rate.etag
      }
    }
  };
}

function wantsJson(request) {
  const accept = request.headers.get("Accept") || "";
  return accept.includes("application/json") && !accept.includes("text/html");
}

function jsonResponse(observation) {
  return new Response(JSON.stringify(observation, null, 2), {
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Vary": "Accept",
      "Cache-Control": `public, max-age=${observation.projection.recommended_cache_ttl_seconds}, stale-while-revalidate=300`,
      "X-SWM-Observed-At": observation.projection.observed_at,
      "X-SWM-Source-Remaining": String(
        observation.projection.source_budget.remaining ?? "unknown"
      )
    }
  });
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function htmlResponse(observation) {
  const issues = observation.observed.open_issues
    .map(issue => `<li><a href="${escapeHtml(issue.url)}">#${issue.number} — ${escapeHtml(issue.title)}</a> <time datetime="${escapeHtml(issue.updated_at)}">${escapeHtml(issue.updated_at)}</time></li>`)
    .join("");

  const pulls = observation.observed.open_pull_requests
    .map(pull => `<li><a href="${escapeHtml(pull.url)}">#${pull.number} — ${escapeHtml(pull.title)}</a> ${pull.draft ? "<strong>draft</strong>" : ""} <time datetime="${escapeHtml(pull.updated_at)}">${escapeHtml(pull.updated_at)}</time></li>`)
    .join("");

  const commits = observation.observed.recent_commits
    .map(commit => `<li><a href="${escapeHtml(commit.url)}">${escapeHtml(commit.sha.slice(0, 8))} — ${escapeHtml(commit.title)}</a></li>`)
    .join("");

  const body = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Shared Work Medium — cached project observation</title>
</head>
<body>
<main>
  <h1>Shared Work Medium</h1>
  <p>Shared cached project observation generated from live source state.</p>

  <section aria-labelledby="health">
    <h2 id="health">Observation health</h2>
    <dl>
      <dt>Observed at</dt><dd><time datetime="${escapeHtml(observation.projection.observed_at)}">${escapeHtml(observation.projection.observed_at)}</time></dd>
      <dt>Source auth</dt><dd>${escapeHtml(observation.projection.source_auth)}</dd>
      <dt>Source budget remaining</dt><dd>${escapeHtml(observation.projection.source_budget.remaining ?? "unknown")}</dd>
      <dt>Shared cache TTL</dt><dd>${escapeHtml(observation.projection.recommended_cache_ttl_seconds)} seconds</dd>
      <dt>Declared-state source revision</dt>
      <dd><a href="${escapeHtml(observation.provenance.declared_state.url)}">${escapeHtml(observation.provenance.declared_state.blob_sha)}</a></dd>
    </dl>
  </section>

  <section aria-labelledby="declared">
    <h2 id="declared">Declared project interpretation</h2>
    <dl>
      <dt>Status</dt><dd>${escapeHtml(observation.declared.status)}</dd>
      <dt>Current frontier</dt><dd>${escapeHtml(observation.declared.frontier)}</dd>
    </dl>
  </section>

  <section aria-labelledby="issues">
    <h2 id="issues">Open Issues</h2>
    <ul>${issues || "<li>None observed.</li>"}</ul>
  </section>

  <section aria-labelledby="pulls">
    <h2 id="pulls">Open pull requests</h2>
    <ul>${pulls || "<li>None observed.</li>"}</ul>
  </section>

  <section aria-labelledby="commits">
    <h2 id="commits">Recent commits</h2>
    <ol>${commits || "<li>None observed.</li>"}</ol>
  </section>

  <p><a href="https://github.com/${REPO}">Open source repository</a></p>
</main>
</body>
</html>`;

  return new Response(body, {
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Vary": "Accept",
      "Cache-Control": `public, max-age=${observation.projection.recommended_cache_ttl_seconds}, stale-while-revalidate=300`,
      "X-SWM-Observed-At": observation.projection.observed_at,
      "X-SWM-Source-Remaining": String(
        observation.projection.source_budget.remaining ?? "unknown"
      )
    }
  });
}

function errorResponse(error, request) {
  const payload = {
    schema: "swm.project-observation-error.v0",
    state: "degraded",
    observed_at: new Date().toISOString(),
    error: error?.message || "unknown source failure",
    source_status: error?.status ?? null,
    source_budget: error?.rate ?? null
  };

  if (wantsJson(request)) {
    return new Response(JSON.stringify(payload, null, 2), {
      status: 503,
      headers: {
        "Content-Type": "application/json; charset=utf-8",
        "Cache-Control": "public, max-age=30",
        "Vary": "Accept"
      }
    });
  }

  const body = `<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>SWM observation degraded</title></head>
<body>
<main>
  <h1>Project observation degraded</h1>
  <p>The shared observation gateway could not refresh its source state.</p>
  <dl>
    <dt>Observed at</dt><dd>${escapeHtml(payload.observed_at)}</dd>
    <dt>Error</dt><dd>${escapeHtml(payload.error)}</dd>
    <dt>Source status</dt><dd>${escapeHtml(payload.source_status ?? "unknown")}</dd>
  </dl>
  <p>Do not infer current project truth from this failed refresh.</p>
</main>
</body>
</html>`;

  return new Response(body, {
    status: 503,
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "public, max-age=30",
      "Vary": "Accept"
    }
  });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Method not allowed", {
        status: 405,
        headers: { "Allow": "GET, HEAD" }
      });
    }

    if (url.pathname === "/health") {
      return new Response(JSON.stringify({
        service: "swm-observation-gateway-v0",
        state: "running",
        now: new Date().toISOString()
      }, null, 2), {
        headers: {
          "Content-Type": "application/json; charset=utf-8",
          "Cache-Control": "no-store"
        }
      });
    }

    if (url.pathname !== "/" && url.pathname !== "/project") {
      return new Response("Not found", { status: 404 });
    }

    try {
      const observation = await observeProject(env);
      return wantsJson(request)
        ? jsonResponse(observation)
        : htmlResponse(observation);
    } catch (error) {
      return errorResponse(error, request);
    }
  }
};
