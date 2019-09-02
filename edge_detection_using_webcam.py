import cv2

def sketch(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)

    canny_edge = cv2.Canny(img_gray_blur,10,80)

    ret ,mask = cv2.threshold(canny_edge,80,255,cv2.THRESH_BINARY)      #The function applies fixed-level thresholding to a multiple-channel array. The function is typically
                                                                        #used to get a bi-level (binary) image out of a grayscale image ( #compare could be also used for
    return mask                                                         #this purpose) or for removing a noise, that is, filtering out pixels with too small or too large
                                                                        #values. There are several types of thresholding supported by the function. They are determined by
                                                                        #type parameter.

cap =cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow("our live sketch",sketch(frame))

    if cv2.waitKey(1)==13:
        cv2.imwrite("image1.jpg", sketch(frame))
        break

cap.release()
cv2.destroyAllWindows()