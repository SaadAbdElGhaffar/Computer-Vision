'''Reinhard color transfer means Reinhard color transfer
 is a technique that adjusts the colors of a target image by 
 transferring the color characteristics (such as mean and standard deviation) 
 from a source image to achieve a consistent visual appearance.'''

import numpy as np
import cv2


def get_mean_and_std(x):
	x_mean, x_std = cv2.meanStdDev(x)
	x_mean = np.hstack(np.around(x_mean,2)) # 9.879
	x_std = np.hstack(np.around(x_std,2))
	return x_mean, x_std

template_img = cv2.imread('data/source_images.jpg')
template_img = cv2.cvtColor(template_img,cv2.COLOR_BGR2LAB)
template_mean, template_std = get_mean_and_std(template_img)



input_img = cv2.imread('data/target_images.jpg')
input_img = cv2.cvtColor(input_img,cv2.COLOR_BGR2LAB)


img_mean, img_std = get_mean_and_std(input_img)


height, width, channel = input_img.shape
for i in range(0,height):
    for j in range(0,width):
        for k in range(0,channel):
            x = input_img[i,j,k]
        # print("x",x)
            x = ((x-img_mean[k])*(template_std[k]/img_std[k]))+template_mean[k]
            x = round(x)
            # boundary check
            x = 0 if x<0 else x
            x = 255 if x>255 else x
            input_img[i,j,k] = x
        
input_img= cv2.cvtColor(input_img,cv2.COLOR_LAB2BGR)
cv2.imwrite("data/modified_images.jpg", input_img)