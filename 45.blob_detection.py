"""
blob(circle detection) detection using OpenCV
"""
import matplotlib.pyplot as plt
import cv2

# The input image.
image = cv2.imread("data/blobs.png", 0)

# Set up the SimpleBlobdetector with default parameters
params = cv2.SimpleBlobDetector_Params()

# Define thresholds
#Can define thresholdStep. See documentation.
params. minThreshold = 0
params. maxThreshold = 255

# Filter by Area.
params. filterByArea = True
params. minArea = 50
params . maxArea = 10000

# Filter by Color (black=0)
params. filterByColor = False #Set true for cast_iron
params. blobColor = 0

# Filter by Circularity
params. filterByCircularity = True
params. minCircularity = 0.5
params. maxCircularity = 1

# Filter by Convexity
params. filterByConvexity = True
params. minConvexity = 0.1
params . maxConvexity = 1

# Setup the detector with parameters
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect (image)

print ("Number of blobs detected are : ", len(keypoints))

# Draw blobs
img_with_blobs = cv2.drawKeypoints(image, keypoints, None, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.imshow(img_with_blobs)
cv2.imshow("Keypoints", img_with_blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the result
cv2.imwrite("output/blobs_detected.png", img_with_blobs)