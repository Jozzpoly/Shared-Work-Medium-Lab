# Medium: one source geometry, two meanings — counterexample (23 Oct 2026)

**Research workpiece, agent-authored, NOT Owner experience or Studio design.** Isolated branch: no main/Opus/Astra/JURE code edits or deployment.

## Source of truth

Two exact, original existing Medium PR #27 HTML instruments, at `419b9c9dbf49301ed9fb9bf65e39de33d35f17bb`:

- [PRZESMYK — playable hydraulic topology](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/419b9c9dbf49301ed9fb9bf65e39de33d35f17bb/experiments/received-workpieces/przesmyk-kowal-2026-10-18/playable-authored-breach-gpt6.html), Git blob SHA-1 `46f1e640d4e4f5643d7f830f795d040a64ed1f15`.
- [ŚLAD — alternate sound/pathfinding interpretation and Jaskinia instrument](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/419b9c9dbf49301ed9fb9bf65e39de33d35f17bb/experiments/received-workpieces/przesmyk-kowal-2026-10-18/second-life-signal-instrument-gpt6.html), Git blob SHA-1 `e846b8c9d4c96a0d60973b22ca3693ab50a60fb9`.

The published donor files were **not modified**. The [test runner](roundtrip.cjs) extracts and executes their original JavaScript in a minimal mock DOM (no browser rendering, no iframe or user gestures). Only the hydraulic solver's simulation function is temporarily exposed **in memory** for synchronized fixed-step qualification.

Run from a local checkout of the two exact donor HTML files:

`node roundtrip.cjs /path/to/playable-authored-breach-gpt6.html /path/to/second-life-signal-instrument-gpt6.html`

Optional third argument is a file prefix to emit both JSONs again. No npm dependencies.

## Authored workpiece and observation

1. Start with the donor's existing 11-cell dam breach, schema `medium.przesmyk.variant.v1`.
2. An independent test agent opens one additional stone at grid index **4872** (x=56, y=43), giving **12 changes**. It assigns the ŚLAD receiver at **(82,40)**, previously unoccupied, using that donor's own supported optional metadata.
3. ŚLAD imports and exports [with-lens.json](with-lens.json): same geometry, explicit authored receiver; its route solver reports **reach=true**, travel cost **79.5269088745** in source grid units.
4. PRZESMYK imports that JSON through its actual `importCapsule`, exports [through-legacy.json](through-legacy.json): **12/12 topology edits, source, drain and feeding remain equal**, but its export **does not include the mediumSignal receiver**.
5. A fresh independent ŚLAD runtime imports the second file. With no receiver in the document, it uses **(62,52)**, not the author's earlier **(82,40)**. It has not preserved the complete interpretation.
6. Negative control: an invalid receiver at (0,0) is rejected by ŚLAD's validation **before applying any change**. The previous world is retained.
7. Stronger red-team: an independent hydraulic edit fills receiver cell **4562** (x=82, y=40), while a hypothetical unaware editor blindly forwards the old opaque receiver metadata. ŚLAD correctly **rejects** that stale interpretation without changing its world. Therefore merely echoing unknown fields can prevent data loss but cannot guarantee their continued validity.
8. With the unchanged PRZESMYK solver at exactly 240 direct test-only steps: original 11-cell version gives right-side water mass **69.66**, 12-cell variant **69.68** (small effect, NOT evidence of a useful new fluid-mechanics interaction).

## Interpretation and boundaries

- **PASS:** two independent donor runtimes materially receive/operate on the same authored topology. This is a real data-semantic integration result without new simulation code or a new editor.
- **FAIL of full interpretation continuity:** a legacy reader intentionally ignores an optional extension, then emits a fresh object without it. This is a compatibility boundary, **not proof of a software bug** or a requirement that all legacy tools must understand future semantics.
- The initial new cell was **agent-authored**, not Owner-authored; no Owner PASS.
- A metadata-preserving envelope must also maintain an explicit validity/uncertainty boundary; passing an opaque extension through after material alteration does not certify its semantics.
- No actual browser file dialogs, WebGL, Jaskinia embedding, cross-origin persistence or user-visible interaction tested. A local Chromium network smoke was blocked by environment policy; don't claim otherwise.
- Different source-derived behaviour in two consumers is useful only if the author understands what survived; no "automatic always-lossless interpretation" claim.

