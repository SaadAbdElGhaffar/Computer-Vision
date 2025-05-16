import cv2
import dlib

'''
dlib is good for face detection and landmarks detection than harrcascade classifier
# In this code, we are using dlib to detect faces and landmarks in a video stream from the webcam. 
# The detected faces are highlighted with rectangles, and the landmarks are marked with circles. 
'''
detector = dlib.get_frontal_face_detector()# this will detect the face in the image
predictor = dlib.shape_predictor("dlib/shape_predictor_68_face_landmarks.dat")#and this will we get the landmarks ,this is model pretrained model for face landmarks detection

cap = cv2.VideoCapture(0) #zero for the first web cam
while True:
    _ , frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)# detector will return four values x1, y1, x2, y2 (top-left, bottom-right)for the face detected in the image
    for face in faces:
        print(face)
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
        landmarks = predictor(gray, face)
        for n in range(0,68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            #print(x,y)
            cv2.circle(frame,(x,y),3,(0,255,0),-1)

    cv2.imshow("my face",frame)
    #cv2.imshow("my gray face",gray)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release ()
cv2.destroyAllWindows()
