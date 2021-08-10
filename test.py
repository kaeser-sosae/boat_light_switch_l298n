# Follow instructions at https://pypi.org/project/rpi-hardware-pwm/

from rpi_hardware_pwm import HardwarePWM
from decimal import Decimal
import time
import os
import RPi.GPIO as GPIO
from time import sleep
import pigpio

pi = pigpio.pi('localhost', 8888)


in1 = 24
in2 = 23
en = 25
temp1=1

#!/usr/bin/python3
# File name   : motor.py
# Description : Control Motors 
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2018/10/12

import RPi.GPIO as GPIO
import time
# motor_EN_A: Pin7  |  motor_EN_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

Motor_A_EN    = 18

Motor_A_Pin1  = 24
Motor_A_Pin2  = 23

Dir_forward   = 0
Dir_backward  = 1

pwm_A = 0

#GPIO.setmode(GPIO.BOARD)

def setup():#Motor initialization
    global pwm_A, pwm_B
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor_A_EN, GPIO.OUT)
    GPIO.setup(Motor_A_Pin1, GPIO.OUT)
    GPIO.setup(Motor_A_Pin2, GPIO.OUT)

    try:
        #pwm_A = GPIO.PWM(Motor_A_EN, 10000)
        #pwm_A = HardwarePWM(0, hz=100)
        pi.set_PWM_frequency(18,40000)
    except:
        print('Could not define PWM pin')

def motorStop():#Motor stops
    GPIO.output(Motor_A_Pin1, GPIO.LOW)
    GPIO.output(Motor_A_Pin2, GPIO.LOW)
    GPIO.output(Motor_A_EN, GPIO.LOW)

def motor1(status, direction, speed):#Motor 1 positive and negative rotation
    global pwm_A
    #print('Frequency is currently ' + str(pi.get_PWM_frequency(18)))
    #print('Range is currently ' + str(pi.get_PWM_range(18)))
    #print('Duty Cycle is currently ' + str(pi.get_PWM_dutycycle(18)))
    if status == 0: # stop
        motorStop()
    else:
        if direction == Dir_forward:#
            GPIO.output(Motor_A_Pin1, GPIO.HIGH)
            GPIO.output(Motor_A_Pin2, GPIO.LOW)
            pi.set_PWM_dutycycle(18,speed)
            #pwm_A.start(100)
            #pwm_A.change_duty_cycle(speed)
        elif direction == Dir_backward:
            GPIO.output(Motor_A_Pin1, GPIO.LOW)
            GPIO.output(Motor_A_Pin2, GPIO.HIGH)
            pi.set_PWM_dutycycle(18,speed)
            #pwm_A.start(100)
            #pwm_A.change_duty_cycle(speed)
    return direction

def destroy():
        motorStop()
        GPIO.cleanup()             # Release resource

setup()

while(1):

        x=input()
    


        if x=='0':
                print("motor stop")
                motorStop()
                x='z'

        elif x=='exit':
                destroy()

        else:
                motor1(1, Dir_backward, float(x))