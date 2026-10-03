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
