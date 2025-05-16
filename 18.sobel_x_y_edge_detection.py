import cv2

import numpy as np
# The Sobel operator is used to find the edges in an image. 
# It uses a pair of 3x3 convolution kernels, 
# one for detecting changes in the horizontal direction (sobelX) and one for detecting changes in the vertical direction (sobelY). 
# The result is a gradient image that highlights the edges in the original image.



#must be used in grayscale image
img = cv2.imread("data/messi.jpeg", 0)

#the arguments are the image, the depth of the image, the x-derivative order, and the y-derivative order.
#in sobelX the x-derivative order is 1 and  y-derivative order is 0
# in sobelY the x-derivative order is 0 and  y-derivative order is 1
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)



sobelX = np.uint8(np.absolute(sobelX))

sobelY = np.uint8(np.absolute(sobelY))



sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow('img',img)
cv2.imshow("sobelX", sobelX) 
cv2.imshow("sobelY", sobelY) 
cv2.imshow("sobelCombined", sobelCombined)

cv2.waitKey(0)
cv2.destroyAllWindows()
