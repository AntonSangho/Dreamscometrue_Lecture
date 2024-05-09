---

marp: true
theme: my-theme 
paginate: true
header: 창의융합인재 프로그램 3기 
footer: 공학도서관 

---

<!--paginate: skip -->
<body>
<h1 style="text-align: center; color: cyan;">공학도서관<h1>
<h2 style="text-align: center; color: white">www.gongdo.kr<h2>
</body>

--- 

###### 창의융합인재 프로그램 3기  

# 데이터를 읽고 쓰기   
---

# 목차 
- 데이터 통신: I2C 
- I2C 실습 
- 조도센서
- 조도센서를 파일에 쓰기


---

<!--paginate: true -->

## 기술 도구를 사용한 읽고 쓰기는 
## 우리에게 어떤 의미인가? 

---

## 사람 간의 언어 vs 기계 간의 언어 

---

# 프로토콜
![width:10000px](./img/I2C_Basic_Address_and_Data_Frames.jpg)

---

# I2C 
![width:1000px](./img/I2C-Block-Diagram.jpg)

---

# 복습하기 
### Thonny의 실행하고 폴더 경로 맞추기 
    1. Thonny 실행

    2. 이 컴퓨터 -> C 드라이브 -> Users -> 사용자명 -> Desktop(더블클릭)  

    3. 새로운 디렉토리 -> 'Project' 폴더 생성 

    4. Project 폴더 안 -> '0509_DataPi' 폴더 생성 

    5. 파일 -> 새 파일  
---
### Thonny의 실행하고 폴더 경로 맞추기 결과
![width:10000px ](img/finaloutput.png)

---

# 복습하기 

2. 데이타 파이 보드 연결하기
3. micropython 연결하기 

---


### I2C 실습 -1 
```python 
from machine import Pin
from machine import I2C
```
---
### I2C 실습 -2 
```python
sdaPIN = Pin(4) 
sclPIN = Pin(5) 

i2c = I2C(0, sda=sdaPIN, scl=sclPIN) 
devices = i2c.scan() 
```
---

### I2C 실습 -3 
```python

if len(devices) == 0:
    print("No I2C device")
else:
    print("I2C device found :", len(devices))

for device in devices:
    print(" Hexa address: ", hex(device))
```

---

### I2C 실습 -완료 
```python
from machine import Pin
from machine import I2C

sdaPIN = Pin(4) 
sclPIN = Pin(5) 

i2c = I2C(0, sda=sdaPIN, scl=sclPIN) 
devices = i2c.scan() 

if len(devices) == 0:
    print("No I2C device")
else:
    print("I2C device found :", len(devices))

for device in devices:
    print(" Hexa address: ", hex(device))
```

---

# 조도 센서 통신하기
## I2C 사용 


---
# 준비
1. bh1750 라이브러리 다운로드: ping시트 
2. Rasberry pi Pico에 lib 폴더 만들기 
3. bh1750.py 파일을 업로드 하기 

---

### 조도센서 실습 -1   
```python
from machine import Pin, I2C
from utime import sleep
from bh1750 import BH1750
```

---

### 조도센서 실습 -2   
```python

i2c0_sda = Pin(4)
i2c0_scl = Pin(5)
i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)

bh1750 = BH1750(0x23, i2c0)
```

---

### 조도센서 실습 -3   
```python
while True:
    print(bh1750.measurement)
    sleep(1)
```

---

### 조도센서 실습 -완료  
```python
from machine import Pin, I2C
from utime import sleep

from bh1750 import BH1750

i2c0_sda = Pin(4)
i2c0_scl = Pin(5)
i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)

bh1750 = BH1750(0x23, i2c0)

while True:
    print(bh1750.measurement)
    sleep(1)
```

---

# 파일 쓰기
## 조도센서  

---
### 파일 쓰기 실습 -1 
```python
from time import sleep
from machine import I2C, Pin
from bh1750 import BH1750
```
- 라이브러리 가져오기 

---
### 파일 쓰기 실습 -2 
```python
led = Pin("LED", Pin.OUT)

sdaPIN = Pin(4)
sclPIN = Pin(5)

i2c = I2C(0, sda=sdaPIN, scl=sclPIN) 

bh1750 = BH1750(0x23, i2c)

def writeLine(text):
    file = open("log.txt", "a")
    file.write(text + "\n")
    file.close()
```
- I2C 연결 
- 쓰기 함수 
---

### 파일 쓰기 실습 -3 
```python
while True:
    light = bh1750.measurement     
    print(light)
    writeLine(str(light))
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)
    #sleep(1800) # 30 minutes
```
- 조도센서 값을 반복해서 쓰기
---

### 파일 쓰기 실습 -완료 
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
    #sleep(1800) # 30 minutes
```


---

# 정리 
- 통신하기
- 데이터 읽어오기
- 데이터 쓰기 

---
<body>
<h1 style="text-align: center; color: white;">감사합니다.<h1>
<h2 style="text-align: center; color: cyan">공학도서관</h2>
<h2 style="text-align: center;" >www.gongdo.kr<h2>
</body>
