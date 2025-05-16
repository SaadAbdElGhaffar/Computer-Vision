import cv2

face_cascade = cv2. CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
# Read the input image
#img = cv2.imread('test.png')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detectMultiScale(image, scaleFactor, minNeighbors)
    #1.1 (scaleFactor): How much the image size is reduced at each scale (10% smaller each time).
    #4 (minNeighbors): Minimum number of overlapping detections required to consider a region as a face.
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0,0), 3)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()