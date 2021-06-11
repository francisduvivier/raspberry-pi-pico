# To use this file, upload it to your raspberry pi pico 
# with the file name main.py
# using the Thonny IDE.
# For more info, check https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/9
from machine import Pin
import time
pins = [Pin(14, Pin.OUT), Pin(15,Pin.OUT), Pin(16,Pin.OUT), Pin(17,Pin.OUT)]
i = 0
while True:
    next = (i +1) %4           
    pins[i].off()
    pins[next].on()
    time.sleep(0.005)
    i = next`
