#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

R,G,B=14,18,15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(R,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)

pwmR = GPIO.PWM(R,80)
pwmG = GPIO.PWM(G,80)
pwmB = GPIO.PWM(B,80)
pwmR.start(0)
pwmB.start(0)
pwmG.start(0)


try:
    T = 0.5
    while True:
        #Red
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(100)
        time.sleep(T)

        #Green
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(100)
        time.sleep(T)

        #Blue
        pwmR.ChangeDutyCycle(100)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(0)
        time.sleep(T)

        #yellow
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(100)
        time.sleep(T)

        #magenta
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(100)
        pwmB.ChangeDutyCycle(0)
        time.sleep(T)

        #white
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        time.sleep(T)
        
        #multcolor
        for r in xrange(0,101,20):
            pwmR.ChangeDutyCycle(r)
            for g in xrange(0,101,20):
                pwmG.ChangeDutyCycle(g)
                for b in xrange(0,101,20):
                    pwmB.ChangeDutyCycle(b)
                    time.sleep(T)

except KeyboardInterrupt:
    pass

finally:
    pwmR.stop()
    pwmG.stop()
    pwmB.stop()
    GPIO.cleanup()
