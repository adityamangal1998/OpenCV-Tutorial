import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, img = cap.read()
    # cv2.imshow("live",frame)
    cv2.imshow("frame", img)
else:
    ret = False

img1=cv2.cvtColor(img,cv2.COLOR_BAYER_BG2BGR)
# cv2.imshow("frame2",img1)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
