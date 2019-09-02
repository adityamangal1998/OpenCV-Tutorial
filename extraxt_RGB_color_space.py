import cv2
import numpy as np

img = cv2.imread('lena.jpg')

cv2.imshow("hu",img)

# cv2.resizeWindow("hu",)
B,G,R=cv2.split(img)
# print(B)
# print(G)
# print(R)
print(img.shape)
zeros=np.zeros(img.shape[:2],dtype="uint8")
# print(zeros.__len__())
#format is B G R
cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.imshow("Red",cv2.merge([zeros,zeros,R]))

cv2.waitKey(0)