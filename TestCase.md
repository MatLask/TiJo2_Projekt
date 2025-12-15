## Manual Test Cases – Event Manager

| ID | Tytuł | Warunki początkowe | Kroki testowe | Oczekiwany rezultat |
|----|-------|--------------------|---------------|---------------------|
| TC001 | Wyświetlenie listy wydarzeń | Aplikacja uruchomiona, baza danych dostępna | 1. Otwórz stronę główną aplikacji | Lista wydarzeń zostaje poprawnie wyświetlona |
| TC002 | Dodanie nowego wydarzenia | Użytkownik na stronie głównej | 1. Kliknij „Add Event”<br>2. Wypełnij wszystkie wymagane pola<br>3. Kliknij „Add Event” | Nowe wydarzenie pojawia się na liście |
| TC003 | Walidacja pustego tytułu | Formularz dodawania wydarzenia otwarty | 1. Pozostaw pole Title puste<br>2. Wypełnij pole Date<br>3. Kliknij „Add Event” | Wyświetlany jest komunikat o błędzie |
| TC004 | Walidacja pustej daty | Formularz dodawania wydarzenia otwarty | 1. Wypełnij pole Title<br>2. Pozostaw pole Date puste<br>3. Kliknij „Add Event” | Wyświetlany jest komunikat o błędzie |
| TC005 | Edycja wydarzenia | Istnieje co najmniej jedno wydarzenie | 1. Kliknij „Edit” przy wydarzeniu<br>2. Zmień tytuł<br>3. Zapisz zmiany | Dane wydarzenia zostają zaktualizowane |
| TC006 | Walidacja edycji bez tytułu | Formularz edycji wydarzenia otwarty | 1. Usuń zawartość pola Title<br>2. Kliknij „Save Changes” | Wyświetlany jest komunikat o błędzie |
| TC007 | Usunięcie wydarzenia | Istnieje co najmniej jedno wydarzenie | 1. Kliknij „Delete” przy wydarzeniu<br>2. Potwierdź usunięcie | Wydarzenie zostaje usunięte z listy |
| TC008 | Oznaczenie wydarzenia jako wykonanego | Istnieje niewykonane wydarzenie | 1. Kliknij „Done” przy wydarzeniu | Wydarzenie zostaje oznaczone jako wykonane |
| TC009 | Cofnięcie statusu wykonanego | Istnieje wydarzenie oznaczone jako wykonane | 1. Kliknij „Undo” przy wydarzeniu | Status wydarzenia wraca do niewykonanego |
| TC010 | Responsywność widoku mobilnego | Aplikacja otwarta na urządzeniu mobilnym | 1. Otwórz aplikację na małym ekranie | Układ kart dopasowuje się do szerokości ekranu |
