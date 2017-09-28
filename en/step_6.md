## Use the joystick

Next, let's link up the Sense HAT's joystick so that the player can use it to control the movement of the slug.

![Moving slug](images/moving-slug.gif)

+ In the functions section, create a new function:

```python
def joystick_moved(event):
```

You will call this function whenever the joystick is moved. It will automatically receive a parameter called `event`, which will let you find out in which direction the the joystick was moved.

You'll want to set the `direction` variable to the direction in which the joystick was pushed. So that you are allowed to change the value of the variable from within this function, you need to specify `global` for the variable. To find out why, read about scope in Python functions.

[[[generic-python-function-scope]]]

+ Add `global direction` to your function:

```python
def joystick_moved(event):
    global direction
```

You can access the direction the joystick was moved in with the help of the `event` parameter: use the command `event.direction`.

+ Inside your function, set the `direction` variable to be equal to `event.direction`.

+ Finally, in the main part of your program, write a line of code to say that, when the Sense HAT joystick is pressed in any direction, the `joystick_moved` function will be called.

[[[rpi-python-sensehat-joystick-event-functions]]]

--- hints ---
--- hint ---
You can find out how to do this in the information section 'Triggering function calls with the Sense HAT joystick' found above.
--- /hint ---

--- hint ---
The code to say "when the joystick is pressed in any direction" is as follows:

```python
sense.stick.direction_any =
```
--- /hint ---

--- hint ---
Here is how the code in the **main program** should look:

```python
sense.stick.direction_any = joystick_moved
```

Here is the full **function** code:
```python
def joystick_moved(event):
    global direction
    direction = event.direction
```

--- /hint ---

--- /hints ---

+ Run your program and test that it works. If you are using the emulator, you can simulate moving the joystick by pressing the arrow keys on your keyboard.
