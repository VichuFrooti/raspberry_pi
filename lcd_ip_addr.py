from subprocess import Popen, PIPE
from time import sleep, perf_counter
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

lcd_columns = 16
lcd_rows = 2

lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)

lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)

def find_interface():
    find_device = "ip addr show"
    interface_parse = run_cmd(find_device)
    for line in interface_parse.splitlines():
        if "state UP" in line:
            dev_name = line.split(':')[1]
            return dev_name
    return 1 
def parse_ip():
    if interface == 1: 
        return "not assigned " #
    ip = "0"
    find_ip = "ip addr show %s" % interface
    ip_parse = run_cmd(find_ip)
    for line in ip_parse.splitlines():
        if "inet " in line:
            ip = line.split(' ')[5]
            ip = ip.split('/')[0]
            return ip 
    return "pending      " 

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output.decode('ascii')

lcd.clear()
interface = find_interface()
ip_address = parse_ip()
timer = perf_counter()

while True:
    if perf_counter() - timer >= 15:
        interface = find_interface()
        ip_address = parse_ip()
        timer = perf_counter()

    lcd_line_1 = datetime.now().strftime('%b %d  %H:%M:%S\n')
    lcd_line_2 = "IP " + ip_address
    lcd.message = lcd_line_1 + lcd_line_2

    sleep(1)
