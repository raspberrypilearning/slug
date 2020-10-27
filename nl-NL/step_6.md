## Gebruik de joystick

Laten we vervolgens de joystick van de Sense HAT koppelen, zodat de speler deze kan gebruiken om de beweging van de slak te regelen.

![Naaktslak verplaatsen](images/moving-slug.gif)

+ Maak in het gedeelte met functies een nieuwe functie:

```python
def joystick_moved(event):
```

Je roept deze functie aan wanneer de joystick wordt verplaatst. Het ontvangt automatisch een parameter met de naam `event`, waarmee je kunt achterhalen in welke richting de joystick is bewogen.

Je zult de variabele `richting` in willen stellen op de richting waarin de joystick werd ingedrukt. Opdat je de waarde van de variabele vanuit deze functie kunt wijzigen, moet je `global` voor de variabele opgeven. Lees over bereik in Python-functies om erachter te komen waarom.

[[[generic-python-function-scope]]]

+ Voeg `global richting` aan je functie:

```python
def joystick_moved(event):
    global richting
```

Je kunt toegang krijgen tot de richting waarin de joystick is verplaatst met behulp van de parameter `event`: gebruik het commando `event.direction`.

+ Stel in je functie de variabele `richting` in op `event.direction`.

+ Schrijf ten slotte in het hoofdgedeelte van je programma een coderegel om te zeggen dat, wanneer de joystick van de Sense HAT in een willekeurige richting wordt ingedrukt, de functie `joystick_moved` wordt aangeroepen.

[[[rpi-python-sensehat-joystick-event-functions]]]

--- hints --- --- hint ---

Je kunt ontdekken hoe je dit kunt doen in het informatiegedeelte 'Functie-aanroepen activeren met de Sense HAT-joystick' hierboven.

--- /hint ---

--- hint ---

De code om te zeggen "wanneer de joystick in een willekeurige richting wordt ingedrukt" is als volgt:

```python
sense.stick.direction_any =
```

--- /hint ---

--- hint ---

Hier is hoe de code in de **hoofdprogramma** eruit moet zien:

```python
sense.stick.direction_any = joystick_moved
```

Hier is de volledige **functie** code:
```python
def joystick_moved(event):
    global richting
    richting = event.direction
```

--- /hint ---

--- /hints ---

+ Voer je programma uit en test of het werkt. Als je de emulator gebruikt, kun je simuleren dat je de joystick verplaatst door op de pijltoetsen op je toetsenbord te drukken.

Op dit punt is het mogelijk om de slak terug "door" zichzelf te bewegen, wat er nogal vreemd uitziet. Later zullen we wat code toevoegen waardoor het spel eindigt als de slak zichzelf bijt, dus je hoeft je geen zorgen te maken over het oplossen van deze uitglijder.
