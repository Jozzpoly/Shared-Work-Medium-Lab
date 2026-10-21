# Medium — jawne przekazanie PRZESMYK ↔ ŚLAD (21 X 2026)

**Niezależny workpiece, nie wydanie Jaskini, nie produkt zaakceptowany przez Ownera.**
Plik: [medium-explicit-handoff-gpt6.html](medium-explicit-handoff-gpt6.html). Rozszerza istniejącą izolowaną gałąź PR #27 bez modyfikowania obu niezależnych donorów ani ich plików źródłowych. Nowa gałąź oparta na HEAD #27: `419b9c9`.

**Próba:** dwa działające przyrządy w osobnych iframe; jawna operacja przesłania aktualnej topologii z jednego do drugiego i z powrotem. Brak automatycznej synchronizacji, uprawnień Jaskini, trwałego zapisu czy domniemanej akceptacji szkicu. Gdy odbiorca jest edytowany po ostatnim przekazaniu, most wymaga dodatkowego potwierdzenia nadpisania. Odbiornik impulsów ŚLADU nie należy do schematu PRZESMYKU — most przechowuje go tylko w pamięci strony i próbuje przywrócić przy powrocie. Oba donory nadal mają własne ograniczenia i walidatory.

**Weryfikacja:** odczyt źródła na GitHub po zapisie potwierdzony; skrypt strony syntaktycznie prawidłowy. W odizolowanym wykonaniu JS z atrapami obu API: 8/8 PASS (uruchomienie kontrolek, przeniesienie geometrii, zachowanie odbiornika, wykrycie jego niezależnej zmiany, odmowa nadpisania, jawne zatwierdzenie, powrót ze świadomą utratą obcego pola i odtworzenie go z pamięci mostu, odmowa fikcyjnie niepoprawnego importu). **To nie jest test w prawdziwej przeglądarce z obydwoma donorami**; mock nie dowodzi poprawnego renderingu, UX ani użycia Ownera. Otwarta przeglądarka Opera trafiła na zewnętrzny ekran ostrzegawczy raw.githack, nie na wykonany prototyp. Nie obchodziłem ostrzeżenia.

**Istotne ryzyko:** implementacja celowo korzysta ze wspólnego originu i dostępu do publicznych API obu ram; nie jest wzorcem bezpiecznej architektury wtyczek, sandboxingu ani drogi do prywatnego stanu Jaskini. Nie importować prywatnych modeli przez demonstracyjny serwis raw.githack. Wspólny stan nie jest transakcją atomową, nie rozwiązuje jednoczesnej edycji wieloagentowej i nie zachowuje symulowanej fizyki ani impulsów.

**Wartość do sprawdzenia:** czy jedno świadome przekazanie konstrukcji pomiędzy *różnymi interpretacjami* naprawdę skraca drogę od odkrycia do nowej możliwości działania. Kolejny dowód musi pochodzić z rzeczywistego uruchomienia, a nie z kolejnego raportu. Nie przenosić tego automatycznie do Jaskini ani do głównej gałęzi Medium.
