## Game over

The final thing you need to check when the slug moves to a new pixel is whether she will bite into her own body. If this happens, she will die and the player will lose the game. The way to do this is very similar to how you checked checked whether the slug is eating a vegetable.

+ In the variables section, create a new Boolean variable called `dead` and initialise it to `False` (so the slug doesn't start off dead!).

+ Inside the `move()` function, add some code to check whether the next pixel the slug is moving to is part of herself.

+ If it is, set the `dead` variable to `True`. Do you remember what you need to do to allow a function to alter a global variable?

--- hints ---
--- hint ---
Here is the code you used to check whether the pixel the slug was moving to contained a vegetable:

```python
if next in vegetables:
    # Do things relating to vegetables
```

Can you use similar code to check whether the next pixel is part of the slug?
--- /hint ---
--- hint ---
Here is how your code should look. Make sure you add it to the `move()` function **above** the code which adds the `next` pixel to the `slug` list, otherwise you will be permanently dead!

```python
if next in slug:
    dead = True
```
--- /hint ---
--- /hints ---


Save and run your code. When you make the slug bite itself now, you'll see that the game doesn't end, even though the `dead` variable is changed to `True`!

+ Change the game loop in the main program from an infinite loop to a loop which only runs while the `dead` variable is not `True`.

Once the game loop ends, the player will want to know how they did in their game.

+ In the main program, add code to display how many vegetables the player guided the slug to by making use of the `score` variable. 

[[[rpi-sensehat-show-message]]]