This directly tests the larger F9/F10 Medium hypothesis of **multiple independent interpretations of one source**: a tool may operate correctly on a shared geometry and still silently discard meaning introduced by another instrument.


## 23 Oct continuation — preserve → quarantine → re-author, no universal schema

After the initial loss-of-interpretation result, two **isolated descendants of the exact original HTML sources** were created under this same research directory:

- [PRZESMYK preserving interpretation](przesmyk-preserving-interpretation.html) — original hydraulic solver, interaction/visual design and core JSON retained; a narrow optional carry slot for `mediumSignal` added. If the source capsule's known core remains exactly the same after import, the foreign extension is re-exported unchanged, leaving actual validity to the ŚLAD recipient. If any core field changes, export **removes active mediumSignal and keeps the original bytes in a flagged mediumPending** (`requires-revalidation`) field. Both import and export present the appropriate warning. Unknown other future extensions are NOT supported.
- [ŚLAD revalidating interpretation](slad-revalidate-interpretation.html) — original independent shortest-path and signalling interpretation retained. The recipient recognizes this one `mediumPending` variant, imports valid shared topology, keeps unresolved provenance, shows a visible warning, labels its Jaskinia-facing status as needing receiver placement and suppresses normal Jaskinia numeric signals while unresolved. An *actual pointer-driven receiver repositioning* on a free cell creates a new active `mediumSignal` description and clears the pending state. Moving it onto occupied material does not clear pending.

This is a **paired compatibility experiment**, not a standardized forward-compatible protocol or a Jaskinia product update. The original donor files and Opus's host remain byte-for-byte untouched. It does not address arbitrary unknown extensions, source re-export identity, concurrent edits, authority conflicts, generic metadata migration, browser persistence or cross-origin storage.

### Falsifiable scenario, exact source-bound data

Source [12-edit variant with receiver](with-lens.json) has its authored ŚLAD receiver at **(82,40)**. After importing into modified PRZESMYK, no change preserves that receiver and the **unchanged original ŚLAD** validates it.

In the actual PRZESMYK mouse-handler test, choosing the `wall` tool and clicking (82,40) paints a **2-cell-radius** area. This increases the authored geometry changes **12 → 25** and fills cell **4562**. The exporting instrument now carries the earlier receiver in `mediumPending`, with a user-visible warning, never as an approved current location.

The modified receiving ŚLAD imports that JSON without losing geometry; it reports pending and displays the original receiver coordinates. The user's pointer gesture first tries (82,40), correctly remaining unresolved because that cell is now wall. A subsequent actual receiver drag to free **(78,40)** creates a valid new interpretation. Re-export into modified PRZESMYK and the **original unchanged ŚLAD** preserves it, and the previously untouched hydraulic geometry remains intact.

[Replay all 22 checks](revalidation.cjs) with no dependencies, passing these five paths in order:

`node revalidation.cjs modified-przesmyk.html modified-slad.html with-lens.json original-przesmyk.html original-slad.html`

Original donor sources are pinned above; the two modified files and JSON exist in this same directory. The runner uses [the same event-capable mock DOM](roundtrip.cjs) and injects **no changes** into either published donor. The observations include untouched receiver forwarding, source-brush-induced quarantine, visible status and export evidence, restart continuity, malformed pending refusal, blocked receiver movement, valid new movement and recipient roundtrip.

