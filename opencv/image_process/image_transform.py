import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread("../image/messi5.jpg")
#
# height, width = img.shape[:2]
# res2 =cv.resize(img,(2*width, 2*height), interpolation=cv.INTER_CUBIC)


def resize(image, fxval, fyval):
    return cv.resize(image,None,fx=fxval, fy=fyval, interpolation=cv.INTER_CUBIC)

def cvtoplt(image) :
    image[:,:,(0,1,2)] = image[:,:,(2,1,0)]
    return image 

def translation(image, x, y):
    rows, cols = image.shape[:2]
    M = np.float32([[1,0,x],[0,1,y]])
    dst = cv.warpAffine(img, M, (cols, rows))
    return dst

def rotate(image, angle, scale):
    rows,cols = image.shape[:2]
    M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), angle, scale)
    dst = cv.warpAffine(img, M, (cols,rows))
    return dst

def affineTransform(image,pts1,pts2):
    rows,cols = image.shape[:2]
    M = cv.getAffineTransform(pts1, pts2)
    dst = cv.warpAffine(image, M, (cols,rows))
    return dst
def drawingcircle(image, x,y):
    cv.circle(image,(x,y),10,(0,255,0),-1)

def perspectiveTransform():
    img = cv.imread('../image/sudoku.png')
    rows,cols,ch = img.shape
    pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    for points in pts1:
        drawingcircle(img, points[0], points[1])
    M = cv.getPerspectiveTransform(pts1,pts2)
    dst = cv.warpPerspective(img,M,(300,300))
    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')
    plt.show()

plt.subplot("231"), plt.imshow(cvtoplt(img))

plt.subplot("232"), plt.imshow(resize(img,2,2))

plt.subplot("233"), plt.imshow(translation(img,50,10))

plt.subplot("234"), plt.imshow(rotate(img,90,1))
img2 = cv.imread("../image/drawing.png")
# import copy
# img2 = copy.deepcopy(img3)

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
cvtoplt(img2)
for points in pts1:
    drawingcircle(img2, points[0], points[1])

plt.subplot("235"), plt.imshow(img2)
plt.subplot("236"), plt.imshow(affineTransform(img2,pts1,pts2))
plt.show()
perspectiveTransform()