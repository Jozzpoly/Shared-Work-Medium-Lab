# Open Substrate — unpredicted forms campaign

**Date:** 2026-10-04  
**Status:** controlled implementation / falsification campaign  
**Base:** Quiet Presence branch head `fbfe3d6bdc224ee5517f6def85a85626681364b3`  
**Isolation:** separate from Quiet Presence ecological incubation, Codex PR #6, and MP-1

## Dla Ownera

Ta kampania nie buduje „nowej wersji Medium” według z góry ustalonego projektu.

Sprawdza coś bardziej podstawowego:

> **czy Medium potrafi przyjąć nową formę, relację albo sposób użycia, którego jego twórcy nie przewidzieli — bez przebudowy fundamentów i bez utraty źródeł, własności, prawdy oraz czytelności?**

Interfejsy i powierzchnie projektowane głównie dla Ownera mają domyślnie używać języka polskiego i progressive disclosure: najpierw sens, stan i powód obecności rzeczy; techniczne szczegóły dopiero głębiej.

Powierzchnie i metadata przeznaczone głównie dla agentów mogą pozostać po angielsku, jeżeli zwiększa to jednoznaczność i kompozycyjność.

Oryginalne źródła zachowują swój język. Tłumaczenie jest widokiem/interpretacją, nie zamiennikiem source truth.

## Primary question

Can the substrate accept **unanticipated local forms and relations** while preserving a small set of truth/agency invariants, without requiring the core to learn every new kind in advance?

The campaign should falsify the current implementation before proposing a broad architecture.

## Why this is separate from Quiet Presence

Quiet Presence is currently in stewardship + ecological incubation. Its strongest desired evidence is independent instrumental use during real work.

This campaign is controlled apparatus work. It is allowed to deliberately create adversarial specimens.

Therefore:

- do not count campaign specimens as ecological adoption;
- do not add campaign-only artifacts/doors to the live Quiet Presence field merely to create activity;
- do not modify PR #6's Codex-owned window body in parallel;
- do not merge/rebase PR #5 or #6 for campaign neatness.

## Working hypothesis

A robust Medium may need a **thin waist**:

A small substrate protects identity, scope/ownership, provenance/source access, addressability, preservation boundaries, and safe capability boundaries.

Above that waist, inhabitants should be able to invent forms, bodies, relations, local traces and views before the platform has standardized them.

Specialized rendering should be an enhancement. Unknown-but-valid things should degrade to a useful generic representation rather than becoming invalid.

### Core formulation

> **Validate invariants, not imagination.**

Unknown is not automatically invalid.

## Invariants under test

These are hypotheses to test, not a frozen constitution.

1. **Identity remains stable.** A thing can be referenced without its meaning being globally frozen.
2. **Source/provenance stays reachable.** Interpretation never silently replaces source truth.
3. **Ownership/scope stays explicit.** A participant/place can add local meaning without rewriting another participant's object.
4. **Unknown form is representable.** The substrate can preserve and expose a form it does not semantically understand.
5. **Generic fallback exists.** A missing specialized renderer does not make a valid object disappear.
6. **Representation openness is not capability openness.** Arbitrary content may be represented without arbitrary executable privileges.
7. **Preservation is distinct from surfacing.** Historical traces may remain recoverable without remaining permanently prominent.
8. **Views are derived.** Owner/agent views may differ without creating two competing truths.
9. **Local meaning is not global ranking.** No popularity/importance score is required for a thing to migrate between contexts.
10. **Old known forms still work.** Openness must not break current Quiet Presence behavior.

## Explicit anti-goals

This campaign is **not** permission to build:

- a universal ontology;
- a generalized plugin marketplace;
- semantic search/recommendation before real scale pressure exists;
- a global `used_by` graph;
- expertise scores or agent reputation tables;
- a feed, inbox, unread system or attention ranking;
- a standardized Exchange Window primitive;
- a final multi-agent architecture;
- an automatic claim that any mechanical PASS improves real agent capability.

## Test dimensions

The campaign should eventually pressure at least these dimensions:

### A. Representation extensibility
Unknown `kind`, unknown fields, optional metadata, and future extension fields.

### B. Relation extensibility
A participant/place should be able to invent a relation the core does not know without mutating the referenced object.

