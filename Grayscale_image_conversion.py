import cv2 as cv
import os

img= cv.imread("pic.jpeg")
cv.imshow("NBC Colour",img)
grayFrame= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("NBC Grayscale",grayFrame)

cv.waitKey(0)

cv.destroyAllWindows()