**Qualification:** 22/22 source-JS assertions passed through a V8 DOM/event stub and were reproducible from GitHub source readback. The original earlier test had 9/9 comparable source checks and remains available. No real Chrome iframe interaction or Owner feel PASS was measured; local networking in available Chromium was blocked by environment restrictions. **Do not conflate event callback invocation with real pointer UX/viewport acquisition or call this shipping-grade.** The exposed research URL and its dependencies still need hosting/framing qualification for first contact in Jaskinia.


### Jaskinia contract negative control

The mock runner gained a host/iframe event surrogate that records `postMessage` target origins. The real updated ŚLAD JavaScript responds to a trusted host `hi` with `hello`, `state`, `signals`. When `mediumPending` exists, a `state?` request receives an explicit **receiver needs human repointing** status and **no numeric `signals`**. A forged `hi` from another origin is ignored. After a pointer-based new receiver placement, a later `state?` again returns **state + numeric signals**; every outgoing message targets `https://jozzpoly.github.io`, not a wildcard.

These are six additional passing source-JavaScript tests (22 total) added to [the existing runner](revalidation.cjs), using [the host-aware simulation](roundtrip.cjs). This tests the **existing Jaskinia v1 message contract** at the code boundary, **not** actual iframe load, browser security response headers, user gesture feel, long-lived saves, or installation.


### 24 Oct (local): real-browser first contact, external origin and portable return

**Different evidence level from the source-mock tests.** The independent ŚLAD HTML was opened in actual Owner-connected Opera. The browser's accessibility tree and screenshot showed a rendered, interactive world with geometry, signal path, file import and JSON export. No agent-driven clicks or actual Owner verdict; the running page was read, not edited. Initial unseeded [source derivative](slad-revalidate-interpretation.html) has no autorun world handoff. We made a **standalone seeded 12-edit donor** ([source snapshot](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/blob/d3f1bc2da2195f9fb61250143ee99b07356d6e0a/experiments/dual-interpretation-2026-10-23/slad-first-contact-12-edits.html)), confirmed in Opera as 12 edits without file import. This is a public agent-authored test variant, not private Owner material.

