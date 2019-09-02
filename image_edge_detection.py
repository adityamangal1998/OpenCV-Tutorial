# Edge Detection
import cv2
import numpy as np

img = cv2.imread("lena.jpg",0)
height, width = img.shape

# Extract slop edges
# Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None)
#     @param src input image.
# .   @param dst output image of the same size and the same number of channels as src .
# .   @param ddepth output image depth, see @ref filter_depths "combinations"; in the case of
# .   8-bit input images it will result in truncated derivatives.
# .   @param dx order of the derivative x.
# .   @param dy order of the derivative y.
# .   @param ksize size of the extended Sobel kernel; it must be 1, 3, 5, or 7.
# .   @param scale optional scale factor for the computed derivative values; by default, no scaling is
# .   applied (see #getDerivKernels for details).
# .   @param delta optional delta value that is added to the results prior to storing them in dst.
# .   @param borderType pixel extrapolation method, see #BorderTypes
# .   @sa  Scharr, Laplacian, sepFilter2D, filter2D, GaussianBlur, cartToPolar
sobel_x = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)
sobel_x_y = cv2.Sobel(img, cv2.CV_8U, 1, 1, ksize=5)  #too much information loss

cv2.imshow('Original Image', img)

cv2.imshow('Sobel X Image', sobel_x)

cv2.imshow('Sobel Y Image', sobel_y)
cv2.imshow('Sobel X Y Image', sobel_x_y)

sobel_Or = cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('Sobel or Image',sobel_Or)
# cv2.waitKey(0)
#
laplacian = cv2.Laplacian(img, cv2.CV_8U,ksize=5)
cv2.imshow('Laplacian Image',laplacian)
# cv2.waitKey(0)
#Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None): # real signature unknown; restored from __doc__
#     .   @param image 8-bit input image.
#     .   @param edges output edge map; single channels 8-bit image, which has the same size as image .
#     .   @param threshold1 first threshold for the hysteresis procedure.
#     .   @param threshold2 second threshold for the hysteresis procedure.
#     .   @param apertureSize aperture size for the Sobel operator.
#     .   @param L2gradient a flag, indicating whether a more accurate \f$L_2\f$ norm
#     .   \f$=\sqrt{(dI/dx)^2 + (dI/dy)^2}\f$ should be used to calculate the image gradient magnitude (
#     .   L2gradient=true ), or whether the default \f$L_1\f$ norm \f$=|dI/dx|+|dI/dy|\f$ is enough (
#     .   L2gradient=false ).
# #Canny Edge detection uses gradiant values as thresholds
#
canny = cv2.Canny(img, 0, 100)
cv2.imshow('Canny Edge', canny)
cv2.waitKey(0)

cv2.destroyAllWindows()
