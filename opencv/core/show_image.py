import numpy as np
import cv2 as cv,sys

if len(sys.argv) < 2:
    print('show_image.py image_path')
    sys.exit(0)
image_path = sys.argv[1]

try:
    f = open(image_path)
except Exception as e:
    print(e)
    sys.exit(-1)

img = cv.imread(image_path, cv.IMREAD_UNCHANGED)
temp  =img.copy()

title = image_path.split('/')[-1] + f' {img.shape}'

gray = False
while True:
    cv.imshow(title, temp)
    k = cv.waitKey(10)
    if k == 27 or k == ord('q'):
        break
    if k  == ord('g'):
        if gray is False:
            temp = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            gray = True
        else:
            temp = img.copy()
            gray = False
cv.destroyAllWindows()