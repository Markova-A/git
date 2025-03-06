import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

pwm = GPIO.PWM(24, 1000)
pwm.start(0)

try:
    while True:
        duty_cycle = (int)(input("Enter duty cycle "))
        pwm.ChangeDutyCycle(duty_cycle)



finally:
    pwm.stop()
    GPIO.output(24, 0)
    GPIO.cleanup()