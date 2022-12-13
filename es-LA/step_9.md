## Crecer y acelerar

Para mantener el juego interesante para el jugador, mientras la babosa come verduras, ésta debería ir creciendo en longitud y e irse moviendo más rápido. Esto la hace más difícil de controlar, y lo que es peor, ¡podría morder accidentalmente su propio cuerpo!

El código que has escrito hasta ahora hace que, cuando la babosa avance un pixel se elimine su último segmento. Para permitirle crecer, puedes agregar un nuevo segmento a la lista `babosa` pero **no** eliminar el último. Por lo tanto, cada vez que la babosa se mueve, debes tomar una decisión sobre si eliminar un segmento o no.

+ Al comienzo de la función `mover()`, crea una variable booleana llamada `eliminar` y configúrala como `True`, ya que la mayoría de las veces queremos eliminar el último segmento cuando la babosa se mueve.

+ Agrega una sentencia condicional a tu función para que las siguientes dos líneas de código solo se ejecuten `si` la variable `eliminar` es `Verdad`.

```python
sense.set_pixel(primero[0], primero[1], vacio)
babosa.remove(primero)
```

+ Decide con qué frecuencia quieres que crezca tu babosa. En nuestro ejemplo, elegimos que nuestra babosa crezca un segmento por cada 5 verduras que coma.

Para ayudar a tu programa a decidir cuándo activar el crecimiento de la babosa, puedes usar el operador **mod** `%`. Al usarlo, puedes determinar si el puntaje actual es un múltiplo de 5.

[[[generic-python-mod-operator]]]

Querrás asegurarte de que la babosa solo pueda crecer cuando haya comido una verdura. Para hacer esto, deberías agregar tu nuevo código para hacer crecer potencialmente la babosa dentro de esta sentencia `if`:

```python
if siguiente in verduras:
```

+ Agrega código para verificar si el puntaje actual es múltiplo de 5. Si lo es, configura `eliminar` como `False` para que ningún segmento sea eliminado.

+ Graba y ejecuta el código. Puede que te decepcione ver que, cuando comes 5 verduras, ¡la babosa no crece! ¿Por qué no?

--- collapse ---
---
title: Respuesta
---

El código para eliminar el segmento se ejecuta actualmente antes del código para verificar si el nuevo pixel es una verdura. Esto significa que al programa no le importa si le hemos dicho que elimine o no un segmento, porque para el momento en que se toma esta decisión, ¡el segmento ya ha sido eliminado!

--- /collapse ---

+ Cambia el orden del código para que lo último en la función `mover()` sea el código para potencialmente eliminar un segmento. Prueba otra vez y deberías ver crecer tu babosa.

Además de configurar `eliminar` como `False` para hacer crecer la babosa, ¡vamos a acelerarla! Actualmente, la velocidad de la babosa está regulada por esta línea de código en el programa principal:

```python
sleep(0.5)
```

Este comando le dice a tu bucle infinito que espere medio segundo entre cada ejecución, de modo que la babosa se mueva a una velocidad de un pixel por medio segundo. Para hacer que se mueva más rápido, deberás disminuir gradualmente esta pausa.

+ En la sección de variables, crea una variable llamada `pausa` y configúrala como `0.5`.

+ Reemplaza el `0.5` entre los paréntesis de la función `sleep()` por la variable `pausa`. Ahora la velocidad de la babosa estará determinada por el valor de `pausa`.

Ya has agregado un poco de código a la sección que verifica si el puntaje actual es un múltiplo de 5, por lo que tu babosa puede crecer. Ese es también el punto en el que el valor de `pausa` debería hacerse más pequeño. Modifica tu función `mover` así:

```python
global pausa 

if puntaje% 5 == 0:
    eliminar = False
    pausa = pausa - 0.1
```

+ Guarda y ejecuta tu programa. ¿Qué ocurre? ¿Por qué no es bueno este código y cómo podrías mejorarlo?

--- collapse ---
---
title: Respuesta
---

Si `pausa` comienza en `0.5` y restamos `0.1` por cada cinco verduras comidas, `pausa` se convertirá finalmente en `0`. ¡Esto hará que el juego sea imposible!

En lugar de restar una cantidad fija, ¿por qué no hacer `pausa` proporcionalmente más pequeña? Por ejemplo:

```python
pausa = pausa * 0.8
```

Esto hará que `pausa` tenga 80% de su valor anterior. De esta manera, nunca se convertirá en `0`.

--- /collapse ---
