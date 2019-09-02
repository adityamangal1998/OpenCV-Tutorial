import numpy as np
import cv2
img=cv2.imread("lena.jpg",1)

height,width=img.shape[:2]
print(height)
print(width)


trans_height,trans_width=height/100,width/100

print(trans_height)
print(trans_width)

# t = |1 0 tx|    1 = width wise zoom  0 = tilt
#     |0 1 ty|    0 = tilt             1 = height wise zoom
#
# t is our translation matrix

t=np.float32([[1,0,trans_width],
              [0,1,trans_height]])
# print(t)
# we use wrapAffine (apply on linear image mean there is no tilt) transformation to shift the image
img_translation=cv2.warpAffine(img,t,(width,height))
print(img_translation.shape)
cv2.imshow("original image",img)
cv2.imshow("translated image",img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()