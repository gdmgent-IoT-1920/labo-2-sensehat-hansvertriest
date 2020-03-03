from sense_hat import SenseHat
from PIL import Image
from random import randint
import time

sense = SenseHat()

amount_of_pics = 3

while True:
    pic_nr = str(randint(1, amount_of_pics))
    img = Image.open('pic'+pic_nr+'.png')
    byteList = list(img.getdata())
    pixels = []
    for index, byte in enumerate(byteList):
        pixels.append([byte[0], byte[1], byte[2]])
    sense.set_pixels(pixels)
    time.sleep(1)
