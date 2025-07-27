"""
in this example, we will calculate the distance between a camera and an object in a 3D space(real distance).
we will use the camera intrinsic parameters and the size of the object in the image to calculate the distance(calibration single camera).
the distance between two eyes is 6.5 cm is constant in every face(average pupillary distance).
focal length = (w * d) / W
where: w is the width of the object in the image with pixels,
       d is the distance between the camera and the object in cm,
         W is the real width of the object in cm.
we want to find the distance between the camera and the face, so we will use the distance between two eyes as the object because we know it as 6.5 cm.
"""
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)# maxFaces=1 means we will detect only one face

while True:
    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=True)# draw = false means we will not draw the face mesh

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        # Drawing
        cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        w, _ = detector.findDistance(pointLeft, pointRight)
        # print(w)
        W = 6.3
 
        # Finding the Focal Length
        # d = 50 # distance between the camera and the object in cm  we assume it is 50 cm and we can measure it with a ruler in real life to get the real distance exactly
        # f = (w*d) / W
        # print(f)
 
        # Finding distance
        f = 840 # we cal the focal length in the previous step and we assume it is 840 pixels 
        d = (W * f) / w
        print(d)
 
        cvzone.putTextRect(img, f'Depth: {int(d)}cm',
                           (face[10][0] - 100, face[10][1] - 50),
                           scale=2)
 
    cv2.imshow("Image", img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()