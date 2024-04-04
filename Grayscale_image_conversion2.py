import os
import cv2

img= cv2.imread("99.jpg")
grayFrame= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("99 Grayscale", grayFrame)

cv2.waitKey(0)
cv2.destroyAllWindows()
