import RPi.GPIO as GPIO
import time
from time import sleep
from rpi_lcd import LCD
from pad4pi import rpi_gpio


m1=22
m2=23
m3=25
m4=24
l1=17
l2=18
l3=15
l4=14
#pwm2=27
#speed=90
lcd = LCD()
GPIO.setmode(GPIO.BCM)
GPIO.setup(m1,GPIO.OUT)
GPIO.setup(m2,GPIO.OUT)
GPIO.setup(m3,GPIO.OUT)
GPIO.setup(m4,GPIO.OUT)
GPIO.setup(l1,GPIO.OUT)
GPIO.setup(l2,GPIO.OUT)
GPIO.setup(l3,GPIO.OUT)
GPIO.setup(l4,GPIO.OUT)
GPIO.output(l2,GPIO.HIGH)
GPIO.output(l1,GPIO.HIGH)
GPIO.output(l4,GPIO.HIGH)
GPIO.output(l3,GPIO.HIGH)
#GPIO.setup(pwm2,GPIO.OUT)
#p2=GPIO.PWM(pwm2,1000)
#p2.start(speed)
def path1():
    lcd.clear()
    lcd.text('Welcome', 1)
    lcd.text('running', 2)
    f()
    sleep(2)
    s()
    sleep(1)
    b()
    sleep(2)
    s()
    sleep(1)
    lcd.text('Please enter    ',1)
    lcd.text('PASSWORD        ',2)
   
def b():
    GPIO.output(m1,GPIO.HIGH)
    GPIO.output(m2,GPIO.LOW)
    GPIO.output(m3,GPIO.HIGH)
    GPIO.output(m4,GPIO.LOW)
def f():
    GPIO.output(m2,GPIO.HIGH)
    GPIO.output(m1,GPIO.LOW)
    GPIO.output(m4,GPIO.HIGH)
    GPIO.output(m3,GPIO.LOW)
def r():
    GPIO.output(m1,GPIO.LOW)
    GPIO.output(m2,GPIO.HIGH)
    GPIO.output(m3,GPIO.HIGH)
    GPIO.output(m4,GPIO.LOW)
def l():
    GPIO.output(m1,GPIO.HIGH)
    GPIO.output(m2,GPIO.LOW)
    GPIO.output(m3,GPIO.LOW)
    GPIO.output(m4,GPIO.HIGH)
def s():
    GPIO.output(m2,GPIO.LOW)
    GPIO.output(m1,GPIO.LOW)
    GPIO.output(m4,GPIO.LOW)
    GPIO.output(m3,GPIO.LOW)
#******************************************#
KEYPAD = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]
COL_PINS = [8, 7, 1, 12] # BCM numbering
ROW_PINS = [16,20,21,26] # BCM numbering

factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

#******************************************#
pw=''
def demo(key):
    global pw
    pw=pw+str(key)
    lcd.clear()
    lcd.text('you entered:', 1)
    lcd.text(pw, 2)
    print(key)
    if pw=='1234':
        print('Tray 1 opened')
        GPIO.output(l1,GPIO.LOW)
        pw=''
        lcd.text('      BOX1      ', 1)
        lcd.text('     OPENED     ', 2)
        sleep(10)
        lcd.clear()
        GPIO.output(l1,GPIO.HIGH)
    elif pw=='5050':
        print('Tray 2 opened')
        GPIO.output(l2,GPIO.LOW)
        pw=''
        lcd.text('      BOX2      ', 1)
        lcd.text('     OPENED     ', 2)
        sleep(10)
        lcd.clear()
        GPIO.output(l2,GPIO.HIGH)
    elif pw=='0000':
        print('Tray 3 opened')
        GPIO.output(l3,GPIO.LOW)
        pw=''
        lcd.text('      BOX3      ', 1)
        lcd.text('     OPENED     ', 2)
        sleep(10)
        lcd.clear()
        GPIO.output(l3,GPIO.HIGH)
    elif pw=='1515':
        print('Tray 4 opened')
        GPIO.output(l4,GPIO.LOW)
        pw=''
        lcd.text('      BOX4      ', 1)
        lcd.text('     OPENED     ', 2)
        sleep(10)
        GPIO.output(l4,GPIO.HIGH)
    elif len(pw)>3:
        print('wrong password')
        pw=''
        lcd.text('     WRONG      ', 1)
        lcd.text('    PASSWORD    ', 2)
       
   
       
   
def printKey(key):
    demo(key)
   

#******************************************#
path1()
# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)





# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005


#******************************************#
def main():
  # Main program block
  global pm
  global system_sts
 
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO number
  while True:
      time.sleep(1)


   

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
