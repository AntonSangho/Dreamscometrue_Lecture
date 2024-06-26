from machine import Pin, ADC, RTC 
from time import sleep
#from ds3231_port import DS3231
from machine import I2C
import utime as time
from bh1750 import BH1750

led = Pin("LED", Pin.OUT)

#rtc = RTC()

#print(rtc.datetime())
sdaPIN = Pin(4)
sclPIN = Pin(5)

i2c = I2C(0, sda=sdaPIN, scl=sclPIN) 

#ds3231 = DS3231(i2c)
bh1750 = BH1750(0x23, i2c)

#analogue_value = machine.ADC(27)
#VOLTAGE_DROP_FACTOR = 1 

def writeLine(text):
    file = open("log.txt", "a")
    file.write(text + "\n")
    file.close()
    #print(text)
 
while True:
    #reading = analogue_value.read_u16()     
    light = bh1750.measurement     
    #voltage = reading * (4.5 / 65535) * VOLTAGE_DROP_FACTOR
    #dateTime = ds3231.get_time()
    #print("hour:min:sec")
    #print(dateTime[3],dateTime[4],dateTime[5])
    print(light)
    #writeLine(str(dateTime[3]) + ":" + str(dateTime[4]) + ":" + str(dateTime[5]) + " " + str(voltage))
    writeLine(str(light))
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)
    #sleep(1800) # 30 minutes
