from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

# Variables -----------------------
snake = [ [2,4], [3,4], [4,4] ]
veggies = []
score = 0
dead = False
white = (255, 255, 255)
blank = (0, 0, 0)
red = (255, 0, 0)
speed = 0.5
add_segment = False
direction = "right"


# Functions -----------------------
def joy_move(event):
  global direction
  direction = event.direction

def move(direction):
  global score, speed, add_segment
  # Get head element
  head = snake[-1]
  new = []
  
  if direction == "up":
    new.append(head[0])
    if (head[1] -1) >= 0:
      new.append(head[1] - 1)
    else:
      new.append(7) # Screen wrap
    
  elif direction == "down":
    new.append(head[0])
    if (head[1] + 1) <= 7:
      new.append(head[1] + 1)
    else:
      new.append(0)
  
  elif direction == "left":
    if (head[0] -1) >= 0:
      new.append(head[0] - 1)
    else:
      new.append(7)
    new.append(head[1])
  
  elif direction == "right":
    if (head[0] + 1) <= 7:
      new.append(head[0] + 1)
    else:
       new.append(0)
    new.append(head[1])
    
  # Did I eat a veggie?
  if new in veggies:
    score += 1
    
    # Remove veggie
    veggies.remove(new)
    
    # Speed up every multiple of 5 score
    if score % 5 == 0:
      speed -= 0.05
      add_segment = True
      print("Add a segment")
  
  # Did I eat myself?
  if new in snake:
    return False
  else:
    return new
    
def draw_snake():
  for segment in snake:
      sense.set_pixel(segment[0], segment[1], white)

def make_veg():
  new = snake[0]
  while new in snake:
    x = randint(0, 7)
    y = randint(0, 7)
    new = [x, y]
  sense.set_pixel(x, y, red)
  veggies.append(new)
  

# Main program -----------------------
sense.clear()

# Capture joystick events      
sense.stick.direction_any = joy_move

# Game loop
while not dead:
  print(add_segment)
  sleep(speed)
  moved = move(direction)
  if moved != False:
    snake.append(moved)
    
    old = snake[0]
    sense.set_pixel(old[0], old[1], blank)
    
    if add_segment == False:
      del snake[0] # Delete last item
    else:
      add_segment = False
      
  else:
    dead = True
    
  # Draw the snake 
  draw_snake()
  
  # Have a 20% chance of making a veggie if there aren't many about
  if len(veggies) < 3 and randint(1, 10) > 8:
    make_veg()
  
# You lost
sense.clear()
sense.show_message(str(score))
