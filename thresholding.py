import cv2
img = cv2.imread("lena.jpg")

ret,threshold = cv2.threshold(img,50,255,cv2.THRESH_BINARY)

grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret2,threshold2=cv2.threshold(grayscaled,50,255,cv2.THRESH_BINARY)

gauss=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

ret3,otsu=cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("oriinal",img)
cv2.imshow("threshold",threshold)
cv2.imshow("threshold2",threshold2)
cv2.imshow("gauss",gauss)
cv2.imshow("otsu",otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()

