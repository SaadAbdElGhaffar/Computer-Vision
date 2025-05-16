import cv2

# read image as it
img = cv2.imread(
    "data/apple.jpg", -1
)  # 0 for gray scale , 1 for color , -1 for alpha channel

# show image
cv2.imshow("image", img)

# specify a wait key from keyboard
k = cv2.waitKey(0) & 0xFF  # 0 mean wait for key pressed 5000 mean wait for 5 sec

if k == 27:  # esc in keyboard
    cv2.destroyAllWindows()  # close the window

elif k == ord("s"):  # if order is s save the image
    cv2.imwrite("data/lena_copy.png", img)  # write image in your pc
    cv2.destroyAllWindows()  # close the window
