import numpy as np
import cv2 as cv

size = (2560,1600)
black = np.zeros(size)
print(black.shape)
print(black[34][56])

cv.imwrite('black.jpg',black)

black[:] = 255
print(black[34][56])

cv.imwrite('white.jpg',black)

img = cv.imread("black.jpg")
print(img.shape)