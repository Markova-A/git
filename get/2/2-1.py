import RPi.GPIO as GPIO
import time

led = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

for i in range (3):
    for j in range (len(led)):
        GPIO.output(led[j], 1)
        time.sleep(0.2)
        GPIO.output(led[j], 0)

GPIO.cleanup()