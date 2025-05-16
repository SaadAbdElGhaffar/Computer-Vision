import numpy as np

import cv2
'''
Detecting geometric shapes in an image using OpenCV
the idea of project is to detect the geometric shapes in an image and label them with their names.
the idea of project is find the contours of the shapes in the image each shape have number of contours different from other shapes.
'''
img = cv2.imread('data/shappes.jpg')

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)



cv2.imshow("img", img)

for contour in contours:
    # get appromation for all contour and it's length also and multiply it with small value to get the best approximation
    #True means that the shape is closed and False means that the shape is open
    #cv2.arcLength means to get the length of the contour
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)          

    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)          

    x = approx.ravel()[0]          

    y = approx.ravel()[1] - 5           

    if len(approx) == 3:          

        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))               

    elif len(approx) == 4 :         

        x1 ,y1, w, h = cv2.boundingRect(approx)                

        aspectRatio = float(w)/h                

        print(aspectRatio)                

        if aspectRatio >= 0.95 and aspectRatio <= 1.05:               

          cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))                

        else:                

          cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))                     

    elif len(approx) == 5:           

        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))                

    elif len(approx) == 10:           

        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))                

    else:            

        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))                 

cv2.imshow("shapes", img)

cv2.waitKey(0)

cv2.destroyAllWindows()