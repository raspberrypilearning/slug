## Créer des légumes

Notre limace a faim, elle a donc besoin de quelque chose à manger ! Nous allons générer des légumes pour elle à des endroits aléatoires sur la matrice LED.

![Légumes](images/vegetables.png)

La création des légumes est assez simple :

1. Choisir une coordonnée aléatoire `x, y` sur la matrice LED
2. Vérifier si cette coordonnée est actuellement occupée par la limace
3. Si c'est le cas, répéter les étapes 1 et 2 jusqu'à ce que tu choisisses un emplacement qui se trouve en dehors de la limace
4. Dessiner le légume sur la matrice LED

Le code dont tu as besoin est un code très similaire que tu as écrit précédemment pour la limace, alors essaie de le faire par toi-même. Si tu es bloqué, utilise les indices.

+ Crée une nouvelle variable pour définir la couleur des légumes que tu vas créer. Tu peux le faire de la même manière que tu as défini la couleur de ta limace.

### Créer la fonction

+ Définis une nouvelle fonction appelée `faire_legumes()` dans ta section de fonctions. Le code à mettre dans la fonction est expliqué dans les étapes suivantes.

+ À l'intérieur de la fonction, écris du code pour choisir une coordonnée aléatoire sur la matrice LED.

[[[generic-python-random]]]

--- hints ---
--- hint ---

Génére une coordonnée x aléatoire et une coordonnée y aléatoire, puis rassemble-les dans une liste. Les deux coordonnées doivent être des nombres aléatoires entre 0 et 7.

--- /hint ---
--- hint ---

Tu peux utiliser la fonction `randint` pour générer des nombres aléatoires. Par exemple, ce code génère un nombre aléatoire entre 5 et 10 :

```python
a = randint(5, 10)
```

--- /hint ---
--- hint ---

Voici à quoi devrait ressembler ton code :

```python
x = randint(0, 7)
y = randint(0, 7)
nouveau = [x, y]
```

--- /hint ---
--- /hints ---


+ Vérifie si cette coordonnée `x, y` est dans la liste `limace`. Si c'est le cas, choisis une nouvelle coordonnée et compare-la à la liste. Répéte cette opération jusqu'à ce que la coordonnée que tu as choisie ne soit pas dans la liste des limaces.

[[[generic-python-item-in-list]]]

--- hints ---
--- hint ---

Voici un pseudo-code pour t'aider. Nous commençons par définir `nouveau` égal à la première coordonnée de la liste `limace` afin qu'il soit garanti de commencer à l'intérieur de la limace. De cette façon, une nouvelle coordonnée doit être générée au moins une fois.

Définir `nouveau` sur la première coordonnée dans la liste `limace` `tandis que` la coordonnée est dans la liste `limace` : définir x sur un nombre aléatoire entre 0 et 7 définir y sur un nombre aléatoire entre 0 et 7 mettre `nouveau` à x, y

--- /hint ---

--- hint ---

Voici à quoi ton code pourrait ressembler :

```python
nouveau = limace[0]
while nouveau in limace:
    x = randint(0, 7)
    y = randint(0, 7)
    nouveau = [x, y]
```

--- /hint ---
--- /hints ---

+ Une fois que tu as trouvé une coordonnée `x, y` qui n'est pas à l'intérieur de la limace, dessine le légume à l'écran en utilisant ta nouvelle variable de couleur.

### Appeler la fonction

+ Dans ton programme principal, appelle la fonction `faire_legumes` et vérifie que les légumes apparaissent au hasard sur la matrice LED.

Tu remarqueras sans doute que pas mal de légumes apparaissent, donc ta limace est vite envahie !

![Trop de légumes](images/too-many-veggies.gif)

Tu as besoin d'un moyen de suivre le nombre de légumes, afin d'éviter cette dangereuse propagation des légumes !

## Garder la trace des légumes

+ Crée une nouvelle liste vide appelée `legumes` dans ta section de variables.

+ Écris une ligne de code à la fin de ta fonction `faire_legumes` pour ajouter les coordonnées du nouveau légume à ta liste `legumes`.

[[[generic-python-append-list]]]

+ Change la façon dont tu appelles la fonction `faire_legumes` dans le programme principal afin qu'elle ne crée un nouveau légume que s'il y a moins de trois éléments dans la liste `legumes`.

--- hints ---
--- hint ---

Tu peux utiliser la fonction `len()` pour connaître la longueur de la liste `legumes`, ou en d'autres termes, combien d'éléments sont dans la liste.

--- /hint ---
--- hint ---

Voici un pseudo-code pour t'aider :

`si` la longueur de la liste des légumes est `inférieure à` 3 Appeler la fonction `faire_legumes`

--- /hint ---
--- hint ---

Voici à quoi devrait ressembler ton code :

```python
if len(legumes) < 3:
   faire_legumes()
```

--- /hint ---
--- /hints ---

### Défi
Peux-tu modifier ton code pour que, s'il y a moins de 3 légumes dans la liste, il n'y ait que 20 % de chances de créer un nouveau légume à chaque exécution de la fonction ? Cela rendra moins prévisible le moment où les légumes pourraient apparaître. Pour créer une chance de 20 %, choisis aléatoirement un nombre entre 1 et 5 et ne crée un légume que pour un nombre spécifique dans cette gamme.

--- collapse ---
---
title: Solution du défi
---

```python
# Laisser 20% de chance de faire un legume s'il n'y en a pas beaucoup 
if len(legumes) < 3 and randint(1, 5) > 4 :
    faire_legumes()
```

--- /collapse ---
