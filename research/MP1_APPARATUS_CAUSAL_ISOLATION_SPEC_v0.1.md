# MP-1 Apparatus and Causal Isolation Spec v0.1

**Status:** pre-implementation apparatus design

## Central correction

The first confirmatory MP-1 comparison should not be 'bad page versus good page'.

It should isolate semantic machine legibility as cleanly as practical while holding human-visible content constant.

## Pixel-equivalent semantic ablation

Generate paired treatment pages from one canonical world:

### P0 — visual-equivalent non-semantic hypertext

- same visible text;
- same resource ordering;
- same link labels;
- same link destinations;
- same CSS/layout;
- same visual grouping;
- same timestamps displayed to the human;
- same task-relevant facts;
- generic `div` / `span` structure where possible;
- no hidden evaluator content;
- no ARIA semantics beyond what is unavoidable for baseline links/forms.

### P1 — visual-equivalent semantic hypermedia

Keep the visible human page intentionally pixel-equivalent to P0 while replacing structural plumbing with meaningful native semantics where appropriate:

- `main`, `nav`, `section`, `article`;
- heading hierarchy;
- native lists and tables for repeated structures;
- `time` elements;
- explicit labels/descriptions where they restate human-meaningful context;
- source/version links associated with the resource they describe;
- stable resource identity in URLs;
- meaningful landmark names.

Do not add any factual sentence, answer cue, or task-specific relation that is absent from P0.

### Why this matters

A sighted human should perceive effectively the same interface.

A body that relies on accessibility/semantic structure should receive a materially different observation topology.

This creates a direct test of:

> same world + same visible UI + same model + different environmental semantic structure.

If the agent searches, batches, navigates or reasons differently, semantic legibility becomes a plausible causal factor rather than a proxy for prettier UI.

## Required parity checks before any agent run

The generator must fail closed if any Stage-1 parity check fails.

### Fact parity

Compile the canonical world into an evaluator-only normalized fact multiset.

Verify P0 and P1 expose the same allowed factual values.

### Visible text parity

Load both surfaces in the same browser viewport.

Extract rendered visible text in DOM order, normalize whitespace, and require exact equality unless an explicitly registered accessibility-only exception exists.

### Link-target parity

Require the same agent-visible resource URLs and link labels.

### Screenshot parity

Render both treatments under the same viewport/font/environment and compute a pixel/image diff.

Target: exact or near-exact equivalence.

Any intentional visual difference must be preregistered before runs.

### Network parity

Require both treatments to load the same static assets and make no undeclared external network calls.

### Hidden-data scan

Search generated HTML/JS/assets for evaluator-only motif identifiers, ground-truth labels, secret seed fragments, and answer keys.

### Semantic divergence check

Confirm that the intended semantic difference actually exists.

For example:

- P1 AXTree contains named regions/headings/list/table structure expected by the generator;
- P0 does not accidentally recover equivalent structure through browser heuristics;
- neither surface contains task-specific ARIA descriptions.

## Optional sham/segmentation ablation

If P0 vs P1 produces a material difference, a follow-up ablation can distinguish two explanations:

1. meaningful semantics help;
2. any stronger segmentation/grouping helps.

Possible P0.5 treatment:

- same visible UI;
- same DOM depth/count distribution as P1;
- structural containers remain semantically generic;
- no misleading/invalid ARIA roles.

Do **not** create intentionally false accessibility semantics.

The purpose is to match structural complexity, not to deceive assistive technology.

## Body interaction prediction

This experiment intentionally predicts an interaction effect.

### Sighted human

P0 and P1 should be almost indistinguishable visually.

### AXTree browser agent

P1 should expose richer addressable structure and cheaper selective queries.

### DOM-aware agent

P1 may expose stronger structural cues directly.

### Plain text/full-context agent

If markup is stripped before observation, P0 and P1 may become effectively equivalent.

This interaction is informative, not a nuisance.

It tests the relational-affordance hypothesis directly.

## Stage-1 primary comparison

Primary confirmatory pair:

> **P0 visual-equivalent non-semantic hypertext vs P1 visual-equivalent semantic hypermedia**

Do not make flat full-context S0 the primary causal comparison.

S0 remains an ecological baseline because it changes the acquisition model as well as the semantics.

## Stage-1 outcome hierarchy

### Primary mechanistic outcomes

- task correctness on T1/T2;
- exact-source fidelity;
- number of resource acquisitions before correct answer;
- observation bytes/chars/tokens before first material finding;
- redundant resource reads;
- invalid/stale claims.

### Primary generativity outcome

For T3, whether the agent independently constructs a systematic operation over the batchable collection rather than serially inspecting every member.

Operationalize the behavior from observable traces, not hidden reasoning.

Strong evidence includes producing/using a derived shortlist, batch filter, repeated-structure query, comparison table, or equivalent generic transformation that covers multiple resources in one strategy.

### Secondary outcomes

- wall-clock time;
- navigation depth;
- number of turns;
- optional useful discoveries;
- treatment-specific failure modes.

## Predefined behavioral trace labels

Environment/action logs can classify observable moves such as:

- `OPEN_RESOURCE`;
- `FOLLOW_LINK`;
- `QUERY_STRUCTURE`;
- `SEARCH_TEXT`;
- `LIST_COLLECTION`;
- `DERIVE_INDEX`;
- `BATCH_TRANSFORM`;
- `COMPARE_VERSIONS`;
- `VERIFY_SOURCE`;
- `RETURN_TO_PARENT`;
- `REPEAT_READ`;
- `FINAL_CLAIM`.

These labels describe behavior and must not be visible to the agent during the run.

## Shinden-like behavior criterion

A run qualifies as a strong Shinden-like workflow candidate only if:

1. a broad repeated search space exists;
2. the prompt does not prescribe batching/systematic transformation;
3. no dedicated task-specific endpoint solves the target directly;
4. the agent identifies a reusable common structure;
5. it uses that structure to reduce or reorganize the search space;
6. coverage or cost materially improves versus serial inspection;
7. the strategy transfers to the perturbation world without being told the mapping.

## Negative-result interpretations

### P0 ≈ P1

Semantic machine structure may add little for the tested body/task, or the body may already infer enough structure from visible content.

### P1 cheaper but not more capable

Supports efficiency/attention leverage but not strong emergent-capability claims.

### P1 better on directed tasks but worse on T4

Evidence that stronger semantic structure may anchor attention and reduce serendipity.

### P1 worse

Potential semantic overload, adapter mismatch, browser tree pathology, or navigation overhead. Treat as material evidence.

## Apparatus implementation boundary

Stage 1 should require no Cloudflare dynamic substrate unless needed for controlled logging.

Prefer deterministic static treatment generation plus a minimal instrumented local/test server.

Cloudflare Browser Rendering may later be used as an independent projection/parity auditor because it can return screenshot, AXTree, HTML and Markdown from the same rendered page, but it must not be required for the causal treatment itself.

## Apparatus acceptance gate

Before pilots, automatically produce a parity report containing:

```text
world commitment
generator version
P0 hash
P1 hash
visible-text equality
link-set equality
fact-set equality
screenshot diff metric
network-request diff
hidden-data scan
AXTree structural summary P0
AXTree structural summary P1
```

If factual or visible-content parity fails, measured runs are prohibited.