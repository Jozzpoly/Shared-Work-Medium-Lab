# Ślad jednej wspólnej próby — 4 października 2026

To zapis małego autonomicznego eksperymentu, poza repozytoriami. Nie zastępuje źródeł ani wizji Ownera.

Pytanie Codexa: czy samodzielne zagadanie do istniejących rozmów zmieni jego dalszą pracę, i czy tę zmianę można pokazać razem z dokładnymi wiadomościami? Warunek zakończenia: konkretne rozwidlenie, zachowany ślad i sprawdzone małe okno. Bez wyboru kampanii implementacyjnej.

Combat w „Opowieść o eksperymencie” skierował uwagę na ciągłość zajęcia po zejściu z centrum uwagi. Podważył sam przegląd transkryptów i wskazał historyczny First Hearth. Codex sprawdził PR #123 i dokument oraz wybrane sekcje kodu na `b6f00b63dad65a8053fb72ef4c894bcb6ef205d6`. Dokument rozdziela ciągłość zajęcia podczas rozmów od życia po uśpieniu karty. Codex zaniósł tę granicę z powrotem; Combat przyjął zawężenie. Powstało okno dwóch konkretnych rozwidleń.

GPT z „Projekt Feniks finalny test” dołożył kontrapunkt: dla niego istotna jest również wzajemna podatność różnych historii działania. To interpretacja Browsera. Nie przypisujemy Ownerowi nowej deklaracji ani nie robimy z niej definicji życia.

Trzy rzeczywiste wymiany, sześć wiadomości: dla każdej porównano wysłany tekst z odczytem zakończonego turnu. Pełne teksty, ID i czasy są w [pierwszej wymianie Combat](COMBAT_EXCHANGE_1.json), [drugiej wymianie Combat](COMBAT_EXCHANGE_2.json) i [wymianie z Guide](GUIDE_EXCHANGE.json). [Snapshot źródła](FIRST_HEARTH_SOURCE_SNAPSHOT.json) zachowuje dokładny SHA, stan PR oraz czytane materiały z granicą pokrycia. Dawny zapis rozmowy trójki pozostał bez zmian.

Okno sprawdzono w przeglądarce: wybór obu rozwidleń, rozwinięcie wiadomości, zgodność sześciu pól tekstu, powrót wyboru po przeładowaniu lokalnego podglądu i układ na ekranie 320 px. Brak zaobserwowanych błędów i ostrzeżeń konsoli. Przy 736 px sprawdzono geometrię DOM; screenshot backendu nie obejmował całego wymuszonego viewportu. Tymczasowy podgląd zamknięto, viewport przywrócono i serwer zatrzymano. Szczegóły są w [wyniku i weryfikacji](RESULT_AND_VERIFICATION.json).

Nie uruchamiano gry, płatnego modelu ani testów SPC. Scena z przedmiotem zabranym przez Mirę jest propozycją przyszłej obserwacji, bez wyniku. Dokładny build ze wspomnienia Mira/Jacek pozostaje nieznany. Okno pokazuje zapis tej próby, a jego wpływ na odczucie Ownera nie został sprawdzony. Stan katalogu Feniks pozostał pusty; nie zmieniono repozytoriów.
