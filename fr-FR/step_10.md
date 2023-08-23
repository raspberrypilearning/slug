## Fin de la partie

La dernière chose que tu dois vérifier lorsque la limace se déplace vers un nouveau pixel est de savoir si elle va mordre dans son propre corps. Si cela se produit, elle mourra et le joueur perdra la partie. La manière de procéder est très similaire à celle utilisée pour vérifier si la limace mange un légume.

+ Dans la section des variables, crée une nouvelle variable booléenne appelée `mort` et initialise-la à `False` (pour que la limace ne démarre pas morte !).

+ Dans la fonction `deplace()`, ajoute du code pour vérifier si le prochain pixel vers lequel la limace se déplace fait partie d'elle-même.

+ Si c'est le cas, définis la variable `mort` sur `True`. Te souviens-tu de ce que tu dois faire pour permettre à une fonction de modifier une variable globale ?

--- hints ---
--- hint ---

Voici le code que tu as utilisé pour vérifier si le pixel vers lequel se dirigeait la limace contenait un légume :

```python
if suivant in legumes :
    # Faire des choses concernant les legumes
```

Peux-tu utiliser un code similaire pour vérifier si le pixel suivant fait partie de la limace ?

--- /hint ---
--- hint ---

Voici à quoi devrait ressembler ton code. Assure-toi de l'ajouter à la fonction `deplace()` **au-dessus** du code qui ajoute les pixels`suivants` à la liste `limace`, sinon tu seras définitivement mort !

```python
if suivant in limace:
    mort = True
```

--- /hint ---
--- /hints ---


Enregistre et exécute ton code. Lorsque tu fais mordre la limace elle-même maintenant, tu verras que le jeu ne se termine pas, même si la variable `mort` est changée en `True` !

+ Modifie la boucle de jeu dans le programme principal d'une boucle infinie à une boucle qui ne s'exécute que lorsque la variable `mort` n'est pas `True`.

Une fois la boucle de jeu terminée, le joueur voudra savoir comment il s'en est sorti dans sa partie.

+ Dans le programme principal, ajoute du code pour afficher le nombre de légumes vers lesquels le joueur a guidé la limace en utilisant la variable `score`.

[[[rpi-sensehat-show-message]]]
