import cv2

img = cv2.imread("bena.jpg")
img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_AREA)
print(img.shape)
img1 = cv2.imread("lena.jpg")
print(img1.shape)
# image adding
add = img + img1
bit_or = cv2.bitwise_or(img, img1)
bit_and = cv2.bitwise_and(img, img1)
bit_xor = cv2.bitwise_xor(img, img1)
bit_not = cv2.bitwise_not(img)

# use masking
gray_img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray_img, 70, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("mask", mask)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow("mask_inv",mask_inv)

#use logical operation with mask
and_mask=cv2.bitwise_and(img1,img1,mask=mask)
and_mask_inv=cv2.bitwise_and(img1,img1,mask=mask_inv)
cv2.imshow("and_mask",and_mask)
cv2.imshow("and_mask_inv",and_mask_inv)





# cv2.imshow("add", add)
# cv2.imshow("bit or", bit_or)
# cv2.imshow("bit and", bit_and)
# cv2.imshow("bit xor", bit_xor)
# cv2.imshow("bit not", bit_not)
# cv2.imshow("original 1", img)
# cv2.imshow("original 2", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
