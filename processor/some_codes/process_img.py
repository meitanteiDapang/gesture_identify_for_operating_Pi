#coding:utf-8
import os  #打开文件时需要
from PIL import Image
import re



for i in range(6):
    dir_path = '../origin1/'+str(i)+'/'
    ignore_list = ['.DS_Store']
    image_list=os.listdir(dir_path)
    a = 1
    for pic in image_list:
        if pic in ignore_list:
            continue
        path = dir_path + pic
        im = Image.open(path)
        print(path,':', im.size)
        im = im.resize((128, 128), Image.ANTIALIAS)
        im.save("../converted_images128/"+str(i)+"/bb"+ str(a)+".jpg")
        a += 1
