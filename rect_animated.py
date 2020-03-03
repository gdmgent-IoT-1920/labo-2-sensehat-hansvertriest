from sense_hat import SenseHat
from random import randint
from math import ceil
import time

sense = SenseHat()

def draw_rect(w, h):
    # find starting coordinate
    coord_x = 0
    coord_y = 0
    if w % 2 == 0:
        coord_x = int(4 - (w / 2)) 
    else:
        coord_x = 4 - ceil(w / 2) 
    if h % 2 == 0:
        coord_y = int(4 - (h / 2)) 
    else:
        coord_y = 4 - ceil(h / 2) 

    x = [100,50,0]
    o = [0, 0, 0]
    display = []
    for i in range(0, 64):
        row = i // 8;
        column = i % 8
        if row >= coord_y and row <= coord_y + h -1:
            if column == coord_x or column == coord_x + w-1:
                display.append(x)
                continue
        if column >= coord_x and column <= coord_x + w-1:
            if row == coord_y or row == coord_y + h -1:
                display.append(x)
                continue
        display.append(o)
    sense.set_pixels(display)

def determine_expansion_factor(length, curr_factor):
    if length == 8 or length == 8:
        return -1
    elif length == 1 or length == 1:
        return 1
    else:
        return curr_factor


width = randint(1,7)
height = randint(1,7)
factor_w = 1
factor_h = 1
counter = 1

while True:
    # leek me cooler om de twee dimensie apart van elkaar te laten varieren daarom twee factors
    factor_w = determine_expansion_factor(width, factor_w);
    factor_h = determine_expansion_factor(height, factor_h);
    width = width + factor_w
    height = height + factor_h
    draw_rect(width, height)
    time.sleep(0.05)
    counter += 1
