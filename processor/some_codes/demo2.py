# coding=utf-8
# 主线程执行拍照操作
# 开启子线程从照片目录中获取最新照片传到模型中进行检测
import sys
sys.path.append("../")
import os  # 打开文件时需要
from PIL import Image
import re
import math # 用于数学运算
import numpy as np # numpy库，用于科学计算
import matplotlib.pyplot as plt  # matlab绘图
import matplotlib.image as mping  # 图像显示
import wtfcv
from threading import Thread # 导入线程模块
import time
import math #用于数学运算
import tensorflow as tf #tensorflow库
import h5py #用于读写数据
from tensorflow.python.framework import ops
from tensorflow import keras

from PIL import Image
import random
import cv2

target_dir = "/Users/yzh/Desktop/motion/"  # 拍照存储照片路径
cp_dir = "/Users/yzh/Desktop/motion2/"
i = 0  # 照片编号
pic_name = target_dir + "gesture" + str(i)+".jpg"
thread_running = True

mmm = keras.models.load_model("../model/1.h5")  # 读取model


class myThread (Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while 1:
            if not thread_running:
                break
            time.sleep(5)

            # ---------------------进行裁剪，缩放，并保存
            pic = 0
            dir_path = '../pi_test_image_orig/'
            path = dir_path + str(pic) + '.jpg'
            print(path)
            im = Image.open(path)
            # im = im.crop((160, 0, 480, 480))  # 裁剪
            im = im.resize((64, 64), Image.ANTIALIAS)  # 缩放
            sbpath = "../pi_test_image_pre/" + str(pic) + ".jpg"
            print(sbpath)
            im.save(sbpath)

            # ------------------- 利用wtfcv 去除背景，获得对应矩阵
            pi_image = wtfcv.to_no_background("../pi_test_image_pre/" + str(i) + ".jpg")  # 读取
            here1 = np.array([pi_image])
            here1 = here1 / 255  # 一些必要处理
            prediction_pi_image5 = mmm.predict(here1)
            print(prediction_pi_image5[0]) # 预测向量打印


if __name__ == '__main__':  
    thread1 = myThread()
    # 开启新线程
    thread1.start()
    print('主线程拍照')
    # 方法一：用motion命令来进行拍照，从指定文件夹获取照片
    # os.system("sudo motion")
    try:
        # print(0)
        cap = cv2.VideoCapture(0)
        # print(1)
        cap.set(3, 480)
        cap.set(4, 480)
        while True:
            # print(2)
            ret, frame = cap.read()
            k = cv2.waitKey(1)
            # print(4)
            cv2.imshow("nmsl",frame)
            if k == 27:
                break
            elif k == ord('s'):
                cv2.imwrite('../pi_test_image_orig/' + str(i) + '.jpg', frame)
            # pic_name = target_dir + "gesture" +str(i)+".jpg"
            # cmd = "fswebcam /dev/video0 -S 10 --no-banner -r 800x600 " + pic_name
            # os.system(cmd)
            # time.sleep(1)
            # i += 1

    except KeyboardInterrupt:
        # 写杀死子线程
        pass
    thread_running = False
    cap.release()
    cv2.destroyAllWindows()


