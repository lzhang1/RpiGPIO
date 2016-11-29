#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

R,G,B=14,18,15

btnR,btnG,btnB=21,20,16

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(R,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)

GPIO.setup(btnR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(btnG,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(btnB,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    GPIO.output(R,True)
    GPIO.output(B,True)
    GPIO.output(G,True)

    while True:
        if (GPIO.input(btnR) == 0):
            GPIO.output(R, False)
        else:
            GPIO.output(R, True)
        
        if (GPIO.input(btnB) == 0):
            GPIO.output(B, False)
        else:
            GPIO.output(B, True)

        if (GPIO.input(btnG) == 0):
            GPIO.output(G, False)
        else:
            GPIO.output(G, True)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
