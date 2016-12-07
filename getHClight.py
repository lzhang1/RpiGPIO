#!/usr/bin/env python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

flag = 1 
NUM = 0

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.IN)
    GPIO.setup(27,GPIO.OUT)


def blink():
    while True:
        if GPIO.input(18):
            GPIO.output(27,GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(27,GPIO.HIGH)
            print "There is some one here"
            global NUM
            NUM += 1
        else:
            GPIO.output(27,GPIO.HIGH)
            print "There is on one here"
        time.sleep(2)


try:
    start_time = time.time()
    init()
    print "Start to detect..."
    blink()

except KeyboardInterrupt:
    end_time = time.time()
    print "Totil Time:%.0f, NUM:%d"%((end_time-start_time)/60, NUM)
    print "End"

finally:
    GPIO.cleanup()

