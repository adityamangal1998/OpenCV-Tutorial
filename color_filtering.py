import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # hsv is Hue Sat Value
    lower_range = np.array([0, 175,175])         # BGR
    uppper_range = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_range, uppper_range)
    res = cv2.bitwise_and(frame, frame, mask=mask)           # mask is work as boolean function

    if cv2.waitKey(1) == 13:
        break
    # frame=cv2.flip(frame,1)
    cv2.imshow("original", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

cap.release()
cv2.destroyAllWindows()
