## Growing and speeding up

To keep the game interesting for the player, as the slug eats vegetables she should grow in length and move faster. This makes her harder to control — and worse, she might accidentally bite into her own body!

The code you've written so far makes it so that, when the slug advances a pixel, her end segment is deleted. To enable her to grow, you can add a new segment to the `slug` list but **not** delete the last one. So each time the slug moves, you need to make a decision as to whether to remove a segment or not.

+ At the start of the `move()` function, create a Boolean variable called `remove` and set it to `True`, as most of the time we do want to remove the end segment when the slug moves.

+ Add a conditional statement to your function so that the following two lines of code are only executed `if` the `remove` variable is `True`.

```python
sense.set_pixel(first[0], first[1], blank)
slug.remove(first)
```

+ Decide how often you want your slug to grow. In our example, we chose for our slug to grow one segment for every 5 vegetables she eats.

To help your program decide when to trigger the slug to grow, you can use the **mod** operator `%`. By using it, you can work out whether the current score is a multiple of 5.

[[[generic-python-mod-operator]]]

You'll want to ensure that the slug can only grow when it has eaten a vegetable. To do this, you should add your new code to potentially grow the slug inside this `if` statement:

```python
if next in vegetables:
```

+ Add code to check whether the current score is a multiple of 5. If it is, set `remove` to `False` so no segment gets removed.

+ Save and run the code. You might be disappointed to see that, when you eat 5 vegetables, the slug doesn't grow! Why not?

--- collapse ---
---
title: Answer
---
The code to remove the segment currently runs before the code to check whether the new pixel was a vegetable. This means that the program doesn't care whether we've told it to remove or not remove a segment, because by the time this decision is taken, the segment has already been removed! --- /collapse ---

+ Alter the order of the code so that the last thing in the `move()` function is the code to potentially remove a segment. Test again, and you should see your slug grow.

As well as setting `remove` to `False` to grow the slug, let's speed it up! Currently, the slug's speed is regulated by this line of code in the main program:

```python
sleep(0.5)
```

This command tells your infinite loop to wait for half a second between each run, so that the slug moves at a speed of one pixel per half-second. To make it move faster, you'll want to gradually decrease this pause.

+ In the variables section, create a variable called `pause` and set it to `0.5`.

+ Replace the `0.5` in the brackets of the `sleep()` function with the variable `pause`. Now the speed of the slug will be determined by the value of `pause`.

You've already added some code to section which check whether the current score is a multiple of 5, so your slug can grow. That is also the point at which the value of `pause` should become smaller. Amend your `move` function like this:

```python
global pause

if score % 5 == 0:
    remove = False
    pause = pause - 0.1
```

+ Save and run your program. What happens? Why is this code not a very good idea, and how could you improve it?

--- collapse ---
---
title: Answer
---
If `pause` begins at `0.5`, and we subtract `0.1` for every five eaten vegetables, `pause` will eventually become `0`. That will make the game impossible!

Instead of subtracting a fixed amount, why not make `pause` proportionally smaller? For example:

```python
pause = pause * 0.8
```

This will make `pause` 80% of its previous value. In this way, it will never become `0`. --- /collapse ---
