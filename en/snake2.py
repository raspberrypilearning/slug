from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Variables -----------------------
slug = [ [2,4], [3,4], [4,4] ]
white = (255, 255, 255)

# Functions -----------------------

def draw_slug():
  for segment in slug:
      sense.set_pixel(segment[0], segment[1], white)

# Main program --------------------

