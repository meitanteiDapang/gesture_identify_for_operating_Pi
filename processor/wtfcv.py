import cv2
import numpy as np
import time
from matplotlib import pyplot as plt
################################################################################


def to_no_background(imgFile):


    width = 63
    height = 63
    # load an original image
    img = cv2.imread(imgFile)

    while img is None:
        time.sleep(1)
        print("none")
        img = cv2.imread(imgFile)
    # print(img.shape)
    # access a pixel at (row,column) coordinates
    px = img[width, height]


    # access a pixel from blue channel
    blue = img[width, height, 0]
    # access a pixel from green channel
    green = img[width, height, 1]
    # access a pixel from red channel
    red = img[width, height, 2]

    ################################################################################




    img[width, height] = [0, 0, 0]

    ################################################################################
    # better way: using numpy

    # access a pixel from blue channel
    blue = img.item(30, height, 0)
    # access a pixel from green channel
    green = img.item(30, height, 1)
    # access a pixel from red channel
    red = img.item(30, height, 2)


    # warning: we can only change pixels in gray or single-channel image

    # modify green value: (row,col,channel)
    img.itemset((30, height, 1), 255)
    # read green value
    green = img.item(30, height, 1)

    ################################################################################



    rows, cols, channels = img.shape

    # prepare an empty image space
    imgSkin = np.zeros(img.shape, np.uint8)
    # copy original image
    imgSkin = img.copy()

    for r in range(rows):
        for c in range(cols):

            # get pixel value
            B = img.item(r, c, 0)
            G = img.item(r, c, 1)
            R = img.item(r, c, 2)

            # non-skin area if skin equals 0, skin area otherwise
            skin = 0

            if (abs(R - G) > 15) and (R > G) and (R > B):
                if (R > 95) and (G > 40) and (B > 20) and (max(R, G, B) - min(R, G, B) > 15):
                    skin = 1
                    # print 'Condition 1 satisfied!'
                elif (R > 220) and (G > 210) and (B > 170):
                    skin = 1
                    # print 'Condition 2 satisfied!'

            if 0 == skin:
                imgSkin.itemset((r, c, 0), 0)
                imgSkin.itemset((r, c, 1), 0)
                imgSkin.itemset((r, c, 2), 0)
                # print 'Skin detected!'

    # convert color space of images because of the display difference between cv2 and matplotlib
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgSkin = cv2.cvtColor(imgSkin, cv2.COLOR_BGR2RGB)
    # cv2.imwrite("./image/test1.jpg", imgSkin)
    # plt.imshow(imgSkin)
    return imgSkin


def to_no_background_with_image(img):
    width = 63
    height = 63

    # access a pixel at (row,column) coordinates
    px = img[width, height]


    # access a pixel from blue channel
    blue = img[width, height, 0]
    # access a pixel from green channel
    green = img[width, height, 1]
    # access a pixel from red channel
    red = img[width, height, 2]

    ################################################################################




    img[width, height] = [0, 0, 0]

    ################################################################################
    # better way: using numpy

    # access a pixel from blue channel
    blue = img.item(30, height, 0)
    # access a pixel from green channel
    green = img.item(30, height, 1)
    # access a pixel from red channel
    red = img.item(30, height, 2)


    # warning: we can only change pixels in gray or single-channel image

    # modify green value: (row,col,channel)
    img.itemset((30, height, 1), 255)
    # read green value
    green = img.item(30, height, 1)

    ################################################################################



    rows, cols, channels = img.shape

    # prepare an empty image space
    imgSkin = np.zeros(img.shape, np.uint8)
    # copy original image
    imgSkin = img.copy()

    for r in range(rows):
        for c in range(cols):

            # get pixel value
            B = img.item(r, c, 0)
            G = img.item(r, c, 1)
            R = img.item(r, c, 2)

            # non-skin area if skin equals 0, skin area otherwise
            skin = 0

            if (abs(R - G) > 15) and (R > G) and (R > B):
                if (R > 95) and (G > 40) and (B > 20) and (max(R, G, B) - min(R, G, B) > 15):
                    skin = 1
                    # print 'Condition 1 satisfied!'
                elif (R > 220) and (G > 210) and (B > 170):
                    skin = 1
                    # print 'Condition 2 satisfied!'

            if 0 == skin:
                imgSkin.itemset((r, c, 0), 0)
                imgSkin.itemset((r, c, 1), 0)
                imgSkin.itemset((r, c, 2), 0)
                # print 'Skin detected!'

    # convert color space of images because of the display difference between cv2 and matplotlib
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgSkin = cv2.cvtColor(imgSkin, cv2.COLOR_BGR2RGB)
    # cv2.imwrite("./image/test1.jpg", imgSkin)
    # plt.imshow(imgSkin)
    return imgSkin

'''
# display original image and skin image
plt.subplot(1, 2, 1), plt.imshow(img), plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 2, 2), plt.imshow(imgSkin), plt.title('Skin Image'), plt.xticks([]), plt.yticks([])
plt.show()
################################################################################



k = cv2.waitKey(0)

# wait for ESC key to exit
if 27 == k:
    cv2.destroyAllWindows()
'''

