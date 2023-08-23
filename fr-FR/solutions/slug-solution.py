from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Variables ---------------------------
limace = [[2,4], [3,4], [4,4]]
blanc = (255, 255, 255)
vide = (0, 0, 0)
rouge = (255, 0, 0)
direction = "right"
legumes = []
score = 0
pause = 0.5
mort = False

# Fonctions ---------------------------
def dessiner_limace():
  for segment in limace:
    sense.set_pixel(segment[0], segment[1], blanc)

def deplace():
  global score, pause, mort
  supprimer = True

  # Trouver le dernier et le premier element de la liste limace
  dernier = limace[-1]
  premier = limace[0]
  suivant = list(dernier) # Créer une copie du dernier élément

  # Trouver le pixel suivant dans la direction de deplacement de la limace
  if direction == "right":

    # Se deplacer le long de la colonne
    if dernier[0] + 1 == 8:
      suivant[0] = 0
    else:
      suivant[0] = dernier[0] + 1

  elif direction == "left":

    if dernier[0] - 1 == -1:
      suivant[0] = 7
    else:
      suivant[0] = dernier[0] - 1

  elif direction == "down":

    if dernier[1] + 1 == 8:
      suivant[1] = 0
    else:
      suivant[1] = dernier[1] + 1

  elif direction == "up":

    if dernier[1] - 1 == -1:
      suivant[1] = 7
    else:
      suivant[1] = dernier[1] - 1

  # Suis-je mort ?
  if suivant in limace:
    mort = True

  # Ajouter ce pixel a la fin de la liste limace
  limace.append(suivant)

  # Definir le nouveau pixel sur la couleur de la limace
  sense.set_pixel(suivant[0], suivant[1], blanc)

  if suivant in legumes:
    legumes.remove(suivant)
    score += 1

    if score % 5 == 0:
      supprimer = False
      pause = pause * 0.8

  if supprimer == True:
    # Definir le premier pixel de la liste limace a vide
    sense.set_pixel(premier[0], premier[1], vide)

    # Supprimer le premier pixel de la liste
    limace.remove(premier)


def joystick_mouvement(event):
  global direction
  direction = event.direction

def faire_legumes():
  nouveau = limace[0]
  while nouveau in limace:
    x = randint(0, 7)
    y = randint(0, 7)
    nouveau = [x, y]
  sense.set_pixel(x, y, rouge)
  legumes.append(nouveau)

# Programme principal ------------------------
sense.clear()
dessiner_limace()

sense.stick.direction_any = joystick_mouvement

while not mort:
  deplace()
  sleep(pause)

  # Avoir 20% de chance de faire un legume s'il n'y en a pas beaucoup
  if len(legumes) < 3 and randint(1, 5) > 4:
    faire_legumes()

sense.show_message( str(score) )
