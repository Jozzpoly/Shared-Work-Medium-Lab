# Medium / warsztat twórczej sprawczości — mapa kampanii, 25.10.2026

**Dokument badawczy dla agentów, nie decyzja Ownera, backlog ani specyfikacja architektury.** Punkt wyjścia: [ŁĄCZNIK](README.md), [pierwszy egzemplarz](workbench.html), jego [testy modelu](test.cjs) i [gestów](test-ui.cjs). Pisane po odzyskaniu historii współpracy z projektu Medium, odczytaniu Jaskini i Opusowego dokumentu *Jaskinia — druga runda* w otwartej Operze, porównaniu Ruch v6.4.1, ReflexBrain R8, ŚLAD/PRZESMYK, dotychczasowych aspiracji Studio/Jozz Vehicle oraz oficjalnych docs przegubów/solwerów. Zewnętrzne wnioski innych agentów są **hipotezami**, dopóki Owner ich nie potwierdzi lub próba nie da właściwego dowodu.

## 0. Czym naprawdę ma być sukces

**Nie:** ładna prezentacja kółek i prętów, liczba testów, jeden kolejny framework, dostęp do każdego stanu, schemat całego Medium ani automatyczne magazynowanie drobnych szkiców.

**Tak:** Owner otwiera *ten sam Jaskiniowy Dom*, uzyskuje ciekawą możliwość, buduje i przebudowuje **nieprzewidziany** wcześniej mechanizm bez proszenia agenta o każde kliknięcie, obserwuje skutki w świecie i decyduje, co zachować. Agent może później zrozumieć i rozwijać **autentycznie edytowalne dzieło**, a nie tylko obejrzeć jego screenshot. Po drugiej stronie ma być także realnie mniejszy koszt Ownera jako pośrednika między agentami, aplikacjami i projektami.

Fundament: **wspólna ciągłość doświadczenia Jaskini ≠ jeden monolit kodu ani uniwersalny format każdego świata**. Prawdziwa Jaskinia ma pozostać Domem; Medium dodaje zasięg i komponowalność. Nowe pracownie mogą być autonomiczne.

## 1. Pięć odrębnych rzeczywistości — nie redukować ich do 'save'

1. **Geometria/struktura autorska:** części, relacje, kotwice, referencje, parametry i semantyczne decyzje autora.
2. **Stan wykonania:** aktualne pozy, prędkości, impulsy, zmęczenie lub inne zmienne runtime.
3. **Obserwacja:** to, co konkretny instrument, agent lub człowiek rzeczywiście widzi; próbki są częściowe i mogą być stare.
4. **Historia/przyczyna:** kto i jak coś zmienił, sekwencja zdarzeń, motywacja; nie wynika z końcowej geometrii ani liczby edycji.
5. **Wartość dla Ownera:** świadomie cenione dzieło vs jednorazowy doodle/test; prawidłowego eksportu nie można oceniać przez brak eksportowania bezwartościowego szkicu.

**Nowy materialny kontrprzykład w ŁĄCZNIKU:** `Linkage.serial()` bierze bieżące pozycje węzłów. Po 400 krokach symulacji (bez autorskiej edycji) 2 z 4 węzłów zmieniają położenie, a import eksportu traktuje nowe pozycje jako spoczynek. `test.cjs` świadomie to dokumentuje (nie oznacza PASS semantyki zapisu). Przy tej iteracji przycisk doprecyzowano do 'Zapisz stan JSON'. **Dług:** przed jakąkolwiek obietnicą zachowania pracy autorskiej wybrać jawne rozdzielenie authored/rest, runtime, ewentualnego snapshotu, oraz protokół ich świadomego transferu. Nie budować całego event-sourcingu z wyprzedzeniem.

## 2. Donorzy i ich granice

