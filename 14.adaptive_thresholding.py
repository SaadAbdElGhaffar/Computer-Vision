import cv2 as cv

import numpy as np

'''there are some image we can't use the global thresholding method to get a good result, 
for example, the image has different illumination in different areas. In this case, 
we can use adaptive thresholding method. 
The adaptive thresholding method calculates the threshold for a pixel based on a small region around it. 
So, it can be used to get a good result even if the image has different illumination in different areas.'''

# must be the image in grayscale for thresholding to work properly
img = cv.imread('data/sudoku.png',0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
#the argument of adaptiveThreshold() are: image, maxValue, adaptiveMethod, thresholdType, blockSize:must be odd number, 
# C:the constant subtracted from the mean or weighted mean and must be above one.
# adaptiveMethod: ADAPTIVE_THRESH_MEAN_C or ADAPTIVE_THRESH_GAUSSIAN_C
# the first one is the mean of the block size, the second one is the weighted mean of the block size.
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)


cv.imshow("Image", img)

cv.imshow("THRESH_BINARY", th1)

cv.imshow("ADAPTIVE_THRESH_MEAN_C", th2)

cv.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)


cv.waitKey(0)

cv.destroyAllWindows()#close window