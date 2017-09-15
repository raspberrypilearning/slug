## Eat vegetables

Your slug already appears to eat the vegetables. Have you noticed that once you've eaten the first three vegetables that appear, no more vegetables ever appear regardless of how long you wait.

**Can you work out why this is?**

--- collapse ---
---
title: Answer
---
Your first three vegetables are generated and added to the vegetables list. When the slug moves onto a pixel containing a vegetable she appears to "eat" it because the slug's pixels are drawn over the top of the vegetable. However, the vegetable is never removed from the `vegetables` list.

Since we only generate vegetables when the list contains fewer than 3 coordinates, no new vegetables will ever be generated once the list contains 3 vegetables.
--- /collapse ---

+ Add some code so that whenever the slug enters a new pixel in the `move()` function, we check if that pixel is in the `vegetables` list.

+ If the pixel is in the vegetables list, remove it from the list.

Let's also add a score to keep track of how many vegetables the slug has eaten.

+ In the variables section, create a score variable which starts as `0`

+ Whenever the slug eats a vegetable, also add one to the score. Don't forget that because this variable was created outside of the function, we will need to specify that we want to use `global score` at the start of the `move()` function or we will not be allowed to change its value.

--- hints ---
--- hint ---
Stuff
--- /hint ---
--- /hints ---
