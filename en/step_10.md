## Game over

The final thing you need to check when the slug moves to a new pixel is whether she will try biting her own body. This should cause the player to lose the game. The way to do this is very similar to how you checked checked whether the slug is eating a vegetable.

+ In the variables section, create a new Boolean variable called `dead` and initialise it to `False` (as we don't want to start off dead!)

+ Inside the `move()` function, add some code to check whether the next pixel the slug is moving to is in fact part of herself.

+ If it is, set the `dead` variable to `True`. Don't forget that because we are altering a variable in the main program from within a function, we need to declare it as a global inside the function.

--- hints ---
--- hint ---
Here is the code you used to check whether the pixel the slug was moving into contained a vegetable:

```python
if next in vegetables:
    # Do things relating to vegetables
```

Can you use some similar code to check whether the next pixel is inside the slug?
--- /hint ---
--- hint ---
Here is how your code should look. Make sure you add this code to the `move()` function **before** the code which adds the `next` pixel to the `slug` list, otherwise you will be permanently dead!

```python
if next in slug:
    dead = True
```
--- /hint ---
--- /hints ---


At the moment, even when the `dead` variable is set to True, the game doesn't end.

+ Change the game loop in the main program from an infinite loop (`while True:`) to a loop which only runs while the `dead` variable is not True.

+ After the game loop ends (i.e. do not indent your code), add a line of code to display the player's score once they die.

[[[rpi-sensehat-show-message]]]
