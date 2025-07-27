import cv2
import numpy as np

img = cv2.imread("data/croping.png")

rows, cols, _ = img.shape
print("Rows", rows)
print("Cols", cols)

# Cut image
cut_image = img[426: 526, 250: 1280] #rows then columns

# ROI (Region of interest)
cv2.rectangle(img, (405, 165), (895, 640), (0, 255, 0), 3)

roi = img[165: 640, 405: 895]

# cv2.imshow("Cut image", cut_image)
cv2.imshow("Roi", roi)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()