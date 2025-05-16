import numpy as np
import cv2
#this example is to show the color of the pixel where you click on the image on new window
#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        mycolorimage= np.zeros((512,512,3),dtype= np.uint8)
        mycolorimage[:]=[ blue ,green, red]

        cv2.imshow('color', mycolorimage)

#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('data/apple.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows() #close window
