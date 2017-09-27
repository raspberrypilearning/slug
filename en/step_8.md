## Eating vegetables

Your slug already appears to eat the vegetables. Have you noticed that, once she has eaten the first three vegetables, no more vegetables ever appear regardless of how long you wait.

**Can you work out why this is?**

--- collapse ---
---
title: Answer
---
Since the `make_veg` function only generates vegetables if the `vegetables` list contains fewer than three items, no new vegetables will appear once the list contains three vegetables. So at the moment, your first three vegetables are generated and added to the `vegetables` list. When the slug moves onto a pixel containing a vegetable, she appears to eat it because the slug's pixels are drawn over the top of the vegetable. However, the vegetable is never removed from the `vegetables` list.
--- /collapse ---

+ Add some code at the end of the `move()` function so that, whenever the slug moves to a new pixel, the function checks whether that pixel is in the `vegetables` list. If the pixel is in the `vegetables` list, remove it from the list.

Let's also add a score to keep track of how many vegetables the slug has eaten.

+ In the variables section, create a `score` variable which starts as `0`.

+ Whenever the slug eats a vegetable, add 1 to the score. Don't forget that, because the `score` variable was created outside of the function, you need to specify that you want to use `global score` at the start of the `move()` function so that the function is allowed to change it.

--- hints ---
--- hint ---
Here is some pseudocode for the check which should occur within the `move()` function:

`if` new pixel is `in` vegetables
`remove` new pixel from vegetables
`add` 1 to score
--- /hint ---
--- hint ---
Here is the code you should add to the end of the `move()` function:

```python
if next in vegetables:
  vegetables.remove(next)
  score += 1
```

Don't forget to also add `global score` on the first line of the `move()` function, and to initialise the `score` variable to `0` in the variables section.
--- /hint ---
--- /hints ---
