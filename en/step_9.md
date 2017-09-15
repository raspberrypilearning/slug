## Grow and speed up

To keep the game interesting for the player, as the slug eats vegetables she should grow in length and speed up. This makes her harder to control and worse, she might accidentally run into her own body!

At the moment, when the slug advances a pixel, the end segment is deleted. To enable her to grow, we will add the new segment to the slug list but **not** delete the last one. Therefore, each time the slug moves, we need to make a decision as to whether to remove a segment or not.

+ At the start of the `move()` function, create a boolean variable called `remove` which begins with the value of `True`, as most of the time we do want to remove a segment as the slug moves.

+ Add a condition to your program so that the following two lines of code are only executed **if** the `remove` variable is `True`

```python
sense.set_pixel(first[0], first[1], blank)
slug.remove(first)
```

+ Decide how often you want your slug to grow. We chose for our slug to grow one segment for every 5 vegetables eaten.

We can use the **mod** operator (%) to decide whether to trigger the slug to grow, by working out whether the current score is a multiple of 5.

[[[generic-python-mod-operator]]]

+ Locate this line of code:

```python
if next in vegetables:
```

We will add the code to potentially grow the slug inside this `if` statement, because it's only possible for the slug to grow on an occasion when it has eaten a vegetable.

+ Add some code to check whether the current score is a multiple of 5 (or your chosen number). If it is, set `remove` to `False` so we don't remove a segment.

+ Save and run the code. You might be disappointed to see that if you eat 5 vegetables the slug doesn't grow! Why not?

--- collapse ---
---
title: Answer
---
The code to remove the segment currently comes before the code to check whether the new pixel was a vegetable. This means that the program doesn't care whether we've told it to remove or not remove a segment, because by the time this decision is taken, the segment has already been removed!
--- /collapse ---

+ Alter the order of the code so that the last thing in the `move()` function is the code to potentially remove a segment (depending on the value of the `remove` variable). Test again and you should see your slug grow.

As well as setting `remove` to `False` to grow the slug, let's speed it up! Currently the slug's speed is regulated by this line of code in the main program:

```python
sleep(0.5)
```

+ In the variables section, create a variable called `speed` which begins as `0.5`

+ Replace the 0.5 in the brackets of the `sleep()` function with the variable `speed`. Now the speed of the snake will be determined by the value of this variable.

We tried adding some code to the code we wrote earlier to check whether the current score is a multiple of 5, like this:

```python
global speed

if score % 5 == 0:
    remove = False
    speed = speed - 0.1
```

+ Add this code to your program. Save and run the code - what happens. Why is this code not a very good idea, and how could you improve it?

--- collapse ---
---
title: Answer
---
If the speed begins at 0.5, and we subtract 0.1 every 5 vegetables, this means that the speed will eventually become 0 which will make the game impossible!

Instead of subtracting a fixed amount, why not make the speed a percentage smaller each time the score increases by 5. For example:

```python
speed = speed * 0.8
```

This will make the speed 80% of its previous value. This might appear to be slowing the slug down, but remember that the speed is actually the time the game waits between each movement of the slug, so the smaller the speed the quicker the slug moves.
--- /collapse ---
