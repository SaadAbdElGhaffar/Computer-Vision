
import cv2

import numpy as np

#laplacian is a second derivative filter

#must be used in grayscale image
img = cv2.imread("data/messi.jpeg", 0)

#the laplacian filter is used to detect edges in an image

#the argument is the image, the depth of the image, and the kernel size
#the ddepth of the image is the data type of the image, here we change from 8 uint to 64 float, if i set to -1, it will be the same as the input image
#the best ksize is 3,must be odd number 
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)#in the is filter we not focus on the edges of  the center of the filter
# if we need to focus on the center of the filter we will use the next line
lap = np.uint8(np.absolute(lap))# to remove the noise in the background and to convert the image to uint8


cv2.imshow('img',img)
cv2.imshow('laplacian image',lap)

cv2.waitKey(0)
cv2.destroyAllWindows()