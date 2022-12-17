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

time.sleep(1)

print('Welcome Back')

while True:
    if homing_switch.is_pressed:
        print('homed')
        break
    
    motor_A.on()
    time.sleep(0.01)
    motor_A.off()

    motor_B.on()
    time.sleep(0.01)
    motor_B.off()

    motor_C.on()
    time.sleep(0.01)
    motor_C.off()

    motor_D.on()
    time.sleep(0.01)
    motor_D.off()
    
while True:
    n = int((mic0.value / 65536 ) * 65536)
    n = abs(n - 32768)
    print('mics', n)
    #print('mic1', mic1.value, mic1.voltage)
    #print('mic2', mic2.value, mic2.voltage)



print('done')