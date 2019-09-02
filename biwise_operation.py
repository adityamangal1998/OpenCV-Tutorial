import cv2
import numpy as np

square=np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),(255,150,15),-1)
cv2.imshow("rec",square)

elli=np.zeros((300,300),np.uint8)
cv2.ellipse(elli,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow("ellipse",elli)

an=cv2.bitwise_and(square,elli)
cv2.imshow("and",an)

oor=cv2.bitwise_or(square,elli)
cv2.imshow("or",oor)

cv2.waitKey(0)
cv2.destroyAllWindows()