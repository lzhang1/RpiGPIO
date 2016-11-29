#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time


LED_A=26   #37
LED_B=19   #35
LED_C=13   #33
LED_D=6    #31
LED_E=5    #29
LED_F=11   #23
LED_G=9    #21
LED_DP=10  #19

VCC=12     #32

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_A, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
GPIO.setup(LED_C, GPIO.OUT)
GPIO.setup(LED_D, GPIO.OUT)
GPIO.setup(LED_E, GPIO.OUT)
GPIO.setup(LED_F, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_DP, GPIO.OUT)
GPIO.setup(VCC, GPIO.OUT)


def showDigit(num,showDotPoint):
    GPIO.setup(VCC, False)
    
    if (num ==0 ):
        GPIO.output(LED_A, True)
        GPIO.output(LED_B, True)
        GPIO.output(LED_C, True)
        GPIO.output(LED_D, True)
        GPIO.output(LED_E, True)
        GPIO.output(LED_F, True)
        GPIO.output(LED_G, False)
        GPIO.output(LED_DP, showDotPoint)
    elif (num == 1):
        GPIO.output(LED_A, False)
        GPIO.output(LED_B, True)
        GPIO.output(LED_C, True)
        GPIO.output(LED_D, False)
        GPIO.output(LED_E, False)
        GPIO.output(LED_F, False)
        GPIO.output(LED_G, False)
        GPIO.output(LED_DP, showDotPoint)
    elif (num == 2):
        GPIO.output(LED_A, True)
        GPIO.output(LED_B, True)
        GPIO.output(LED_C, False)
        GPIO.output(LED_D, True)
        GPIO.output(LED_E, True)
        GPIO.output(LED_F, False)
        GPIO.output(LED_G, True)
        GPIO.output(LED_DP, showDotPoint)
    elif (num == 3):
        GPIO.output(LED_A, True)
        GPIO.output(LED_B, True)
        GPIO.output(LED_C, True)
        GPIO.output(LED_D, True)
        GPIO.output(LED_E, False)
        GPIO.output(LED_F, False)
        GPIO.output(LED_G, True)
        GPIO.output(LED_DP, showDotPoint)
    elif (num == 4):
        GPIO.output(LED_A, False)
        GPIO.output(LED_B, True)
        GPIO.output(LED_C, True)
        GPIO.output(LED_D, False)
        GPIO.output(LED_E, False)
        GPIO.output(LED_F, True)
        GPIO.output(LED_G, True)
        GPIO.output(LED_DP, showDotPoint)
    elif (num == 5):
        GPIO.output(LED_A, True)
        GPIO.output(LED_B, False)
        GPIO.output(LED_C, True)
        GPIO.output(LED_D, True)
        GPIO.output(LED_E, False)
        GPIO.output(LED_F, True)
        GPIO.output(LED_G, True)
        GPIO.output(LED_DP, showDotPoint)
    elif (num == 6):
        GPIO.output(LED_A, True)
        GPIO.output(LED_B, False)
        GPIO.output(LED_C, True)
        GPIO.output(LED_D, True)
        GPIO.output(LED_E, True)
        GPIO.output(LED_F, True)
        GPIO.output(LED_G, True)
        GPIO.output(LED_DP, showDotPoint)
    elif (num == 7):
        GPIO.output(LED_A, True)
        GPIO.output(LED_B, True)
        GPIO.output(LED_C, True)
        GPIO.output(LED_D, False)
        GPIO.output(LED_E, False)
        GPIO.output(LED_F, False)
        GPIO.output(LED_G, False)
        GPIO.output(LED_DP, showDotPoint)
    elif (num == 8):
        GPIO.output(LED_A, True)
        GPIO.output(LED_B, True)
        GPIO.output(LED_C, True)
        GPIO.output(LED_D, True)
        GPIO.output(LED_E, True)
        GPIO.output(LED_F, True)
        GPIO.output(LED_G, True)
        GPIO.output(LED_DP, showDotPoint)

    else:
        GPIO.output(LED_A, True)
        GPIO.output(LED_B, True)
        GPIO.output(LED_C, True)
        GPIO.output(LED_D, True)
        GPIO.output(LED_E, False)
        GPIO.output(LED_F, True)
        GPIO.output(LED_G, True)
        GPIO.output(LED_DP, showDotPoint)

    GPIO.output(VCC, True)


try:

    for x in xrange(9,-1,-1):
        showDigit(x,True)
        time.sleep(1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
