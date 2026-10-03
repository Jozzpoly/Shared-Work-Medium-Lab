# MP-1A BrowserGym apparatus spike

This is a bounded donor spike, not an SWM implementation.

It tests one seam only:

> Can BrowserGym observe two human-visible-equivalent pages as materially different semantic environments while preserving factual/text/link/screenshot parity?

## Treatments

- `p0.html` — generic containers / weak semantic structure.
- `p1.html` — native semantic HTML: main/nav/section/article/headings/list.

Both deliberately expose the same visible text, links, ordering, CSS and factual content.

## PASS criteria

The CI probe must establish:

1. BrowserGym installs and runs in a clean GitHub Actions runner.
2. Visible normalized text is identical.
3. Link labels/targets are identical.
4. Screenshots are exact or within a very small predefined pixel-diff tolerance.
5. P1 exposes materially richer AXTree roles (at minimum headings + list structure).
6. P0 does not accidentally expose equivalent semantic structure.
7. Raw observation artifacts are retained for inspection.

A failure stops here. It does not trigger work on the micro-world generator.

## Boundary

This only validates BrowserGym as a possible laboratory body and MP-1A semantic-ablation seam.

It does **not** test the full Shinden-like Affordance Generativity hypothesis.


## Live result — 2026-10-03

### Run 1 — setup failure, hypothesis not exercised

GitHub Actions run `37146374251` failed before loading P0/P1.

Cause: `browsergym-core 0.14.3` pins Playwright 1.44; its `playwright install --with-deps chromium` helper attempted to install the obsolete Ubuntu package `libasound2` on the current Ubuntu 24.04 runner.

Scoped judgement:

- **APPARATUS SETUP FAIL**
- no semantic-ablation claim tested.

The workflow was changed only at the environment seam: install the Playwright Chromium binary without invoking the stale dependency helper.

### Run 2 — apparatus seam PASS

GitHub Actions run `37146441856` completed successfully.

Observed:

| Check | Result |
| --- | --- |
| BrowserGym core | `0.14.3` |
| normalized visible text equality | **PASS** |
| raw link label/target equality | **PASS** |
| pixel mismatch ratio | **0.0** |
| mean absolute pixel delta | **0.0** |
| P0 heading roles | **0** |
| P1 heading roles | **4** |
| P0 list roles | **0** |
| P1 list roles | **1** |
| P0 listitem roles | **0** |
| P1 listitem roles | **3** |
| P0 AXTree chars | **1156** |
| P1 AXTree chars | **1687** |

P1 additionally exposed `main`, `navigation`, `article`, `paragraph`, and `region` roles while preserving the same rendered pixels.

Scoped judgement:

> **PASS — BrowserGym can serve as an MP-1A laboratory body for a visual/factual-equivalent semantic ablation.**

This proves the apparatus seam, not the causal hypothesis.

No LLM subject has been run. No claim is made yet that richer semantics improve correctness, search cost, or generativity.

## Next gate

Proceed to a generated **pilot** micro-world only.

The next apparatus must:

- compile P0/P1 mechanically from one canonical world representation;
- fail closed on visible-text, link, factual and screenshot parity;
- emit exact AXTree/DOM evidence;
- use a public/non-secret pilot seed;
- remain explicitly non-confirmatory.

Measured hidden-seed worlds remain gated until the pilot generator and scoring seam have been exercised.
