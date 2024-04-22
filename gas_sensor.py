import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
do_pin = 7
GPIO.setup(do_pin, GPIO.IN)
try:
    while 1:
        gas_present = GPIO.input(do_pin)
        if gas_present == GPIO.LOW:
            gas_present = "Gas Present"
        else:
            gas_present = "No gas"
        print("Gas State:", gas_present)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
GPIO.cleanup()