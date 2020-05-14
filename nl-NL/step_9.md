## Groeien en versnellen

Om het spel interessant te houden voor de speler, moet de slak groenten eten en sneller groeien. Dit maakt haar moeilijker te beheersen - en erger, ze zou per ongeluk in haar eigen lichaam kunnen bijten!

De code die je tot nu toe hebt geschreven, zorgt ervoor dat, wanneer de naaktslak een pixel vooruitgaat, haar eindsegment wordt verwijderd. Om haar in staat te stellen te groeien, kun je een nieuw segment toevoegen aan de lijst `naaktslak`, maar **niet** de laatste verwijderen. Elke keer dat de slak beweegt, moet je dus beslissen of je een segment wilt verwijderen of niet.

+ Maak aan het begin van de functie `beweeg()` een Booleaanse variabele met de naam `verwijder` en stel deze in op `True`, omdat we meestal het eindsegment willen verwijderen wanneer de slak beweegt.

+ Voeg een voorwaardelijke instructie toe aan je functie, zodat de volgende twee coderegels alleen worden uitgevoerd `als` de variabele `verwijder` `True` is.

```python
sense.set_pixel(eerste[0], eerste[1], leeg)
naakslak.remove(eerste)
```

+ Bepaal hoe vaak je je naaktslak wilt laten groeien. In ons voorbeeld kozen we voor onze slak om haar één segment te laten groeien voor elke 5 groenten die ze eet.

Om je programma te helpen beslissen wanneer je de naaktslak wilt activeren, kun je de **mod** operator `%` gebruiken. Door het te gebruiken, kun je bepalen of de huidige score een veelvoud van 5 is.

[[[generic-python-mod-operator]]]

Je wilt ervoor zorgen dat de slak alleen kan groeien als hij een groente heeft gegeten. Om dit te doen, moet je je nieuwe code toevoegen om de naaktslak in deze `if` instructie mogelijk te laten groeien:

```python
if volgende in groenten:
```

+ Voeg code toe om te controleren of de huidige score een veelvoud van 5 is. Als dit het geval is, stel je `verwijder` in op `False` zodat er geen segment wordt verwijderd.

+ Sla op en voer de code uit. Je zult misschien teleurgesteld zijn om te zien dat als je 5 groenten eet, de slak niet groeit! Waarom niet?

--- collapse ---
---
title: Antwoord
---

De code om het segment te verwijderen, loopt momenteel vóór de code om te controleren of de nieuwe pixel een groente was. Dit betekent dat het programma niet uitmaakt of we het hebben verteld om een segment te verwijderen of niet, want tegen de tijd dat deze beslissing wordt genomen, is het segment al verwijderd!

--- /collapse ---

+ Wijzig de volgorde van de code zodat het laatste in de functie `beweeg()` de code is om mogelijk een segment te verwijderen. Test opnieuw en je zou je naaktslak moeten zien groeien.

Evenals `verwijder` in te stellen op `False` om de naaktslak te laten groeien, laten we het versnellen! Momenteel wordt de snelheid van de slak geregeld door deze coderegel in het hoofdprogramma:

```python
sleep(0.5)
```

Dit commando vertelt je oneindige lus om een halve seconde te wachten tussen elke run, zodat de slak beweegt met een snelheid van één pixel per halve seconde. Om het sneller te laten gaan, wil je deze pauze geleidelijk verminderen.

+ Maak in de sectie met variabelen een variabele met de naam `pauze` en stel deze in op `0.5`.

+ Vervang de `0.5` tussen haakjes van de functie `sleep ()` door de variabele `pauze`. Nu wordt de snelheid van de slak bepaald door de waarde van `pauze`.

Je hebt al wat code toegevoegd aan de sectie die controleert of de huidige score een veelvoud van 5 is, zodat je slak kan groeien. Dat is ook het punt waarop de waarde van `pauze` kleiner moet worden. Wijzig uw `beweeg` functie als volgt:

```python
global pauze

if score% 5 == 0:
    verwijder = False
    pauze = pauze - 0.1
```

+ Sla je programma op en voer het uit. Wat gebeurt er? Waarom is deze code geen goed idee, en hoe kun je deze verbeteren?

--- collapse ---
---
title: Antwoord
---

Als `pauze` begint bij `0.5`, en we trekken `0.1` af voor elke vijf gegeten groenten, dan wordt `pauze` uiteindelijk `0`. Dat maakt het spel onmogelijk!

Waarom maak je in plaats van een vaste hoeveelheid er vanaf te trekken, `pauze` niet verhoudingsgewijs kleiner? Bijvoorbeeld:

```python
pauze = pauze * 0.8
```

Dit maakt `pauze` 80% van de vorige waarde. Op deze manier wordt het nooit `0`.

--- /collapse ---
