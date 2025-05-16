import cv2 as cv

import numpy as np

#this used for gray scale image and thresholding
#this is called global thresholding
# must be the image in grayscale for thresholding to work properly
img = cv.imread('data/gradient.png',0)

#arguments are (image, threshold value, max value, type of thresholding)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)# this is thresholding means that all value below 50 will be 0 and all value above 50 will be 255 

_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV) # this is inverse thresholding means that all value below 200 will be 255 and all value above 200 will be 0

_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) # this is truncating means that all value below 127 will be the same as the original image and all value above 127 will be 127

_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # this is to zero means that all value below 127 will be 0 and all value above 127 will be the same as the original image

_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)# this is inverse to zero means that all value below 127 will be the same as the original image and all value above 127 will be 0



cv.imshow("Image", img)

cv.imshow("th1", th1)

cv.imshow("th2", th2)

cv.imshow("th3", th3)

cv.imshow("th4", th4)

cv.imshow("th5", th5)



cv.waitKey(0)

cv.destroyAllWindows() #close window

