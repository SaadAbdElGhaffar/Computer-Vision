"""
SIFT (Scale-Invariant Feature Transform) is a feature detection algorithm used in computer vision to detect and describe local features in images.
it's like the Harris corner detector but more robust to changes in scale, rotation, and illumination.
it's like the Fast corner detector but more accurate and robust to noise but slower than Fast corner detector.
all of these use to detect keypoints(features) in images, but SIFT is more advanced and can handle more variations in the image.
SIFT is used to detection and description of local features in images, which can be used for tasks like image matching, object recognition, and 3D reconstruction. 
"""
#import numpy as np
import cv2 as cv

img = cv.imread('data/SIFT.png')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
kp = sift.detect(gray)
img=cv.drawKeypoints(gray,kp,None)

cv.imshow("Keypoints", img)


img=cv.drawKeypoints(gray,kp,img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS will draw the keypoints
# flags make the size of the keypoints proportional to their scale and orientation
# this will make the keypoints more visible and easier to see
cv.imshow("Keypoints with flags", img)


sift = cv.SIFT_create()
kp, des = sift.detectAndCompute(gray,None) #sift.compute() computes the descriptors for the keypoints only
imgg=cv.drawKeypoints(gray,kp,img)
cv.imshow("Keypoints with descriptors", imgg)

cv.waitKey(0)
cv.destroyAllWindows()