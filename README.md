# Testowanie i Jakość Oprogramowania

## Autor
Mateusz Lasko

## Temat projektu
Event Manager – aplikacja webowa do zarządzania wydarzeniami

## Opis projektu
Projekt jest aplikacją webową stworzoną w technologii Flask, umożliwiającą zarządzanie wydarzeniami.  
Użytkownik może dodawać, edytować, usuwać wydarzenia oraz oznaczać je jako wykonane.  
Aplikacja wykorzystuje bazę danych SQLite oraz ORM SQLAlchemy.

## Uruchomienie projektu
Przed każdym uruchomieniem aplikacji należy usunąć plik `events.db` z katalogu `instance/`.


### Instalacja zależności
pip install flask flask_sqlalchemy pytest

### Uruchomienie aplikacji
python app.py

Aplikacja dostępna jest pod adresem:  
http://127.0.0.1:5000

## Testy automatyczne

### Testy jednostkowe
- Lokalizacja: tests/test_unit.py  
- Liczba testów: 10  

Uruchomienie:
pytest tests/test_unit.py

### Testy integracyjne
- Lokalizacja: tests/test_integration.py  
- Liczba testów: 10  

Uruchomienie:
pytest tests/test_integration.py

## Technologie
- Python 3  
- Flask  
- Flask-SQLAlchemy  
- SQLite  
- Pytest  
- HTML  
- CSS

## Manual Test Cases – Event Manager

| ID | Tytuł | Warunki początkowe | Kroki testowe | Oczekiwany rezultat |
|----|-------|--------------------|---------------|---------------------|
| TC001 | Wyświetlenie listy wydarzeń | Aplikacja uruchomiona, baza danych dostępna | 1. Otwórz stronę główną aplikacji | Lista wydarzeń zostaje poprawnie wyświetlona |
| TC002 | Dodanie nowego wydarzenia | Użytkownik na stronie głównej | 1. Kliknij „Add Event” 2. Wypełnij wszystkie wymagane pola 3. Kliknij „Add Event” | Nowe wydarzenie pojawia się na liście |
| TC003 | Walidacja pustego tytułu | Formularz dodawania wydarzenia otwarty | 1. Pozostaw pole Title puste 2. Wypełnij pole Date 3. Kliknij „Add Event” | Wyświetlany jest komunikat o błędzie |
| TC004 | Walidacja pustej daty | Formularz dodawania wydarzenia otwarty | 1. Wypełnij pole Title 2. Pozostaw pole Date puste 3. Kliknij „Add Event” | Wyświetlany jest komunikat o błędzie |
| TC005 | Edycja wydarzenia | Istnieje co najmniej jedno wydarzenie | 1. Kliknij „Edit” przy wydarzeniu 2. Zmień tytuł 3. Zapisz zmiany | Dane wydarzenia zostają zaktualizowane |
| TC006 | Walidacja edycji bez tytułu | Formularz edycji wydarzenia otwarty | 1. Usuń zawartość pola Title 2. Kliknij „Save Changes” | Wyświetlany jest komunikat o błędzie |
| TC007 | Usunięcie wydarzenia | Istnieje co najmniej jedno wydarzenie | 1. Kliknij „Delete” przy wydarzeniu 2. Potwierdź usunięcie | Wydarzenie zostaje usunięte z listy |
| TC008 | Oznaczenie wydarzenia jako wykonanego | Istnieje niewykonane wydarzenie | 1. Kliknij „Done” przy wydarzeniu | Wydarzenie zostaje oznaczone jako wykonane |
| TC009 | Cofnięcie statusu wykonanego | Istnieje wydarzenie oznaczone jako wykonane | 1. Kliknij „Undo” przy wydarzeniu | Status wydarzenia wraca do niewykonanego |
| TC010 | Responsywność widoku mobilnego | Aplikacja otwarta na urządzeniu mobilnym | 1. Otwórz aplikację na małym ekranie | Układ kart dopasowuje się do szerokości ekranu |

## Dokumentacja API – Event Manager

### REST API

#### GET /events
- Opis: Pobiera listę wszystkich wydarzeń.
- Parametry: brak
- Przykład odpowiedzi:
{
  "events": [
    {
      "id": 1,
      "title": "Spotkanie zespołu",
      "date": "2026-01-20",
      "location": "Biuro",
      "description": "Omówienie projektu",
      "done": false
    }
  ]
}

#### GET /events/<id>
- Opis: Pobiera szczegóły jednego wydarzenia po ID.
- Parametry: id (int) – identyfikator wydarzenia
- Przykład odpowiedzi:
{
  "id": 1,
  "title": "Spotkanie zespołu",
  "date": "2026-01-20",
  "location": "Biuro",
  "description": "Omówienie projektu",
  "done": false
}

#### POST /events
- Opis: Dodaje nowe wydarzenie.
- Parametry (JSON body):
{
  "title": "Nowe wydarzenie",
  "date": "2026-01-25",
  "location": "Online",
  "description": "Opis wydarzenia"
}
- Przykład odpowiedzi:
{
  "id": 2,
  "title": "Nowe wydarzenie",
  "date": "2026-01-25",
  "location": "Online",
  "description": "Opis wydarzenia",
  "done": false
}

#### PUT /events/<id>
- Opis: Aktualizuje dane istniejącego wydarzenia.
- Parametry: id (int) – identyfikator wydarzenia, JSON body:
{
  "title": "Zaktualizowany tytuł",
  "done": true
}
- Przykład odpowiedzi:
{
  "id": 1,
  "title": "Zaktualizowany tytuł",
  "date": "2026-01-20",
  "location": "Biuro",
  "description": "Omówienie projektu",
  "done": true
}

#### DELETE /events/<id>
- Opis: Usuwa wydarzenie po ID.
- Parametry: id (int) – identyfikator wydarzenia
- Przykład odpowiedzi:
{
  "message": "Event deleted successfully."
}

### Web API (zgodne z logami Flask)

#### GET /event/new
- Opis: Wyświetla formularz dodawania nowego wydarzenia.
- Przykład odpowiedzi: HTML strony formularza

#### POST /event/new
- Opis: Tworzy nowe wydarzenie na podstawie formularza.
- Przykład odpowiedzi: Przekierowanie (HTTP 302) na "/"

#### GET /event/edit/<id>
- Opis: Wyświetla formularz edycji wydarzenia o podanym ID.
- Przykład odpowiedzi: HTML strony formularza

#### POST /event/edit/<id>
- Opis: Aktualizuje wydarzenie o podanym ID.
- Przykład odpowiedzi: Przekierowanie (HTTP 302) na "/"

#### GET /event/delete/<id>
- Opis: Usuwa wydarzenie o podanym ID.
- Przykład odpowiedzi: Przekierowanie (HTTP 302) na "/"

#### GET /event/toggle_done/<id>
- Opis: Zmienia status "done" wydarzenia (true/false).
- Przykład odpowiedzi: Przekierowanie (HTTP 302) na "/"
