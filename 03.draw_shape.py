import cv2
import numpy as np
from sympy import im

# img = cv2.imread("data/lena.jpg", 1)
img = np.zeros([512, 512, 3], np.uint8)  # create image uint8 means 0-255

img = cv2.line(img, (0, 0), (255, 255), (147, 96, 44), 10)  # 44, 96, 147 #draw line
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)  # draw arrow

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)  # draw rectangle
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)  # draw circle to make it filled choose -1
font = cv2.FONT_HERSHEY_SIMPLEX  # type of font
img = cv2.putText(img, "OpenCv", (10, 500), font, 3, (0, 255, 255), 10, cv2.LINE_AA)  # write a text fontscale make zoom in text make it bigger
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)  # draw ellipse

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)  # make array to draw it by polylines
pts = pts.reshape((-1, 1, 2))  # reshape it
img = cv2.polylines(img, [pts], True, (0, 255, 255))  # draw polyline true means closed shape
img = cv2.fillPoly(img, [pts], (0, 255, 0))  # fill polyline like triangle
cv2.imshow("image", img)  # show your work by window

cv2.waitKey(0)  # wait key from keyboard
cv2.destroyAllWindows()  # close any opened window
