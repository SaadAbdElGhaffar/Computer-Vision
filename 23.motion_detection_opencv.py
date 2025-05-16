import cv2

import numpy as np
from xgboost import cv

''''first step, movement is difference between two frames second, difference has noises because of
details and light on video so gaussian blurring is eliminating the noises, third, obtaining threshold
from clean difference fourth, dilating for eliminating district small weak threshold lines which
corrupt healthy threshold detection fifth, finding contours from clean threshold sixth, eliminating
small contours which can not be a human by filtering contour area seventh, drawing rectangles for
each detected contour on the frame, rectangle dimensions obtained from
cv2.boundingRect(contour) that is it'''

cap = cv2.VideoCapture('data/vtest.avi')

frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))



frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))



fourcc = cv2.VideoWriter_fourcc('X','V','I','D')



out = cv2.VideoWriter("data/output.avi", fourcc, 5.0, (1280,720))



ret, frame1 = cap.read()# 1st frame

ret, frame2 = cap.read() #2nd frame

print(frame1.shape)

while cap.isOpened():

    diff = cv2.absdiff(frame1, frame2)  # this is the difference between two frames to detect movement      

    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # to use cv2.threshold and contours, we need to convert the image to gray scale      

    blur = cv2.GaussianBlur(gray, (5,5), 0)    # because of the details and light on video, we need to eliminate the noises

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)        

    dilated = cv2.dilate(thresh, None, iterations=3)        

    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)        



    for contour in contours:        

        (x, y, w, h) =  cv2.boundingRect(contour)             



        if cv2.contourArea(contour) < 900:  # if the contour area is too small, it can not be a human, so we need to eliminate it, there are some other small somthing in the video movement

            continue                    

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)              

        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20),                                                     cv2.FONT_HERSHEY_SIMPLEX,

                    1, (0, 0, 255), 3)

    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)



    image = cv2.resize(frame1, (1280,720))

    out.write(image)

    cv2.imshow("feed", frame1)
    # cv2.imshow("thresh", thresh)
    # cv2.imshow("dilated", dilated)

    frame1 = frame2

    ret, frame2 = cap.read()#read



    if cv2.waitKey(40) == 27:

        break     



cv2.destroyAllWindows()#close window

cap.release()#close camera

out.release()#close when write