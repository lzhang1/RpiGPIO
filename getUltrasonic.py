#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import threading
import time
import sys
import os

GPIO.setmode(GPIO.BCM)
GPIO_Trigger=27
GPIO_Echo=22

GPIO.setwarnings(False)
GPIO.setup(GPIO_Trigger, GPIO.OUT)
GPIO.setup(GPIO_Echo, GPIO.IN)

disStack=[]
restoreFlag = 1

def getDistance():
    global disStack
    GPIO.output(GPIO_Trigger, False)
    time.sleep(0.02)
    GPIO.output(GPIO_Trigger, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_Trigger, False)
    start = time.time()

    while GPIO.input(GPIO_Echo) == 0:
        start = time.time()

    while GPIO.input(GPIO_Echo) == 1:
        stop = time.time()

    elapsed = stop - start
    distance = elapsed * 343000
    distance = distance / 2
    if len(disStack) == 2:
        for i in xrange(len(disStack)-1):
            disStack[i]=disStack[i+1]
        disStack.pop()
    disStack.append(distance)
    print disStack


def changeFlag():
    global restoreFlag 
    restoreFlag = 1

def clearScreen():
    os.write(1,".")
    sys.stdout.flush()
    time.sleep(1)

try: 
    start_time=time.time()
    num = 0
    while True:
        getDistance()
        if restoreFlag == 1 and (max(disStack)-min(disStack)>300):
            num += 1
            print "\nFound someone"
            restoreFlag = 0
            t=threading.Timer(1,changeFlag)
            t.start()
        else:
            clearScreen()
            pass
        print restoreFlag
except KeyboardInterrupt:
    stop_time=time.time()
    print "Time:%f Num:%d passed"%(stop_time-start_time,num)
    pass

finally:
    GPIO.cleanup()

