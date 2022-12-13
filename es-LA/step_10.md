## Fin del juego

Lo último que debes verificar cuando la babosa se mueva a un nuevo pixel es si morderá su propio cuerpo. Si esto sucede, ella morirá y el jugador perderá el juego. La forma de hacer esto es muy similar a cómo verificaste si la babosa está comiendo una verdura.

+ En la sección de variables, crea una nueva variable booleana llamada `muerta` e inicialízala en `False` (¡para que la babosa no empiece el juego muerta!).

+ Dentro de la función `mover()`, agrega un poco de código para verificar si el siguiente pixel al que se mueve la babosa es parte de sí misma.

+ Si es así, configura la variable `muerta` como `True`. ¿Recuerdas lo que debes hacer para permitir que una función altere una variable global?

--- hints --- --- hint ---

Aquí está el código que usaste para verificar si el pixel al que se movía la babosa contenía una verdura:

```python
if siguiente in verduras:
    # Hacer cosas relacionadas con verduras
```

¿Puedes usar un código similar para verificar si el siguiente pixel es parte de la babosa?

--- /hint --- --- hint ---

Así es como debería verse tu código. Asegúrate de agregarlo a la función `mover()` **arriba** del código que agrega el `siguiente` pixel a la lista `babosa`, de lo contrario, ¡estarás permanentemente muerto!

```python
if siguiente in babosa:
    muerta = True
```

--- /hint --- --- /hints ---


Graba y ejecuta tu código. Ahora, cuando hagas que la babosa se muerda a sí misma, verás que el juego no termina, ¡aunque la variable `muerta` cambie a `True`!

+ Cambia el ciclo del juego en el programa principal de un bucle infinito a un bucle que solo se ejecute mientras la variable `muerta` no sea `True`.

Una vez que finaliza el ciclo del juego, el jugador querrá saber cómo le fue en su juego.

+ En el programa principal, agrega código para mostrar cuántas verduras comió la babosa, haciendo uso de la variable `puntaje`.

[[[rpi-sensehat-show-message]]]
