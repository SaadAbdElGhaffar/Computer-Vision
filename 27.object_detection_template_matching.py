import cv2
import numpy as np

img = cv2.imread("data/messi.jpeg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template =cv2.imread("data/messi_face.jpg", 0)

w, h = template.shape[ ::- 1]# to reverse the order of the shape of the image

res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED )
cv2.imshow("res", res) #there are lighter point in image that mean the template is found in the image it's the max value in the image

print(res)
threshold = 0.99
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[ ::- 1]): #zip(loc[1], loc[0])
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()