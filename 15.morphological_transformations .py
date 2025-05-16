import cv2

import numpy as np

from matplotlib import pyplot as plt

'''Definition: Morphological transformations are image processing operations based on the shape or structure of objects in a binary image.

Used For: Noise removal, image enhancement, object segmentation, and feature extraction.

Basic Operations:

Erosion: Removes pixels on object boundaries; shrinks objects boundaries. 

Dilation: Adds pixels to object boundaries; expands objects boundaries.

Opening: Erosion followed by dilation; removes small objects/noise.

Closing: Dilation followed by erosion; fills small holes/gaps.

Structuring Element: A kernel used to probe and process the image.

Applications:
Noise removal, edge detection, object segmentation, and preprocessing.'''

# must be the image in grayscale or binary for morphological transformations to work properly
img = cv2.imread('data/smarties.png', cv2.IMREAD_GRAYSCALE)

_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)



kernal = np.ones((5,5), np.uint8)

# all the morphological transformations take the mask as input 
# and the kernal as the second argument not take the orignal image. 

#iterations is the number of times the kernal is applied to the image.
dilation = cv2.dilate(mask, kernal, iterations=2)

erosion = cv2.erode(mask, kernal, iterations=1)

opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)



titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']

images = [img, mask, dilation, erosion, opening, closing, mg, th]



for i in range(8):

    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')      

    plt.title(titles[i])      

    plt.xticks([]),plt.yticks([])#ticks      



plt.show()#show