| Źródło | Faktyczna wartość | Czego nie wolno wywnioskować |
|---|---|---|
| [Jaskinia v6.4.1 / Ruch](https://github.com/Jozzpoly/Jozz-Cave-Workbench/pull/4), `85aaaae` | Natywne modele Blockbench, interfejs Domu, wybieranie części, przenośny zapis ruchu; krytyczne naprawy błędów technicznych | Że Ruch daje już swobodne tworzenie zależności; Owner ocenił jego obecne doświadczenie negatywnie |
| [ReflexBrain R8 / PR #89](https://github.com/Jozzpoly/ReflexBrain-Lab/pull/89) | Rapier, prawdziwe fizyczne obiekty, kotwiczenie, edycja w świecie, wizualna percepcja aktora, nauka o zerwanych przyczynach | Że automatycznie jest lepszym builderem; źródło samo nie daje Owner acceptance ani żywej ekologii |
| [ŚLAD/PRZESMYK](../dual-interpretation-2026-10-23/README.md) | Realny first-contact wewnątrz Jaskini; trwałość wybranej interpretacji; częściowa obserwowalność i znaczenie jawnego eksportu | Że każdy gest powinien być automatycznie zapisany albo że metryki opisują cały świat |
| [ŁĄCZNIK](workbench.html) | Tani, niezależny, modyfikowalny graf dystansów i gesty authoring→run→edit; izolacja od hosta | Że punktowo-prętowe PBD jest prawdziwym mechanizmem części Blockbench, sztywną bryłą lub dobrym UI |
| Jozz Vehicle / JES / Feniks / Studio (kontekst Ownera, nie bieżące źródła implementacji) | Aspiracje: direct builder loop, kształt/części, kontakt, świat reagujący na działanie, autonomiczne assety oraz przyszłe transfery | Że te projekty mają przejąć ŁĄCZNIK albo że obowiązuje jeden solver i jeden dokument dla różnych dziedzin |

**Badanie zewnętrzne, nie wybór technologii:** [Rapier joints](https://rapier.rs/docs/user_guides/javascript/joints/): revolute, prismatic, constraints, motors, local frames; [Planck.js joints](https://piqnt.com/planck.js/docs/joint.html): 2D więzy między bryłami; [Box2D docs](https://box2d.org/documentation/): joint frames, limits, motors; [XPBD paper](https://mmacklin.com/xpbd.pdf): dlaczego naiwna sztywność PBD zależy od iteracji i kroku czasowego. Ulepszenie solvera nie jest równoważne zwiększeniu przestrzeni konstrukcyjnej.

## 3. Cztery realnie konkurencyjne hipotezy

**A — 'minimum semantyczne wygrywa':** proste relacje bez brył dają wystarczającą sprawczość i najszybszy authoring. Obali ją: użyteczny pomysł Ownera wymaga orientacji bryły, przesuniętej osi, rzeczywistego kontaktu albo momentu siły, więc solver daje fałszywą odpowiedź.

**B — 'dojrzała fizyka jest tańsza':** 2D bryły i przeguby lokalne z Rapier/Planck za mniejszą złożoność zachowania dają większy zakres mechanizmów niż samodzielne dopisywanie praw. Obali ją: integracja natywnego modelu kontaktów/joints zużywa uwagę bez istotnej poprawy łatwości budowania.

**C — 'najważniejszy jest transfer prawdy konstrukcyjnej':** wartość pojawia się wtedy, gdy Agent tworzy wariant, Owner otwiera go i **zmienia strukturę bez tłumaczenia kodu**, a inny agent później kontynuuje, z zachowaną tożsamością części/relacji. Obali ją: nawet poprawny eksport/import wymaga zbyt wielu ręcznych przejść lub traci autorskie znaczenie.

**D — 'nie mechanika, lecz Dom jest ograniczeniem':** osobna pracownia może być dobra, ale w prawdziwej Jaskini przejścia, fokus, uruchamianie, adresowanie, brak dostępu do oryginalnego workspace lub historia są głównym źródłem tarcia. Obali ją: bezpośredni przyrząd działa równie dobrze w Domu, a główne FAIL dotyczą samego authoringu.

Możliwe wyniki mieszane. Nie wybierać jednej architektury przez głosowanie modeli.

## 4. Sekwencja kampanii — warunkowa, nie automatyczny backlog

**E0 · Odzyskanie i zerwanie fałszywego PASS — WYKONANE.** Odczyt Owner feedback Ruch FAIL, Opus źródła v6.4.1, R8 PR #89, ŚLAD, rozmów Medium i Astry. Świeży audit ujawnił błąd `serial()` wobec authored/runtime. Najnowsza regresja 24/24 source JS po oznaczeniu eksportu; zero nowego browser-PASS.

**E1 · Sprzeczne reprezentacje / authoring truth — ROZPOCZĘTE.** Opracować *dwa jawnie różne oczekiwania wobec zapisu*: 'powróć do zaprojektowanej geometrii' i 'wczytaj bieżący stan'. Testować scenę po 400 krokach i po zmianie topologii podczas ruchu. Nie zmieniać schematu `medium.linkage.v1` arbitralnie; jeśli potrzeba oddzielnego formatu, test ma najpierw pokazać różnicę w zachowaniu. Agent ma umieć rozpoznać niezgodność źródła/runtime bez podpowiedzi Ownera.

**E2 · Przestrzeń ekspresji kontra fizyka.** Tylko jeśli E1 jest rozstrzygnięte lub niezależnie obejście ma jawne granice: jednym *identycznym zadaniem*, np. koło–korbowód–suwak, skonfrontować punktowo-prętowy instrument z minimalnym 2D solverem prawdziwych brył i przegubów. Oceniać ile razy trzeba przełączać tryb, przepinać, naprawiać, ile materialnie różnych konstrukcji da się stworzyć. Nie kopiować ReflexBrain bez audytu; nie budować 3D zanim będzie potrzebne.

**E3 · Cross-agent continuation.** Niezależny 'zimny agent' otrzymuje tylko adres pracy i jej dokument/eksport, nie całą rozmowę. Powinien rozpoznać istniejące części, zrobić *autorsko inny* mechanizm oraz pozostawić Ownerowi edytowalny wariant, nie screenshot. Testy: exact source identity, brak zgubionych relacji, świadoma decyzja o aktualizacji vs zamrożeniu wariantu.

**E4 · Real first-contact wewnątrz Jaskini.** Dobrowolnie, gdy jest bezpieczny/prywatny albo rzeczywiście izolowany runtime. Nie przejmować fokusu Opery bez konkretnej korzyści. Test prawdziwej manipulacji i powrotu do pracy. Wynik **Owner FAIL** ma pierwszeństwo nad zielonym CI. Nie rozszerzać infrastruktury, jeśli brak wartości.

## 5. Próg wyboru / rozliczenie

Każda kampania musi dawać **jedną decyzję opartą na dowodzie**, nie liczbę plików:
- PASS techniczny: reprodukowalne źródło + odpowiedni test oryginalnego runtime;
- ADEQUATE eksperymentalnie: mechanizm faktycznie różnicuje hipotezy A–D;
- Owner acceptance: **nieudowodniona**, dopóki nie ma jego realnego doświadczenia;
- FAIL: koszt gestów, brak nowych możliwości, niejasność budowy/pozy, utrata danych, niebezpieczna współdzielona pamięć;
- HOLD: niedostępny niezależny browser lub realny właścicielski feedback.

**Ważny sygnał zatrzymania:** jeśli znowu przybywa frameworków, komentarzy i testów szybciej niż tworzenia nieprzewidzianych konstrukcji albo autonomicznej kontynuacji przez innego agenta, kampania zboczyła z celu. Nie potrzebujemy drugiej Jaskini, kolejnego managera, automatycznego archiwum bazgrołów ani wspólnego formatu wszystkich światów.

## 6. Źródła i autonomia

Medium pozostaje na własnej gałęzi `experiment/medium-relational-linkage-2026-10-25`; kod Jaskini Opusa, R8, Studio, Feniksa/JV, prywatne materiały i `main` nietknięte. [Kompas Jaskini #5](https://github.com/Jozzpoly/Jozz-Cave-Workbench/issues/5) i [PR #4](https://github.com/Jozzpoly/Jozz-Cave-Workbench/pull/4) pozostają źródłem decyzji hosta. Odczytany w Operze dokument Opusa *Jaskinia — druga runda* zawiera m.in. H1–H8 o adresowaniu dzieł, operacjach, edytowalności wyników agenta, uprawnieniach, wersjach i niezależności świata od okna; to **kandydaci do falsyfikacji, nie zatwierdzone wymagania**. Żadnej z tych idei nie przemycać jako narzuconej architektury.

**Najbliższy rzeczywisty ruch:** pogłębić test autorski `source vs live state`, sformułować konkretny *zimny transfer* i dopiero potem porównać inne silniki. Jeśli po pierwszym Owner użyciu problem okaże się zupełnie inny, zawiesić ten plan bez kosztownej obrony.
