# Medium World — question field → source atelier

**2026-10-11 · isolated experiment PR #24 · human-facing Owner FAIL remains in force**

## Owner-observed pressure (higher authority than CI)

The Owner spent a short session exploring the initial five-world constellation, switching between questions and lenses, and explicitly judged it **progress, but still an empty shell ("wydmuszka")**. The video showed the mechanical loop: select node / relationship / lens → new prose and off-site link → repeat. It did **not** show an instrumental task being completed. Preserve this negative result without treating it as a complaint that needs more CSS or layout polish.

The subsequent change is **not yet Owner-tested**. It attempts a different interaction mechanism: enter the actual source material, investigate, compare and produce a concrete field note.

## What is implemented now

1. From a place or relationship, click **"Wejdź do źródeł i zbadaj pytanie"**. Enter a two-sided research atelier inside the same page.
2. Browser fetches **two actual public original Markdown documents** from immutable GitHub commit paths under `raw.githubusercontent.com`; no generated source substitute or hidden AI verdict.
3. Navigate source headings, search both documents independently or use **one shared term**. Expand actual nearby lines. The viewer does not synthesize or rewrite the underlying facts.
4. Pin up to 10 exact-line source excerpts into a temporary evidence tray. After a no-hit search capture is explicitly disabled.
5. Write a human/agent hypothesis and produce Markdown with links to the pinned GitHub lines and the selected excerpts. Clipboard copy has a visible manual fallback.
6. **Optional/on-demand:** sample the corresponding moving `main` file and compare its normalized text with the pinned document. Report match vs difference, examples of lines absent from the baseline, or read failure — **never invent a new commit SHA**. This is not an atomic or complete diff, an authenticated Git revision, or necessarily the active research branch.

The initial spatial world and three lenses remain, but are now an entrypoint into a real operation rather than the entire experience.

## Hard boundaries

- Curated subset of **five public projects and five editorial questions**. Not a whole-estate census and not a proven integrated world.
- Exact pinned source URLs are supplied from inspected public repository revisions at 2026-10-11; the moving `main` comparison can be stale (including GitHub edge caching) and may not be the project's active research branch. ReflexBrain `main` is historical: its active branch is separately linked in the World source door.
- `Content-Security-Policy` permits outbound reads **only** to `https://raw.githubusercontent.com`. No private API, GitHub token, database, writes, event broker, analytics, cookies, web storage, login, automatic polling or external image/font assets.
- A generated note is **not stored or published**. To continue outside the page, the participant must deliberately copy it; this does **not yet remove Owner courier work or enable independent receiver discovery**.
- HTMLPreview renders the World but does **not propagate selected view/lens into the outer shareable URL** (real browser FAIL). Do not promise portable viewpoints on that host.
- All cross-project edges are questions, not accepted transfers of runtime architecture or evidence of causal benefit.

## Evidence hierarchy

- Source snapshots directly inspected at these five `main` commits: SWM `77fef7dd2bd7d2c58d26de0bb738f042fe12eb72`; Combat `c96c7535b35de62d410899713522c869dd0c3ac4`; FrameMatter `34e5a290c0e2315999ec76403ab731df196299db`; ReflexBrain `75b95725292fb73d9c8e322bce05bd285aeec237`; LLM Live NPC `f207419ee87c03979544d2d579e624f043300bbc`.
- [Previous World baseline browser CI #38103313340](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/actions/runs/38103313340): static map, viewport control and outer-URL deep link limitation qualified. **Owner FAIL supersedes any product-level reading of this PASS.**
- [Real two-source atelier CI #38104134498](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/actions/runs/38104134498): 3/3 static contract tests; actual Chromium desktop (1440px), mobile (390px), public HTMLPreview executed source fetch, search/capture/export. This is implementation evidence **not a new Owner trial**.
- New moving-main comparison CI: follow the **latest exact PR #24 HEAD** and read its run before treating this feature as qualified.

## Decision frontier

The lab now tests whether an environment can make research across two independent projects *actionable* in place. Next meaningful evidence is an unprompted participant finding a useful connection and carrying a source-grounded result into genuine project work. A forced smoke scenario is not ecological adoption.

**Do not merge or redirect `main` based on CI.** If direct use still feels like a hollow source browser, examine the absence of actual agents/world consequences and radically reconsider, instead of polishing the map or adding another surface for its own sake. Other draft PRs (#5, #17, #22, #23) remain independent.
