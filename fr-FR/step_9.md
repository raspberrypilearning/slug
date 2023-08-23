## Grandir et accélérer

Pour que le jeu reste intéressant pour le joueur, quand la limace mange des légumes, elle doit grandir et se déplacer plus rapidement. Cela la rend plus difficile à contrôler, et pire, elle pourrait accidentellement mordre dans son propre corps !

Le code que tu as écrit jusqu'à présent fait en sorte que, lorsque la limace avance d'un pixel, son segment final est supprimé. Pour lui permettre de grandir, tu peux ajouter un nouveau segment à la liste `limace` mais **pas** supprimer le dernier. Ainsi, chaque fois que la limace se déplace, tu dois prendre une décision quant à la suppression ou non d'un segment.

+ Au début de la fonction `deplace()`, crée une variable booléenne appelée `supprimer` et définis-la sur `True`, car la plupart du temps, nous voulons supprimer le segment de fin lorsque la limace se déplace.

+ Ajoute une instruction conditionnelle à ta fonction pour que les deux lignes suivantes ne soient exécutées que `si` la variable `supprimer` est `True`.

```python
sense.set_pixel(premier[0], premier[1], vide)
limace.remove(premier)
```

+ Décide à quelle fréquence tu veux que ta limace grandisse. Dans notre exemple, nous avons choisi pour notre limace de faire pousser un segment pour 5 légumes qu'elle mange.

Pour aider ton programme à décider quand déclencher la croissance de la limace, tu peux utiliser l'opérateur **mod** `%`. En l'utilisant, tu peux déterminer si le score actuel est un multiple de 5.

[[[generic-python-mod-operator]]]

Tu voudras t'assurer que la limace ne peut pousser que lorsqu'elle a mangé un légume. Pour ce faire, tu dois ajouter ton nouveau code pour potentiellement développer la limace à l'intérieur de cette instruction `if` :

```python
if suivant in legumes:
```

+ Ajoute du code pour vérifier si le score actuel est un multiple de 5. Si c'est le cas, définis `supprimer` sur `False` afin qu'aucun segment ne soit supprimé.

+ Enregistre et exécute le code. Tu pourrais être déçu de voir que lorsque tu manges 5 légumes, la limace ne grandit pas ! Pourquoi pas ?

--- collapse ---
---
title: Réponse
---

Le code pour supprimer le segment s'exécute actuellement avant le code pour vérifier si le nouveau pixel était un légume. Cela signifie que le programme ne se soucie pas de savoir si nous lui avons dit de supprimer ou non un segment, car au moment où cette décision est prise, le segment a déjà été supprimé !

--- /collapse ---

+ Modifie l'ordre du code afin que la dernière chose dans la fonction `deplace()` soit le code permettant de supprimer potentiellement un segment. Teste à nouveau et tu devrais voir ta limace grandir.

En plus de mettre `supprimer` à `False` pour faire grandir la limace, accélérons-la ! Actuellement, la vitesse de la limace est régulée par cette ligne de code dans le programme principal :

```python
sleep(0.5)
```

Cette commande indique à ta boucle infinie d'attendre une demi-seconde entre chaque exécution, de sorte que la limace se déplace à une vitesse d'un pixel par demi-seconde. Pour le faire avancer plus vite, tu voudras diminuer progressivement cette pause.

+ Dans la section des variables, crée une variable appelée `pause` et définis-la sur `0.5`.

+ Remplace le `0.5` entre parenthèses de la fonction `sleep()` par la variable `pause`. Maintenant, la vitesse de la limace sera déterminée par la valeur de `pause`.

Tu as déjà ajouté du code à la section qui vérifie si le score actuel est un multiple de 5, afin que ta limace puisse grandir. C'est aussi le point où la valeur de `pause` devrait devenir plus petite. Modifie ta fonction `deplace` comme ceci :

```python
global pause

if score % 5 == 0:
    supprimer = False
    pause = pause - 0.1
```

+ Enregistre et exécute ton programme. Que se passe-t-il ? Pourquoi ce code n'est-il pas une très bonne idée, et comment pourrais-tu l'améliorer ?

--- collapse ---
---
title: Réponse
---

Si `pause` commence à `0.5`, et que nous soustrayons `0.1` pour cinq légumes consommés, `pause` deviendra éventuellement `0`. Cela rendra le jeu impossible !

Au lieu de soustraire un montant fixe, pourquoi ne pas faire `pause` proportionnellement plus petit ? Par exemple :

```python
pause = pause * 0.8
```

Cela fera `pause` 80 % de sa valeur précédente. De cette façon, il ne deviendra jamais `0`.

--- /collapse ---
