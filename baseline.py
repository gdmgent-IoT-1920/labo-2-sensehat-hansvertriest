from sense_hat import SenseHat
from random import random
sense = SenseHat()
intensity = 0.4
random_r = round(random() * 255)
random_g = round(random() * 255)
random_b = round(random() * 255)
print(random_r)
sense.show_message('Melissa is prachtig', text_colour=[random_r,random_g,random_b], back_colour=[round(random_r * intensity), round(random_g * intensity), round(random_b * intensity)])