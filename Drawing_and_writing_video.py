import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret,img = cap.read()
    pts = np.array([[10, 186], [20, 20], [30, 250], [100, 70]], np.int32)
    cv2.line(img, (512, 512), (0, 0), (255, 0, 0), 5)
    cv2.rectangle(img, (200, 200), (300, 300), (255, 0, 0), 5)
    cv2.polylines(img, [pts], True, (0, 0, 255), 5)
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, "Lena Raani", (0, 45), font, 2, (0, 255, 0), 4, cv2.LINE_AA)
    cv2.imshow("original",img)
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
