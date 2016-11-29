#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time


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
    else:
        checkTempData()



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


if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    PIN = 2
    Temp = []

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
    
    GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(DIGIT1, True)
    GPIO.output(DIGIT2, True)
    GPIO.output(DIGIT3, True)
    GPIO.output(DIGIT4, True)

    try:
        t = 0.004
        checkTempData()
        while True:
            if (GPIO.input(btn) == 0 ):
                time.sleep(t)
                showDigit(3,int(Temp[0]/10),False)
                time.sleep(t)
                showDigit(4,int(Temp[0]%10),False)
                time.sleep(t)
            else:
                time.sleep(t)
                showDigit(3,int(Temp[1]/10),False)
                time.sleep(t)
                showDigit(4,int(Temp[1]%10),False)
                time.sleep(t)
    
    except KeyboardInterrupt:
        pass
    
    finally:
        GPIO.cleanup()
