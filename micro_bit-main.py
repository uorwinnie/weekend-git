# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    #display.scroll('RED')
    display.show('R')
    sleep(1000)
    display.show(Image(
        '00900:'
        '09990:'
        '00900:'
        '00900:'
        '09090:' 
    ))
    sleep(10000)
    display.show('G')
    sleep(1000)
    display.show(Image(
        '90009:'
        '09090:'
        '00900:'
        '09090:'
        '90009:'
    ))
    sleep(10000)
    display.show('Y')
    sleep(1000)
    display.scroll('Slow down...')
        

