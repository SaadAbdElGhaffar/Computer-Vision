"""
ORB (Oriented FAST and Rotated BRIEF) is a feature detector and descriptor that is designed to be fast and efficient. It combines the FAST keypoint detector and the BRIEF descriptor, while also adding orientation information to the keypoints.
ORB is particularly useful for real-time applications and is invariant to rotation and scale, making it suitable for various computer vision tasks such as object recognition, image stitching, and 3D reconstruction.
ORB make detection and description of keypoints fast and efficient, making it suitable for real-time applications. It is invariant to rotation and scale, which means it can handle images taken from different viewpoints or scales without losing performance.
in this code we will use ORB to match keypoints between two images.
"""
import cv2

img1 = cv2.imread('data/template1.png',0)
img2 = cv2.imread('data/template2.png',0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
img=cv2.drawKeypoints(img2,kp2,None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('Keypoints', img)
# Match descriptors using BFMatcher / we will use Brute Force Matcher to match the descriptors of two images

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# Draw matches
img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)# flags=2 means Only matched keypoints are drawn.
cv2.imshow('Matches', img_matches)


cv2.waitKey(0)
cv2.destroyAllWindows()