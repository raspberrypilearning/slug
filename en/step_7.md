## Create vegetables

Our slug is hungry, she needs something to eat! Let's generate some vegetables at random locations on the LED matrix for her to eat.

Creating the vegetables is fairly straightforward:

1. Pick a random coordinate on the LED matrix
2. Check that this coordinate isn't somewhere inside the slug
3. If it is, pick a new location until you pick one that isn't inside the slug
4. If not, draw the vegetable
5. Keep track of this vegetable's location in a list

These are all things we've done before with the slug, so why not see if you can do it yourself, and use the hints if you get stuck.

+ Create a new list called `vegetables` in your variables section

+ Create a new function called `make_veg()`

+ Inside the function, write some code to pick a random coordinate on the LED matrix.

[[[generic-python-random]]]

+ Check if this coordinate is in the slug list. If it is, pick a new one.

(ingredient about in list)

+ If it isn't, draw the vegetable on the screen. Don't forget you'll need to set up a new colour variable for the colour you want your vegetables to be.

[[[rpi-sensehat-single-pixel]]]

+ Add the coordinates of this vegetable to your `vegetables` list

[[[generic-python-append-list]]]

+ In your main program, call the `make_veg` function and check that vegetables are randomly inserted on the LED matrix.

Only create a vegetable if there are < 3 and also do it with an 80% chance so that they don't spawn all the time
