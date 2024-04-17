from machine import Pin
from utime import sleep
import utime 

led = Pin('LED', Pin.OUT)
button = Pin(20, Pin.IN, Pin.PULL_UP)


while True:
    print(button.value())
    if button.value() == 0:
        led.value(False)
    else:
        led.value(True)
    utime.sleep(0.1)