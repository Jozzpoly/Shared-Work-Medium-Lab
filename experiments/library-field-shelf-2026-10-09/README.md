# Library Field Shelf — deliberately narrow visual specimen

Date: 2026-10-09. This is **not** the entire estate, a canonical ontology, or a replacement for Claude's broader private-inclusive library research. It is a public-source-only, manually authored first human-usable panorama on a separate candidate branch.

## Exact coverage boundary

Four **selected** public repository entrypoints, not a sampled estimate of all repositories and not a complete GitHub census: Shared-Work-Medium-Lab, Combat-Lab, ReflexBrain-Lab, Jozz-Universal-Rig-Editor. Feniks and local workspaces are explicitly *outside* coverage, not absent from reality. The source descriptions were checked against their project-native research state/README before writing.

## What the experiment exposes

- Source-first *actionable* doors; no artificial "latest branch", global priority, score or ambient unread obligation.
- Different project-native authority: SWM draft vs main, Combat experimental branch vs main, ReflexBrain historical main vs live research campaign, JURE canonical main.
- Search enhances an already-present semantic HTML card grid; all links and all cards are readable without JavaScript.
- The optional **“Sprawdź dokument projektu tutaj”** section fetches a public Markdown source only when the reader presses “Odczytaj teraz”, retaining first-party GitHub links for full context. The visible preview is the first 38 lines / 4500 characters of the source text, rendered with `textContent` so source content cannot execute as HTML. A moving ref is **not** an immutable version, nor does read time equal source update time. Failure/timeout (10 s) leaves the native source link accessible. This is an opt-in *retrieval affordance*, not a declared current project-state inference.
- Native links open first-party repo sources; no source navigation depends on HTMLPreview hash-fragment handling.
- Public-only sources. No private Kataster ZIP, branch forest inventory or secrets are embedded.

## What must be falsified

1. Does the rendered page have an accessible heading/card/link structure in a real browser with all four entry sources?
2. Does a human find it **more useful** than QP's existing three-place field? This cannot be declared by its maker; ask only if the Owner voluntarily tries it.
3. Would an agent with a real project task actually find relevant unknown material that native project search missed? Needs a later reader and no-library baseline.
4. Does the presentation create an inaccurate illusion of completeness or live current truth? If yes, change or discard it.

Read-only prototype. Keep on an isolated draft until qualified; no owner approval is assumed.

## Current qualification boundary — 2026-10-09

- **Opera rendered:** the exact on-branch HTML preview exposes all four source-inspection disclosure triangles, four project cards, eight native source/action links and a search box in its accessibility tree. Earlier screenshot review led to viewport compaction.
- **Logic mock PASS:** executed the **exact committed inline JavaScript** against a minimal in-memory browser-element/fetch mock. Verified source-relevant filtering, on-demand successful source response with text-only insertion, HTTP failure fallback, and re-enabled retry. The syntax parsed. This is not a live network/CORS/browser-click test.
- **Remaining unqualified:** real click-through/keypress in Opera (connector here is read-only), raw.githubusercontent.com CORS from HTMLPreview at runtime, actual Owner benefit, agent-native ecological use, corpus coverage/freshness. The native source links do not depend on the optional fetch succeeding.
