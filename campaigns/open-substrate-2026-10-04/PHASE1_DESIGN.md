# Phase 1 design decision — parallel identity-first adapter

**Status:** candidate implementation direction, not final Medium architecture  
**Evidence base:** specimen #1 current-closure run `37220764133`

## Dla Ownera

Nie będziemy teraz przepisywać Quiet Presence tak, jakbyśmy już znali finalną architekturę.

Zamiast tego budujemy obok niego mały, odwracalny adapter eksperymentalny.

Stare Quiet Presence pozostaje **kontrolą regresji**.

Nowa warstwa ma odpowiedzieć tylko na pytanie:

> czy możemy dopuścić nieznaną formę do wspólnego środowiska na podstawie identity/provenance/body, bez uczenia core jej semantycznego typu?

Jeśli odpowiedź okaże się zła, warstwę można wyrzucić bez naruszenia #5/#6.

## Why a parallel adapter

Directly generalizing `quiet-presence/render.py` now would create two risks:

1. campaign-specific laws could silently become universal substrate laws;
2. a failed abstraction would contaminate the ecological specimen we are using as regression evidence.

Therefore Phase 1 will build an **experimental Open Substrate view** beside the legacy renderer.

The legacy renderer/verifier continue unchanged.

## Candidate thin waist v0

This is intentionally smaller than specimen #1's shape.

The adapter must not understand the semantics of `kind`.

At minimum it needs:

- a stable object `id`;
- a package boundary from which files cannot escape;
- optional passive body reference;
- optional source/provenance references;
- raw metadata preserved exactly;
- identity-based local/participant references.

Everything else is candidate content, not core semantics.

### Important

`kind` is descriptive metadata.

The adapter may display it.

It must **not dispatch behavior from it**.

No branch such as:

`if kind == "browser/field-knot"`

is allowed.

## Discovery candidate

For Phase 1 only, foreign forms are supplied to the adapter as explicit package roots.

This avoids prematurely inventing a universal repository-wide discovery convention.

The experiment will render:

- existing Quiet Presence through its unchanged renderer;
- one or more explicit foreign package roots through the generic adapter.

Later evidence can decide whether Medium wants a directory convention, manifest, local registration, search index or something else.

## Identity-first references

The experimental adapter will resolve foreign local relations and participant perspectives by:

> `object_id`

not by a closed `target_kind` enum.

Unknown relation/perspective semantics remain raw metadata.

Resolution still fails if the referenced identity does not exist.

This preserves integrity without requiring semantic standardization.

## Owner view candidate

Default experimental human view:

- Polish wrapper/navigation;
- Owner-provided Polish title/summary if the package contains one;
- otherwise safe fallback to id/kind;
- body and provenance visible through voluntary depth;
- participant/local interpretation clearly attributed;
- technical/raw metadata behind a deeper action.

This view is derived.

It does not rewrite the raw package or original source.

## Agent view candidate

The same object also gets a technical/raw view:

- exact object JSON;
- exact relation/perspective JSON;
- body/source locations;
- identity;
- hashes where declared.

English is acceptable for campaign-owned technical labels.

No requirement exists that the raw object's content itself be English.

## Body boundary for Phase 1

Specimen #1 is passive.

The adapter may copy/read only passive body/source files inside the package boundary.

Phase 1 does not establish arbitrary HTML/JS execution.

If a body declares active execution or leaves the package boundary, the adapter must refuse that capability rather than reject the object's identity.

A later phase will pressure sandbox/capability behavior separately.

## Generic fallback

A foreign object's existence must not depend on specialized rendering.

If Owner-specific presentation metadata is absent, the generic view still exposes:

- stable id;
- descriptive kind if present;
- body link if safely preservable;
- provenance/source links if present;
- attributed local/participant notes if supplied;
- raw metadata.

Specialized future views may enhance this, not gate existence.

## Phase 1 anti-overfitting checks

The implementation must not contain specimen-specific ids/kinds/relation kinds.

The strict verifier will scan implementation source for those exact fixture identifiers.

This is not sufficient proof of generality, but catches the most direct cheat.

Real generality remains reserved for specimen #2.

## Output isolation

Use a separate generated directory such as:

`campaigns/open-substrate-2026-10-04/site/`

Do not overwrite Quiet Presence generated/public pages.

The Open Substrate landing page may link to the legacy Quiet Presence surface and the foreign generic entry, but this is campaign apparatus — not ecological surfacing.

## First implementation slice

1. load and integrity-check explicit foreign package roots;
2. build identity index;
3. generate Polish Owner generic page;
4. generate raw technical page;
5. copy passive body and source files under bounded paths;
6. display local relation and participant perspective without interpreting their semantic kinds;
7. strict Phase-1 verifier checks specimen expectations;
8. run unchanged Quiet Presence regression alongside it.

Do not add search, ranking, live agent discovery or execution capabilities.
