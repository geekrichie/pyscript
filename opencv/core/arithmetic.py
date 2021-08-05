import cv2 as cv
img1 = cv.imread('../image/messi5.jpg')
img2 = cv.imread('../image/opencv-logo-white.png')

# img2 = cv.resize(img2,(img1.shape[1], img1.shape[0]))
# print(img1.shape,img2.shape)

# dst = cv.addWeighted(img1, 0.7, img2, 0.3 ,0)
# cv.imshow('dst',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()

rows,cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

img1_bg = cv.bitwise_and(roi, roi, mask = mask_inv)
img2_fg = cv.bitwise_and(img2, img2,mask= mask)

dst = cv.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()

