#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import sys
import time


if len(sys.argv)==3:
    print ("PIN%s: blinking..."%sys.argv[1])
    num = int(sys.argv[1])
    Times = int(sys.argv[2])
else:
    num = 11
    Times = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(num,GPIO.OUT)
try:
    for i in range(1,Times):
        GPIO.output(num,GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(num,GPIO.LOW)
        time.sleep(0.2)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
