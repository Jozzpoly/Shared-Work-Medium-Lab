# ŁĄCZNIK — mechaniczne relacje zamiast gotowych animacji (25.10.2026)

**Eksperyment Medium, nie Jaskinia v6.5, Ruch 2.0, nowy builder JV ani gotowy produkt.** Celem jest możliwie tanio sfalsyfikować jedną hipotezę: *czy tworzenie i zmienianie zależności między własnymi elementami daje odczuwalnie większą sprawczość niż parametryzowanie ruchu przygotowanych części?*

## Wejście

- [**ŁĄCZNIK — pojedynczy samowystarczalny HTML**](workbench.html). Nie wymaga zewnętrznych bibliotek ani serwera.
- [Oryginalny przyrząd Jaskini v1](https://github.com/Jozzpoly/Jozz-Cave-Workbench/blob/85aaaaec7334428cbc85ce9379930e17b4f5d6cb/docs/przyrzad/KONTRAKT.md): strona może działać samodzielnie lub jako zwykły zewnętrzny `Przyrząd` w **oryginalnej** Jaskini. Odpowiada na `hi/state?`, przesyła wyłącznie liczniki i bieżącą odchyłkę więzów jako `state/signals`. Nie przenosi geometrii ani plików do hosta.
- [Szybki podgląd publicznego eksperymentu](https://raw.githack.com/Jozzpoly/Shared-Work-Medium-Lab/144a6124f2c00ae0041da55d2279a49293512ef4/experiments/relational-linkage-2026-10-25/workbench.html) — adres przygotowany do dobrowolnego otwarcia, **nieprzetestowany w żywej przeglądarce** w tej iteracji. Trzeci origin preview nie jest prywatnym hostingiem. Nigdy nie wprowadzać do tego egzemplarza wartościowych/prywatnych materiałów.

## Jeden konkretny test swobody

Początkowa scena ma cztery węzły, trzy sztywne pręty, dwie kotwice i jeden napęd. Użytkownik może **uruchomić**, **chwycić węzeł**, **dodać nowy punkt**, **połączyć go jednym lub kilkoma prętami**, **zmienić kotwice/napęd**, **usunąć zależność** i zobaczyć zmianę zachowania całego układu. Nie ma przygotowanej jedynej „prawidłowej” konstrukcji ani zaprogramowanej ścieżki animacji każdego ogniwa.

Natywne gesty myszy/dotyku trafiają do jednego canvasa. Zależności pozostają aktywne także podczas chwytania i na pauzie. Świadomy `Zapisz JSON` / `Otwórz JSON` obsługuje wartościowy wariant. **Brak autosave jest świadomą granicą tego badania, nie oceną wartości eksportu.** Przywracanie importu sprawdza referencje, duplikaty i zakresy danych przed zamianą aktywnego modelu. Cofnięcie dotyczy autorskiej zmiany, nie każdej klatki symulacji. Aktywne przeciąganie należy tylko do jednego `pointerId`; drugi palec nie może go zakończyć.

## Co jest prawdziwe, a co uproszczone

Model: punkty poddane grawitacji, więzy stałej długości rozwiązane iteracyjnym *position-based dynamics* (20 iteracji na krok, 120 Hz), kotwice w świecie i **jeden kinematyczny napęd ramienia**. To nie silnik brył sztywnych; nie symuluje masy prętów, momentów bezwładności, kolizji pręt–pręt, tarcia ani realistycznego momentu napędu. Silnie nadmiernie związane układy mogą się odkształcić: pręty o dużej odchyłce czerwienieją, a `odchylka` jest pomiarem, nie zapewnieniem poprawności. To wystarcza do ograniczonego testu „tworzenie relacji ≠ ustawianie animacji”, ale **nie wystarcza do oceny finalnej mechaniki Jozz Vehicle**.

**Ważny donor i antywzorzec:**
- Jaskinia **Ruch** v6.4.1: technicznie poprawiony, lecz negatywny osąd dotyczy samej swobody tworzenia mechanizmów, nie liczby testów.
- [ReflexBrain R8 PR #89](https://github.com/Jozzpoly/ReflexBrain-Lab/pull/89): prawdziwe ciała Rapier, kotwiczenie, manipulacja, ale odmienne pytanie eksperymentalne; nie kopiowano jego kodu ani nie zmieniano tego projektu.
- [ŚLAD/PRZESMYK](../dual-interpretation-2026-10-23/README.md): doświadczenie spontanicznego użycia wewnątrz Jaskini oraz wartość jawnego, świadomego eksportu, nie gotowy model mechaniki.

## Weryfikacja i poziomy dowodu

```
node test.cjs
node test-ui.cjs
```

**22/22** testów wykonanych na *odczytanych z GitHuba bajtach* tej gałęzi: 12 obliczeń i warunków danych + 10 syntetycznych zdarzeń UI / protokołu Jaskini. Dodatkowo lokalny prototyp przed wypchnięciem przeszedł 13 + 10 testów źródła. Stanowisko Chromium w obecnym środowisku odrzuca nawet `data:` przez `ERR_BLOCKED_BY_ADMINISTRATOR`; **nie było rzeczywistego testu renderingu, dotyku, fizycznego feelu, osadzenia w Operze ani oceny Ownera**. Nie przedstawiać PASS z JS jako PASS produktu.

**Test rozstrzygający, jeśli będzie bezpieczna okazja:** bez instruktażu i bez otwierania przez agenta nowej karty bez wyraźnej wartości, czy w realnym przyrządzie Owner potrafi w jednej krótkiej spontanicznej sesji przejść od obserwacji przykładu do **własnego, działającego układu relacji**? Czy przewidywanie i naprawianie jego zachowania jest czytelne? Czy wariant bez napędu nadal daje interesującą manipulację? Jeżeli narzędzie pozostaje zestawem niezrozumiałych kontrolek albo zachowanie jest zbyt sztuczne, zamknąć to jako *FAIL* i zachować dowód. Nie tworzyć automatycznie kolejnego generica.

## Granice repozytorium

Gałąź `experiment/medium-relational-linkage-2026-10-25` powstała od `main` Medium i zawiera wyłącznie folder tego eksperymentu. Żadnych zmian w `main`, Jaskini Opusa, ReflexBrain, assetach użytkownika, publikacji Pages ani wdrożeniu. Nie zmieniać własności projektów i nie sugerować merge na podstawie samej sprawności solvera.
