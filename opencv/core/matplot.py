import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
img = cv.imread("../image/messi5.jpg")
img[:,:,(0,1,2)] = img[:,:,(2,1,0)]

plt.imshow(img)
plt.xticks([]); plt.yticks([])
plt.show()
