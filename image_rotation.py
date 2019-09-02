import cv2
import numpy as np

img = cv2.imread("lena.jpg")

height,width=img.shape[:2]
print(height)
print(width)
center=(width/2,height/2)
rotation_matrix = cv2.getRotationMatrix2D(center,angle=-15,scale=0.7)

rotation_image=cv2.warpAffine(img,rotation_matrix,(width,height))

cv2.imshow("ordinal image",img)
cv2.imshow("rotated image",rotation_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

