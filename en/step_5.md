## Move the slug

Next, let's make the slug move. The slug will always be moving, and will only change direction when the player specifies it. Therefore, you need to store the direction in which the slug is moving.

+ In the variables section, create a variable called `direction`. The slug will begin the game moving right, so initialise this variable to the string `"right"`.

You also need a way to 'erase' pixels, so you can turn off an LED once the slug has moved on.

+ Create a variable called `blank`, and set it to the RGB colour `(0, 0, 0)`.

We stored the pixel coordinates of the slug's current position in a list, so that we can now follow this process to move the slug:

![Move right](images/move-right.png)

+ Find the last item in the `slug` list (`[4, 4]`)
+ Find the next pixel in the `direction` in the slug is currently moving (`[5, 4]`)
+ Add this pixel at the end of the `slug` list
+ Set this pixel to the slug's colour
+ Set the first pixel in the `slug` list (`[2, 4]`) to `blank`
+ Remove this pixel from the list

This algorithm works even when the player changes the direction of the slug. When that happens, the slug's body will simply bend to point in the new direction.

The slug is actually a **queue** data structure.

--- collapse ---
---
title: What is a queue?
---
A queue is a data structure where the first piece of data added is the first piece of data to come out. It is also called a FIFO or 'first in, first out' data structure. This is like waiting in a supermarket to pay for your shopping: you join the queue at the back, and the person at the front gets to pay for their items first and then leaves the queue.

Imagine the pixels of the slug are bits of food queuing up to be pooped out of the slug. The first item in the list is at the front of the queue, which is the back of the slug: this item will exit the slug and be deleted. New pixels join the slug queue at the end, which is where the mouth of the slug is. They gradually work their way towards the front of the queue as the slug moves.
--- /collapse ---

+ In the functions section, create a function called `move()`.

+ In the main program section, create an infinite loop which calls this function followed by a `sleep(0.5)`. Once you've written the code for the function, this loop will make the slug continually move around the screen.

[[[generic-python-while-true]]]

Here is some code to start off the `move()` function. It **does not** work properly yet.

+ Copy this code into your function and run the program. We used the colour variable `white` for the slug, but if you chose a different variable name (e.g. `blue`), you will need to change the name in the code. Look at what happens to the slug.

```python
def move():
  # Find the last and first items in the slug list
  last = slug[-1]
  first = slug[0]
  next = list(last)     # Create a copy of the last item

  # Find the next pixel in the direction the slug is currently moving
  if direction == "right":

    # Move along the column
    next[0] = last[0] + 1

  # Add this pixel at the end of the slug list
  slug.append(next)

  # Set the new pixel to the slug's colour
  sense.set_pixel(next[0], next[1], white)

  # Set the first pixel in the slug list to blank
  sense.set_pixel(first[0], first[1], blank)

  # Remove the first pixel from the list
  slug.remove(first)
```

+ Run the program and look at what happens to the slug.

+ Fix the code so that when the slug reaches the right-hand wall, instead of the code crashing, the slug 'moves through' the wall and reappears at the same y coordinate but on the opposite side of the screen.

![Wrap the slug](images/wrap-slug.gif)

--- hints ---
--- hint ---
Examine this code:
```python
# Move along the column
next[0] = last[0] + 1
```
If we always add 1 to the x coordinate, eventually it will reach 8. The LED matrix only has LEDs 0-7 along each axis — 8 doesn't exist, which is why the code crashes. How could you check if the `value of the x coordinate + 1` would be 8, and in that case set it to 0 instead to make the slug move through the wall?
--- /hint ---

--- hint ---
Here is some pseudo code to help you:

`if` `last[0]` + 1 `equals` 8
  `next[0]` `equals` 0
`else`
  `next[0]` `equals` `last[0]` + 1
--- /hint ---

--- hint ---
Here is how you code might look, but there are lots of different ways you could successfully write this section:

```python
# Move along the column
if last[0] + 1 == 8:
 next[0] = 0
else:
 next[0] = last[0] + 1
```
--- /hint ---
--- /hints ---

+ Add some more code to make the slug able to move up, down, and left. This code will be very similar to the code for moving right, but you'll need to work out which coordinate needs to change and whether to add or subtract 1.

--- hints ---
--- hint ---
Add an `elif` statement to check whether the direction equals `"left"`. Then check whether moving the slug would result in the x coordinate being outside LED matrix, e.g. `-1`. If that would be the case, set the x coordinate to `7` to make the slug move to the opposite side of the screen.

You can test your program by changing the value of the `direction` variable to `"left"`. Note: because this causes the slug to reverse, the slug may appear to behave oddly for the first few moves, but it will then behave normally.
--- /hint ---

--- hint ---
The up and down directions work exactly the same as left and right, except that you will be examining the `y` coordinate instead: `last[1]` and `next[1]`.
--- /hint ---

--- hint ---
Here is how your code might look. Again, there are lots of potential solutions, so your code might look different and work correctly anyway.

```python
# Find the next pixel in the direction the slug is currently moving
 if direction == "right":
   if last[0] + 1 == 8:
     next[0] = 0
   else:
     next[0] = last[0] + 1

 elif direction == "left":
   if last[0] - 1 == -1:
     next[0] = 7
   else:
     next[0] = last[0] - 1

 elif direction == "down":
   if last[1] + 1 == 8:
     next[1] = 0
   else:
     next[1] = last[1] + 1

 elif direction == "up":
   if last[1] - 1 == -1:
     next[1] = 7
   else:
     next[1] = last[1] - 1
```

--- /hint ---
--- /hints ---
