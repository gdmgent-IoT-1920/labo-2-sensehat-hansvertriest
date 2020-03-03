from sense_hat import SenseHat, ACTION_RELEASED
from random import randint
from math import ceil, sin
import time


sense = SenseHat()


x = 1
global y
y = 7
global is_jumping
is_jumping = False
global counter
counter = 0

def get_delta(counter):
    return ceil(3 * sin(counter/ 200))

def jump():
    print('jump')
    global is_jumping
    is_jumping = True

def refresh():
    global y
    global counter
    new_y = y - get_delta(counter)
    if new_y > 7:
        new_y = 7
        global is_jumping
        is_jumping = False
        counter = 0
        sense.clear()
    if new_y != y:
        sense.clear()
    sense.set_pixel(x, new_y - 1, 0, 0, 255)
    sense.set_pixel(x, new_y, 255, 0, 0)

while True:
    for event in sense.stick.get_events():
        if event.direction == 'up' and event.action == 'released':
            jump()
    if is_jumping:
        counter += 1
    refresh()

