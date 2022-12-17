from gpiozero import LED, Button
import time
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)
ads.gain = 1

print(ads.bits)
print(ads.rates)

mic = AnalogIn(ads, ADS.P1)

#while True:
#    n = int((mic.value / 65536 ) * 65536)
#    n = abs(n - 32768)
#    print('mics', n)


print("{:>5}\t{:>5}".format('raw', 'v'))

while True:
    print("{:>5}\t{:>5.3f}".format(mic.value, mic.voltage))
    time.sleep(0.5)