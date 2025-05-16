import numpy as np

import cv2
''''
the contours are the boundaries of the objects in the image.

we must used any thresholding method to get edges before we can find contours.

'''


img = cv2.imread('data/opencv-logo.jpg')
img = cv2.resize(img, (512, 512))

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 20, 255, 0)

#the arguments are (image, mode, method)
# there are two modes: cv2.RETR_TREE and cv2.RETR_EXTERNAL
# there are two methods: cv2.CHAIN_APPROX_SIMPLE and cv2.CHAIN_APPROX_NONE
# cv2.RETR_TREE will retrieve all the contours and reconstruct a full hierarchy of nested contours.
# cv2.RETR_EXTERNAL will retrieve only the extreme outer contours.
# cv2.CHAIN_APPROX_SIMPLE will stores only endpoints of straight lines, remove all redundant points and compress the contour, thereby saving memory.
# cv2.CHAIN_APPROX_NONE will store all the points of the contour.
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print("Number of contours = " + str(len(contours)))

print(contours[0])



cv2.drawContours(img, contours, -1, (0, 255, 0), 3) #-1 means draw all contours


cv2.imshow('Image', img)

cv2.imshow('Image GRAY', imgray)

cv2.imshow('Image THRESH', thresh)

cv2.waitKey(0)

cv2.destroyAllWindows()#close window