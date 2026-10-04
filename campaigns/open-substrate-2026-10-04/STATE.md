# Open Substrate — live campaign state

**Updated:** 2026-10-04  
**Branch:** `campaign/open-substrate-2026-10-04`  
**Current head at campaign start:** `03ce155ee48d578f9001d2add8c0af7bc4c3a635`  
**Base specimen:** Quiet Presence at `fbfe3d6bdc224ee5517f6def85a85626681364b3`

## Current phase

**Phase 0 — baseline characterization**

No substrate behavior has been changed yet.

The campaign has only established its isolated branch and research contract.

## Already demonstrated from current code

The existing Quiet Presence implementation is intentionally closed in several places:

### Renderer closure

`render.py` branches on known target kinds:

- `episode`
- `artifact`
- `source`

Any other door target kind triggers:

> unsupported target_kind

Participant perspectives are similarly limited to known `artifact` / `episode` targets.

The renderer also builds specialized page sets from fixed directories:

- `places/*/place.json`
- `episodes/*.json`
- `artifacts/*.json`
- `sources/*.json`
- `participants/*/participant.json`

This is valid for the Quiet Presence campaign, but currently acts as an implicit ontology.

### Verifier closure

`verify.py` explicitly treats unknown target kinds as failures.

It also computes the expected page count from the known type sets.

This means an unanticipated form can fail before we learn whether its identity/body/source would otherwise be useful.

### UI closure

Current generated/public surfaces assume English labels and one rendering path.

Owner-facing and agent-facing views are not yet separated.

### Capability boundary is under-specified

Recovered HTML bodies are copied and exposed, but the campaign has not yet defined a general rule separating:

- arbitrary representable content;
- active executable content;
- privileged actions/capabilities.

Do not infer safety or generality from the existing recovered window alone.

## Important non-failures

The following current behaviors are **not** being called mistakes:

- Quiet Presence using specific types for its own controlled specimen;
- specialized rendering for known types;
- validation of its campaign-specific claims;
- Codex's recovered body using a bespoke wrapper.

The research question is whether those local choices have accidentally become a hard platform boundary.

## Phase 0 questions

Before changing code, establish exact answers to:

1. What minimum fields are truly required for an unknown thing to be preserved and entered?
2. Which existing validation rules protect truth/ownership, and which merely encode today's ontology?
3. Can a new object exist without being globally placed?
4. Can a new relation be stored locally without the renderer understanding its semantics?
5. What is the narrowest generic fallback that remains useful to Owner and agents?
6. What must remain immutable/source-bound when a view adds Polish explanation or translation?
7. What does "active body" mean in the actual current hosting model, and where would a capability boundary need to live?
8. Which current Quiet Presence tests must remain unchanged as regression guards?

## First adversarial specimen — requirements, not schema

The first unknown organism must be designed *before* substrate changes.

It should pressure all of these at once:

- a kind unknown to current core;
- stable identity;
- at least one field the core does not know;
- its own body;
- an exact source/provenance link;
- one local relation whose semantic label is also unknown to core;
- one participant-owned interpretation;
- an Owner-facing Polish explanation;
- agent-facing technical metadata;
- source text preserved in its original language;
- no new executable privileges.

The specimen must be useful enough to inspect, but it must remain intentionally artificial so it cannot be mistaken for ecological adoption evidence.

## Baseline expected result

With no substrate changes, the first specimen is expected to **FAIL** current rendering/verification.

That failure is desirable evidence if it is specific and reproducible.

Do not patch the specimen to fit existing kinds.

## Phase 1 acceptance target

After the smallest substrate change:

- the same specimen can be preserved and entered;
- no `elif kind == "<specimen-kind>"` special case exists;
- current known Quiet Presence types still behave as before;
- exact source/provenance remains reachable;
- unknown fields survive round-trip/render derivation;
- local relation does not rewrite the target;
- Owner sees a Polish default explanation without losing access to original source/technical data;
- agent can inspect exact machine-facing metadata;
- no ecological-adoption claim is made.

## Phase 1 falsifiers

Treat any of these as a meaningful FAIL:

- core must add a new hard-coded type branch;
- unknown fields are silently dropped;
- object identity changes between views;
- owner translation replaces original source;
- local relation becomes a central/global placement;
- generic fallback hides provenance or body;
- accepting the object requires granting script/privileged execution;
- existing Quiet Presence regression tests break;
- the "generic" solution only works for specimen #1.

## Next concrete work

1. Create a baseline test fixture for the unknown organism without changing production behavior.
2. Run current renderer/verifier against it and capture the exact failure path(s).
3. Audit which checks are ontology checks versus invariant checks.
4. Only then design the smallest generic-envelope/fallback change.

## Coordination state

- Quiet Presence PR #5 remains draft/unmerged and untouched by this campaign.
- Codex PR #6 remains draft/unmerged and untouched by this campaign.
- Browser has already left Codex one narrow 4-vs-6 clarification seam.
- Do not reopen theory discussion with Codex until this campaign has implementation evidence worth attacking.
