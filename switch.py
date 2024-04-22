import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
switch = 16
led = 8

GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while 1:
    button_state = GPIO.input(switch)
    if button_state == False:
        GPIO.output(led, True)
    while GPIO.input(switch) == False:
        time.sleep(0.5)
    else:
        GPIO.output(led, False)
    