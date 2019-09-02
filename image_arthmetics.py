import cv2
import numpy as np
img=cv2.imread("lena.jpg")

m=np.ones(img.shape,dtype="uint8")*150

#m2=np.zeros(img.shape,dtype="uint8")+150  both are same
add=cv2.add(img,m)
sub=cv2.subtract(m,img)
sub2=cv2.subtract(img,m)

cv2.imshow("original",img)
cv2.imshow("bright",add)
cv2.imshow("dark",sub)
cv2.imshow("dark2",sub2)


cv2.waitKey(0)
cv2.destroyAllWindows()