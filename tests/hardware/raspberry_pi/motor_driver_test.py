#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# for 1st Motor on ENA
ENA = 33
IN1 = 35
IN2 = 37
ENB = 32
IN3 = 38
IN4 = 40
ENA1 = 31
IN11 = 29
IN21 = 26
ENB1 = 24
IN11 = 23
IN21 = 22

# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)

# initialize EnA, In1 and In2
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setwarnings(False)
# Stop
GPIO.output(ENA, GPIO.HIGH)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.setup(ENB, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
time.sleep(1)

# Forward
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW)
time.sleep(1)

# Stop
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)
time.sleep(1)

# Backward
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.HIGH)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.HIGH)
time.sleep(1)

# Stop
GPIO.output(ENA, GPIO.LOW)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(ENB, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)
time.sleep(1)

GPIO.cleanup()
