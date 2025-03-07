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
    i = 128
    dac_value = dectobin(i)
    GPIO.output(dac, dac_value)
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 128
    i = i + 64
    dac_value = dectobin(i)
    GPIO.output(dac, dac_value)
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 64
    i = i + 32
    dac_value = dectobin(i)
    GPIO.output(dac, dac_value)
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 32
    i = i + 16
    dac_value = dectobin(i)
    GPIO.output(dac, dac_value)
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 16
    i = i + 8
    dac_value = dectobin(i)
    GPIO.output(dac, dac_value)
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 8
    i = i + 4
    dac_value = dectobin(i)
    GPIO.output(dac, dac_value)
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 4
    i = i + 2
    dac_value = dectobin(i)
    GPIO.output(dac, dac_value)
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 2
    i = i + 1
    dac_value = dectobin(i)
    GPIO.output(dac, dac_value)
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 1
    return i

try:
    while True:
        i = adc()
        voltage = i * 3.3 / 256
        print("{:.2f}V".format(voltage))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()