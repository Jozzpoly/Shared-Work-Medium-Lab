# AGENTS.md

This repository is an experimental lab for **Shared Work Medium (SWM)**.

Your first responsibility is to recover the real project state from the repository rather than relying on a prompt summary.

## Start here

1. Read `START_HERE.md`.
2. Read `docs/RESEARCH_STATE.md`.
3. While the post-reconnaissance phase is active, read `docs/STRUCTURAL_RESEARCH_PROGRAM_2026-10-03.md` before proposing or extending architecture.
4. Read `docs/NORTH_STAR.md` and `docs/DESIGN_GUARDRAILS.md` when direction or scope is material.
5. Inspect the current live work objects named by `docs/RESEARCH_STATE.md`, plus relevant open issues and draft pull requests. Do not assume a previously named issue is still the frontier.

## Working contract

- Treat repository state as authority for repository facts.
- Distinguish established evidence, hypotheses, Owner observations, and decisions.
- A machine/test PASS is only valid for the scope it actually tests.
- Do not overwrite experiential/product-level Owner feedback with narrower mechanical evidence.
- Prefer exact repository paths, commits, issues, PRs, and artifacts over prose context copying.
- Preserve links to rich sources instead of replacing them with one canonical summary.
- Keep changes small, reversible, and justified by observed collaboration friction.
- Do not invent infrastructure because it might be useful later.
- Do not turn GitHub Issues or documents into a project-manager bureaucracy the Owner must maintain.
- Do not hardcode Browser→Codex as the architecture. It is only the first live collaboration specimen.
- If the smallest valid result is "no code is needed yet", say so and explain why.

## Owner burden

A central success criterion is reducing the amount of context transfer, routing, recovery, and technical administration the Owner must do.

Do not ask the Owner to make low-level technical choices when you can investigate and make a reversible engineering judgement yourself.

Escalate to the Owner when the question genuinely depends on:
- product feel,
- experiential judgement,
- vision,
- priorities,
- meaningful trade-offs in project direction.

## Current research posture

The central signal remains **emergent capability from environmental affordances**, as observed in the founding Shinden browser experiment.

The fast `semantic-medium-v0` / draft PR #3 campaign is now **reconnaissance evidence**, not proto-architecture.

The active phase is the structural research program in `docs/STRUCTURAL_RESEARCH_PROGRAM_2026-10-03.md`.

Do not extend v0 merely because its mechanisms already exist. Re-select any donor mechanism from evidence. Cloudflare, GitHub, AXTree, WebMCP, event logs, observation IDs, and the current HTML/JSON shapes are all hypotheses rather than commitments.

The next architecture-bearing specimen should be clean-slate, falsifiable, instrumented, and explicitly compare against a baseline while measuring Owner burden and preserving room for unprogrammed useful behavior.

## Before material implementation

Ask yourself:

- What concrete friction does this remove?
- Does it increase real capability or only add organization?
- Does it reduce Owner burden?
- Could existing GitHub/repository primitives already do the job?
- Is this preserving freedom and composability?
- Can this choice be replaced cheaply later?

If those answers are weak, stop and investigate before building.
