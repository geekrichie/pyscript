#用滑动条做调色板
import cv2 as cv
import numpy as np

def nothing(x):
    pass

drawing = False
ix , iy = -1, -1
mode  = 0
img = np.zeros((512, 512, 3), np.uint8)

def draw(event, x, y, flags, param):
    r = cv.getTrackbarPos('R', 'namedWindow')
    g = cv.getTrackbarPos('G', 'namedWindow')
    b = cv.getTrackbarPos('B', 'namedWindow')
    color = (b, g, r)
    global drawing, ix,iy ,mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == 0:
                cv.rectangle(img,(ix,iy),(x,y), color,-1)
            else:
                cv.circle(img,(x,y),2,color,-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

#没加这句，导致鼠标怎么移动都不变
cv.namedWindow('namedWindow')
cv.createTrackbar('R', 'namedWindow', 0, 255, nothing)
cv.createTrackbar('G', 'namedWindow', 0, 255, nothing)
cv.createTrackbar('B', 'namedWindow', 0, 255, nothing)
cv.setMouseCallback("namedWindow",draw)

while True:
    cv.imshow("namedWindow", img)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('g'):
        mode = not mode


cv.destroyAllWindows()