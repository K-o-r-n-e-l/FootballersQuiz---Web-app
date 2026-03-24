# Footballers Quiz App

Interaktywna aplikacja webowa typu quiz, stworzona w Pythonie z wykorzystaniem frameworka Flask. Projekt pozwala użytkownikom testować swoją wiedzę o piłkarzach poprzez odgadywanie ich tożsamości na podstawie statystyk lub rozszyfrowywanie nazwisk z pomieszanych liter.

## Funkcje aplikacji
* **System kont**: Rejestracja i logowanie z bezpiecznym hashowaniem haseł.
* **Card Game**: Odgadnij piłkarza na podstawie odkrywanych kafelków z informacjami takimi jak narodowość, kluby czy liczba bramek.
* **Puzzle Game**: Wyzwanie polegające na poprawnym wpisaniu nazwiska gracza z przemieszanych liter.
* **Automatyczna Baza**: System sam generuje strukturę tabel przy pierwszym uruchomieniu.

## Użyte technologie
* **Język**: Python 3.x
* **Framework**: Flask
* **Baza danych**: SQLAlchemy (SQLite)
* **Formularze**: Flask-WTF

## Instrukcja szybkiego startu

### 1. Przygotowanie środowiska
Sklonuj repozytorium i przejdź do folderu projektu:
```bash
git clone <LINK_DO_TWOJEGO_REPOZYTORIUM>
cd footballers_quiz_project
```
Utwórz i aktywuj wirtualne środowisko:
```bash
python -m venv venv
# Aktywacja (Windows):
venv\Scripts\activate
# Aktywacja (Mac/Linux):
source venv/bin/activate
# Instalacja zależności:
pip install -r requirements.txt
```
### 2. Inicjalizacja bazy danych
Uruchom aplikację raz, aby wygenerować plik bazy i tabele, a następnie zamknij serwer (Ctrl+C):
```bash
python run.py
```
Wypełnij bazę danych startową listą 30 słynnych piłkarzy:
```bash
python seed.py
```
### 3. Uruchomienie gry
Uruchom serwer ponownie i ciesz się grą:
```bash
python run.py
```
Adres lokalny: https://www.google.com/search?q=http://127.0.0.1:5000
