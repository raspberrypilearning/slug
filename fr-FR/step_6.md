## Utiliser le joystick

Ensuite, connectons le joystick du Sense HAT afin que le joueur puisse l'utiliser pour contrôler le mouvement de la limace.

![Limace en mouvement](images/moving-slug.gif)

+ Dans la section des fonctions, crée une nouvelle fonction :

```python
def joystick_mouvement(event):
```

Tu appelleras cette fonction chaque fois que le joystick sera déplacé. Il recevra automatiquement un paramètre appelé `event`, qui permettra de savoir dans quel sens le joystick a été déplacé.

Tu voudras régler la variable `direction` sur la direction dans laquelle le joystick a été poussé. Pour que tu sois autorisé à modifier la valeur de la variable à partir de cette fonction, tu dois spécifier `global` pour la variable. Pour savoir pourquoi, lis à propos de la portée dans les fonctions Python.

[[[generic-python-function-scope]]]

+ Ajoute `globale direction` à ta fonction :

```python
def joystick_mouvement(event):
    global direction
```

Tu peux accéder à la direction dans laquelle le joystick a été déplacé avec l'aide du paramètre `event` : utilise la commande `event.direction`.

+ Dans ta fonction, définis la variable `direction` pour qu'elle soit égale à `event.direction`.

+ Enfin, dans la partie principale de ton programme, écris une ligne de code pour dire que, lorsque le joystick Sense HAT est pressé dans n'importe quelle direction, la fonction `joystick_mouvement` sera appelée.

[[[rpi-python-sensehat-joystick-event-functions]]]

--- hints ---
--- hint ---

Tu peux découvrir comment procéder dans la section d'information « Déclencher des appels de fonction avec le joystick Sense HAT » ci-dessus.

--- /hint ---

--- hint ---

Le code à dire « quand le joystick est pressé dans n'importe quelle direction » est le suivant :

```python
sense.stick.direction_any =
```

--- /hint ---

--- hint ---

Voici à quoi devrait ressembler le code dans le **programme principal** :

```python
sense.stick.direction_any = joystick_mouvement
```

Voici le code complet de la **fonction** :
```python
def joystick_mouvement(event):
    global direction
    direction = event.direction
```

--- /hint ---

--- /hints ---

+ Exécute ton programme et teste qu'il fonctionne. Si tu utilises l'émulateur, tu peux simuler le déplacement du joystick en appuyant sur les touches fléchées de ton clavier.

À ce stade, il est possible de déplacer la limace « à travers » elle-même, ce qui semble plutôt étrange. Plus tard, nous ajouterons du code qui met fin au jeu si la limace se mord elle-même, donc il n'y a pas besoin de s'inquiéter pour résoudre ce problème.
