import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 3000) #set your frame width if above the value of width of the camera will set the max value of the camera
cap.set(4, 3000) #set your frame height if above the value of height of the camera will set the max value of the camera

print(cap.get(3)) #get your frame width
print(cap.get(4)) #get your frame height

while(cap.isOpened()):#while camera is open
    ret, frame = cap.read()#read frames        
    if ret == True: #still there is a frame to process        
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to gray scale       
     cv2.imshow('frame', gray)                 
     if cv2.waitKey(1) & 0xFF == ord('q'):#wait key from keyboard                 
         break                     
    else: #if ret=false         
        break              

cap.release()#close camera
cv2.destroyAllWindows()#close window