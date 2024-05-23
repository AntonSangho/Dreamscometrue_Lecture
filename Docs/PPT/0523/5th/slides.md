---

# 데이터 파이 
## 환경데이터 수집하기 

---

# 목차 

1. 어떻게 만들지 생각해보기 
2. 코드 참고하기 
3. 코드 작성하기 

---

# 반복문 

```python
while True:
    # 기록 중인 상태 
        # 데이터 기록 시작 
    # 기록 중이 아닌 상태 
        # 기록 대기 
```

<style>
    code{
        font-size: 3em;
    }
</style>


---

# 기존의 버튼 처리

```python
from machine import Pin
from utime import sleep
import utime 

led = Pin('LED', Pin.OUT)

button = Pin(20, Pin.IN, Pin.PULL_UP)

while True:
    # button의 상태를 출력합니다. (눌렸을 때 0, 눌리지 않았을 때 1)
    print(button.value())

    if button.value() == 0:
        led.value(False)
    else:
        led.value(True)

    # 0.1초마다 반복합니다.
    utime.sleep(0.1)
```



---

# 상태변수 선언    

```python
recording_active = False

while True:
    # 기록 중인 상태 
    if recording_active: 
        # 데이터 기록 시작 
    # 기록 중이 아닌 상태 
    else:
        # 기록 대기 
```


---

# 버튼핸들러 

```python
recording_active = False

def button_handler(pin):
    #만약 버튼이 눌렸을 때 
        # recording_active를 False에서 True로 변경 
        recording_active = not recording_active

button.irq(trigger-Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=button_handler)

while True:
    # 기록 중인 상태 
    if recording_active: 
        # 데이터 기록 시작 
    # 기록 중이 아닌 상태 
    else:
        # 기록 대기 
`

```

---

# 네오픽셀로 상태추적 
```python
def np_red():
    for i in range(0, np0.n):
        np0[i] = (64,0,0)
    np0.write()
def np_green():
    for i in range(0, np0.n):
        np0[i] = (0,64,0)
    np0.write()
def np_blue():
    for i in range(0, np0.n):
        np0[i] = (0,0,64) 
    np0.write()
def np_yellow():
    for i in range(0, np0.n):
        np0[i] = (64,64,0) 
    np0.write()
def np_off():
    for i in range(0, np0.n):
        np0[i] = (0,0,0)
    np0.write()

```

---

# 버튼에 따라 네오픽셀 변경  

```python
def button_handler(pin):
    #만약 버튼이 눌렸을 때 
        # recording_active를 False에서 True로 변경 
        recording_active = not recording_active
        if recording_active:
            np_blue()
            utime.sleep(1)
            np_off()
        else:
            np_yellow()
            utime.sleep(1)
            np_off()
```

---

# 파일에 데이터 쓰기 
```python

file = None

def record_data():
    global file
    for rom in roms:
        temp_sensor.convert_temp()
        utime.sleep_ms(100)
        t = temp_sensor.read_temp(rom)
        dateTime = ds3231.get_time()
        timestamp = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(dateTime[0], dateTime[1], dateTime[2], dateTime[3], dateTime[4], dateTime[5])
        data_line = "{}, {:6.2f}, {:6.2f}\n".format(timestamp, t)
        if file:
            file.write(data_line)

```

---

# 파일에 따라 네오픽셀 변경 

```python
def button_handler(pin):
        recording_active = not recording_active
        if recording_active:
            Led.value(1)
            np_blue()
            utime.sleep(1)
            np_off()
        else:
            np_yellow()
            utime.sleep(1)
            np_off()
            if file:
                file.close()
                utime.sleep(1)
                np_green()

```
---

# 기록하는 간격 설정 

```python 
recording_interval = 1800

while True:
    if recording_active:
        record_data()
        utime.sleep(recording_interval) 
    else:
        Led.value(0)

```

--- 

# 종합 - 1 

## 라이브러리 참조 
- ds3231_port 
- neopixel 
- sdcard
- ds18x20  
- utime
- I2C

## 상태 변수 글로벌 선언 
- recording_active  
- sensing_active 
- file

--- 

# 종합 - 2 
## 함수 선언 
- button_handler()  
- np_blue(), np_green(), np_yellow(), np_off()
- record_data()

## 반복문 
- while True: 

---

# [코드 다운로드](https://github.com/AntonSangho/DataPi_Beekeeping/blob/production/src/main_v0_3.py) 





