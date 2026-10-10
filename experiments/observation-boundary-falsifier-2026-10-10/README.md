# Medium / Cloudflare: observation boundary falsifier (2026-10-10)

**Status: bounded, isolated regression experiment — no deployment, no new architecture, no Owner product PASS.**

## Why this exists

The old Cloudflare gateway caches a *derived interpretation* of project sources. Before comparing Cloudflare with GitHub-native alternatives, test whether the interpretation remains accurate when the project entry document evolves. Faster transport of the wrong "current" project state is negative value.

**Pinned evidence:**
- Current canonical source at audit time: [RESEARCH_STATE.md @ cff9839](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/cff9839c1ac33189c23d93a399f17b44e8f219a0/docs/RESEARCH_STATE.md), blob `ee457f2951d9014f05e0f9fb944d93ab574cebc8`.
- Historical [gateway source](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/4ee5c9c6f31d216de7e9bd0af0d507a21c863038/experiments/semantic-medium-v0/cloudflare-observation-gateway/src/index.js) and [design/readme](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/4ee5c9c6f31d216de7e9bd0af0d507a21c863038/experiments/semantic-medium-v0/cloudflare-observation-gateway/README.md).
- Live source was independently read with the connected GitHub tool; the four negative controls were checked against its **pinned content**. The Node test syntax/runner was separately exercised against a small local fixture. Full-checkout qualification was subsequently completed in [GitHub Actions run #38015268165](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/actions/runs/38015268165): Node 22.23.3, eight tests passed, and two read-only views generated from the actual checked-out Medium document (52 navigational headings).

## Actual negative findings

1. The v0 parser searches for an exact `## Current frontier` heading. The current canonical document uses `## Frontier topology refresh`. Result: `frontier: unknown`, despite current frontier information and PR links existing in the source.
2. Its top-level `Status:` extraction omits the explicit **Owner-observed FAIL / not accepted** product verdict elsewhere in the current file.
3. The heading-dependent link projection drops currently available first-party entry links.
4. A newly appended historical `## Current frontier` section would instead be silently promoted as a current frontier (controlled adversarial injection, **not** an observed live repository incident).

These are defects/risks in a **historical undeployed gateway**, not claims that Cloudflare itself is broken. No production bug is implied.

## Run

From repository root: `node --test experiments/observation-boundary-falsifier-2026-10-10/observation.test.mjs`.

The tests are intentionally **negative controls** for the *old* parser. They may need requalification if the canonical document changes; do not silently modify fixtures to keep a green result. If they fail, inspect the new source and pinned historical behavior.

## Minimal observation contract under consideration

Separate:
- **Source receipt:** original URL, exact version where established, observation time and coverage/permissions.
- **Mechanical projection:** links, heading/navigation structure and inspected versions, without manufacturing product judgements.
- **Interpretation:** typed, provenance-backed claims with explicit uncertainty; Owner verdict must not be overwritten by mechanical status.
- **Representations:** HTML and JSON should derive from the *same acquired observation*, not two independently refreshed requests that merely share a nominal schema.

A content SHA-256 is an integrity digest of acquired bytes, **not** proof of a Git commit identity or of freshness.

## First native-source baseline (bounded)

Using the connected GitHub tools against pinned main `cff9839`, a directed retrieval of `START_HERE.md` lines 1–34, `RESEARCH_STATE.md` lines 1–65 and the live open-PR listing took **three source operations**. It recovered the explicit Owner FAIL, the current frontier, and draft PRs #5/#17 (plus this draft #22). The two textual read responses contained ~3.3 KB and ~10.6 KB respectively. The source revision and explicit PR HEADs were separately identified.

**Scope:** this shows GitHub-native retrieval is adequate for one small, prompted orientation task. It is NOT a clean independent agent run, a latency/token experiment, a matched A/B against the gateway, or evidence that Cloudflare is unnecessary for more complex shared observations. In particular, the PR list is a moving response while the file reads were pinned; **they are not a single atomic snapshot**.

## Executable A candidate: no Cloudflare

`native-baseline.mjs` makes **one local source read**, then emits semantic navigation in `index.html` and `observation.json` from the same byte-digested observation. It does not infer current project claims, certify source freshness or host itself. The source URL remains moving (`main`) and its Git revision is **explicitly unverified**; the SHA-256 is only a content digest.

From the root of a full checkout:

- `node --test experiments/observation-boundary-falsifier-2026-10-10/*.test.mjs`
- `node experiments/observation-boundary-falsifier-2026-10-10/native-baseline.mjs <output-directory>`

**Execution evidence:** a stand-in local copy on Node 22 generated both representations and passed eight smoke/negative-control tests against a deliberately small synthetic `RESEARCH_STATE.md` fixture. Four historical-parser checks were also independently evaluated against the pinned real source using the connected GitHub reader. The exact remotely committed Node files **were qualified against the full repository checkout** in [GitHub Actions #38015268165](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/actions/runs/38015268165): 8/8 PASS and a 52-heading HTML/JSON navigation generation. No Cloudflare deployment, real-browser UX qualification or agent capability-lift test has occurred.

This candidate is deliberately limited: it will go stale until regenerated, covers one public source only, and creates a link/index rather than a useful World or For me experience. Its purpose is to give Cloudflare a **working, cheap comparator**, not become Medium by momentum.

## Next real decision: does Cloudflare earn a role?

Run a bounded A/B for the same real source change:
- **A:** native GitHub direct read, or a GitHub Actions-generated static snapshot when appropriate;
- **B:** a small versioned Cloudflare Worker projection, only if A exposes material pressure.

Compare: correct orientation and Owner boundary, source calls, provenance coverage, stale/unknown honesty, time-to-useful-action and Owner interventions. Keep both conditions scoped to the same permissions and source revisions. A successful cache hit is *not* an agent capability gain.

**Stop conditions:** A suffices; B loses current truth; B adds Owner maintenance; privacy boundaries cannot be enforced; the experiment becomes a central database/notification/workflow project.

## Resume checkpoint

On the next `kontynuuj`: recover the current `START_HERE.md` and the head of `docs/RESEARCH_STATE.md`, plus active PR #5/#17 only if relevant. Confirm this experiment's pinned evidence still means what it claims. Next useful work is the **GitHub-native baseline and comparator design**, not deploying Durable Objects or MCP. Keep all work on this isolated branch until it proves real value. Do not write a second continuity charter: main already contains the Browser long-run checkpoint.
