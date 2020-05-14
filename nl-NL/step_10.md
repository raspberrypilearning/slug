## Game over

Het laatste wat je moet controleren wanneer de slak naar een nieuwe pixel beweegt, is of ze in haar eigen lichaam zal bijten. Als dit gebeurt, gaat ze dood en verliest de speler het spel. De manier om dit te doen is vergelijkbaar met hoe je hebt gecontroleerd of de slak een groente eet.

+ Maak in de sectie met variabelen een nieuwe Booleaanse variabele met de naam `dood` en initialiseer deze op `False` (zodat de slak niet dood begint!).

+ Voeg binnen de `beweeg()` functie wat code toe om te controleren of de volgende pixel waar de slak naar toe beweegt een deel van zichzelf is.

+ Als dit het geval is, stel je de variabele `dood` in op `True`. Weet je nog wat je moet doen om een functie een globale variabele te laten wijzigen?

--- hints --- --- hint ---

Hier is de code die je hebt gebruikt om te controleren of de pixel waarnaar de slak werd verplaatst, een groente bevatte:

```python
if volgende in groenten:
    # Doe dingen met betrekking tot groenten
```

Kun je vergelijkbare code gebruiken om te controleren of de volgende pixel deel uitmaakt van de naaktslak?

--- /hint --- --- hint ---

Hier is hoe je code eruit zou moeten zien. Zorg ervoor dat je het toevoegt aan de `beweeg()` functie **boven** de code die de `komende` pixel toevoegt aan de `naaktslak` lijst, anders zul je permanent dood zijn!

```python
if volgende in naaktslak:
    dood = True
```

--- /hint --- --- /hints ---


Bewaar en voer je code uit. Wanneer je de slak nu zichzelf laat bijten, zul je zien dat het spel niet eindigt, ook al is de variabele `dood` gewijzigd in `True`!

+ Verander de spel lus in het hoofdprogramma van een oneindige lus in een lus die alleen wordt uitgevoerd als de variabele `dood` niet `True`.

Zodra de spel lus eindigt, wil de speler weten hoe hij het in zijn spel heeft gedaan.

+ Voeg in het hoofdprogramma code toe om te tonen hoeveel groenten de speler de slak naartoe geleid heeft door gebruik te maken van de variabele `score`.

[[[rpi-sensehat-show-message]]]
