#!/usr/bin/env node
// swm-state.mjs v0 (Claude draft, 2026-10-08) — no dependencies.
// Anchors a project state to a commit SHA and builds a verdict registry from test output.
// Usage (from repo root):
//   node swm-state.mjs --out STATE_AS_OF.json            # runs `npx vitest run`
//   node swm-state.mjs --log vitest.log --out STATE_AS_OF.json   # parse an existing log
// It states what it can verify and what it cannot. It never calls the network.
import { spawnSync } from 'node:child_process';
import { readFileSync, writeFileSync, readdirSync, existsSync } from 'node:fs';
import { createHash } from 'node:crypto';

const arg = (k) => { const i = process.argv.indexOf(k); return i > -1 ? process.argv[i + 1] : null; };
const sh = (c, a) => spawnSync(c, a, { encoding: 'utf8', shell: process.platform === 'win32', maxBuffer: 1 << 28 });
const git = (...a) => (sh('git', a).stdout || '').trim();

const head = git('rev-parse', 'HEAD');
const branch = git('rev-parse', '--abbrev-ref', 'HEAD');
const remote = git('config', '--get', 'remote.origin.url');
const logFile = arg('--log');
const raw = logFile ? readFileSync(logFile, 'utf8') : (() => { const r = sh('npx', ['vitest', 'run']); return (r.stdout || '') + (r.stderr || ''); })();
const log = raw.replace(/\x1b\[[0-9;]*m/g, '');

const num = (re) => { const m = log.match(re); return m ? Number(m[1]) : null; };
const tests = {
  files_passed: num(/Test Files\s+(?:\d+ failed \| )?(\d+) passed/), files_failed: num(/Test Files\s+(\d+) failed/) ?? 0,
  tests_passed: num(/Tests\s+(?:\d+ failed \| )?(\d+) passed/), tests_failed: num(/Tests\s+(\d+) failed/) ?? 0,
};

// 1) Verdict registry: every `<TAG>_RESULT {json}` line the tests print.
const registry = [];
for (const line of log.split('\n')) {
  const m = line.match(/^\s*([A-Za-z0-9_]+_RESULT)\s+(\{.*\})\s*$/);
  if (!m) continue;
  let d; try { d = JSON.parse(m[2]); } catch { registry.push({ tag: m[1], kind: 'unparseable' }); continue; }
  const outcome = typeof d.outcome === 'string' ? d.outcome : null;
  registry.push(outcome
    ? { tag: m[1], kind: 'verdict', outcome, first_reason: (d.reasons || [])[0] || null }
    : { tag: m[1], kind: 'measurement-only', fields: Object.keys(d).length });
}

// 2) Non-gating tests: assertions that accept PASS and FAIL alike (green CI cannot tell them apart).
const non_gating = [];
if (existsSync('tests')) for (const f of readdirSync('tests')) {
  const src = readFileSync(`tests/${f}`, 'utf8');
  if (/expect\(\[\s*['"]PASS['"]\s*,\s*['"]FAIL['"]/.test(src)) non_gating.push(`tests/${f}`);
}

// 3) Verdict language in commit subjects (claims, not proofs).
const claims = git('log', '-150', '--format=%h\t%cI\t%s').split('\n').map((l) => l.split('\t'))
  .filter(([, , s]) => /^(MEDIUM-|docs: close|medium: (record|persist|promote))/.test(s || '') && /(PASS|FAIL|partial)/i.test(s || ''))
  .map(([sha, at, subject]) => ({ sha, at, subject }));

const state = {
  schema: 'swm-state/v0',
  anchor: { remote, branch, head, head_time: git('log', '-1', '--format=%cI'), generated_at: new Date().toISOString() },
  freshness: {
    rule: 'This file is NOT self-validating. It is current only while the remote branch head equals anchor.head.',
    verify: `git ls-remote ${remote} refs/heads/${branch}   # first column must equal anchor.head`,
  },
  tests: { ...tests, log_sha256: createHash('sha256').update(raw).digest('hex') },
  verdict_registry: registry,
  gaps: {
    measurement_only_tags: registry.filter((r) => r.kind === 'measurement-only').map((r) => r.tag),
    non_gating_tests: non_gating,
    note: 'measurement-only: the test prints data, the verdict lives in assertions/docs. non-gating: CI is green whatever the outcome. Some verdicts are Owner/browser judgements and cannot be derived from tests at all.',
  },
  commit_verdict_claims: claims,
};
const out = arg('--out');
if (out) writeFileSync(out, JSON.stringify(state, null, 2) + '\n');
console.log(`head ${head.slice(0, 7)} | tests ${tests.tests_passed}/${tests.files_passed} files | verdict-lines ${registry.length} (` +
  `${registry.filter((r) => r.kind === 'verdict').length} with outcome, ${state.gaps.measurement_only_tags.length} measurement-only) | non-gating: ${non_gating.length} | claims: ${claims.length}`);
