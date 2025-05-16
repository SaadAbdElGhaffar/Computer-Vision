import numpy as np 
import cv2 
cap =cv2.VideoCapture(0)

face_cascade =cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
eyes_cascade =cv2.CascadeClassifier("haarcascade/haarcascade_eye.xml")

while(cap.isOpened()):
    ret ,frame =cap.read()
    #must convert to gray scale for haar cascade
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #detectMultiScale(image, scaleFactor, minNeighbors)
    #1.3 (scaleFactor): How much the image size is reduced at each scale (30% smaller each time).
    #4 (minNeighbors): Minimum number of overlapping detections required to consider a region as a face.
    faces =face_cascade.detectMultiScale(gray ,1.3 , 4)
    for (x,y,h,w) in faces :
        cv2.rectangle(frame ,(x,y),(x+w ,y+h),(0,255,0),3) 
        cv2.putText(frame,"Face",(x,y-4),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)      
        roi_gray=gray[y:y+h ,x:x+w]       
        roi_color=frame[y:y+h ,x:x+w]       
        eyes =eyes_cascade.detectMultiScale(roi_gray)       
        for(ex,ey,eh,ew) in eyes :      
            cv2.rectangle(roi_color ,(ex,ey),(ex+ew ,ey+eh),(0,0,255),3)            
    
    cv2.imshow("frame" ,frame)
    
    key =cv2.waitKey(1)
    if(key == 27):
        break 
        
cap.release()
cv2.destroyAllWindows()
