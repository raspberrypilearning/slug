## Manger des légumes

Ta limace semble déjà manger les légumes, c'est super ! Cependant, tu as probablement constaté qu'une fois qu'elle a mangé les trois premiers légumes, plus aucun légume n'apparaît, quel que soit le temps d'attente.

**Sais-tu pourquoi ?**

--- collapse ---
---
title: Réponse
---

Étant donné que la fonction `faire_legumes` ne génère des légumes que si la liste `legumes` contient moins de trois éléments, aucun nouveau légume n'apparaîtra une fois que la liste contiendra trois légumes.

Pour le moment, tes trois premiers légumes sont générés et ajoutés à la liste `legumes`. Lorsque la limace se déplace vers un pixel contenant un légume, le légume disparaît car la fonction `deplace` dessine les pixels de la limace par-dessus. C'est pourquoi la limace semble le manger. Cependant, le légume n'est jamais supprimé de la liste `legumes`, donc la fonction `faire_legumes` n'est pas autorisée à en faire plus.

--- /collapse ---

+ Ajoute du code à la fin de la fonction `deplace()` afin que, chaque fois que la limace se déplace vers un nouveau pixel, la fonction vérifie si ce pixel se trouve dans la liste `legumes`. Si le pixel est dans la liste `legumes`, supprime-le de la liste.

Ajoutons également un score pour comptabiliser le nombre de légumes que la limace a mangés, afin que le joueur sache ce qu'il a fait à la fin de son tour.

+ Dans la section des variables, crée une variable `score` qui commence à `0`.

+ Chaque fois que la limace mange un légume, ajoute 1 au score. N'oublie pas que, comme la variable `score` a été créée en dehors de la fonction, tu dois spécifier que tu veux utiliser `global score` au début de la fonction `deplace()` pour que la fonction soit autorisée à le changer.

--- hints ---
--- hint ---

Voici un pseudo-code pour la vérification qui devrait se produire dans la fonction `deplace()`:

`si` nouveau pixel est `dans` légumes
`enlever` nouveau pixel des légumes
`ajouter` 1 à score

--- /hint ---
--- hint ---

Voici le code que tu dois ajouter à la fin de la fonction `deplace()` :

```python
if suivant in legumes:
  legumes.remove(suivant)
  score += 1
```

N'oublie pas d'ajouter également `global score` sur la première ligne de la fonction `deplace()`, et d'initialiser la variable `score` à `0` dans la section des variables.

--- /hint ---
--- /hints ---
