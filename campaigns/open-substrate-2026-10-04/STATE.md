# Open Substrate — live campaign state

**Updated:** 2026-10-04  
**Branch:** `campaign/open-substrate-2026-10-04`  
**Base specimen:** Quiet Presence `fbfe3d6bdc224ee5517f6def85a85626681364b3`  
**Evidence through:** `de1bbaf85e6b905ab7af9c1aaebe259f285c1e07`

## Current phase

**Phase 0 — baseline characterization and invariant audit: materially complete.**

No production substrate behavior has been changed yet.

The branch now contains:

- campaign contract in `README.md`;
- behavioral probe in `baseline_probe.py`;
- preserved baseline output in `baseline.json`;
- ontology-vs-invariant audit in `PHASE0_AUDIT.md`;
- dedicated Actions workflow `.github/workflows/open-substrate.yml`.

## First CI evidence

Actions run `37219836032` at head `89131cfa2689c5ba3a71cb11bb02d26c842a8662` completed **success**.

It established two things simultaneously:

1. current known Quiet Presence still renders/verifies with PASS;
2. the Open Substrate probe can reproduce current closure without modifying the live specimen.

Exact baseline observations:

- unknown standalone object family: render succeeds but the object is **silently not discovered**;
- unknown local relation target: render fails with `unsupported target_kind organism`;
- unknown participant perspective target: render fails with `unsupported target_kind organism`;
- unknown field on a known object: survives in source JSON but is absent from the generated view;
- current Owner surface: `<html lang="en">`, English `Enter this place`, no Polish entry label.

These are characterization results, not yet product failures.

## Phase 0 audit conclusion

The current implementation mixes three different categories:

### Candidate invariants worth protecting

- stable identity / resolvable references;
- reachable source/provenance;
- participant/local interpretation must not silently become shared truth;
- local adoption should not require rewriting shared object identity;
- declared revision-bound evidence should actually be revision-bound;
- generated internal links should resolve;
- body paths/content integrity should remain bounded and verifiable;
- representation openness must remain separate from executable/privileged capability.

### Quiet Presence campaign laws

- place-only quiet root;
- no global attention/relevance ranking;
- deep trace not leaking into root;
- specific no-notification posture.

These remain regression laws for Quiet Presence but are not automatically universal Medium laws.

### Ontology closure to challenge

- fixed discovery directories as the only discoverable object families;
- closed `target_kind` dispatch;
- participant perspectives limited to two target families;
- fixed page-count formula based on known families;
- specialized renderer being required for existence;
- one English-first view serving both Owner and agents.

## Capability boundary

Current repository code has no general explicit sandbox/capability model for arbitrary active bodies.

The known body mechanism copies body files into generated output and links to them.

Do not infer a universal safe execution model from this.

**Specimen #1 must remain passive.**

Active-body execution is a later dedicated phase with runtime/browser evidence.

## Campaign vetoes remain active

Do not:

- modify Quiet Presence merely to create campaign activity;
- modify Codex PR #6/body in parallel;
- count artificial specimens as ecological adoption;
- add semantic search/recommendation before scale pressure;
- solve specimen #1 by hard-coding its kind;
- introduce a universal schema before evidence requires one;
- trade Owner-facing clarity for machine elegance.

## Next frontier — Specimen #1

The next step is **not yet substrate refactoring**.

Create a deliberately foreign passive fixture outside live Quiet Presence ecology.

It must pressure:

- unknown kind/family;
- stable identity;
- unknown nested metadata;
- own passive body;
- exact source/provenance;
- one unknown local relation;
- one participant-owned interpretation;
- Polish Owner-facing explanation;
- English agent-facing technical metadata;
- original-language source preserved;
- no executable capability.

Before production behavior changes, define exact assertions for what current substrate does with this fixture and what Phase 1 must change.

## Phase 1 target

After the smallest justified substrate change:

- specimen #1 is discoverable and enterable;
- no specimen-specific type branch exists;
- existing Quiet Presence still passes unchanged;
- unknown metadata is preserved and inspectable;
- local relation does not rewrite target identity;
- source/provenance remains direct;
- Owner can understand the thing in Polish without a technical wall;
- agent can inspect exact technical/raw metadata;
- original source is not replaced by translation;
- no new executable privilege is granted.

A later **materially different specimen #2** must pass without another core-type patch before any generality claim.

## Coordination

- PR #5: untouched by this campaign, draft/unmerged.
- PR #6: untouched by this campaign, draft/unmerged.
- Browser already left Codex the narrow 4-vs-6 seam.
- Return to Codex after implementation evidence exists that he can independently attack.

## Continue protocol

When Owner says `kontynuuj`:

1. recover this branch's live head and this state;
2. inspect CI/evidence since the last checkpoint;
3. continue the current unresolved phase rather than restarting design;
4. execute reversible work to evidence;
5. update this state before stopping at a meaningful boundary.

The next `kontynuuj` should start by designing and materializing **Specimen #1**, then building its assertion harness before changing substrate behavior.
