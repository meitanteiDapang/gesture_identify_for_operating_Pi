import sys
sys.path.append("../")

import os  #打开文件时需要
from PIL import Image
import re
import math #用于数学运算
import numpy as np #numpy库，用于科学计算
import matplotlib.pyplot as plt  #matlab绘图
import matplotlib.image as mping #图像显示
import wtfcv

# 先打开图片

pic = 5

dir_path = '../pi_test_image_orig/'
path = dir_path + str(pic) + '.jpg'
im = Image.open(path)
im = im.crop((160, 0, 480, 480))  # 裁剪
im = im.resize((64, 64), Image.ANTIALIAS)  # 缩放
im.save("../pi_test_image_pre/" + str(pic) + ".jpg")
