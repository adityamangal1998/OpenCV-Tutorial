import cv2

img=cv2.imread("lena.jpg")

#transpose the image
rotated_image=cv2.transpose(img,dst=-5)
# rotated_image2=cv2.transpose(img,dst=-2)
# rotated_image3=cv2.transpose(img,dst=0)
# rotated_image4=cv2.transpose(img,dst=1)
# rotated_image5=cv2.transpose(img,dst=5)

cv2.imshow("original",img)
cv2.imshow("rotated",rotated_image)
# cv2.imshow("rotated1",rotated_image2)
# cv2.imshow("rotated2",rotated_image3)
# cv2.imshow("rotated3",rotated_image4)
# cv2.imshow("rotated4",rotated_image5)

cv2.waitKey(0)
cv2.destroyAllWindows()