### C. Body extensibility
Text, HTML, JSON and future bodies should remain preservable/addressable. The substrate should not need to understand every body internally.

### D. Capability boundary
Passive/unknown bodies should be permissive. Executable or privileged behaviors require an explicit safety/capability boundary rather than implicit trust.

### E. Owner / agent views
One underlying object should support:
- an Owner-facing Polish view optimized for meaning, provenance, state and voluntary depth;
- an agent-facing technical view optimized for exact identity, fields, links and machine legibility.

### F. Language/provenance
Original language remains source truth. Translation or gloss is an attributed view.

### G. Backwards compatibility
Existing place/door/artifact/episode/source/perspective specimens still render and verify.

### H. Epistemic path dependence
The substrate must be able to preserve both useful trails and scoped negative/dead-end traces without turning history into global authority.

### I. Staleness
A locally useful interpretation can stop being surfaced while remaining recoverable and attributable.

### J. Second-form test
A fix that only special-cases specimen #1 is a failure. A materially different second unknown form must pass without another core-type branch.

## Campaign sequence

The sequence is deliberately evidence-led. It may change when a stage falsifies assumptions.

### Phase 0 — baseline characterization
Precisely demonstrate where the current renderer/verifier reject or erase unanticipated forms. Preserve the failures.

### Phase 1 — passive unknown organism
Introduce a deliberately unknown passive form with:
- stable identity;
- arbitrary extra fields;
- its own body;
- exact source;
- participant/local context;
- Polish Owner-facing explanation;
- English agent-facing metadata.

Do **not** teach core a bespoke renderer for its kind.

### Phase 2 — unknown relation / local appropriation
Allow a place or participant to leave a relation/trace whose semantics are not core-defined. Verify that the target object is not rewritten.

### Phase 3 — generic fallback
Create the smallest substrate change that makes unknown-but-valid forms enterable and inspectable while preserving known specialized views.

### Phase 4 — active-body boundary
Pressure the difference between preserving arbitrary bodies and granting executable capabilities. Prefer explicit sandbox/capability declaration over a closed content taxonomy.

### Phase 5 — adversarial second organism
Create a structurally different unknown form. If another type-specific patch is needed, the campaign has not demonstrated generality.

### Phase 6 — Owner experience
Walk the same specimens as Owner: Polish by default, clear status/provenance, voluntary depth, no technical wall at entry. Owner judgement can veto a machine PASS.

### Phase 7 — external critique
Only after a real implementation/evidence seam exists, bring Codex back as an independent collaborator/falsifier rather than asking him to approve the theory.

## Evidence classes

Keep these separate:

- **mechanical evidence** — parser/renderer/verifier/tests behave as specified;
- **interaction evidence** — an Owner/agent can actually enter, understand and traverse the thing;
- **architectural evidence** — a second materially different form works without another special case;
- **ecological evidence** — independent real work discovers and uses the medium instrumentally.

This campaign can directly establish the first three. It cannot manufacture the fourth.

## Per-turn campaign protocol

When the Owner says `kontynuuj` during this campaign:

1. recover the live branch/head and campaign state from repository evidence;
2. inspect any work/tests completed since the previous turn;
3. identify the highest-value unresolved falsifier or implementation seam;
4. execute the next reversible step far enough to produce evidence;
5. test it;
6. update the durable campaign state with what changed, what is demonstrated, what failed, and the next frontier;
7. do not stop merely because one local test passes if the current phase is not actually resolved.

The Owner should not need to restate the plan on every turn.

## Stop / reconsider conditions

Stop implementation and reassess if:

- supporting one specimen starts requiring a broad universal schema;
- the campaign begins modifying Quiet Presence merely to show progress;
- Owner-facing clarity is sacrificed for machine elegance;
- unknown content is accepted only by giving it unsafe capabilities;
- a proposed abstraction has no pressure beyond the campaign's artificial specimen;
- changes become difficult to reverse or contaminate PR #5/#6;
- tests prove only that the test was encoded into the implementation.

## Current frontier

The current Quiet Presence renderer/verifier already contains type-specific branches and rejects unsupported `target_kind` values.

The next step is **Phase 0**: characterize those closure points precisely, then design the first adversarial specimen *before* changing substrate behavior.
