from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Variabelen ---------------------------
naaktslak = [[2,4], [3,4], [4,4]]
wit = (255, 255, 255)
leeg = (0, 0, 0)
rood = (255, 0, 0)
richting = "right"
groenten = []
score = 0
pauze = 0,5
dood = False

# Functies ---------------------------
def teken_naaktslak():
  for segment in naaktslak:
    sense.set_pixel (segment[0], segment[1], wit)

def beweeg():
  global score, pauze, dood
  verwijder = True

  # Zoek de laatste en eerste items in de naaktslakkenlijst
  laatste = naaktslak[-1]
  eerste = naaktslak[0]
  volgende = list(laatste) # Maak een kopie van het laatste item

  # Zoek de volgende pixel in de richting waarin de slak momenteel beweegt
  if richting == "right":

    # Beweeg langs de kolom
    if laatste[0] + 1 == 8:
      volgende[0] = 0
    else:
      volgende[0] = laatste[0] + 1

  elif richting == "left":

    als laatste[0] - 1 == -1:
      volgende[0] = 7
    else:
      volgende[0] = laatste[0] - 1

  elif richting == "down":

    if laatste[1] + 1 == 8:
      volgende[1] = 0
    else:
      volgende[1] = laatste[1] + 1

  elif richting == "up":

    als laatste[1] - 1 == -1:
      volgende[1] = 7
    else:
      volgende[1] = laatste[1] - 1

  # Ben ik doodgegaan?
  if volgende in naaktslak:
    dood = True

  # Voeg deze pixel toe aan het einde van de naaktslakkenlijst
  naaktslak.append(volgende)

  # Stel de nieuwe pixel in op de kleur van de naaktslak
  sense.set_pixel(volgende[0], volgende[1], wit)

  if volgende in groenten:
    groeten.remove(volgende)
    score += 1

    if score % 5 == 0:
      verwijder = False
      pauze = pauze * 0.8

  if verwijder == True:
    # Stel de eerste pixel in de naaktslakkenlijst in op leeg
    sense.set_pixel(eerste[0], eerste[1], leeg)

    # Verwijder de eerste pixel uit de lijst
    naaktslak.remove(eerste)


def joystick_moved (event):
  global richting
  richting = event.direction

def maak_groente():
  nieuw = naaktslak[0]
  while nieuw in naaktslak:
    x = randint(0, 7)
    y = randint(0, 7)
    nieuw = [x, y]
  sense.set_pixel(x, y, rood)
  groenten.append(nieuw)

# Hoofdprogramma ------------------------
sense.clear()
teken_naaktslak()

sense.stick.direction_any = joystick_moved

while not dood:
  beweeg()
  sleep(pauze)

  # Heb een kans van 20% om een groente te maken als er niet veel over zijn
  if len(groenten) < 3 and randint(1, 5) > 4:
    maak_groente()

sense.show_message( str(score) )
