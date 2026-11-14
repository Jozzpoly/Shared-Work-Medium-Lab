# Gałęzie Medium — spis i status

Migawka z 14 XI 2026 (Opus czatu, model claude-opus-5-5), złożona poleceniem: `git branch -r` + `git log -1` + `git rev-list --count origin/main..<gałąź>` + lista PR-ów z API GitHuba. **Żadnej gałęzi nie kasujemy**: dla wielu prac gałąź jest jedyną kopią. Zasada Medium: PR zamknięty bez scalenia = dawca (wiedza zostaje, kod nie wchodzi do `main`).

Wcześniejszy przegląd gałęzi przed wycofaniem (3–4 XI, z przypiętymi SHA): [BRANCH_RETIREMENT_PREFLIGHT_2026-11-03.md](BRANCH_RETIREMENT_PREFLIGHT_2026-11-03.md).

Gałęzi poza `main`: **41**. Bez PR: **14**.

| Ostatni commit | Gałąź | Commitów ponad `main` | Status | Ostatni commit — temat |
| --- | --- | --- | --- | --- |
| 2026-10-03 | `experiment/mp1a-browsergym-apparatus-spike` | 7 | bez PR — praca istnieje tylko na tej gałęzi | Record BrowserGym apparatus PASS and bounded next gate |
| 2026-10-03 | `experiment/mp1a-pilot-world-generator` | 33 | PR #4 zamknięty niescalony (dawca) | Self-test OpenAI adapter without credentialed inference |
| 2026-10-03 | `experiment/semantic-medium-v0` | 38 | PR #3 zamknięty niescalony (dawca) | Frame Cloudflare as shared observation substrate |
| 2026-10-03 | `research/cloudflare-observation-substrate-audit` | 5 | bez PR — praca istnieje tylko na tej gałęzi | Add cache invalidation, provenance and capability-binding findings |
| 2026-10-03 | `research/medium-physics-experiment-design` | 12 | bez PR — praca istnieje tylko na tej gałęzi | Add novelty ledger and MP-1A/MP-1B scoring boundary |
| 2026-10-04 | `campaign/open-substrate-2026-10-04` | 130 | bez PR — praca istnieje tylko na tej gałęzi | Mark Open Substrate Codex-ready after real-work admission |
| 2026-10-04 | `codex/recover-exchange-window` | 57 | PR #6 scalony | Record publication and Browser delivery evidence |
| 2026-10-05 | `campaign/capability-expedition-2026-10-05` | 4 | PR #8 zamknięty niescalony (dawca) | Recover broader affordance work through native search |
| 2026-10-08 | `codex/medium-entry-cleanup-2026-10-08` | 7 | PR #15 scalony | docs: distinguish optional World visit from source recovery |
| 2026-10-08 | `experiment/r3c-canvas-visual-actuator-2026-10-08` | 5 | PR #13 zamknięty niescalony (dawca) | experiment: preserve R3C two-run evidence, semantics and receiving-project donor |
| 2026-10-08 | `research/current-truth-topology-dogfood-2026-10-07` | 20 | PR #9 zamknięty niescalony (dawca) | research: record semantic read-back failure during frontier lifecycle update |
| 2026-10-08 | `research/heterogeneous-shared-browser-roundtrip-2026-10-08` | 16 | PR #11 zamknięty niescalony (dawca) | research: source-gate Claude CI concern against ReflexBrain truth |
| 2026-10-08 | `research/open-substrate-record-alias-falsifier-2026-10-08` | 132 | PR #14 zamknięty niescalony (dawca) | test(open-substrate): validate independent technical record identity without frozen digest |
| 2026-10-08 | `research/slack-live-substrate-2026-10-07` | 51 | PR #10 zamknięty niescalony (dawca) | research: correct Opera history provenance after observer-effect finding |
| 2026-10-08 | `research/source-bound-heterogeneous-co-creation-2026-10-08` | 36 | PR #12 zamknięty niescalony (dawca) | research: qualify Claude Free reverse-activation boundary |
| 2026-10-09 | `experiment/owner-signal-lab-2026-10-09` | 0 | PR #19 scalony | research: register Owner Signal Lab as preserved non-frontier donor |
| 2026-10-09 | `field/dual-time-world-entrance-2026-10-09` | 2 | PR #16 scalony | docs: distinguish pinned World visit from evolving field preview |
| 2026-10-09 | `routing/library-field-frontier-2026-10-09` | 1 | PR #18 scalony | routing: expose visual Library draft without promoting it into canonical design |
| 2026-10-10 | `campaign/quiet-presence-2026-10-04` | 93 | PR #5 zamknięty niescalony (dawca) | verify: catch stale public previews diverging from place source truth |
| 2026-10-10 | `experiment/library-field-shelf-2026-10-09` | 58 | PR #17 zamknięty niescalony (dawca) | evidence: record exact connected-Opera five-source pinned E2E and rendered World destinati |
| 2026-10-10 | `research/browser-continuity-run-2026-10-10` | 1 | PR #21 scalony | truth: preserve one recoverable Browser Medium objective and evidence gate |
| 2026-10-10 | `research/library-v2-source-boundary-2026-10-10` | 2 | bez PR — praca istnieje tylko na tej gałęzi | truth: retain Owner's newer parallel Cloudflare test without inventing deploy status |
| 2026-10-10 | `routing/owner-experience-truth-2026-10-10` | 1 | PR #20 scalony | truth: preserve Owner product FAIL separately from scoped mechanism PASS |
| 2026-10-11 | `experiment/observation-boundary-falsifier-2026-10-10` | 45 | PR #22 otwarty | fix: fence-aware Markdown headings in native and Cloudflare observation projections |
| 2026-10-11 | `experiment/world-question-constellation-2026-10-11` | 57 | PR #24 zamknięty niescalony (dawca) | truth: close unqualified Rapier bare-runtime control, remove noisy CI, preserve bounded so |
| 2026-10-11 | `research/event-substrate-provenance-2026-10-11` | 44 | PR #23 zamknięty niescalony (dawca) | test: cursor is evidence of received deliveries, not complete upstream event coverage |
| 2026-10-12 | `research/real-gloop-world-portal-2026-10-12` | 11 | bez PR — praca istnieje tylko na tej gałęzi | Consolidate source-exact two-world qualification and supersede obsolete preview claims |
| 2026-10-12 | `research/world-frontier-truth-2026-10-12` | 61 | PR #25 zamknięty niescalony (dawca) | Exercise genuinely incomplete 300-file frontier cap |
| 2026-10-18 | `experiment/file-origin-idb-return-2026-10-18` | 5 | PR #28 zamknięty niescalony (dawca) | docs(idb): distinguish closed-tab reopen from full-browser restart |
| 2026-10-18 | `experiment/received-przesmyk-2026-10-18` | 13 | PR #26 otwarty | docs(przesmyk): qualify 9/9 Opera and controlled 240-step causal difference |
| 2026-10-19 | `experiment/agent-night-ii-2026-10-18` | 23 | bez PR — praca istnieje tylko na tej gałęzi | plomyk: cache unchanged field rendering in POLE XI |
| 2026-10-19 | `experiment/gpt-przesmyk-oneclick-workpiece-2026-10-18` | 15 | PR #27 otwarty | experiment(medium): Jaskinia read-only instrument for ŚLAD via trusted-origin state/signal |
| 2026-10-21 | `experiment/medium-two-tools-explicit-handoff-2026-10-21` | 19 | bez PR — praca istnieje tylko na tej gałęzi | docs(medium): bound explicit handoff evidence and live-browser limitation |
| 2026-10-23 | `experiment/tworzywo-owner-preview-2026-10-23` | 4 | PR #29 zamknięty niescalony (dawca) | test: await actual file-origin autosave before reload; avoid redundant HTTP E2E rerun |
| 2026-10-24 | `research/medium-nadwozie-identity-2026-10-23` | 77 | bez PR — praca istnieje tylko na tej gałęzi | research: link concise verified lab entry from full historical evidence report |
| 2026-10-25 | `experiment/medium-authorable-rails-2026-10-25` | 37 | bez PR — praca istnieje tylko na tej gałęzi | docs(e2b): single clear re-entry from existing linkage README |
| 2026-10-25 | `experiment/medium-e2-prismatic-2026-10-25` | 12 | bez PR — praca istnieje tylko na tej gałęzi | docs(e2): repair cross-branch E1 and campaign references |
| 2026-10-25 | `experiment/medium-material-contact-falsifier-2026-10-25` | 44 | bez PR — praca istnieje tylko na tej gałęzi | docs(medium): recover E2b–E2d from one existing re-entry |
| 2026-10-25 | `experiment/medium-relational-linkage-2026-10-25` | 30 | bez PR — praca istnieje tylko na tej gałęzi | E1: evidence update with exact browser-qualified source and visual counterexample |
| 2026-10-26 | `experiment/medium-authoring-contact-workshop-2026-10-25` | 75 | bez PR — praca istnieje tylko na tej gałęzi | docs(e2e): remove contradictory stale Owner-unconfirmed verdict and retire pre-Owner testi |
| 2026-11-13 | `opus-code/sasiedzi` | 0 | PR #30 scalony | README mowi, co jest obok: adresy pozostalych repozytoriow ekosystemu |
