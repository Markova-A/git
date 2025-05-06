import RPi.GPIO as GPIO
from time import sleep 

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dectobin(number):
    return [int(element) for element in bin(number)[2:].zfill(8)]

T = float(input("Enter periond of signal ")) 
t = T / (255 * 2) 

try:
    while True:
        for i in range (0, 255):
            GPIO.output(dac, dectobin(i))
            sleep(t)
        for i in range (254, 0, -1):
            GPIO.output(dac, dectobin(i))
            sleep(t)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()