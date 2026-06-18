# Notizen
## Tag 1 - Montag

### Software herunterladen
- VSCode installiert
- Git installiert

### Verbindungen erstellen
- In Eingabeaufforderung verbindung zum Ordner: cd "dateilink"
- danach: git clone "https://github.com/louis011209-1901/python_KO-01.git" link von repositorie von GitHub
- auch mit mail und name verbinden

### Arbeiten
- Dateien und Ordner erstellen und bearbeiten
- Codes erstellen und überprüfen

### Dateien hochladen
- Status der Dateien (Files) testen mit: git status
- fürs hochladen: git add .gitignore Notizen.md
- wenn alle hochgalden werden sollen: git add -A
- danach die Dateien commiten: git commit -m "Kommentar"
- am Schluss pushen mit (main kann auch anders sein, falls in eine andere Branch gepusht werden sollte): git push origin main
- danach mit git status überprüfen

### Links einfügen
- in eckigen Klammern den Namen des links und danach in normalen Klammern den link einfügen
- Bsp: [WM Tippspiel] (https://wmtippspiel.srf.ch/)

### Python einführung

#### Python in Terminal
- Python im Terminal mit Befehl "python3" starten
- und mit "exit()" beenden

#### Berechnungen in Python
1. zahl1 = 2
2. zahl2 = 5
3. ergebnis: Literal[3] = zahl1 ** zahl2
4. print("Das Ergebnis ist:", ergebnis)
5. zahl3 = 4
6. ergebnis2: Literal[3] = ergebnis / zahl3
7. print(f"Das Ergebnis von {ergebnis} durch {zahl3} ist: {ergebnis2}")
8. zahl4 = 81
9. zahl5 = 0.5
10. ergebnis3: Literal[3] = zahl4 ** zahl5
11. print(f"Die Wurzel aus {zahl4} ist: {ergebnis3}")

- Bsp in Python:
```python
zahl1 = 2
zahl2 = 5
ergebnis: Literal[3] = zahl1 ** zahl2
print("Das Ergebnis ist: ", ergebnis)
zahl3 = 4
ergebnis2: Literal[3] = ergebnis / zahl3
print(f"Das Ergebnis von {ergebnis} durch {zahl3} ist: {ergebnis2}")
zahl4 = 81
zahl5 = 0.5
ergebnis3: Literal[3] = zahl4 ** zahl5
print(f"Die Wurzel aus {zahl4} ist: {ergebnis3}")
```

Lösung:
- Das Ergebnis ist: 32
- Das Ergebnis von 32 durch 4 ist: 8.0
- Die Wurzel aus 81 ist: 9.0

```python
"Hello World, Hello World, Hello World, Hello World".replace("World", "People", 2)
```

## Tag 2 - Dienstag

### Notizen im Python
- ctrl. + k + c = Formel/Text zu einem Kommentar machen
- ctrl. + k + u = Kommentar wieder zu einer Formel/zu Python hinzufügen

### Funktionen verstehen
- Damit Funktionen/Formeln verstanden und richtig angewendet werden können, kann mit einem Hover über sie die Informationen/Anleitung angezeigt werden.

### Funktionen erstellen
- Funktionen werden mit "def" angezeigt. Sie bekommen auch einen Namen.
- Funktionsbeispiel: def check_r():

## Tag 3 - Mittwoch

### 

## Tipps und Tricks
- Pfeil nach oben/unten werden die letzten codes angezeigt
- Notizen in Python-Datei wird am Anfang der Zeile mit einem # gekennzeichnet
- Hilfe für Codes: ctrl. + shift + p -> github Copilot: Toggle (Enable/Disable) inline suggestions
- wenn dateinamen/-pfade eingefügt werden und danach geprinted werden, muss ein r (steht für raw) hinzugefügt werden, sonst kann python das "\t" als Tab interpretieren:
```python
dateipfad = r'C:\Users\louis\OneDrive - sluz\Desktop'
```

## TODO
- Link abschnitt verbessern
