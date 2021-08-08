import cv2 as cv
import numpy as np

import os
import errno

path = "../image/messi5.jpg"

if not os.path.exists(path):
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
img = cv.imread(path, cv.IMREAD_UNCHANGED)
cv.imshow('src', img)
cv.waitKey(0)