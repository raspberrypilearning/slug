## Die

Our final check is to test when the slug moves into a new space, whether she would be eating her own body, and thus lose the game. The way to check this is very similar to the way we checked if the slug was eating a vegetable.

+ In the variables section, create a new Boolean variable called `dead` and initialise it to `False` (as we don't want to start off dead!)

+ Inside the `move()` function, add some code to check whether the next pixel the slug is moving to is in fact part of herself.

+ If it is, set the `dead` variable to `True`. Don't forget that because we are altering a variable in the main program from within a function, we need to declare it as a global inside the function.

At the moment, even when the `dead` variable is set to True, the game doesn't end.

+ Change the game loop in the main program from an infinite loop (`while True:`) to a loop which only runs while we are not dead.

+ After this loop (not indented), add a line of code to display the player's score once they die.
