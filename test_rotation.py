from gpiozero import LED, Button
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)


print('Hi Nicky')

ads = ADS.ADS1115(i2c)
ads.gain = 1

mic0 = AnalogIn(ads, ADS.P1)
mic1 = AnalogIn(ads, ADS.P2)
mic2 = AnalogIn(ads, ADS.P3)


homing_switch = Button(21)

motor_A = LED(6)
motor_B = LED(13)
motor_C = LED(19)
motor_D = LED(26)


revolution_steps = 3300
step_time = 0.01
count = 0

speed = step_time / 4


def step(duration):
    motor_A.on()
    time.sleep(duration)
    motor_A.off()

    motor_B.on()
    time.sleep(duration)
    motor_B.off()

    motor_C.on()
    time.sleep(duration)
    motor_C.off()

    motor_D.on()
    time.sleep(duration)
    motor_D.off()
    

def stepback(duration):
    motor_D.on()
    time.sleep(duration)
    motor_D.off()

    motor_C.on()
    time.sleep(duration)
    motor_C.off()
    
    motor_B.on()
    time.sleep(duration)
    motor_B.off()
    
    motor_A.on()
    time.sleep(duration)
    motor_A.off()



def rotate(angle, speed):
    revolution_steps = 3300
    step_time = 0.01
    
    forward = True
    
    if angle < 0:
        forward = False
        angle = abs(angle)
    
    steps = round(angle / 360 * revolution_steps)
    
    for i in range(steps):
        if forward:
            step(step_time / speed)
        else:
            stepback(step_time / speed)

rotate(45,1)
rotate(-45,4)

# 
# while True:
#     print(count)
#     count = count + 1
#     
#     motor_A.on()
#     time.sleep(speed)
#     motor_A.off()
# 
#     motor_B.on()
#     time.sleep(speed)
#     motor_B.off()
# 
#     motor_C.on()
#     time.sleep(speed)
#     motor_C.off()
# 
#     motor_D.on()
#     time.sleep(speed)
#     motor_D.off()


print('done')
