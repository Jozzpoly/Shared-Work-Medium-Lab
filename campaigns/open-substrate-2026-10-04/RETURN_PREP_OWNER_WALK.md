# Return preparation — real Owner / Browser walk

**Date:** 2026-10-04  
**Status:** next-pressure preparation, not implementation  
**Precondition:** Phases 0–4 complete; latest branch run `37223755721` on `730aacfd43138735ac2c01af4bbdd280105daf38` is green.

## Judgement

The next highest-value pressure should be **interaction evidence**, not another representation abstraction.

Phases 0–4 have already produced useful mechanical and architectural evidence:

- unknown passive shared objects can survive generic fallback;
- independently owned records can point to shared identity without moving/mutating it;
- Medium-level relationships are explicit rather than inferred from arbitrary raw data;
- a second radically different shared object passed without another renderer change.

The largest untested claim now concerns the human/agent experience:

> does this actually feel like a clear, quiet, traversable Medium surface rather than generated apparatus?

This matters especially because the Owner explicitly requires:

- Polish where the surface is meant for him;
- progressive disclosure instead of technical walls;
- direct access to source truth;
- freedom to enter/leave without attention pressure;
- no dashboard/feed semantics;
- no artificial narrowing of future agent behavior.

## Why not capability sandbox next

Active execution is important but premature.

Representation openness has only recently stabilized enough to support broader inspection.

Adding capability/sandbox work now would:

- expand security/runtime scope sharply;
- provide weak leverage if the passive surface itself is confusing;
- risk turning the campaign into a platform-engineering project before actual use validates the substrate.

Capability work remains deferred.

## Why not stale-reference machinery next

Staleness/revision binding is a real future pressure.

But current `medium.refs.json` is still an experimental carrier, not a committed protocol.

Building lifecycle machinery around it before real traversal/use would risk hardening the carrier rather than the invariant.

First see what people/agents actually need to understand and revisit.

## Why not semantic discovery/search next

No scale pressure exists.

Adding search/recommendation would contaminate the current question of whether the environment itself has understandable information scent.

Deferred.

## Why not contact Codex immediately

Codex PR #6 remains open/draft on `44c5aaaf1787fa909c9bc4bda53fe5ca3c11e487`.

Browser's last direct comment is still the latest exchange; Codex has not yet replied or changed the branch.

Do not pile a second theoretical request on top of the existing seam.

After the Owner/Browser walk produces concrete UX or substrate findings, Codex can be invited to attack a real object rather than approve a theory.

## Proposed next phase — Interaction Walk

This phase should be evidence-first and deliberately small.

### Step 1 — make the Open Substrate derived surface actually reachable

Create the smallest isolated preview mechanism that exposes the deterministic generated `site/` for this campaign.

Constraints:

- do not publish it as the canonical Medium;
- do not modify Quiet Presence public ecology;
- do not merge PR #5/#6;
- do not add search/feed/navigation features merely to make the preview look complete;
- keep generated output clearly labeled as controlled Open Substrate apparatus;
- preserve raw/source links.

Prefer a reversible branch/static preview over a new service.

### Step 2 — Browser self-walk before Owner attention

Browser should traverse the preview as an ordinary visitor, not by reading JSON first.

Minimum path:

1. enter the Open Substrate root;
2. understand what kind of place this is without campaign archaeology;
3. enter Specimen #1;
4. distinguish shared thing from local/participant interpretations;
5. reach body and exact source;
6. reach technical/raw view voluntarily;
7. return without losing orientation;
8. enter the minimal Specimen #4;
9. verify that absence of metadata looks honest rather than broken;
10. inspect mobile/narrow layout if practical.

Record actual friction before modifying anything.

### Step 3 — agent-facing inspection

From the same underlying packages, test whether a Browser agent can recover:

- stable ids;
- raw metadata;
- explicit reference sidecars;
- exact source/body;
- ownership/scope of independent records;

without needing to parse the Owner prose as the authoritative machine surface.

This should not require a second competing truth.

### Step 4 — only fix observed friction

No speculative polish.

Each change should have:

- observed interaction problem;
- smallest reversible fix;
- regression evidence.

### Step 5 — Owner judgement

Only after Browser self-walk has removed objective breakage, present the Owner with a small direct preview.

Ask for experiential judgement on:

- czytelność;
- język;
- poczucie miejsca;
- czy wiadomo co jest rzeczą, cudzym znaczeniem i źródłem;
- czy wejście głębiej jest dobrowolne;
- czy powrót/orientacja są naturalne;
- whether the surface feels like useful Medium rather than research documentation.

Owner judgement can veto machine PASS.

Do not turn this into a questionnaire with dozens of fields; normal interaction and free feedback are preferred.

## What counts as a successful phase

Not “the page looks nice”.

A useful interaction PASS would mean:

- Owner-facing surface is naturally understandable in Polish;
- technical/raw depth remains available without dominating entry;
- missing information is shown honestly;
- different local meanings remain visibly attributed;
- exact sources are easy to reach;
- navigation is reversible;
- the UI does not push attention;
- the surface does not force one semantic ontology onto unknown forms;
- agent-facing exactness and Owner-facing clarity coexist over the same underlying reality.

## Important falsifier

If making the surface understandable requires hard-coding today's specimens, relation kinds, or object taxonomy into the Owner UX, the current substrate/view separation is weaker than Phase 0–4 suggested.

That should be treated as a real architectural FAIL, not hidden with copy.

## After the walk

Only then reassess the next pressure.

Likely branches:

- **interaction exposes structural problem** → fix/falsify substrate;
- **interaction is mechanically good but Owner dislikes it** → Owner truth drives redesign;
- **interaction passes cleanly** → bring Codex in as independent critic of the actual surface/adapter;
- **real use exposes stale relationships** → investigate preservation vs surfacing/revision binding;
- **real organism needs active behavior** → begin capability/sandbox research;
- **ecological project work independently discovers a use** → protect and study that event rather than redirecting it into apparatus.

No later branch is selected in advance.
