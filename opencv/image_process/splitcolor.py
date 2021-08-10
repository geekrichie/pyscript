import numpy as np
import cv2 as cv

img = cv.imread("../image/opencv-logo.png")
b=img[:,:,0]

#使所有像素的红色通道值都为 0,你不必先拆分再赋值。
# 你可以 直接使用 Numpy 索引,这会更快。
img[:,:,2]=0

#保存到文件，看下效果
cv.imwrite(filename='../image/split_color2.jpg',img=img)
