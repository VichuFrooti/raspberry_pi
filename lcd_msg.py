from Adafruit_CharLCD import Adafruit_CharLCD 
from time import sleep
lcd = Adafruit_CharLCD (rs=26, en=19, d4=13, d5=6, d6=5, d7=21, cols=16, lines=2)
lcd.clear()
lcd.message('Hello\nWorld!!!')
sleep(2)
try:
    while 1:
        for x in range(0, 16):
            lcd.move_left()
            sleep(0.1)
        sleep(1)
        # scroll Right
        for x in range(0, 16):
            lcd.move_right()
            sleep(0.1)
        sleep(3)
except KeyboardInterrupt:
    pass
lcd.clear()