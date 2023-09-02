#!/usr/bin/python3

# File name   : motor_pwm_test.py
# Description : Test  Motors Control
# E-mail      : me@claudiofreddi.eu
# Author      : Claudio Freddi
# Date        : 2023-08-28

#run 
#

import RPi.GPIO as GPIO
import time


Motor_Left_EN    = 25
Motor_Right_EN    = 4 
Motor_Left_Pin1  = 23 
Motor_Left_Pin2  = 24 
Motor_Right_Pin1  = 14 
Motor_Right_Pin2  = 15 

Dir_forward   = 0
Dir_backward  = 1

pwm_Left = 0
pwm_Right = 0

def setup(): #Motor initialization
    global pwm_Left, pwm_Right
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor_Left_EN, GPIO.OUT)
    GPIO.setup(Motor_Right_EN, GPIO.OUT)
    GPIO.setup(Motor_Left_Pin1, GPIO.OUT)
    GPIO.setup(Motor_Left_Pin2, GPIO.OUT)
    GPIO.setup(Motor_Right_Pin1, GPIO.OUT)
    GPIO.setup(Motor_Right_Pin2, GPIO.OUT)
    try:
        pwm_Left = GPIO.PWM(Motor_Left_EN, 1000)
        pwm_Right = GPIO.PWM(Motor_Right_EN, 1000)
    except:
        pass

def motorStop():#Motor stops
    GPIO.output(Motor_Left_Pin1, GPIO.LOW)
    GPIO.output(Motor_Left_Pin2, GPIO.LOW)
    GPIO.output(Motor_Right_Pin1, GPIO.LOW)
    GPIO.output(Motor_Right_Pin2, GPIO.LOW)
    GPIO.output(Motor_Left_EN, GPIO.LOW)
    GPIO.output(Motor_Right_EN, GPIO.LOW)

def motor_right(status, direction, speed):#Motor 2 positive and negative rotation
    global  pwm_Right
    if status == 0: # stop
        motorStop()
    else:
        if direction == Dir_forward:
            GPIO.output(Motor_Right_Pin1, GPIO.HIGH)
            GPIO.output(Motor_Right_Pin2, GPIO.LOW)
            pwm_Right.start(100)
            pwm_Right.ChangeDutyCycle(speed)
        elif direction == Dir_backward:
            GPIO.output(Motor_Right_Pin1, GPIO.LOW)
            GPIO.output(Motor_Right_Pin2, GPIO.HIGH)
            pwm_Right.start(0)
            pwm_Right.ChangeDutyCycle(speed)

def motor_left(status, direction, speed):
    global pwm_Left
    if status == 0: # stop
        motorStop()
    else:
        if direction == Dir_forward:#
            GPIO.output(Motor_Left_Pin1, GPIO.HIGH)
            GPIO.output(Motor_Left_Pin2, GPIO.LOW)
            pwm_Left.start(100)
            pwm_Left.ChangeDutyCycle(speed)
        elif direction == Dir_backward:
            GPIO.output(Motor_Left_Pin1, GPIO.LOW)
            GPIO.output(Motor_Left_Pin2, GPIO.HIGH)
            pwm_Left.start(0)
            pwm_Left.ChangeDutyCycle(speed)
    return direction


def destroy():
    motorStop()
    GPIO.cleanup()            


try:
    pass
except KeyboardInterrupt:
    destroy()

def GoFw(speed, duration):
   motor_left(1, Dir_forward,speed)
   motor_right(1, Dir_forward,speed)
   time.sleep(duration)

def GoBw(speed, duration):
   motor_left(1, Dir_backward,speed)
   motor_right(1, Dir_backward,speed)
   time.sleep(duration)

def RotateLeft(speed, duration):
   motor_left(1, Dir_backward,speed)
   motor_right(1, Dir_forward,speed)
   time.sleep(duration)

def RotateRight(speed, duration):
   motor_left(1, Dir_forward,speed)
   motor_right(1, Dir_backward,speed)
   time.sleep(duration)

def main():
   setup()
   GoFw(50,2)
   GoBw(50,2)
   RotateLeft(50,2)
   RotateRight(50,2)
   
   motorStop()

if __name__ == '__main__':
    main()
