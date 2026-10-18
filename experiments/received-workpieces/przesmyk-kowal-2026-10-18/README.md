# PRZESMYK — recovered workpiece, editable descendant

**Experimental Medium workpiece · 18 October 2026 · draft only · not an accepted product or a proposed Jaskinia architecture.**

This directory contains an existing, independently authored instrument and a bounded later-agent modification that makes a concrete *authored world* portable between separate browser sessions.

## The things one can actually do

- `original-kowal.html`: Run **PRZESMYK**, a single-file interactive 2D water/topology toy produced by the separately scheduled **Kowal** participant. Open and close passages in the dam, draw barriers, move source and drain, pause or reset. This file is the original, unmodified source.
- `portable-variant.html`: The same instrument with **Save variant / Download JSON / Import variant (paste or file)** controls. A variant preserves authored solid-cell changes and source/drain positions and feed state, not the dynamic fluid state. A receiving participant can change the topology, export JSON, reopen another browser session, import the same JSON and continue editing.

Both are independent single HTML files with inline JS/CSS and no package build step. Download the file or inspect source directly. GitHub code pages show source; the `htmlpreview.github.io` helper can render a pinned version but is external and is not a Jaskinia release or permanent site.

## Evidence, separated

**Original:** 13,889 UTF-8 bytes; creator's recorded SHA-256 `21a0d7cada718ff876f2761d36fa9165da6c5a7f6a640d93325e8f16dd51e843`. The original task's report and the later independent recipient's successful browser evaluation are in private authorized context, not copied here. A new Medium agent independently recovered the same original from the owner's Library in a subsequent conversation.

**This GitHub handoff:** source bytes for each HTML file were read from exact file snapshots (original Library and later Medium derivative), committed under a *new isolated branch*, and independently **read back from the exact branch byte-for-byte as identical decoded UTF-8 text**. No Git branch cleanup, legacy app mutation, Owner product acceptance or merge occurred.

**Earlier local browser qualification:** in the original Medium experiment, 18/18 controlled Chromium checks passed for authoring/transfer and a separately restarted Chromium process imported a saved topology with changed downstream physical outcome (48.1 versus 0 in a closed-dam control). This is **evidence reported by that earlier bounded run**, not a claim we reran the browser qualification on this GitHub-hosted URL or in the Owner's own Jaskinia. The simple water model is not physically precise fluid simulation.

**Not established:** automatic unsaved work recovery, solver replay, real HTTPS-origin save continuity, acceptance on Owner's desktop/mobile, autonomous/unprompted agent discovery, recipient interpretation of unknown future JSON versions, the entire artifact ecosystem functioning as one world.

## Keyboard focus and unintentional work loss

The first portable variant had a concrete **FAIL**: its inherited document-wide `R` shortcut reset the running world even while the recipient was typing `r` into the new JSON textarea; the inherited Space shortcut intercepted spaces inside the same editor. This was not a bug in the original Kowal instrument (which had no such textarea): it arose at the boundary when one agent added a new authoring affordance to another agent's work.

Commit `a15ced2` now ignores world shortcuts when editing form controls, contenteditable targets, using browser modifier shortcuts, or composing text with an IME. Twelve isolated checks of the **actual extracted event callback** passed, preserving normal world shortcuts. The reproducible no-dependency Node check is `node tests/keyboard-shortcuts.test.mjs` from this directory. These tests do not certify real mouse/touch behaviour, unsaved draft persistence or the full HTML browser application.

## Browser smoke on the pinned source

A separate [self-running, branch-commit-pinned browser rehearsal](https://htmlpreview.github.io/?https://raw.githubusercontent.com/Jozzpoly/Shared-Work-Medium-Lab/4483887075bd483e614a87ba7e864847605f7c09/experiments/received-workpieces/przesmyk-kowal-2026-10-18/browser-regression.html) was opened in the Owner-connected Opera browser and the resulting accessibility tree was read back. It **reported 9/9 PASS** using the actual fork HTML loaded into a test-only same-origin iframe: instrument boot; nine authored cell changes imported; imported draft remains editable; `R`/Space events directed at the JSON editor preserve the world; a deliberately mismatched source digest is rejected without resetting the current world; and normal in-world `1` and `R` shortcuts still work. Test-only in-memory access to the **unchanged original solver** then ran exactly 240 simulation steps in a closed-dam control and a recovered authored breach: downstream water **0 versus 66.03** model units. The instrument source itself was not modified to expose the solver step; only the disposable harness input string was. The exact self-running harness is `browser-regression.html`.

This is a **hosted browser smoke**, not human interaction/Owner acceptance, long-run stability, mobile touch qualification, post-closure persistence, or a secure production iframe contract. Synthetic KeyboardEvents test routing, not how an actual OS keyboard interacts with every editing surface. Forced solver steps are controlled experimental stimulation, not a long-running game replay or claim of physically conserved liquid.

This is why **recoverable artifacts must retain the conditions under which they remain editable**, not only the bytes and variant schema.

## Why this workpiece matters

The meaningful unit is neither the commit nor an HTML build. **A participant can alter a topology and pass that authored fact to the next participant**, who can then continue from it, while keeping the original Kowal world unchanged. A separate Feniks Studio line independently reached analogous—but different—authoring/recovery findings with bridge geometry and exposed real self-export/import failure; neither prototype is certified as a common protocol or foundation.

This is a **donor**, not an obligation or a new integration work order. Opus and Astra may use, ignore, criticize or adapt it without depending on Medium's choices.

## Source and handling boundaries

The file contents contain no external network calls, credentials or embedded personal recordings in this narrowly inspected version. This is a best-effort static inspection, **not a security audit** of arbitrary historical branches. Keep executable untrusted historical builds separated from private Owner notes in any later exhibition. Do not alter or delete the original Scheduled Task's private Library artifact.

Agent-performed-by: GPT-6 (Medium), through the authorized owner GitHub connector. All outcomes explicitly agent-tested unless marked otherwise.
