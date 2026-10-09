# Owner Signal Lab R1 — archived donor

A local-first video annotation instrument for converting Owner observations, feel/judgement, hypotheses, intent and questions into a compact AI handoff without flattening those epistemic roles.

## Why it exists

The useful capability is not “video notes” by itself. It is **Owner cognition capture**: point to an exact moment/range, say what kind of claim it is, and hand the result to an agent without requiring the Owner to reconstruct the entire observation in prose.

The tool is intentionally standalone. It does not depend on ChatGPT `@visualize`, MCP, a backend, or a hosted service.

## R1 hardening

Compared with the first working R0 specimen, R1 fixes or adds:

- lossless millisecond formatting at export/handoff boundaries;
- R0 JSON migration and source-name recovery;
- source metadata rather than annotations floating free of their footage identity;
- explicit source reattachment after recovery/import;
- edit-in-place for signals;
- untimed `GENERAL` signals;
- active A/B timeline semantics;
- optional manual A/B offset alignment and paired BOTH ranges;
- honest ±33 ms seek wording instead of pretending frame-accurate stepping;
- non-destructive invalid JSON import;
- source-mismatch confirmation before rebinding;
- graceful operation without localStorage;
- an explicit agent contract forbidding invented footage content when video is unavailable;
- restrictive CSP with `connect-src 'none'`.

## Deliberate limits

R1 does **not** establish frame-accurate stepping, content-based A/B alignment, universal browser-local-storage behaviour, large-session performance, or product value beyond the Owner's initial smoke test. It does not automatically write into an AI conversation.

## Archive placement

The runnable HTML, ZIP package, screenshot and verification report are preserved in the Owner's private ChatGPT Library at:

`/Medium/Owner Signal Lab R1/`

The public SWM repository intentionally preserves only this bounded donor record and test summary. The Owner's private smoke-test exports and random video names are not published here.

Artifact checksums at archive time:

- HTML SHA-256: `ccfe459819dc6ccb7560ad982397ec73c16b00352ec9f294cf57ca995aadf383`
- ZIP SHA-256: `e76c3e0feee79036f21fc23619802bc0fbedc27a8da89a85c15ed68a7b2e91bd`

## Status

**ARCHIVED DONOR / useful standalone tool.**

This is not a current Shared Work Medium architecture decision or live frontier. Reopen only under real usage pressure — especially repeated video-feedback work — or if a future conversation-native UI can materially eliminate the remaining manual handoff boundary.
