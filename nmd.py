from sense_hat import SenseHat
import time
sense = SenseHat()
string = input('Type your string please ')
duration = int(input('How many seconds do you want to display each letter? '))


while True:
    for index, char in enumerate(string):
        sense.show_letter(char)
        time.sleep(duration)
    time.sleep(3)