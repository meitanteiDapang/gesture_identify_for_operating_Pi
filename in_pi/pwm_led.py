#coding:utf-8
import time
#加入时间模块用于延时
import RPi.GPIO as GPIO
#导入RPi.GPIO模块，
GPIO.setmode(GPIO.BCM)
#设置编码模式为BCM
GPIO.setwarnings(False)
#屏蔽警告信息

print('------------R,G,B---------------')
'''
R = 22
B = 17
G = 27
'''
R = 23
B = 24
G = 25

GPIO.setup(R,GPIO.OUT)		#设置R为输出功能
GPIO.setup(G,GPIO.OUT)		#设置G
GPIO.setup(B,GPIO.OUT)		#B
#--------------添加pwm
pwm_R = GPIO.PWM(R,50)
pwm_G = GPIO.PWM(G,50)
pwm_B = GPIO.PWM(B,50)
pwm_R.start(0)
pwm_G.start(0)
pwm_B.start(0)

def cmd0():
    #蓝灯闪
    pwm_B.ChangeDutyCycle(50)
    time.sleep(1)
    pwm_B.ChangeDutyCycle(0)
    time.sleep(1)
def cmd1():
    #绿灯闪
    pwm_G.ChangeDutyCycle(50)
    time.sleep(1)
    pwm_G.ChangeDutyCycle(0)
    time.sleep(1)
def cmd2():
    #红灯闪
    pwm_R.ChangeDutyCycle(50)
    time.sleep(1)
    pwm_R.ChangeDutyCycle(0)
    time.sleep(1)
def cmd3():
    #没有灯闪烁
    pwm_R.ChangeDutyCycle(0)
    time.sleep(1)
    pwm_R.ChangeDutyCycle(0)
    time.sleep(1)

'''
if __name__ == "__main__":
    try:
        while(True):
            cmd = int(input("please input cmd:"))
            if(0 == cmd):
                #0手势 蓝灯闪烁
                cmd0()
                break
            elif(1 == cmd):
                #1手势
                cmd1()
                break            
            elif(2 == cmd):
                #5手势
                cmd2()
                break
            else:
                break
    except KeyboardInterrupt:
        pass
    pwm_R.stop()
    pwm_G.stop()
    pwm_B.stop()

'''
