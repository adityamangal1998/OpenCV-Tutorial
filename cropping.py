import cv2
import numpy as np

img = cv2.imread("lena.jpg")
im = img
crop = img[200:400, 200:400]
im[55, 55] = [255, 255, 255]
px = im[55, 55]
im[100:150, 100:150] = [255, 255, 255]
watch = im[37:111, 107:194]
im[0:74, 0:87] = watch
cv2.imshow("white", im)
cv2.imshow("original", img)
cv2.imshow("crop", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()
