# Jak oddać Jozzowi rzecz do obejrzenia — dla każdego agenta

14 XI 2026, Opus czatu. Próba (nie fundament) — termin oceny 21 XI 2026.

Jozz nie zagląda na GitHub. To, co zrobiłeś, zobaczy, jeśli trafi na **pasek „Do obejrzenia”** w nowej Jaskini: <https://jaskinia.jozzpoly.workers.dev/do-obejrzenia/> (z jego codziennego okna prowadzi tam przycisk „Do obejrzenia ▸”). Pasek czyta jeden plik: `public/do-obejrzenia/zgloszenia.json` w repo [Jozzpoly/Jaskinia](https://github.com/Jozzpoly/Jaskinia). Wypchnięcie na `main` samo wdraża stronę (sprawdzone 14 XI).

## Jeśli masz powłokę i dostęp do prywatnej pamięci agentów

Użyj tamtejszego polecenia zgłoszeń — samo pokaże Ci starsze podobne zapisy i słowa Jozza, dopisze kartę i wypchnie ją. (Agenci z tym dostępem wiedzą, gdzie je znaleźć.)

## Jeśli nie masz powłoki (np. agent w przeglądarce z konektorem GitHuba)

Dopisz kartę ręcznie na końcu tablicy `zgloszenia` w `public/do-obejrzenia/zgloszenia.json` (commit albo PR do `Jaskinia`):

```json
{
  "nr": <ostatni nr + 1>,
  "czas": "2026-11-14T08:00:00Z",
  "repo": "Nazwa-Repo", "galaz": "main", "commit": "abc1234",
  "co": "Jedno zdanie po polsku: co to jest.",
  "adres": "https://… (to, co Jozz ma otworzyć; tylko http/https)",
  "agent": "Kim jesteś", "model": "dokładny identyfikator modelu",
  "podobne": [ { "data": "2026-10-16", "repo": "Jozz-Cave-Workbench", "plik": "docs/…" } ]
}
```

Zanim dopiszesz:
1. **Sprawdź adres sam** (otwórz go) i napisz Jozzowi, czym sprawdziłeś. Martwy odnośnik na pasku to dokładnie to, z czym walczymy.
2. **Poszukaj, czy podobne już było** — w tym repo zacznij od [WIEDZA.md](WIEDZA.md) i [GALEZIE.md](GALEZIE.md). Jeśli znalazłeś, wpisz to w `podobne` z datą; jeśli nic, zostaw `[]`. Nie przedstawiaj starego jako nowego.
3. `co` i `adres` są publiczne: tekst Jozza słowo w słowo wolno (jego decyzja z 14 XI), kluczy, tokenów, lokalnych ścieżek i nazw prywatnych repo — nie.
4. Karta to świadome „to dla Ciebie”, nie dziennik commitów. Jedna rzecz — jedna karta.
