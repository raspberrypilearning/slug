## Create vegetables

Our slug is hungry, she needs something to eat! Let's generate some vegetables at random locations on the LED matrix.

Creating the vegetables is fairly straightforward:

1. Pick a random coordinate on the LED matrix
2. Check that this coordinate isn't somewhere inside the slug
3. If it is, pick a new location until you pick one that isn't inside the slug
4. If not, draw the vegetable
5. Keep track of this vegetable's location in a list

The code you need is all very similar to things we've done before with the slug, so why not see if you can do it yourself and use the hints if you get stuck.

+ Create a new empty list called `vegetables` in your variables section

+ Create a new function called `make_veg()`

+ Inside the function, write some code to pick a random coordinate on the LED matrix.

[[[generic-python-random]]]

--- hints ---
--- hint ---
Generate a random x coordinate and a random y coordinate and then put them together in a list. Both coordinates must be random numbers between 0 and 7.
--- /hint ---
--- hint ---
You can use the `randint` function to generate random numbers. For example, this code generates a random number between 5 and 10.

```python
a = randint(5, 10)
```
--- /hint ---
--- hint ---
Here is how your code should look:

```python
x = randint(0, 7)
y = randint(0, 7)
new = [x, y]
```
--- /hint ---
--- /hints ---


+ Check if this coordinate is in the slug list. If it is, pick a new one.

[[[generic-python-item-in-list]]]

--- hints ---
--- hint ---
Here is some pseudo code to help you. We start off by setting new equal to the first coordinate in the `slug` list so that it is guaranteed to start off inside the slug, so a new coordinate must be generated.

**SET** `new` to the first coordinate in the `slug` list
**WHILE** the coordinate is in the `slug` list:
...**SET** x to a random number between 0 and 7
...**SET** y to a random number between 0 and 7
...**SET** new to x, y
--- /hint ---

--- hint ---
Here is how your code might look:

```python
new = slug[0]
while new in slug:
    x = randint(0, 7)
    y = randint(0, 7)
    new = [x, y]
```
--- /hint ---
--- /hints ---

+ If it isn't, draw the vegetable on the screen. Don't forget you'll need to set up a new colour variable for the colour you want your vegetables to be.

[[[rpi-sensehat-single-pixel]]]

+ Add the coordinates of this vegetable to your `vegetables` list

[[[generic-python-append-list]]]

+ In your main program, call the `make_veg` function and check that vegetables are randomly inserted on the LED matrix.

Only create a vegetable if there are < 3 and also do it with an 80% chance so that they don't spawn all the time
