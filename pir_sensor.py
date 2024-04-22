import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
inp = 8
led = 10
dig = 0
GPIO.setup(inp, GPIO.IN)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

pins = [12, 16, 15, 22, 24, 3, 5]
for i in range(7):
    GPIO.setup(pins, GPIO.OUT, initial=GPIO.LOW)
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

def DigitDisplay(digit):
    for i in range(7):
        GPIO.output(pins[i], GPIO.HIGH)

while 1:
    if GPIO.input(inp):
        DigitDisplay(arr[dig])
        dig = (dig + 1) % 10
    time.sleep(1)