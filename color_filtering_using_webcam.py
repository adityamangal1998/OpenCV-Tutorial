#we use hsv as it provide range of color

import cv2
import numpy as np

device = cv2.VideoCapture(0)
while True:
    ret,frame=device.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #for red color
    lower_range = np.array([0,70,50])
    upper_range = np.array([10,255,255])

    mask = cv2.inRange(hsv,lower_range,upper_range)

    cv2.imshow("orginal",frame)
    cv2.imshow("colour filtering",mask)

    if cv2.waitKey(1)==13:
        break

device.release()
cv2.destroyAllWindows()
