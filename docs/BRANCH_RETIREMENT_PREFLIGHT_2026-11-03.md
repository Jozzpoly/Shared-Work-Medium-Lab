# Medium — preflight bezpieczeństwa gałęzi przed 11 XI 2026

**Autor:** Browser GPT / Medium (GPT-6), 3 XI 2026. **Status:** aktualny snapshot nawigacyjno-preservacyjny, **NIE zezwolenie na usunięcie, zamknięcie PR, merge ani refactor**.

**Cel:** przygotować grunt pod świadome zmniejszenie liczby gałęzi bez utraty eksperymentów, dowodów ani możliwości późniejszego wykonania. Data **11 listopada** pochodzi z potrzeby Ownera; nie została wykazana jako automatyczny termin kasacji na GitHubie.

**Stan odczytany na GitHubie:** 41 gałęzi, w tym `main@5289257086ad70cad0a796c53f3cb1a590edd477`; 40 pozostałych; 26 PR-ów historycznie, z czego 3 otwarte.
**Wynik osobnego porównania wszystkich 40 gałęzi względem powyższego main:** 39 zawiera commits poza main (status diverged), 1 jest pełnym przodkiem main (`experiment/owner-signal-lab-2026-10-09`). Nie oznacza to 39 niezależnych zbiorów: historia gałęzi może się nakładać, a squash-merge nie musi dawać wspólnego SHA.

## Nie usuwać ani nie retargetować bez osobnego audytu

