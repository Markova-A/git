import RPi.GPIO as GPIO 
from time import sleep
GPIO.setmode(GPIO.BCM)

led = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(led, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dectobin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():
    i = 128
    GPIO.output(dac, dectobin(i))
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 128
    i = i + 64
    GPIO.output(dac, dectobin(i))
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 64
    i = i + 32
    GPIO.output(dac, dectobin(i))
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 32
    i = i + 16
    GPIO.output(dac, dectobin(i))
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 16
    i = i + 8
    GPIO.output(dac, dectobin(i))
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 8
    i = i + 4
    GPIO.output(dac, dectobin(i))
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 4
    i = i + 2
    GPIO.output(dac, dectobin(i))
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 2
    i = i + 1
    GPIO.output(dac, dectobin(i))
    sleep(0.01)
    if GPIO.input(comp) == 1:
        i = i - 1
    return i

def volume(value):
    value = int(value / 256 *10)
    array = [0] * 8
    for i in range (value - 1):
        array[i] = 1
    return array

try:
    while True:
        i = adc()
        volume_val = volume(i)
        GPIO.output(led, volume_val)
        print(int(i/256*10))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()