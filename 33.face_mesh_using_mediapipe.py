import cv2
import mediapipe as mp
'''
face mesh means it likes landmarks of face that  was used by dlib(68 landmarks) and in mediapipe more than dlib it have (468 landmarks)
# In this code, we are using mediapipe to detect faces and landmarks.
'''


image = cv2.imread("data/persson.jpeg")
image = cv2.resize(image, (800, 600))

# Face Mesh
mp_face_mesh = mp. solutions. face_mesh. FaceMesh()

#face mesh works on RGB image so we need to convert BGR to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Facial landmarks
result = mp_face_mesh.process(rgb_image)

height, width, _ = image. shape

#multi_face_landmarks means it can detect multiple faces in the image and it will return a list of landmarks for each face
for facial_landmarks in result.multi_face_landmarks:
    for i in range(0, 468):
        pt1 = facial_landmarks. landmark[i] # it's will return 3 values x, y, z as a prcentage of image size like 0.5% of width and 0.5% of height so we will multiply it with width and height to get the actual pixel value
        print(pt1)
        x = int(pt1.x * width)
        y = int(pt1.y * height)
        cv2.circle(image, (x, y), 2, (100, 100, 0), -1)

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()