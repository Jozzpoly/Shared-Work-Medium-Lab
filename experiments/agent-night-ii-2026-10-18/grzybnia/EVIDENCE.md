# GRZYBNIA — sesja 2 / eksperyment mechaniczny (18.10.2026)

**Źródło badanej wersji:** `workpiece.html`, blob `504a824f21d6817cdc6cf4f4011764b23584e742`. Zastany HEAD gałęzi przed zapisem: `2c822108f5f6eb28aa89b6f1b749db6d76145ec4`.

## Pytanie
Czy chmura deszczu jest tylko pędzlem do rysowania ścieżki, czy faktycznie wytwarza problem *zbuduj i utrzymuj* żywą sieć?

## Próba
Wykonano 36 deterministycznych symulacji polityk sterowania, w tym 30-, 90- i 120-sekundowych. Headless Node.js: wyodrębniono reguły siatki 48×30, wilgoci, wzrostu, wysychania i BFS z `workpiece.html`; pominięto DOM/canvas. Krok symulacji 0,025 s. Lokalny przebieg zestawu: 5,31 s czasu ściennego, ok. 35 MB maksymalnego RSS. **To test modelu mechaniki, nie oryginalnego browser runtime ani telefonu.**

| Sterowanie | Pierwsze połączenie | Wynik |
| --- | ---: | --- |
| Chmura stale przy korzeniu | brak / 30 s | 137 żywych pól, bez celu |
| Chmura stale przy celu | brak / 30 s | brak wzrostu poza korzeniem |
| Prosty przejazd przez skałę (14 s) | brak / 30 s | przeszkoda zatrzymuje sieć |
| Płynny objazd dołem (5 odcinków × 1,5 s) | 8,58 s | połączenie powstało |
| Płynny objazd dołem (5 × 4 s) | 17,78 s | połączenie powstało |
| Losowe skoki chmury co 1,5 s | brak / 30 s | rozproszone pola, bez celu |
| Po objeździe chmura zostaje przy celu | 8,58 s | pierwsze przerwanie po 39,00 s symulacji |
| Ciągły patrol deszczu tam i z powrotem, 5 × 1–4 s na półprzejazd | 5,28–17,78 s | połączenie utrzymane do 120 s, bez przerwy |

Warianty trzech i czterech dalekich skoków przez dolną trasę nie połączyły celu; pięć przystanków po 8 s — tak, po 32,62 s. Wynik zależy od ciągłości wilgotnego frontu, a nie tylko od końcowej pozycji deszczu.

## Wniosek / falsyfikacja
**Hipoteza częściowo obroniona:** to nie zwykłe malowanie; połączenie wymaga sąsiedztwa żywych pól, obejścia skały i późniejszego odświeżania szlaku. Samo doprowadzenie deszczu do celu nie wystarcza. **Nowe odkrycie:** stabilny stan można osiągnąć regularnym *patrolem* deszczu; bez patrolu wygrywający szlak umiera mimo pozostawienia chmury przy owocniku.

**Konkurencyjne wyjaśnienie:** gra może być tylko prostym zadaniem przeprowadzania kursora po przewidywalnym łuku, a patrole jedynie automatyczną rutyną. Test modelowy nie mierzy ciekawości, czytelności, satysfakcji, reakcji na dotyk ani kosztu renderowania. Brak Owner-playtestu i pomiaru na telefonie. Dodatkowo test jest ręczną ekstrakcją reguł: możliwe rozminięcie z rzeczywistym JS. W Operze dostępny był działający DOM gry, ale bez niezależnego testu tych polityk w przeglądarce.

**Prostsza alternatywa:** ręczne malowanie ścieżki i zanikanie farby. Tańsze, lecz traci przyczynowy wzrost od korzenia i konieczność zachowania ciągłości. Nie rozstrzygnięto, czy ten dodatkowy koszt jest gameplayowo wart zachowania.

## Transfer
Brak donorstwa i integracji. `workpiece.html` pozostaje bez zmian. Wynik jest hipotezą do dalszego eksperymentowania w izolacji, nie wymaganiem dla Jaskini ani innych prac.
