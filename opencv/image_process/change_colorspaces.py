import numpy as np
import cv2 as cv
frame = cv.imread("../image/opencv-logo-white.png")
print(frame.shape)
hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
# define range of blue color in HSV
lower_blue = np.array([50,0,0])
upper_blue = np.array([70,255,255])
# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower_blue, upper_blue)
# Bitwise-AND mask and original image
res = cv.bitwise_and(frame,frame, mask= mask)
cv.imshow('frame',frame)
cv.imshow('mask',mask)
cv.imshow('res',res)
k = cv.waitKey(0) 
cv.destroyAllWindows()

# 查看颜色范围
# >>> green = np.uint8([[[0,255,0 ]]])
# >>> hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
# >>> print( hsv_green )
# [[[ 60 255 255]]]