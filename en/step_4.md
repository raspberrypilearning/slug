## Draw the slug

The first job is to draw the slug on the Sense HAT's LED display. It is important to keep track of which pixels the slug is inhabiting so that we can move her around the screen

![Draw the slug](images/draw-slug.png)

To be able to light up a pixel on the LED display, we need to specify three things - the x and y coordinates of the pixel and the colour we would like.

[[[rpi-sensehat-led-coordinates]]]

+ In the variables section, create an empty list called `slug` which we will use to store the x, y coordinates of the pixels which will make up the slug.

[[[generic-python-create-list]]]

+ Choose three pixels in a horizontal row. Each pixel's position will be represented as a list containing its x,y coordinate. For example, we chose the pixels [2,4], [3,4] and [4,4].

+ Add three lists to your `slug` list to define the coordinates where the slug will start. You have now created a 2D list, or a list of lists!

We also need to specify a colour for the slug.

+ In the variables section, create a variable to store the RGB colour of your slug. We chose white, but you can choose any colour you like.

```python
white = (255, 255, 255)
```

[[[generic-theory-colours]]]

+ In the functions section, create a function called `draw_slug()` where we will put the code to draw the slug.

[[[generic-python-simple-functions]]]

+ Inside your `draw_slug()` function, add a `for` loop to loop through each element in the `slug` list.

Each of the x, y coordinates in the list represents a segment of the slug.

+ Use the `set_pixel` method to light up each pixel on the LED display, thus drawing the slug.

--- hints ---
--- hint ---
The `set_pixel` method requires three arguments - the x coordinate of the pixel, the y coordinate of the pixel and the colour.
--- /hint ---

--- hint ---
Your `for` loop will examine each segment of the slug in turn. If you wrote your loop as

```python
for segment in slug:
```
...then `segment[0]` will be the x coordinate of the segment you are currently looking at.
--- /hint ---

--- hint ---
Here is how your code might look:

```python
def draw_slug():
  for segment in slug:
      sense.set_pixel(segment[0], segment[1], white)
```
--- /hint ---
--- /hints ---

If you run your program at this point, nothing will happen. This is because we haven't _called_ the function, so the code will not execute.

+ In the main program section, call the function by adding the following code:

```python
draw_slug()
```

+ Run your program and check that you see three pixels in a row light up to form your slug.
