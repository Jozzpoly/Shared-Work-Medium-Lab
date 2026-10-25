# E2b · autorska prowadnica — stan po kampanii 25.10.2026

**Ocena: ADEQUATE jako wąski eksperyment mechanicznego authoringu. NIEPOTWIERDZONE jako narzędzie Ownera.**
Bez integracji/merge do Jaskini, Jozz Vehicle, ReflexBrain lub Studio. Wszystko na izolowanej gałęzi Medium.

## Dlaczego powstało

E2 pokazało, że ten sam ŁĄCZNIK PBD uzyskuje suwak po dodaniu jednej reguły osi. Jednak oryginalne E2 *wstawiało prowadnicę w kodzie*, więc nie badało twórczej sprawczości. E2b testuje silniejszą, wciąż wąską hipotezę: **autor sam wybiera dowolny ruchomy punkt i rysuje kierunek jego dozwolonego ruchu, zamiast dostawać gotową animację**.

## Egzemplarz i reprodukcja

- [Edytowalny ŁĄCZNIK E2b](authorable-rails.html): samodzielny HTML bez zależności sieciowych.
- [Samouruchamiający się browser smoke](browser-selftest.html): rzeczywiste wykonanie HTML w Chromium/Operze, DOM, canvas, rozsyłane *syntetyczne* zdarzenia PointerEvent (nie prawdziwy sprzętowy touch).
- [Niezmienny dowód przeglądarkowy 19/19](https://raw.githack.com/Jozzpoly/Shared-Work-Medium-Lab/5dad347361e19beb7997a92ffd95ad7e1233e944/experiments/relational-linkage-2026-10-25/browser-selftest.html). Wynik odczytany z aktywnej Opery 25.10.2026, źródło i iframe z tego samego SHA.
- [Poprzednia, zaprogramowana prowadnica E2](https://github.com/Jozzpoly/Shared-Work-Medium-Lab/tree/experiment/medium-e2-prismatic-2026-10-25/experiments/e2-prismatic-2026-10-25) oraz [E1: projekt versus poza](README.md).

### Co faktycznie zrobiono

1. Domyślny otwarty układ: korba — korbowód — wolna końcówka, jeszcze **bez** prowadnicy.
2. Narzędzie `Prowadnica`: gest od wybranego ruchomego węzła w kierunku osi; ponowny gest zmienia oś; stuknięcie węzła usuwa relację.
3. Relacja ogranicza pozycję *w samym solverze PBD*, w każdej iteracji, bez wymiany solvera. Oś może być ukośna, nie tylko pozioma. Obsługa cofania, usuwania węzła i importu.
4. Wprowadzono jawne `medium.linkage.v2` i envelope `medium.linkage.transfer.v2`; stary `v1` nadal jest odczytywany. Starszy edytor E1 nie przyjmie V2 — jest to świadoma ochrona przed cichym zgubieniem prowadnicy.
5. Wykryto i skorygowano przejmowanie rozpoczętego gestu przez drugi wskaźnik i konflikt prowadnicy z kinematycznie napędzanym punktem, również przy imporcie.
6. Częściowo niezależny test modelu w izolacie JS: 22/22; dowód przeglądarkowy: **19/19** na realnym kodzie, w tym 720 kroków bez zejścia z osi i bez naruszenia więzów długości, tworzenie gestem, odwołanie, cofnięcie, import poprawnego oraz odrzucenie sfałszowanego dokumentu.

**Zastrzeżenie dowodowe:** liczby dotyczą automatycznych testów, nie Owner PASS. PointerEvent były syntetyczne, a `setPointerCapture` w harnessie jest zastąpione przez no-op (syntetyczny pointer nie pochodzi z OS). Nie testowano realnej dłoni na telefonie, bezpieczeństwa osadzania w Jaskini, trudniejszych mechanizmów, ani jakości samodzielnego odkrywania możliwości.

## Co test może obalić

- **Łatwość tworzenia:** użytkownik może kliknąć `Prowadnica` i przeciągnąć punkt w przygotowanym przykładzie. To nie dowodzi, że umie wyrazić własny mechanizm, jego zamysł czy nietypowy kontakt części.
- **Mechaniczna prawda:** pręty pozostają *bezmasowymi więzami punktowymi*. Prowadnica jest przypięta do świata; to nie pełny przegub pryzmatyczny między bryłami. Bez kolizji, orientacji brył, reakcji momentów i realistycznego napędu.
- **E1 wciąż otwarte:** gdy autor dodaje prowadnicę podczas ruchu, oś może przechodzić przez chwilowe położenie węzła, podczas gdy zapamiętany projekt nadal przechowuje wcześniejsze położenia. Eksport projektu ostrzega o napiętych więzach, nie rozwiązuje semantycznie tej sprzeczności.
- **UX telefonu:** wąski viewport działa, ale wcześniejsze letterboxing i ograniczona przestrzeń gestów pozostają problemem. To nie jest test fizycznego telefonu.
- **Jeden Dom / współpraca agentów:** brak dowodu, że Jaskinia potrafi ten eksperyment naturalnie udostępniać, że użytkownik go odnajdzie lub że zimny agent potrafi kontynuować konstrukcję bez całego kontekstu.

## Dalej — nie automatyczny backlog

**Najpierw falsyfikator twórczy:** na jednym własnym pomyśle, poza przygotowanym suwakowym scaffoldem, zbudować i przebudować nieprzewidziany mechanizm; porównać koszt i możliwości tego języka z minimalnym rozwiązaniem na prawdziwych bryłach/przegubach (np. istniejącym Rapier donorem ReflexBrain), bez przenoszenia implementacji między repo.

**Nie robić teraz:** katalogu joints, rozbudowanego autosave, hostingu, PR do Jaskini, refaktoru E1, wyboru finalnego solvera, integracji Studio/JV, sztucznego polerowania na podstawie 19 zielonych testów.

**Owner intent:** jednym Domem jest Jaskinia, a Medium zwiększa zasięg twórczych działań. Zielony test techniczny nie nadpisuje doświadczenia Ownera. Każdy eksperyment może być porzucony, jeśli nie tworzy realnej sprawczości.
