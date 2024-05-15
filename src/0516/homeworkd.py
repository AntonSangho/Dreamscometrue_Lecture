from time import sleep
from machine import I2C, Pin
from bh1750 import BH1750
import onewire, ds18x20
import time 


led = Pin("LED", Pin.OUT)

sdaPIN = Pin(4)
sclPIN = Pin(5)

i2c = I2C(0, sda=sdaPIN, scl=sclPIN) 

bh1750 = BH1750(0x23, i2c)

# GPIO 26번 핀에 OneWire 버스를 생성합니다.
data = machine.Pin(26)
temp_wire = onewire.OneWire(data) # GPIO 26번 핀에서 OneWire 버스 생성

# OneWire 버스를 사용하여 DS18X20 온도 센서 객체를 생성합니다.
temp_sensor = ds18x20.DS18X20(temp_wire)

# 버스에서 연결된 장치(온도 센서)를 스캔합니다.
roms = temp_sensor.scan()
print(len(roms), 'temperature sensor found')  # 연결된 온도 센서의 수를 출력합니다.


def writeLine(text):
    file = open("log.txt", "a")
    file.write(text + "\n")
    file.close()
 
while True:
    light = bh1750.measurement     
    #print(light)
    temp_sensor.convert_temp()
    time.sleep_ms(100)
    for rom in roms:
        t = temp_sensor.read_temp(rom)
        writeLine(str(t))
    #writeLine(str(light))
    print(t)
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)

 
