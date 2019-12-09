#coding:utf-8
#电机转

accelerating_forward = False
decelerating_forward = False
speed1 = 0

import time	#加入时间模块用于延时
import RPi.GPIO as GPIO	#导入RPi.GPIO模块，
import sys
from threading import *
GPIO.setmode(GPIO.BCM)	#设置编码模式为BCM
GPIO.setwarnings(False) #屏蔽警告信息

print('------------MOTO---------------')

MOTO1 = 6
MOTO2 = 19
MOTO3 = 13
MOTO4 = 26

GPIO.setup(MOTO1,GPIO.OUT)#设置引脚输出
GPIO.setup(MOTO2,GPIO.OUT)
GPIO.setup(MOTO3,GPIO.OUT)
GPIO.setup(MOTO4,GPIO.OUT)

pwm_MOTO1 = GPIO.PWM(MOTO1, 500)#设置pwm输出，的引脚和频率
pwm_MOTO2 = GPIO.PWM(MOTO2, 500)
pwm_MOTO3 = GPIO.PWM(MOTO3, 500)
pwm_MOTO4 = GPIO.PWM(MOTO4, 500)

pwm_MOTO1.start(0)#启用pwm，用占空比初始化
pwm_MOTO2.start(0)
pwm_MOTO3.start(0)#启用pwm，用占空比初始化
pwm_MOTO4.start(0)


def accelerate():
    global speed1
    while 1:
        if speed1 > 95:
            break
        if not accelerating_forward:
            break
        speed1 += 5
        if speed1 >= 0:
            pwm_MOTO1.ChangeDutyCycle(speed1)
            pwm_MOTO2.ChangeDutyCycle(speed1)
        if speed1 <= 0:
            pwm_MOTO3.ChangeDutyCycle(-speed1)
            pwm_MOTO4.ChangeDutyCycle(-speed1)
        time.sleep(1)
    sys.exit(1)
#创建一个子线程，第一个参数为子线程名称，第二个为参数
t1 = Thread(target = accelerate)

def decelerate():
    global speed1
    while 1:
        if speed1 < -95:
            break
        if not decelerating_forward:
            break
        speed1 -= 5
        if speed1 >= 0:
            pwm_MOTO1.ChangeDutyCycle(speed1)
            pwm_MOTO2.ChangeDutyCycle(speed1)
        if speed1 <= 0:
            pwm_MOTO3.ChangeDutyCycle(-speed1)
            pwm_MOTO4.ChangeDutyCycle(-speed1)
        time.sleep(1)
    sys.exit(1)
#创建一个子线程，第一个参数为子线程名称，第二个为参数
t2 = Thread(target = decelerate)

#def stop():
def cmd2():
    #停止
    pwm_MOTO1.ChangeDutyCycle(0)#更改占空比
    pwm_MOTO2.ChangeDutyCycle(0)
    pwm_MOTO3.ChangeDutyCycle(0)#更改占空比
    pwm_MOTO4.ChangeDutyCycle(0)

#def acc():
def cmd0():
    #前转加速
    global accelerating_forward
    global decelerating_forward
    if not decelerating_forward and not accelerating_forward:
        accelerating_forward = True
        t1 = Thread(target = accelerate)
        t1.start()

#def dec():
def cmd1():
    #后转加速
    global accelerating_forward
    global decelerating_forward
    if not accelerating_forward and not decelerating_forward:
        decelerating_forward= True 
        t2 = Thread(target = decelerate)
        t2.start()

#def keep():
def cmd3():
    #保持匀速
    global accelerating_forward
    global decelerating_forward
    accelerating_forward = False
    decelerating_forward = False
'''
try:
    while(1):
        time.sleep(0.1)
        
        cmd = int(input("input your cmd:"))
        if(0 == cmd):
            #停止
            pwm_MOTO1.ChangeDutyCycle(0)#更改占空比
            pwm_MOTO2.ChangeDutyCycle(0)

        elif(3 == cmd):
            #加速转
            if not decelerating_forward and not accelerating_forward:
                accelerating_forward = True
                t1 = Thread(target = accelerate)
                t1.start()
        elif(30==cmd):
            accelerating_forward = False
        elif(4 == cmd):
            #减速转
            if not accelerating_forward and not decelerating_forward:
                decelerating_forward= True 
                t2 = Thread(target = decelerate)
                t2.start()
        elif(40==cmd):
            decelerating_forward = False



except KeyboardInterrupt:
    pass
pwm_MOTO1.stop()#关闭pwm
pwm_MOTO2.stop()
'''        
