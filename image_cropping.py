import cv2
img=cv2.imread("lena.jpg")
height,width=img.shape[:2]

start_row,end_row=int(height*0.1),int(height*0.75)
start_col,end_col=int(width*0.1),int(width*0.75)


img_crop=img[start_row:end_row,start_col:end_col]

cv2.imshow("original",img)
cv2.imshow("cropped",img_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()