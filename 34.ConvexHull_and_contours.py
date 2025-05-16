# Convex HuLL
import cv2
import matplotlib.pyplot as plt
'''
we use the convex hull to find the largest contour in the image 
see video: https://www.youtube.com/watch?v=nFJWsHG4CGI&list=PLyhJeMedQd9QrXtCspclJ9ace2urp05o0&index=53 if you don't understand the idea of convex hull
'''

image = cv2.imread('data/cars.png')
image = cv2.resize(image,(650,500))

# Convert it to greyscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image
ret, thresh = cv2.threshold(img, 50,255,0)

# Find the contours
contours, hierarchy = cv2. findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# For each contour, find the convex hull and draw it
# on the original image.
for i in range(len(contours)):
    hull = cv2.convexHull(contours[i]) # we send the contour to the convex hull function and it returns the convex hull of the contour
    cv2.drawContours(image, [hull], -1, (255,0,0),2)

# Display the final convex hull image
cv2.imshow('ConvexHull', image)
cv2.waitKey(0)