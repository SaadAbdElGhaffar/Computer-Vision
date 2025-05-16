import cv2

import numpy as np

'''
1- convert image to gray scale by equation y = 0.299R + 0.587G +0.114B

2- remove the noise from the image by using gaussian filter which
discuss before

3- use sobel X and Sobel y to get the edges in two directions and
combine them by using ( Edge_Gradient(G)=Gx^2+Gy^2)

4- apply Non-maximum Suppression to make the edges thin

5- Hysteresis Thresholding to connect the strong edges and ignore other weak edges.'''

img = cv2.imread("data/lena.jpg", 0)


# the argument of canny is the image, the first threshold and the second threshold
''' 
the first threshold is used to find the strong edges and the second threshold is used to find the weak edges
the strong edges are the edges that have a gradient value greater than the first threshold
the weak edges are the edges that have a gradient value greater than the second threshold and less than the first threshold
the weak edges are connected to the strong edges and are considered as edges
the weak edges that are not connected to the strong edges are considered as non-edges'''
canny = cv2.Canny(img, 100, 200)


cv2.imshow("Original", img)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()