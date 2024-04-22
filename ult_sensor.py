import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
trigger_pin = 23
echo_pin = 24
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
try:
    while 1:
        GPIO.output(trigger_pin, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(trigger_pin, GPIO.LOW)
        while GPIO.input(echo_pin) == 0:
            start = time.time()
        while GPIO.input(echo_pin) == 1:
            end = time.time()
        pulse_duration = end - start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print("Distance:", distance, "cm")
        time.sleep(1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()