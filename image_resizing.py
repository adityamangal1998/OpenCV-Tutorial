import cv2

img = cv2.imread("lena.jpg")
im_scaled = cv2.resize(img, None, fx=0.75, fy=0.75)
im_scaled2 = cv2.resize(img, (640, 480), fx=0.75, fy=0.75,interpolation=cv2.INTER_AREA)  # dsize is used to desirable size # Skewed size
im_scaled_interplotation=cv2.resize(img, None, fx=2, fy=2,interpolation=cv2.INTER_CUBIC)

cv2.imshow("original", img)
cv2.imshow("scaled", im_scaled)
cv2.imshow("scaled2", im_scaled)
cv2.imshow("scaled_interplotation", im_scaled_interplotation)

cv2.waitKey(0)
cv2.destroyAllWindows()

print(img.shape)
print(im_scaled.shape)
print(im_scaled2.shape)
print(im_scaled_interplotation.shape)