**Actual cross-origin frame in Opera:** A minimal disposable host on `https://raw.githack.com` embedded the lab from `https://htmlpreview.github.io`. The [original test harness snapshot](https://raw.githack.com/Jozzpoly/Shared-Work-Medium-Lab/95648ccf9cc32eb7bd97836dc43d71634a959b84/experiments/dual-interpretation-2026-10-23/cross-origin-frame-host-probe.html) reached **PASS**: iframe loaded; `hello`, `state`, numeric `signals` came from checked child origin and source; `visible:false` allowed state but no numbers; `visible:true` restarted numeric signals. Host never inspected or controlled iframe DOM. Critical: this child is deliberately a **test-only origin-switched copy** trusting raw.githack, not the genuine Jaskinia origin; the result does not claim an end-to-end test inside Jaskinia. No Jaskinia sources or Owner browser storage touched.

**World as a recoverable first-contact link:** [The isolated public-world link source](slad-worldlink-first-contact.html) adds a visible `LINK DO ŚWIATA` action and URL-fragment `#world=` restore of the existing `medium.przesmyk.variant.v1` workpiece. It carries actual grid edits and optional ŚLAD receiver interpretation, including explicitly unresolved `mediumPending`. No extra server, user account, web storage, new engine or universal schema. A 13-edit variant that was not the default 12-edit workpiece opened in a **new real Opera tab**, and the UI displayed `ODZYSKANY ŚWIAT · Z LINKU`, precisely **13 edits**. The [second actual cross-origin frame snapshot](https://raw.githack.com/Jozzpoly/Shared-Work-Medium-Lab/1751749e99c56f925dca2c7094247377477a8305/experiments/dual-interpretation-2026-10-23/cross-origin-recovered-world-probe.html) displayed the **same 13-edited workpiece inside an iframe**, with `state` explicitly stating `13 zmian`, and passed handshake and visibility transitions. That host also uses a test-only origin-adapted child.

**Crucial negative cases and repairs:** A pending 13-edit URL exposed a real UI false assertion: after successfully importing pending geometry, the startup text incorrectly said *interpretation recovered* (despite its receiver being unresolved). Repaired so the UI says `ODBIORNIK NIEPOTWIERDZONY` and visibly asks for deliberate repointing; **verified in real Opera**, commit `7b6dc6b8be2727c009f2fa5c3d6a199c6d113056`. A second regression in URL-mode startup let a fallback `else` overwrite the 12-edit preload with the 11-edit demo whenever there was no `#world` fragment; fixed at commit `c89f7cd81426e7cad4f80a2b74dbadcc65369bb2`, **verified in real Opera as 12 edits**. This is why positive seed+restore tests alone had been insufficient.

[Reproduce the final 11-link cases](worldlink-smoke.cjs) against [the current link variant](slad-worldlink-first-contact.html) and [12-edit source JSON](with-lens.json):

`node worldlink-smoke.cjs slad-worldlink-first-contact.html with-lens.json`

11/11 mocked event-level assertions cover: bare 12-edit start, explicit 13-edit URL restore, copying exact current capsule, visible recovery-link field, reimport, hiding stale link after editing, pending meaning and share warning, invalid hash's conspicuous failure with safe exemplar, and oversize rejection in favour of JSON. Re-read exact GitHub files and reran. The original dual-interpretation 22/22 regression checks also remain passing. Link-copy button was verified through the real page's event callback in a mock DOM; **it was not physically clicked in Opera**.

**Boundaries:** These are research-only public small-grid variants. A URL carries its world **in plaintext**, visible in browser history, copied links and any external page that obtains it; explicitly **not for private Jozz asset geometry or notes**. Previews rely on unrelated third-party htmlpreview/raw.githack hosting, which is not under the Studio's security or uptime contract; raw.githack may show a first-visit confirmation. Explicit JSON export remains the offline alternative. The link currently captures at click time; subsequent edits require clicking again, and browser refresh inside a Jaskinia iframe may reset its URL to the original instrument source. **No automatic recovery from arbitrary browser crash** and no guarantee of separate-tab/embedded storage continuity. Full production Jaskinia v6.4.1 First-Contact (URL entering the actual `Przyrząd` picker, file dialog, owner comfort, permanent hosting) remains **UNVERIFIED**.

**Decision:** the cross-origin basic delivery, status messaging, explicit portable authored world and carefully represented uncertainty are real browser evidence; this is a better starting test item than a new SDK. Do not equate the harness with the actual Dom. The next economically valuable validation is a trusted-origin hosting path plus the actual Jaskinia First-Contact with a consciously disposable workpiece. Avoid adding application-wide plugin design, private-asset movement or a mandatory Owner test ritual before necessary.

### Critical remaining failure boundary

Even the cautious `mediumPending` can be lost by *another* older reader that does not preserve that field. A mere opaque echo is not proof of continuing validity; a tool that cannot interpret foreign semantics cannot safely decide their future meaning. The paired test makes that boundary visible only for these two known interpretations.

The transferable principle is narrower than a proposed architecture: the receiving tool must retain authority for its own semantic validity, while an intermediate tool should not silently claim or discard another author's decision. This is a real example of a **composable environmental capability**, though not evidence of independent, spontaneous Medium adoption.

## Next useful decision

Before designing plugins or an overarching universal format, distinguish workpiece **core data**, **optional tool-specific interpretation**, and **forward-preserved but unrecognized information**. The smallest future test is to compare ordinary forward preservation versus deliberate explicit conversion with a real recipient, without secretly replacing the author's decision. Do not promote a new schema until a real task requires it.

For a later Jaskinia first-contact test, the existing ŚLAD variant is the less-privileged candidate (file input + Blob download, optional status handshake). JURE relies on File System Access pickers that Chromium disallows in a cross-origin iframe. Both observations are separately documented in [the adjacent field checkpoint](../nadwozie-identity-2026-10-23/RESULT.md). A standalone source/import success does not imply a full Jaskinia product PASS.
