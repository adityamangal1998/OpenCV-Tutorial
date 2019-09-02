import cv2
import numpy as np

img=cv2.imread("lena.jpg")
cv2.imshow("original show",img)


#creating kernel

kernal_3X3_1= np.ones((3,3),np.float32)/9
kernal_3X3_2 = np.ones((3,3),np.uint8)/9
kernal_6X6_1 = np.ones((6,6),np.int8)/36

#we use the cv2.filter2D to convolve the kernel with an image
#find the impact of depth

blurred1 = cv2.filter2D(img,ddepth=-1,kernel=kernal_3X3_1)
cv2.imshow("kernal_3X3_1",blurred1)

blurred2 = cv2.filter2D(img,ddepth=-1,kernel=kernal_3X3_2)
cv2.imshow("kernal_3X3_2",blurred2)

blurred3 = cv2.filter2D(img,ddepth=-1,kernel=kernal_6X6_1)
cv2.imshow("kernal_6X6_1",blurred3)


cv2.waitKey(0)
cv2.destroyAllWindows()