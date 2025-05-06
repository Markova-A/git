import RPi.GPIO as GPIO
import time 
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
led = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 0)
GPIO.setup(comp, GPIO.IN)

def dectobin(val):
    return [int(el) for el in bin(val)[2:].zfill(8)]

def adc():
    i = 128
    GPIO.output(dac, dectobin(i))
    time.sleep(0.01)
    if GPIO.input(comp) == 1: 
        i = i - 128
    i = i + 64   
    GPIO.output(dac, dectobin(i))
    time.sleep(0.01)
    if GPIO.input(comp) == 1: 
        i = i - 64
    i = i + 32
    GPIO.output(dac, dectobin(i))
    time.sleep(0.01)
    if GPIO.input(comp) == 1: 
        i = i - 32
    i = i + 16
    GPIO.output(dac, dectobin(i))
    time.sleep(0.01)
    if GPIO.input(comp) == 1: 
        i = i - 16
    i = i + 8
    GPIO.output(dac, dectobin(i))
    time.sleep(0.01)
    if GPIO.input(comp) == 1: 
        i = i - 8
    i = i + 4
    GPIO.output(dac, dectobin(i))
    time.sleep(0.01)
    if GPIO.input(comp) == 1: 
        i = i - 4
    i = i + 2
    GPIO.output(dac, dectobin(i))
    time.sleep(0.01)
    if GPIO.input(comp) == 1: 
        i = i - 2
    i = i + 1
    GPIO.output(dac, dectobin(i))
    time.sleep(0.01)
    if GPIO.input(comp) == 1: 
        i = i - 1
    return i

try:
    measure_data = []
    start_time = time.time()
    val = 0

    print("charge\n")

    GPIO.output(troyka, 1)
    while (val/256 <= 0.95):
        print(val)
        val = adc()
        measure_data.append(val)

    print("uncharge\n")

    GPIO.output(troyka, 0)
    while (val/256 >= 0.02):
        val = adc()
        print(val)
        measure_data.append(val)

    end_time = time.time()
    experiment_time = end_time - start_time

    plt.plot(measure_data)
    plt.show()

    measure_data_str = [str(item) for item in measure_data]

    with open("data.txt", "w") as output:
        output.write("\n".join(measure_data_str))

    freq = str(len(measure_data)/experiment_time)
    step = str(3.3 / 256)
    intfreq = len(measure_data)/experiment_time
    p = 1 / intfreq

    with open("settings.txt", "w") as settings:
        settings.write(freq)
        settings.write("\n")
        settings.write(step)

    print("experiment time - ")
    print(experiment_time)
    print("\nperiod")
    print(p)
    print("\nfrequency")
    print(float(freq))
    print("\nstep")
    print(step)

finally:
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()