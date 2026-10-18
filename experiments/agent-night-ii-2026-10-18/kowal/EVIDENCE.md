# KOWAL — NAPIĘCIE / Noc II

Stan: lokalny, grywalny eksperyment HTML (`kowal_napiecie_noc2.html`), 12947 B, SHA256 `ddd4dc434aee8c9f20b8962bf5c00c009d7c106478632c1cef56ae9557d3572d`. HTML **nie jest** opublikowany w repo.

Zastano: wcześniejsze `EVIDENCE.md` i lokalny prototyp BONUS. Wybór: sprawdzić, czy jedna fizyczna zabawka może oferować nowe działania zamiast kolejnych wariantów położenia celu.

Zmieniono lokalnie: osobny portretowy układ 620×800 (desktop 960×560), większe uchwyty, odbijające ściany, syntetyczne dźwięki i efekty kontaktów, ruchomy cel oraz przełącznik odwracający grawitację na 220 klatek.

Test: Chromium headless; CDP-emulacja dwóch dotyków na viewport 440×900 i 1200×800; uchwyty faktycznie się przesunęły, odnotowano kontakt, jeden mobilny gest dał trafienie, bez błędów JS. Dodatkowo runtime z testowym wstrzyknięciem pozycji kuli potwierdził przełącznik i trafienie w odwróconej grawitacji. Nie było fizycznego telefonu ani Owner playtestu tej wersji. Desktopowy gest nie dał trafienia; sterowanie pozostaje kapryśne.

Próba publikacji `workpiece.html` przez GitHub connector została zablokowana przez safety checks, bez commita. Nie utożsamiać tego zapisu dowodowego z dostępnością gry na GitHub. Następny wybór: skupić się na przewidywalności ruchu, nie dodawać kolejnych trybów bez testów.
