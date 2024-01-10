## Comer verduras

Tu babosa ya parece comerse las verduras. ¡Genial! Sin embargo, probablemente hayas descubierto que, una vez que ha comido las tres primeras verduras, no aparecen más verduras, independientemente de cuánto tiempo esperes.

**¿Puedes determinar por qué pasa esto?**

--- collapse ---
---
title: Respuesta
---

Dado que la función `crear_verdura` solo genera verduras si la lista `verduras` contiene menos de tres elementos, no aparecerán nuevas verduras una vez que la lista contenga tres verduras.

Por el momento, tus primeras tres verduras se generan y se agregan a la lista `verduras`. Cuando la babosa se mueve a un pixel que contiene una verdura, la verdura desaparece porque la función `mover()` dibuja los pixeles de la babosa sobre ella. Por eso la babosa parece comérsela. Sin embargo, la verdura nunca es eliminada de la lista `verduras`, por lo que la función `crear_verdura` no puede crear más.

--- /collapse ---

+ Agrega un poco de código al final de la función `mover()` para que, cada vez que la babosa se mueva a un nuevo pixel, la función verifique si ese pixel está en la lista `verduras`. Si el pixel está en la lista `verduras`, elimínalo de la lista.

Agreguemos también un puntaje para monitorear cuántas verduras se ha comido la babosa, de modo que el jugador sepa qué tan bien lo ha hecho al terminar su ronda.

+ En la sección de variables, crea una variable `puntaje` que comience en `0`.

+ Cada vez que la babosa se coma una verdura, suma 1 al puntaje. No olvides que, debido a que la variable `puntaje` ha sido creada fuera de la función, debes especificar que quieres usar `puntaje global` al comienzo de la función `mover()` para que la función pueda cambiarla.

--- hints ---
--- hint ---

Aquí hay un poco de pseudocódigo para la verificación que debería ocurrir dentro de la función `mover()`:

`Si` hay nuevo pixel `en` verduras
`eliminar` nuevo pixel en verduras
`agregar` 1 a puntaje

--- /hint ---
--- hint ---

Aquí está el código que debes agregar al final de la función `mover()`:

```python
if siguiente in verduras:
  verduras.remove(siguiente)
  puntaje += 1
```

No olvides agregar también `global puntaje` en la primera línea de la función `mover()` e inicializar la variable `puntaje` a `0` en la sección de variables.

--- /hint ---
--- /hints ---
