---

marp: true
theme: my-theme 
paginate: false 
header: 창의융합인재 프로그램 3기 
footer: 공학도서관 

---


## 과제 1  

# 온도데이터를 
# 파일에 기록하기  
---

실습) Code#1은  온도센서의 값을 PC화면에 출력하는 코드이고 Code#2는 조도센서를 파일에 기록하는 코드입니다.
두 코드를 참고해서 온도 센서가 파일에 쓰여지도록 수정하는 방법을 생각해보세요.

---
### Code#1

```python
import time
import machine
import onewire, ds18x20

data = machine.Pin(26)
temp_wire = onewire.OneWire(data) 

temp_sensor = ds18x20.DS18X20(temp_wire)

roms = temp_sensor.scan()
print(len(roms), 'temperature sensor found')  

while True:
    print('temperatures:', end=' ')
    temp_sensor.convert_temp()
    time.sleep_ms(100)  

    for rom in roms:
        t = temp_sensor.read_temp(rom)
        print('{:6.2f}'.format(t), end=' ')  
    print()  

```

---
### Code#2

```python
from time import sleep
from machine import I2C, Pin
from bh1750 import BH1750

led = Pin("LED", Pin.OUT)

sdaPIN = Pin(4)
sclPIN = Pin(5)

i2c = I2C(0, sda=sdaPIN, scl=sclPIN) 

bh1750 = BH1750(0x23, i2c)


def writeLine(text):
    file = open("log.txt", "a")
    file.write(text + "\n")
    file.close()
 
while True:
    light = bh1750.measurement     
    print(light)
    writeLine(str(light))
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)
```

---
<body>
<h1 style="text-align: center; color: white;">감사합니다.<h1>
<h2 style="text-align: center; color: cyan">공학도서관</h2>
<h2 style="text-align: center;" >www.gongdo.kr<h2>
</body>
