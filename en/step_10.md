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

Can you use some similar code to check whether the next pixel is part of the slug?
--- /hint ---
--- hint ---
Here is how your code should look. Make sure you add it to the `move()` function **above** the code which adds the `next` pixel to the `slug` list, otherwise you will be permanently dead!

```python
if next in slug:
    dead = True
```
--- /hint ---
--- /hints ---


At the moment, even when the `dead` variable is set to `True`, the game doesn't end.

+ Change the game loop in the main program from an infinite loop (`while True:`) to a loop which only runs while the `dead` variable is not `True`.

+ Add a line of code to display the player's score once they die after the game loop ends. Note: do not indent your code. 

[[[rpi-sensehat-show-message]]]
