import RPi.GPIO as GPIO
import time

pins = [3, 5, 11, 15, 19, 18, 22]
GPIO.setmode(GPIO.BOARD)

for i in pins:
    GPIO.setup(i, GPIO.OUT, initial= GPIO.LOW)

arr = [[1, 1, 1, 1, 1, 1, 0],
       [0, 1, 1, 0, 0, 0, 0],
       [1, 1, 0, 1, 1, 0, 1],
       [1, 1, 1, 1, 0, 0, 1],
       [0, 1, 1, 0, 0, 1, 1],
       [1, 0, 1, 1, 0, 1, 1],
       [1, 0, 1, 1, 1, 1, 1],
       [1, 1, 1, 0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 1],
       [1, 1, 1, 1, 0, 1, 1]]

while 1:
    for num in arr:
        for i in range(7):
            if(not num[i]):
                GPIO.output(pins[i], GPIO.HIGH)
        time.sleep(0.1)
        for i in range(7):
            GPIO.output(pins[i], GPIO.LOW)
        