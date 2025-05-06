import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dectobin(number):
    return [int(element) for element in bin(number)[2:].zfill(8)]

try:
    while True:
        number = input("Enter number from 0 to 255 ")
        try:
            number = int(number)
            if 0 <= number <= 255:
                GPIO.output(dac, dectobin(number))
                voltage = float(number) / 256.0 *3.3
                print(f"Output voltage is {voltage:.4} volt")
            else:
                if number < 0:
                    print("Enter number greater than or equal 0")
                elif number > 255:
                    print("number is out of range, it has to be less then 256")
        except Exception:
            if number == "q": 
                break
            elif number.isdigit() == 0: 
                print("Enter int digit")
            

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()