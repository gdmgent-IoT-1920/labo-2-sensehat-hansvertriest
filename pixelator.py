from sense_hat import SenseHat
import time
from random import randint
from math import cos
sense = SenseHat()

while True:
    for i in range(0, 64):
        
        sense.clear()
        x = i % 8
        y = i // 8
        sense.set_pixel(x, y, randint(0,255), randint(0,255), randint(0,255))
        sleep_time = abs(cos(i / 10)) * 0.2
        time.sleep(sleep_time)