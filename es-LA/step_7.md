## Crea verduras

Nuestra babosa tiene hambre, ¡y necesita algo de comer! Vamos a generar algunas verduras para ella en ubicaciones aleatorias en la matriz LED.

![Verduras](images/vegetables.png)

Crear las verduras es bastante sencillo:

1. Elige una coordenada aleatoria `x, y` en la matriz LED.
2. Comprueba si esta coordenada está actualmente habitada por la babosa.
3. Si es así, repite los pasos 1 y 2 hasta que escojas una ubicación que esté fuera de la babosa.
4. Dibuja la verdura en la matriz LED.

El código que necesitas es muy similar al que has escrito anteriormente para la babosa, así que intenta hacerlo tú mismo. Si te quedas atascado, usa las pistas.

+ Crea una nueva variable para definir el color de las verduras que vas a hacer. Puedes hacer esto de la misma manera que definiste el color de tu babosa.

### Crea la función

+ Define una nueva función llamada `crear_verdura()` en la sección de funciones. El código a poner dentro de la función se explica en los siguientes pasos.

+ Dentro de la función, escribe un poco de código para elegir una coordenada aleatoria en la matriz LED.

[[[generic-python-random]]]

--- hints ---
--- hint ---

Genera una coordenada "x" aleatoria y una coordenada "y" aleatoria, y luego ponlas juntas en una lista. Ambas coordenadas deben ser números aleatorios entre 0 y 7.

--- /hint ---
--- hint ---

Puedes usar la función `randint` para generar números aleatorios. Por ejemplo, este código genera un número aleatorio entre 5 y 10:

```python
a = randint(5, 10)
```

--- /hint ---
--- hint ---

Así es como debería verse tu código:

```python
x = randint(0, 7)
y = randint(0, 7)
nuevo = [x, y]
```

--- /hint ---
--- /hints ---


+ Verifica si esta coordenada `x, y` está en la lista `babosa`. Si es así, elige una nueva coordenada y compárala con la lista. Repite esto hasta que la coordenada que has elegido no esté en la lista.

[[[generic-python-item-in-list]]]

--- hints ---
--- hint ---

Aquí tienes un poco de pseudocódigo para ayudarte. Empecemos por configurar `nuevo` igual a la primera coordenada de la lista `babosa` para garantizar que comenzará dentro de la babosa. De esta manera, una nueva coordenada debe ser generada al menos una vez.

Configura `nuevo` con la primera coordenada de la lista `babosa`
`mientras` la coordenada está en la lista `babosa`:
configura "x" con un número aleatorio entre 0 y 7
configura "y" con un número aleatorio entre 0 y 7
configura `nuevo` con x, y

--- /hint ---

--- hint ---

Así es como podría verse tu código:

```python
nuevo = babosa[0]
while nuevo in babosa:
    x = randint(0, 7)
    y = randint(0, 7)
    nuevo = [x, y]
```

--- /hint ---
--- /hints ---

+ Una vez que hayas encontrado una coordenada `x, y` que no esté dentro de la babosa, dibuja la verdura en la pantalla usando tu nueva variable de color.

### Llama a la función

+ En tu programa principal, llama a la función `crear_verdura` y verifica que las verduras aparezcan al azar en la matriz LED.

Probablemente notarás que aparecen muchas verduras, ¡por lo que tu babosa se ve invadida rápidamente!

![Demasiadas verduras](images/too-many-veggies.gif)

¡Necesitas una forma de rastrear cuántas verduras hay para evitar esta peligrosa propagación de verduras!

## Haz un seguimiento de las verduras

+ Crea una nueva lista vacía llamada `verduras` en tu sección de variables.

+ Escribe una línea de código al final de tu función `crear_verdura` para agregar las coordenadas de la nueva verdura a tu lista `verduras`.

[[[generic-python-append-list]]]

+ Cambia la forma en que llamas a la función `crear_verdura` en el programa principal para que solo cree una nueva verdura si hay menos de tres elementos en la lista `verduras`.

--- hints ---
--- hint ---

Puedes usar la función `len()` para averiguar la longitud de la lista `verduras`, o en otras palabras, cuántos elementos hay en la lista.

--- /hint ---
--- hint ---

Aquí tienes un poco de pseudocódigo para ayudarte:

`si` la longitud de la lista de verduras es `menor que` 3
llamar a la función `crear_verdura`

--- /hint ---
--- hint ---

Así es como debería verse tu código:

```python
if len(verduras) < 3:
   crear_verdura()
```

--- /hint ---
--- /hints ---

### Desafío
¿Puedes cambiar tu código para que, si hay menos de 3 verduras en la lista, solo haya un 20% de posibilidades de crear una nueva verdura cada vez que se ejecute la función? Esto hará que sea menos predecible cuando puedan aparecer verduras. Para crear el 20% de probabilidad, elige al azar un número entre 1 y 5, y solo crea una verdura para un número específico en este rango.

--- collapse ---
---
título: Solución del desafío
---

```python
# Dejar que haya un 20% de probabilidad de crear una verdura si no hay muchas alrededor
if len(verduras) < 3 and randint(1, 5) > 4:
    crear_verdura ()
```

--- /collapse ---
