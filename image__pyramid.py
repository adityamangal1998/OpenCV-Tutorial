import cv2

img = cv2.imread("lena.jpg")

smaller=cv2.pyrDown(img)   #half the size of image
larger=cv2.pyrUp(img)      #double the size of image

cv2.imshow("orginal",img)
cv2.imshow("smaller",smaller)
cv2.imshow("larger",larger)
print(img.shape)
print(smaller.shape)
print(larger.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()