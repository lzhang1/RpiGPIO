#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

btn=2
Lpin=3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(btn,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Lpin,GPIO.OUT)

try:
    while True:
        #按下按钮
        if (GPIO.input(btn) == 0):
            #设为高电平
            GPIO.output(Lpin, True)
        else:
            GPIO.output(Lpin, False)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
