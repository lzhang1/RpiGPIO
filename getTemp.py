#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

PIN = 2
Temp = []

def getTempData():
    data = []
    j = 0
    time.sleep(1)
    GPIO.setup(PIN, GPIO.OUT)

    GPIO.output(PIN, GPIO.LOW)
    time.sleep(0.06)
    GPIO.output(PIN, GPIO.HIGH)

    GPIO.setup(PIN, GPIO.IN)

    while GPIO.input(PIN) == GPIO.LOW:
        continue

    while GPIO.input(PIN) == GPIO.HIGH:
        continue

    while j < 40:
        k = 0
        while GPIO.input(PIN) == GPIO.LOW:
            continue
        while GPIO.input(PIN) == GPIO.HIGH:
            k += 1
            if k > 100:
                break
        if k < 8:
            data.append(0)
        else:
            data.append(1)

        j += 1
    return data

def checkTempData():
    global Temp
    data = getTempData()
    humidity_bit = data[0:8]
    humidity_point_bit = data[8:16]
    temperature_bit = data[16:24]
    temperature_point_bit = data[24:32]
    check_bit = data[32:40]


    humidity = 0
    humidity_point = 0
    temperature = 0
    temperature_point = 0
    check = 0

    for i in range(8):
        humidity += humidity_bit[i]*2**(7-i)
        humidity_point += humidity_point_bit[i]*2**(7-i)
        temperature += temperature_bit[i]*2**(7-i)
        temperature_point += temperature_point_bit[i]*2**(7-i)
        check += check_bit[i]*2**(7-i)


    tmp=humidity+humidity_point+temperature+temperature_point  
    if check==tmp:  
        Temp.append(temperature)
        Temp.append(humidity)
        print Temp
    else:
        checkTempData()


try:
    while True:
        del Temp[:]
        checkTempData()
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
