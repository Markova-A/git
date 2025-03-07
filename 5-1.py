import RPi.GPIO as GPIO 
from time import sleep
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dectobin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        dac_value = dectobin(i)
        GPIO.output(dac, dac_value)
        sleep(0.01)
        if GPIO.input(comp) == 1:
            return i
    return 0

try:
    while True:
        i = adc()
        voltage = i * 3.3 / 256
        print("{:.2f}V".format(voltage))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()