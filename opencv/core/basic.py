import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("../image/messi5.jpg",cv.IMREAD_UNCHANGED)

# 根据x,y坐标获取像素值
px = img[100,100]
print(px)
#BGR 0表示blue，2表示red，1 表示green
blue = img[100,100,0]
print(blue)

red = img.item(10,10,2)
print(red)

# img.itemset((10,10,2), 100)
print(img.item(10,10,2))

print(img.shape)

print(img.size)

print(img.dtype)

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

cv.imshow('image', img)#窗口会自动调整为图像大小
# 在窗口上按任意键退出
cv.waitKey(delay=0)#返回按键的 ASCII 码值

cv.destroyAllWindows()


img = cv.imread('messi5.jpg', 0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
# 彩色图像使用 OpenCV 加载时是 BGR 模式。但是 Matplotlib 是 RGB 模式。所以彩色图像如果已经被OpenCV 读取，  它将不会被 Matplotlib 正 确显示。