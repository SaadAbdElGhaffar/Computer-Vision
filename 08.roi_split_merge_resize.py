import cv2
import os
#ROI means Region of Interest that is the selected rectangle area from the image

img = cv2.imread("data/messi.jpeg")
img2 = cv2.imread("data/apple.jpg")
print(img.shape)
print(img.size)
print(img2.size)

print(img.dtype)
b,g,r = cv2.split(img)

img = cv2.merge((b,g,r)) #merge the channels back to the original image

# ball = img[280:340, 330: 390] # y2:y1 , x2:x1
# img [273:333, 100:160] = ball
### to combine two images in one image must be two images the same size 

img = cv2.resize(img, (512,512))
img2= cv2.resize(img2, (512,512))

dst1 =cv2.add(img,img2)

### to add two images with ratio we use addWeighted function
dst2 = cv2.addWeighted(img,.8,img2, .2,100)#the last parameter is the gamma value is cotrol the brightness of the image

cv2.imshow("image", img)
cv2.imshow("image1", dst1)
cv2.imshow("image2", dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
