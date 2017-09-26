## Use the joystick

Next, let's link up the Sense HAT's joystick so that the player can use it to control the movement of the slug.

![Moving slug](images/moving-slug.gif)

+ In the functions section, create a new function:

```python
def joystick_moved(event):
```

We will call this function whenever the joystick is moved. It will automatically receive a parameter called `event` which will let us find out what happened to the joystick - which direction was it moved in?

We want to be able to set our `direction` variable to the direction the joystick was pushed in. To be allowed to change the value of this variable from within a function, we need to specify `global` for the variable. To find out why, read about scope in Python functions.

[[[generic-python-function-scope]]]

+ Add `global direction` to your function:

```python
def joystick_moved(event):
    global direction
```

We can access the direction the joystick was moved in using the `event` parameter we were given. The direction can be found as `event.direction`

+ Inside your function, set the `direction` variable to be equal to `event.direction`

+ Finally, in the main part of your program, write a line of code to say that when the Sense HAT joystick is pressed in any direction, call the `joystick_moved` function.

[[[rpi-python-sensehat-joystick-event-functions]]]

--- hints ---
--- hint ---
You can find out how to do this by reading the information "Triggering function calls with the Sense HAT joystick".
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
