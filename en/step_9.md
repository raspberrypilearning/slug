## Grow and speed up

To keep the game interesting for the player, as the slug eats vegetables she should grow in length and speed up. This makes her harder to control and worse, she might accidentally run into her own body!

At the moment, when the slug advances a pixel, the end pixel is deleted. To enable her to grow, we will add the new pixel to the slug list but **not** delete the last one. Therefore, each time the slug moves, we need to make a decision as to whether to remove a segment or not.

+ At the start of the `move()` function, create a boolean variable called `remove` which begins with the value of `True`, as most of the time we do want to remove a segment as the slug moves.

+ Add to your program so that the following lines of code are only executed if the `remove` variable is `True`

```python
sense.set_pixel(first[0], first[1], blank)
slug.remove(first)
```

+ Decide how often you want your slug to grow. We chose for our slug to grow one segment for every 5 vegetables eaten.

We can use the **mod** operator (%) to decide whether to trigger the slug to grow, by working out whether the current score is a multiple of 5.

[[[generic-python-mod-operator]]]
