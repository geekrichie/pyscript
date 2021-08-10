import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

BLUE = [255,0,0 ]
img1 = cv.imread("../image/opencv-logo.png")
replicate = cv.copyMakeBorder(img1, top=10,bottom=10, left=10, right=10, borderType=cv.BORDER_REPLICATE)

reflect = cv.copyMakeBorder(img1, top=10,bottom=10, left=10, right=10, borderType=cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1, top=10,bottom=10, left=10, right=10, borderType=cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1, top=10,bottom=10, left=10, right=10, borderType=cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img1, top=10,bottom=10, left=10, right=10, borderType=cv.BORDER_CONSTANT, value=BLUE)

#2行3排第几副图
plt.subplot(231), plt.xticks([]) ,plt.yticks([]), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.xticks([]) ,plt.yticks([]), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.xticks([]) ,plt.yticks([]), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.xticks([]) ,plt.yticks([]), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.xticks([]) ,plt.yticks([]), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.xticks([]) ,plt.yticks([]), plt.imshow(constant, 'gray'), plt.title('CONSTANT')


plt.show()