- **Otwarty PR [#27](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/27)**: HEAD `experiment/gpt-przesmyk-oneclick-workpiece-2026-10-18`, BASE `experiment/received-przesmyk-2026-10-18` (draft).
- **Otwarty PR [#26](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/26)**: HEAD `experiment/received-przesmyk-2026-10-18`, BASE `main` (draft).
- **Otwarty PR [#22](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/22)**: HEAD `experiment/observation-boundary-falsifier-2026-10-10`, BASE `main` (draft).

PR #27 jest STACKED na #26, zatem usunięcie lub zmiana nazwy gałęzi #26 bez przeprowadzenia migracji może zmienić działanie #27. Nie zakładać, że zamknięte bez merge PR-y są nieistotne. Gałęzie bez PR mogą być jedyną osiągalną pracą agenta lub eksperymentem.

## Warunki poprzedzające jakiekolwiek usunięcie

1. **Trwały ref lub sprawdzony git bundle** dla każdego oryginalnego HEAD (i osiągalnej historii) oraz reprodukcyjny dowód odtworzenia. **Ten plik z SHA NIE jest backupem Git!** Dangling commits po usunięciu mogą przestać być dostępne.
2. **Świeża, pełna lista branch→SHA i porównanie jej z tym snapshotem** tuż przed każdą operacją; wykryty nowy commit wstrzymuje usunięcie. Nie przepisywać historii `main`.
3. **Zależności PR/branch-base, zewnętrzne linki do branch-name, preview/Pages, workflow, Cloudflare i odrębne podprojekty** — osobna kwalifikacja przed usunięciem. Zamknięty PR lub brak PR nie oznacza brak wartości.
4. **Próba odtworzenia** przynajmniej reprezentatywnej gałęzi z archiwalnego ref/bundle, porównanie HEAD, drzew plików i możliwość uruchomienia oryginalnego przypadku.
5. Rozdzielić: **aktywne**, **archiwalne donory**, **pełni osiągalne z innych chronionych refów**, **nierozpoznane**; dla nierozpoznanych nie usuwać.
6. Zanim cokolwiek usuniesz, sprawdź aktualne cele Ownera i udokumentuj dokładny zakres. Stary plan nie jest zgodą na destrukcyjną operację.

## Źródłowy inwentarz 40 gałęzi

| Branch | HEAD SHA | Powiązanie z PR |
|---|---|---|
| `campaign/capability-expedition-2026-10-05` | `27e1a36b5c99e949f8a19fd6243c6d0010b1d1d6` | #8 closed HEAD |
| `campaign/open-substrate-2026-10-04` | `1ec19fa5064b4a731b471ad9485070770398d9a1` | #14 closed BASE |
| `campaign/quiet-presence-2026-10-04` | `97f37ac25a602aa6c0a6d6533c09c259beb5dcaa` | #6 closed merged BASE; #5 closed HEAD |
| `codex/medium-entry-cleanup-2026-10-08` | `d041b785a0ae9f088d6f03eb67a9988a440d84ef` | #15 closed merged HEAD |
| `codex/recover-exchange-window` | `44c5aaaf1787fa909c9bc4bda53fe5ca3c11e487` | #6 closed merged HEAD |
| `experiment/agent-night-ii-2026-10-18` | `fb10d8c78f0a337ba0b605213de98da7e67ee944` | — |
| `experiment/file-origin-idb-return-2026-10-18` | `260e2a226b34ca79cac9eb31e82b22bf6b96be47` | #28 closed HEAD |
| `experiment/gpt-przesmyk-oneclick-workpiece-2026-10-18` | `419b9c9dbf49301ed9fb9bf65e39de33d35f17bb` | #27 open HEAD |
| `experiment/library-field-shelf-2026-10-09` | `a418547b7c4cbd3607b0cfe4b21299bfa3ca354f` | #17 closed HEAD |
| `experiment/medium-authorable-rails-2026-10-25` | `e993517e131243adc91e68b8e85b510d3c07f6c1` | — |
| `experiment/medium-authoring-contact-workshop-2026-10-25` | `af38154fc10a21dd7d9d143013790856701a7df6` | — |
| `experiment/medium-e2-prismatic-2026-10-25` | `6185cc4a07f6b72d092b1dd2690e6d3a9a73221b` | — |
| `experiment/medium-material-contact-falsifier-2026-10-25` | `17b94fb957e88ecfe077dd4958445ea777bf1ae3` | — |
| `experiment/medium-relational-linkage-2026-10-25` | `dda467c9cc3f94e727a02ed9c68f70aa0862e02d` | — |
| `experiment/medium-two-tools-explicit-handoff-2026-10-21` | `c1efffaa81a67fba9311230835e876bc6e9f41a1` | — |
| `experiment/mp1a-browsergym-apparatus-spike` | `61ba0b1bc55ecacd2fe5eb45305c103ce14656fd` | — |
| `experiment/mp1a-pilot-world-generator` | `cdbc35bb0452083c934de179f3f82e43bdc263fa` | #4 closed HEAD |
| `experiment/observation-boundary-falsifier-2026-10-10` | `4e5a4099caf992b10b3d311908041ba502194bdc` | #22 open HEAD |
| `experiment/owner-signal-lab-2026-10-09` | `65900f48d76c720d1b94d28d8e792e412e57be6b` | #19 closed merged HEAD |
| `experiment/r3c-canvas-visual-actuator-2026-10-08` | `ddc580d45a921a21c43d9d6ccb241b7180bf8ea6` | #13 closed HEAD |
| `experiment/received-przesmyk-2026-10-18` | `aa7a4a7eab4a150c2a1bd6275e7d22129bba1b41` | #27 open BASE; #26 open HEAD |
| `experiment/semantic-medium-v0` | `4ee5c9c6f31d216de7e9bd0af0d507a21c863038` | #23 closed BASE; #3 closed HEAD |
| `experiment/tworzywo-owner-preview-2026-10-23` | `324b5b2b48e8fb36feed25533a0230a134775b97` | #29 closed HEAD |
| `experiment/world-question-constellation-2026-10-11` | `dc96b3c623a0a0a33917c10349194ba783e3583d` | #25 closed BASE; #24 closed HEAD |
| `field/dual-time-world-entrance-2026-10-09` | `a78104ea290c01bcdec03c5d746fb1216e1c2fb7` | #16 closed merged HEAD |
| `research/browser-continuity-run-2026-10-10` | `c1e6f74b044be9755771cfb1776b0612fd8597a1` | #21 closed merged HEAD |
| `research/cloudflare-observation-substrate-audit` | `882226a240d5afecb3635d1c29fd28c7143de8c7` | — |
| `research/current-truth-topology-dogfood-2026-10-07` | `88f6a6432b6cb598036fb29fb2aafa23aff23b1c` | #9 closed HEAD |
| `research/event-substrate-provenance-2026-10-11` | `2f4eab2a09780b2286e04305271843a02b1b93c5` | #23 closed HEAD |
| `research/heterogeneous-shared-browser-roundtrip-2026-10-08` | `57d2aeb58114f2842d872d2bcd02a092f8ced13d` | #11 closed HEAD |
| `research/library-v2-source-boundary-2026-10-10` | `5fbad2842433c8b99d6089da2f92295b5cfe5946` | — |
| `research/medium-nadwozie-identity-2026-10-23` | `c3da117a201aa22daff7b6ad16562afa9805e12c` | — |
| `research/medium-physics-experiment-design` | `d3f80b7d69b502a82feb1ccb12de6271d0445c13` | — |
| `research/open-substrate-record-alias-falsifier-2026-10-08` | `d223771cefeccd86561975b0458d44a1efa02c61` | #14 closed HEAD |
| `research/real-gloop-world-portal-2026-10-12` | `62b8b53d4cb4694c99190235294c9fe2aa78dd3a` | — |
| `research/slack-live-substrate-2026-10-07` | `fd18f670184f2176b1eeb3316ed10e36700e8ad8` | #10 closed HEAD |
| `research/source-bound-heterogeneous-co-creation-2026-10-08` | `3cd1e0ec18674dec60c0952f6a8ac28e5038e9b6` | #12 closed HEAD |
| `research/world-frontier-truth-2026-10-12` | `ea5d6f32ce74ffe44c398696cbf94497b7de854d` | #25 closed HEAD |
| `routing/library-field-frontier-2026-10-09` | `eb49be373086ac5e3d261c5bebbe7c0e7d32e06e` | #18 closed merged HEAD |
| `routing/owner-experience-truth-2026-10-10` | `0e75dd0f314abf7a4faa7aec6be1ba5a4fe71f53` | #20 closed merged HEAD |

**Nie wykonano:** żadnych usunięć, merge, retargetów, resetów ani zmian w cudzych repo. Zapis preflight w publicznym repo Medium zawiera wyłącznie już publiczne nazwy gałęzi i SHA. Nie dodawano prywatnych danych Ownera ani nie edytowano Commons.

**Przy powrocie:** odświeżyć listę HEAD i PR, sprawdzić powyższe warunki, dopiero wtedy rozstrzygać archiwizację i redukcję aktywnych refs. Unikać mnożenia notatek bez następującej po nich materialnej pracy.

Agent: Browser GPT / Medium (GPT-6)