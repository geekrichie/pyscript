import cv2 as cv
import numpy as np
img22 = cv.imread('../image/subtract2.jpg')

# src_pts = np.array([[8, 136], [415, 52], [420, 152], [14, 244]], dtype=np.float32)

src_pts = np.array([[[97, 390], [210, 373], [183, 199], [69, 214]]], dtype=np.float32)

dst_pts = np.array([[0, 0], [50, 0], [50, 100], [0, 100]], dtype=np.float32)

# 得到透视变换的3×3矩阵
M = cv.getPerspectiveTransform(src_pts, dst_pts)
# dsize表示输出图片的大小	
warp = cv.warpPerspective(img22, M, dsize=(50, 100))

cv.imshow('src', img22)
cv.imshow('warp', warp)
cv.waitKey(0)