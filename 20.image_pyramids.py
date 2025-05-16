import cv2

import numpy as np

"""
the image pyramid is a technique used in computer vision to represent an image at different scales.
the image pyramid is a multi-scale representation of an image that is used in computer vision and image processing.
the image pyramid is a set of images that are created by repeatedly downsampling the original image.
the image pyramid is used in many applications such as image blending, image stitching, and object detection.
there are two types of image pyramids: Gaussian pyramid and Laplacian pyramid.
Gaussian pyramid is down sampled version of the original image.
Laplacian pyramid is make edge detection by subtracting the Gaussian pyramid from the original image.
there aren't function in opencv to creat the Laplacian pyramid but we can create it by using the Gaussian pyramid.
the function in opencv is cv2.pyrDown() to downsample by 1/4 the image and cv2.pyrUp() to upsample the image by 1/4.
"""
img = cv2.imread("data/lena.jpg")

layer = img.copy()

gaussian_pyramid_list = [layer]



for i in range(6):

    layer = cv2.pyrDown(layer)     

    gaussian_pyramid_list.append(layer)     

    #cv2.imshow(str(i), layer)     



layer = gaussian_pyramid_list[5]

cv2.imshow('upper level Gaussian Pyramid', layer)

laplacian_pyramid_list = [layer]



for i in range(5, 0, -1):

    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])     
    #laplacian used for edge detection
    laplacian = cv2.subtract(gaussian_pyramid_list[i-1], gaussian_extended)     

    cv2.imshow(str(i), laplacian)     



cv2.imshow("Original image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()#close window