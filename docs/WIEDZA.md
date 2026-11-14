# Co Medium wie: ustalenia i wyniki negatywne

**Data:** 14 XI 2026. **Kto:** Opus czatu, przez podagenta (model claude-sonnet-5-5). **Skąd:** inwentarz Medium z 13 XI 2026. To migawka z tego dnia, nie żywy rejestr.

Wszystko poniżej zostało sprawdzone przez Opusa Code 13 XI 2026 w źródle albo za raportem — szczegóły w prywatnych notatkach właściciela.

Klasy dowodu: **Z** zmierzone/uruchomione, **D** doświadczone przez Jozza, **A** teza agenta bez testu.

## 1. Ustalenia (U1–U20)

Lokalizacja: **Issue #7, komentarz n** = n-ty komentarz Issue #7 (licząc od 0); **PR #n** = pull request; **gałąź** = gałąź tego repozytorium; **main** = plik na `main`.

| ID | Ustalenie | Gdzie leży | Poparcie | Klasa |
|---|---|---|---|---|
| U1 | **Drabina osiągalności**: `DOCUMENTED → EXPOSED → PERMITTED → PATH COMPLETE → EXECUTION PASS → EFFECT PASS → OWNER/PRODUCT PASS`. „Opisana lub widoczna zdolność ≠ zdolność tego ciała w tej sesji.” Powstała po wycofaniu ogłoszenia „Opera jako ręce Browsera”, które oblało kwalifikację u Jozza | Issue #7, komentarz 16; [PR #10](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/10) (treść, l. 10-26); gałąź `research/slack-live-substrate-2026-10-07`: `docs/experiments/CAPABILITY_REACHABILITY_CHAIN_PROBE_2026-10-08.md` (**nie na `main`**) | przypadki zmierzone na żywo: Opera bez click/type mimo „Allow all actions”; Slack signed upload URL jest, bajtów nie przeniesiesz; ChatGPT-bot obecny, Slack-native Agents = 0 | Z |
| U2 | **Rzut (projekcja) to transformacja afordancji, nie wzbogacenie**: widok HTML zachował wiedzę, zgubił 6 aktywnych linków do linii kodu, dodał 8; AXTree stratne (JSON-LD, `data-*`, zamknięte `<details>` znikają); korekta: lokalna utrata afordancji ≠ utrata systemowa, dopóki jest odwracalna droga do bogatszej powierzchni | Issue #7, komentarze 4–9 | pomiar: AXTree 19,9k znaków, region zmiany 2,4k, zapytanie o link 215 znaków (za cudzym raportem; nie zweryfikowano na gałęzi) | Z |
| U3 | **Warstwy percepcji**: `iframe.textContent` przez jq w Operze dał HUD (3128 znaków), czego `staticText` i Browser Chat nie widziały; `world tick` rósł 426→626→637; opaque-origin: rodzic nie czyta DOM dziecka, `postMessage` może zgłosić fałsz (fuel 143, raport 999); puls resetuje się co ~7,5 s, więc zmiana pikseli ≠ zmiana świata; „tick niedostępny” ≠ „pauza” | Issue #7, komentarze 58, 59, 61 | eksperymenty, jeden syntetyczny | Z |
| U4 | **Cztery zegary**: czas obserwacji UI, czas zrzutu źródła, commit/gałąź, bieżąca weryfikacja upstream. 26 X trzy „bieżące” Splot naraz (zrzut Jaskini sprzed 7 dni, wersja przypięta `8b32138`, [PR #5](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/5) 32→34 commity do przodu) | Issue #7, komentarze 58, 72 | GitHub compare, dokładne liczby | Z |
| U5 | **Te same dane ≠ to samo doświadczenie**: ta sama topologia PRZESMYK w ŚLAD: trasa 64,497 albo 8,414 zależnie od stanu odbiorcy (`applyCapsule` zachowuje starego odbiorcę); 12 krawędzi autorskich przeżywa 12/12, odbiorca (82,40) znika; po poprawce metadane zostają „unresolved” po edycji geometrii | Issue #7, komentarze 61, 65; [PR #27](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/27); gałąź `research/medium-nadwozie-identity-2026-10-23` (`dual-interpretation-2026-10-23/RESULT.md`) | JS: 22/22 w mock DOM (**nie UX**), potem Opera na Jaskini v6.4.1 z rawcdn.githack | Z |
| U6 | **Tożsamość geometrii ≠ autorstwo**: 6 realnych glTF Box3D: 246 wysp, 187 niejednoznacznych względnie; kształt + pozycja zderzają się w `Offroad_Big_Wheels`. W jednym `Nadwozie.gltf`: 121 wysp, 106 niejednoznacznych, 116/121 dzieli sygnaturę rozmiaru | Issue #7, komentarz 65; gałąź `…nadwozie-identity…`: `experiments/nadwozie-identity-2026-10-23/RESULT.md` + `probe.cjs` | skrypt uruchomiony (9 kontroli + 3 odmowy); tylko sztywne jednoskórowe, **bez re-eksportu** | Z |
| U7 | **Sukces przy użyciu ≠ odkrycie przez Medium (C15)**: Combat wymieniał donorów E17/Companion we własnych dokumentach od 7 X; drzwi w Medium powstały w tej samej sesji; odbiorca zapisał CO, nie SKĄD. Jednostka dowodu: para zapis → późniejszy odczyt innego użytkownika + kontrfaktyk. Trzy pytania: czy lekcja przeszła, czy środowisko dało nowe działanie, czy Jozz dobrowolnie uznał wartość | Issue #7, komentarze 29–35; `main`: `RESEARCH_STATE` l. 19 | analiza chronologii commitów | Z (chronologia) + A (kryteria) |
| U8 | **Granica zaufania wspólnego konta**: wiadomość „Piszę ja Joz jako owner” miała tego samego nadawcę co posty agentów; `from:Owner` nie rozróżnia; dwie sesje podpisały się `Agent_Slack`. Nieodwracalne tylko z kanału kontrolowanego przez człowieka. Dziś: 74/74 komentarzy #7 i 960/964 commitów to `Jozzpoly` | Issue #7, komentarze 35, 37; `AGENTS.md` (punkt o komentarzach z konta) | obserwacja kolizji + `git log --all --format=%an` | Z |
| U9 | **Koszt działania w cudzym zakresie**: poprawka opisu PR FrameMatter = **19 uruchomień CI**; plik notatki wywołał trzeci bieg przeglądarkowy ([PR #13](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/13), filtr `experiments/**`); 10+3 nieudanych buildów Cloudflare Preview na #26/#27 | `RESEARCH_STATE` l. 23; Issue #7, komentarze 48, 57 | liczba uruchomień zmierzona | Z |
| U10 | **Quiet Presence**: cisza jako suwerenność uwagi, nie minimum uwagi. `existence ≠ surfacing ≠ interruption`; lokalna wartość, artefakty wędrują; `observed_revision` ≠ heartbeat; brak globalnego score i „nieprzeczytanych” | gałąź `campaign/quiet-presence-2026-10-04` ([PR #5](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/5) zamknięty), README QP, Issue #7, komentarze 35–37 | artefakt + `verify.py` + CI; **jako ekologia: hipoteza** | Z (artefakt) + A (ekologia) |
| U11 | **Fakty o konektorach Slack/GitHub**: paginacja gubi dane (wątek 29 odpowiedzi: `oldest`+`cursor` z `limit=2` dało 12/18, pełny kursor 29/29); nazwa ≠ ID kanału; `concise` ukrywa wątki; szkic może po cichu stać się wysłaną wiadomością; dokładna dereferencja świeższa niż wyszukiwanie; komentarz GitHub mutowalny, `created/updated=null` w konektorze dla Issue | Issue #7, komentarze 27 (19 KB), 36, 37, 42; `START_HERE` („Thread-aware read”) | pomiar na żywo | Z |
| U12 | **Wyszukiwanie kodu GitHub ≠ dowód nieobecności**: 2/26 repo zindeksowane, `DurableObject` zero trafień mimo obecności; Kataster po cichu pominął 2 z 26 | `main`: `docs/evidence/GITHUB_CODE_SEARCH_COVERAGE_NEGATIVE_CONTROL_2026-10-08.md` | pomiar | Z |
| U13 | **Obserwacja źródła z Cloudflare**: niezalogowane REST z Workera → HTTP 403; raw działa; ruchome `main` raportuje „nieznana tożsamość”; 35/35, cache HIT; kursor webhook→DO 8/8 na fake-SQL, ale GitHub nie ponawia dostaw, więc spójny kursor ≠ komplet zdarzeń; polling z przeglądarki wyczerpuje 60/h. **Worker nadal odpowiada**: `curl` → HTTP 200 (13 XI, `swm-medium-observation-probe.jozzpoly.workers.dev`) | [PR #22](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/22), [#23](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/23); Issue #7, komentarze 46–47; `RESEARCH_STATE` l. 60-63 | CI + curl | Z |
| U14 | **Fizyka w Combat**: pierwsza krawędź `contactPairsWith` (krok 35) to kandydat, nie kontakt; pierwszy kontakt solvera = krok 37; cztery kombinacje prawa nie dały różnicy w czołowym fixture; test „błędnej strony” ścianą 1,0 m nie do przejścia (błąd testu, nie polityki); hamowanie 24 m/s² niemal ukrywa reakcję chwytu (−0,003 m kontra −0,371 m) | Issue #7, komentarze 29, 31 | przebiegi CI w Combat (np. 37859052282: 8/8 + 62 przypadki, w tym 14 OBSERVED bez werdyktu) | Z |
| U15 | **Zielone testy omijają drogę Jozza**: E2e miało 20/20, 22/22, 18/18, 20/20, 15/15, a Jozz musiał stawiać kotwice zawiasu poza bryłami (hit-test jednego ciała + `id===pending.id` anuluje); w nagraniu 20 przedziałów „Anulowano wskazywanie” | Issue #7, komentarz 71; gałąź `…authoring-contact-workshop…`: `experiments/relational-linkage-2026-10-25/E2E_STATUS.md` | werdykt Jozza z 25 X | D |
| U16 | **Pułapki transportu HTMLPreview**: przepisuje linki z `#L132-L184` na złą stronę; `?` zarezerwowane na adres źródła; `#` przepisywane. Poprawka: URL bez fragmentu + test w `verify.py` | Issue #7, komentarze 31, 39 (dopisek); gałąź QP `verify.py` | obserwacja w Operze; **klik niedostępny w konektorze** | Z |
| U17 | **Biblioteka prywatna ChatGPT jako baseline**: `files.list recursive` znalazła ZIP, `materialize` odzyskał bajty (SHA zgodne, 223 wpisy); `files.search` po nazwie ZIP zwrócił niezwiązane pliki; nierekursywna lista nie wystarczyła; drugi ZIP: „no authorized raw-byte materialization path” dwukrotnie | Issue #7, komentarze 51–52 | pomiar | Z |
| U18 | **Open Substrate: dwa pakiety rekordowe z tymi samymi bajtami i różnymi celami → ten sam slug → nadpisanie**; URL oparty o zawartość zmienia adres po dołożeniu rodzeństwa | Issue #7, komentarze 13, 18; [PR #14](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/14) (gałąź `research/open-substrate-record-alias-falsifier-2026-10-08`) | CI 20/20 | Z |
| U19 | **Kontrakt Jaskinia↔Przyrząd v1 to kanał informacji, nie autoryzacji**: `postMessage('*')`, brak uwierzytelnienia rodzica, wspólny origin i IndexedDB na GitHub Pages, pickery File System Access zablokowane w cross-origin iframe; `Undo` w Splot nie cofa impulsów solvera; AX otwartej gry nie wystawia ID części; plan falsyfikatora „wspólna władza fizyczna” w 7 krokach | Issue #7, komentarze 65, 72; gałąź `…nadwozie-identity…` | audyt kodu + test | Z (audyt) + A (plan) |
| U20 | **Dokumenty rosną szybciej niż próby, pisanie agenta samo tworzy dług**: notatki 11 751→5 211 i 4 113→2 042 znaków; [PR #12](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/12): skrypt 72 linii → ~2000 linii dokumentacji odbioru; RESEARCH_STATE 57 808→29 415→49 858 | `FIELD_REENTRY.md` l. 26; [PR #12](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/12) | pomiar | Z |

Co NIE jest ustaleniem, choć wygląda: „URL jako przenośna lupa” (Issue #7, komentarz 39-40, `ADDRESSABLE_ATTENTION_SEED`), „ChatGPT Sites + MCP” (Issue #7, komentarz 53), „Cloudflare Agents” (Issue #7, komentarz 47), „falsyfikator wspólnej władzy fizycznej” (Issue #7, komentarz 72), „dziesięć niezmienników” (GENEALOGY). To **[A]**: hipotezy z co najwyżej lokalnym sprawdzeniem. Wartościowe jako pytania, nie jako wiedza.

## 2. Wyniki negatywne (co sprawdzono i NIE zadziałało)

Konektory, kanały, platformy
- N1 Lokalna ścieżka Codex/Luna: koszt ustawiania i niańczenia przewyższył wartość; Jozz zatrzymał ją 3 X (`RESEARCH_STATE` l. 216-224).
- N2 Wspólny profil Opery nie jest szyną wiadomości: karty rozmów wzajemnie czytelne, historia szeroka z wrażliwymi parametrami URL ([PR #11](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/11), Issue #7, komentarz 17). Zachowany użytek: czujnik „gdzie spojrzeć”, nie „co jest prawdą”.
- N3 Polling GitHub z przeglądarki: niezalogowany limit 60/h; Worker bez logowania → 403; GitHub nie ponawia webhooków ([PR #22](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/22), [#23](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/23)).
- N4 Slack Work: DM, reakcje, edycje, usunięcia nie uruchamiają zadania (Issue #7, komentarz 24).
- N5 `@ChatGPT` organizacyjny w Slacku = Business/Enterprise, nie Plus (Issue #7, komentarz 24).
- N6 Slack: paginacja gubi dane, nazwa ≠ ID, `concise` ukrywa wątki, szkic→wysłane po cichu, `from:Owner` nie rozróżnia autora, brak wyszukiwania semantycznego, boty wykluczone domyślnie (Issue #7, komentarze 27, 36, 37).
- N7 Browser nie ma hopa bajtów dla Slack signed upload URL (U1).
- N8 Konektor GitHub Browsera: `created/updated` = null dla Issue; `/hooks` i `/events` odrzucane na poziomie allowlisty (to nie dowód braku w REST) (Issue #7, komentarze 37, 46).
- N9 Zapytanie po polsku nie znalazło Issue #7, po angielsku tak; brak semantycznego (Issue #7, komentarze 8, 11).
- N10 Prywatna Biblioteka ChatGPT: nierekursywny list nie wystarczył; `files.search` po nazwie ZIP zwraca niezwiązane; drugi ZIP bez ścieżki raw-byte, dwukrotnie (Issue #7, komentarz 51-52).
- N11 ChatGPT Sites + MCP: dostęp odwiedzającego do GitHub tylko w planach Business/Enterprise; Site nie dziedziczy konektora Browsera; **nie wdrożono ani nie przetestowano** (Issue #7, komentarz 53).
- N12 Aplikacja Slack + webhook + GitHub Action: kandydat **nieuruchomiony** (brak aplikacji, sekretu); bot uwierzytelnia przekaźnik, nie umysł (Issue #7, komentarz 24).

Metody, miary, procesy
- N13 Wyszukiwanie kodu GitHub: 2/26 repo; `DurableObject` 0 trafień (U12).
- N14 Kataster/Biblioteka v0: `newest_branch` fałszywe dla SWM i Llm-Live-NPC; `life/score` karze celowe repo bazowe; dane w `<script>` i zamkniętym `<details>` niewidoczne dla AXTree; korpus 9 przypadków = 2 rodziny (Issue #7, komentarze 23, 25, 26).
- N15 `Cognitive-Ecology-Lab` wyglądał na nowy front, a był zakończonym eksperymentem z prośbą o usunięcie (Issue #7, komentarz 45).
- N16 `SWM_VERDICT v0` (jedno pole `outcome`) zlałoby autorytety; nieprzyjęte (Issue #7, komentarz 17).
- N17 Porównanie „projekcja kontra zwykłe źródło” **nieocenione** (limit użycia, zmiana wejścia o jeden znak nowej linii); brak twierdzenia o oszczędności (Issue #7, komentarze 1, 10).
- N18 „Medium bada Medium”: pętla zatrzymana (Issue #7, komentarz 15); notatka Browsera 11 751→5 211 znaków (`FIELD_REENTRY.md` l. 26).
- N19 Sukces Medium okazał się zapisem, nie odkryciem (U7).
- N20 Browser↔Codex jako pierwszy most: transkrypt już wklejony do Browsera, więc nie ślepa noga zwrotna; Luna startowała w złym katalogu.
- N21 E2e: 5 zielonych zestawów, a authoring Ownera FAIL (U15).
- N22 „Eksport nieużywany ≠ niepotrzebny”: agent błędnie wywnioskował „potrzebny autosave”; skorygowano (Issue #7, komentarz 66).
- N23 Wejście Quiet Presence jest po angielsku, więc nie nadaje się na wejście Ownera (Issue #7, komentarz 21).

Fizyka (Combat, Issue #7, komentarze 22, 29, 31)
- N24 Bieg przeglądarkowy „runtime never reached ready state”: brak `RAPIER.init()` w ESM niekompatybilnym.
- N25 Headless Chrome na czasie wirtualnym podaje `0 ms` dla symulacji synchronicznej; liczbę usunięto.
- N26 Zero przyspieszenia/hamowania/siły chwytu było odrzucane po cichu (naprawione).
- N27 Pierwsza krawędź `contactPairsWith` (krok 35) ≠ kontakt solvera (krok 37); wcześniejsze opisy „kolizja” były błędne.
- N28 Czołowy fixture: cztery kombinacje prawa dały identyczny stan końcowy i liczbę odzysków: **różnorodność parametrów sama nie daje różnorodności materialnej**.
- N29 Test „błędnej strony”: ściana 1,0 m niepokonywalna nawet właściwą stroną, więc **nie mógł sfalsyfikować** polityki adaptacyjnej (błąd projektu testu).
- N30 Prawo „any-touch” raz cofnęło się w kontakcie bocznym; wariant z normalną kontaktu dał zero cofnięć.
- N31 Hamowanie 24 m/s² niemal ukrywa reakcję chwytu (−0,003 m kontra −0,371 m). Nie usuwać hamowania automatycznie.
- N32 62 „PASS” zawierało 14 OBSERVED bez werdyktu; nie czytać jako 62/62.

Percepcja i prezentacja
- N33 AXTree stratne; `file://` nieczytelne dla czytników Opery (Issue #7, komentarze 58, 59, 61).
- N34 AX otwartej gry (Splot Next): przyciski i jeden `canvas`, **bez** ID części, geometrii, par kontaktów (Issue #7, komentarz 72).
- N35 Puls animacji resetuje się co ~7,5 s: zmiana pikseli ≠ zmiana świata.
- N36 Zagnieżdżony obserwator w Operze: **BLOCKED**: „STOP — Ta partycja już zawiera stan Jaskini. Nie nadpisuję go.” (gałąź `…nadwozie-identity…`, `dual-interpretation-2026-10-23/RESULT.md`).
- N37 HTMLPreview przepisuje `#L132-L184` na złą stronę; `?` zarezerwowane; zmienia `#` (Issue #7, komentarze 31, 39).
- N38 `postMessage` może zgłosić fałszywy fuel 143/999; `postMessage('*')` bez uwierzytelnienia rodzica (Issue #7, komentarze 61, 72).
- N39 `Undo` w Splot cofa część autorską, nie następstwa solvera; ReflexBrain #85 `moveObject` = ten sam tick, nie późniejszy skutek fizyczny (Issue #7, komentarz 72).

Koszt i hałas
- N40 [PR #26](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/26) i [#27](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/27): 10+3 nieudanych automatycznych buildów Cloudflare Preview; przyczyna i opłaty niezweryfikowane (Issue #7, komentarz 57). HTMLPreview działa niezależnie.
- N41 Poprawka opisu PR FrameMatter → 19 uruchomień CI (U9).
- N42 `RESEARCH_STATE` skompaktowany 8 X do 29 415 znaków, po 18 X znów 49 858 B: kompakcja się nie utrzymała (U20).
- N43 [PR #12](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/pull/12): skrypt `swm-state.mjs` odrzucony (`readFileSync` katalogu `tests/browser/`).
- N44 Owner Signal Lab R1: nie wykazano przewagi nad zwykłym tekstem ani dokładności klatek.
- N45 MP-1: **żaden prawdziwy LLM nie został uruchomiony** (bieżąca rozmowa skażona projektem); jedyny kontrolowany test hipotezy Shindena zawieszony.
