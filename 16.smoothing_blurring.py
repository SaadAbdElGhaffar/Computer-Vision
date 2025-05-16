import numpy as np
import cv2

''' blurring are used to enhancement the image and  remove the noise from the images
and it use diverse linear filter it's apply above the image it's linear because linear filter 
easy to achive and relatively fast'''
# there are two types form linear filter:
#1.high pass filter: it use to make detect the edges 
#2.low pass filter: it use to remove noise from the image and make enhance the image


img = cv2.imread('data/balloons_noisy.png')

blur = cv2.blur(img, (5, 5))# averaging filter each bigger the kernel size the more blur the image and reduce the noise
gblur = cv2.GaussianBlur(img, (5, 5), 0)
median = cv2.medianBlur(img, 5)#5 mean the size of filter ane it use for salt and paper images
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)#foucs on the edges and make the image smooth and it use for the images which have the noise and edges

cv2.imshow('Original', img)
cv2.imshow('Averaging', blur)
cv2.imshow('Gaussian Blur', gblur)
cv2.imshow('Median Blur', median)
cv2.imshow('Bilateral Filter', bilateralFilter)

cv2.waitKey(0)
cv2.destroyAllWindows()#close window