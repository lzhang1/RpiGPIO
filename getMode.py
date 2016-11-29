import RPi.GPIO as GPIO
import time

strmap={\
GPIO.IN: "GPIO.IN",\
GPIO.OUT: "GPIO.OUT",\
GPIO.SPI: "GPIO.SPI",\
GPIO.I2C: "GPIO.I2C",\
GPIO.HARD_PWM: "GPIO.HARD_PWM",\
GPIO.SERIAL: "GPIO.SERAIL",\
GPIO.UNKNOWN: "GPIO.UNKNOWN"
}


GPIO.setmode(GPIO.BOARD)
for x in range(1,40):
    if x in [1,2,4,17]:
        print ("PIN"+str(x)+":POWER")
    elif x in [6,9,14,20,25,30,34,39]:
        print ("PIN"+str(x)+" :GND") 
    elif x in [27,28]:
        print ("PIN"+str(x)+" :UNKOWN")
    else:
        print ("PIN"+str(x)+" :"+strmap[GPIO.gpio_function(x)]) 
