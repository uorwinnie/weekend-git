# Imports go at the top
from microbit import *
import neopixel
Red = (255,50,50)
Yellow = (255,255,0)
Green = (0,255,0)

np=neopixel.NeoPixel(pin12,4)

# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
       np[0]=Green
       np.show()
       sleep(7000)
       np.clear()
       sleep(1000)
    
       np[1]=Yellow
       np.show()
       sleep(4000)
       np.clear()
       sleep(1000)

       np[2]=Red
       np.show()
       sleep(7000)
       np.clear()
       sleep(1000)
       
      
        

