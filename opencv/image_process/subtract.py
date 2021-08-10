import cv2 as cv
import numpy as np

# img1=cv2.imread('subtract1.jpg')
img1=cv.imread('../image/subtract1.jpg',0)#灰度图
# img2=cv2.imread('subtract2.jpg')
img2=cv.imread('../image/subtract2.jpg',0)

cv.imshow('subtract1',img1)
cv.imshow('subtract2',img2)

st=img2-img1
# st=img1-img2#相反
cv.imshow('after subtract',st)

#效果好一点
# ret,threshold=cv2.threshold(st,0, 127, cv2.THRESH_BINARY)
ret,threshold=cv.threshold(st, 50,255, cv.THRESH_BINARY)
cv.imshow('after threshold', threshold)


cv.waitKey(0)
cv.destroyAllWindows()