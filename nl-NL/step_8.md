## Groenten eten

Je slak lijkt de groenten al op te eten - geweldig! Je hebt echter waarschijnlijk ontdekt dat, zodra ze de eerste drie groenten heeft gegeten, er nooit meer groenten verschijnen, ongeacht hoe lang je wacht.

**Kun je achterhalen waarom dit zo is?**

--- collapse ---
---
title: Antwoord
---

Omdat de functie `maak_groente` alleen groenten genereert als de lijst met `groenten` minder dan drie items bevat, worden er geen nieuwe groenten meer weergegeven zodra de lijst drie groenten bevat.

Op dit moment worden je eerste drie groenten gegenereerd en toegevoegd aan de lijst met `groenten`. Wanneer de slak naar een pixel met een groente gaat, verdwijnt de groente omdat de functie `beweeg` de pixels van de slak eroverheen plaatst. Dit is de reden waarom de naaktslak het lijkt op te eten. De groente wordt echter nooit verwijderd uit de lijst met `groenten`, dus de functie `maak_groente` mag niet meer maken.

--- /collapse ---

+ Voeg code toe aan het einde van de functie `beweeg()` zodat, telkens wanneer de slak naar een nieuwe pixel wordt verplaatst, de functie controleert of die pixel in de lijst met `groenten` staat. Als de pixel in de lijst `groenten` staat, verwijder je deze uit de lijst.

Laten we ook een score toevoegen om bij te houden hoeveel groenten de slak heeft gegeten, zodat de speler weet hoe goed ze het hebben gedaan als hun ronde is afgelopen.

+ Maak in de sectie met variabelen een variabele met `score` die begint met `0`.

+ Telkens als de slak een groente eet, tel 1 op bij de score. Vergeet niet dat, omdat de variabele `score` buiten de functie is gemaakt, je moet opgeven dat je `global score` wilt gebruiken aan het begin van de functie `beweeg()`, zodat de functie het mag veranderen.

--- hints --- --- hint ---

Hier is wat pseudocode voor de controle die zou moeten plaatsvinden binnen de functie `beweeg()`:

`als` nieuwe pixel `in` groenten zit `verwijder` nieuwe pixel uit groenten `voeg` 1 toe aan de score

--- /hint --- --- hint ---

Hier is de code die je moet toevoegen aan het einde van de functie `beweeg()`:

```python
if volgende in groenten:
  groenten.remove(volgende)
  score += 1
```

Vergeet niet ook `global score` toe te voegen op de eerste regel van de functie `beweeg()` en de variabele `score` te initialiseren op `0` in het gedeelte met variabelen.

--- /hint --- --- /hints ---
