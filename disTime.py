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

DIGIT1=12     #32
DIGIT2=16     #36
DIGIT3=20     #38
DIGIT4=21     #40


btn = 17 #11

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
GPIO.setup(DIGIT1, GPIO.OUT)
GPIO.setup(DIGIT2, GPIO.OUT)
GPIO.setup(DIGIT3, GPIO.OUT)
GPIO.setup(DIGIT4, GPIO.OUT)

GPIO.output(DIGIT1, False)
GPIO.output(DIGIT2, False)
GPIO.output(DIGIT3, False)
GPIO.output(DIGIT4, False)

GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def showDigit(no, num,showDotPoint):
    GPIO.output(DIGIT1, True)
    GPIO.output(DIGIT2, True)
    GPIO.output(DIGIT3, True)
    GPIO.output(DIGIT4, True)
    
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

    elif (num == 9):
        GPIO.output(LED_A, True)
        GPIO.output(LED_B, True)
        GPIO.output(LED_C, True)
        GPIO.output(LED_D, True)
        GPIO.output(LED_E, False)
        GPIO.output(LED_F, True)
        GPIO.output(LED_G, True)
        GPIO.output(LED_DP, showDotPoint)

    if (no == 1 ):
        GPIO.output(DIGIT1, False)
    elif (no == 2):
        GPIO.output(DIGIT2, False)
    elif (no == 3):
        GPIO.output(DIGIT3, False)
    elif (no == 4):
        GPIO.output(DIGIT4, False)


try:
    t = 0.004
    while True:
        if (GPIO.input(btn) == 1 ):
            time.sleep(t)
            showDigit(1,int(time.strftime("%H",time.localtime(time.time())))/10,False)
            time.sleep(t)
            showDigit(2,int(time.strftime("%H",time.localtime(time.time())))%10,True)
            time.sleep(t)
            showDigit(3,int(time.strftime("%M",time.localtime(time.time())))/10,False)
            time.sleep(t)
            showDigit(4,int(time.strftime("%M",time.localtime(time.time())))%10,False)
            time.sleep(t)
        else:
            time.sleep(t)
            showDigit(1,int(time.strftime("%m",time.localtime(time.time())))/10,False)
            time.sleep(t)
            showDigit(2,int(time.strftime("%m",time.localtime(time.time())))%10,True)
            time.sleep(t)
            showDigit(3,int(time.strftime("%d",time.localtime(time.time())))/10,False)
            time.sleep(t)
            showDigit(4,int(time.strftime("%d",time.localtime(time.time())))%10,False)
            time.sleep(t)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
