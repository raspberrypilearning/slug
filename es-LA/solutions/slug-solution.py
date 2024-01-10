from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Variables ---------------------------
babosa = [[2,4], [3,4], [4,4]]
blanco = (255, 255, 255)
vacio = (0, 0, 0)
rojo = (255, 0, 0)
direccion = "derecha"
verduras = []
puntaje = 0
pausa = 0.5
muerta = False

# Funciones ---------------------------
def dibujar_babosa():
  for segmento in babosa:
    sense.set_pixel(segmento[0], segmento[1], blanco)

def mover():
  puntaje global, pausa, muerta
  eliminar = True

  # Encontrar el último y el primer elemento en la lista babosa
  ultimo = babosa[-1]
  primero = babosa[0]
  siguiente = lista(ultimo) # Crea una copia del último elemento

  # Encontrar el siguiente pixel en la dirección en la que la babosa se está moviendo actualmente
  if direccion == "derecha":

    # Mover a lo largo de la columna
    if ultimo[0] + 1 == 8:
      siguiente[0] = 0
    else:
      siguiente[0] = ultimo[0] + 1

  elif direccion == "izquierda":

    if ultimo[0] - 1 == -1:
      siguiente[0] = 7
    else:
      next[0] = last[0] - 1

  elif direccion == "abajo":

    if ultimo[1] + 1 == 8:
      siguiente[1] = 0
    else:
      siguiente[1] = ultimo[1] + 1

  elif direccion == "arriba":

    if ultimo[1] - 1 == -1:
      siguiente[1] = 7
    else:
      siguiente[1] = ultimo[1] - 1

  # ¿He muerto?
  if siguiente in babosa:
    muerta = True

  # Agregar este pixel al final de la lista babosa
  babosa.append(siguiente)

  # Configurar el nuevo pixel con el color de la babosa
  sense.set_pixel(siguiente[0], siguiente[1], white)

  if siguiente in verduras:
    verduras.eliminar(siguiente)
    puntaje += 1

    if puntaje % 5 == 0:
      eliminar = False
      pausa = pausa * 0.8

  if eliminar == True:
    # Configurar el primer pixel en la lista babosa como vacío
    sense.set_pixel(primero[0], primero[1], vacio)

    # Eliminar el primer pixel de la lista
    babosa.remove(primero)


def palanca_de_mando_movida(event):
  direccion global
  direccion = event.direction

def crear_verdura():
  nuevo = babosa[0]
  while nuevo in babosa:
    x = randint(0, 7)
    y = randint(0, 7)
    nuevo = [x, y]
  sense.set_pixel(x, y, red)
  verduras.append(nuevo)

# Programa principal ------------------------
sense.clear()
dibujar_babosa()

sense.stick.direction_any = palanca_de_mando_movida

while not muerta:
  mover()
  sleep(pausa)

  # Ten un 20% de posibilidades de crear una verdura si no hay muchas alrededor
  if len(verduras) < 3 y randint(1, 5) > 4:
    crear_verdura()

sense.show_message( str(puntaje) )
