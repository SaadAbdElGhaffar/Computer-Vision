import cv2
import pytesseract
'''
here we are using pytesseract to make text recognition on an image and make number recognition.
we will make bounding boxes around the detected numbers.
'''

pytesseract.pytesseract.tesseract_cmd = r"pytesseract/Tesseract-OCR/tesseract.exe"

# 1. Load the image

img = cv2.imread("data/testt.jpg")
img1 = cv2.imread("data/testt.jpg")
img2 = cv2.imread("data/testt.jpg")
Himg , Wimg , _ = img.shape

#**********************************************************************************************************

# this code to detect each character in the image and draw bounding boxes around them
boxes = pytesseract. image_to_boxes(img, lang="eng")
print(boxes)# example output: "A 100 200 300 400 0.0\nB 150 250 350 450 0.0\nC 200 300 400 500 0.0\n
for b in boxes.splitlines(): # splitlines() will split the string into a list of lines
    print(b)
    b = b.split(" ")# split between the spaces and set in the list b
    print(b)
    x1,y1,x2,y2 =int(b[1]),int(b[2]),int(b[3]),int(b[4])
    # x1,y1 is the bottom-left corner of the bounding box
    # x2,y2 is the top-right corner of the bounding box
    # we need to convert these coordinates to the top-left corner and bottom-right corner
    # Tesseract uses a coordinate system where (0,0) is at the **bottom-left** of the image.
    # OpenCV uses a coordinate system where (0,0) is at the **top-left** of the image.
    # So we need to flip the y-coordinates by subtracting from the image height (Himg)
    # Himg-y1 will give us the bottom-left y-coordinate
    # Himg-y2 will give us the top-right y-coordinate
    cv2.rectangle(img, (x1,Himg-y1),(x2,Himg-y2),(0,255,0),3)
    cv2.putText(img, b[0], (x1, Himg - y1 + 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)

#**********************************************************************************************************

#this code to detect each word in the image and draw bounding boxes around them
# image_to_data will return coordinates of each word in the image
boxes = pytesseract. image_to_data(img1, lang="eng")
print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x != 0:# skip the first line which is the header
        b = b.split()
        print(b)
        if len(b) == 12:# check if the line has 12 elements to ensure it is a valid word detection
            # b[0] is the word, b[6] is the x-coordinate, b[7] is the y-coordinate, b[8] is the width, b[9] is the height
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img1, (x,y),(x+w,y+h),(0,255,0),3)
            cv2.putText(img1, b[11], (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)

#**********************************************************************************************************

# what if we want to detect only number ?
config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'# oem 3 is the default OCR Engine Mode, psm 6 is the Page Segmentation Mode for a single uniform block of text.
# -c variable_name=value: like set the tessedit_char_whitelist=value it will make the ocr recognize only number.
# tessedit_char_whitelist=0123456789 will tell Tesseract to recognize only numbers
# you can also use tessedit_char_blacklist to exclude certain characters
boxes = pytesseract.image_to_data(img2, lang="eng", config = config)
print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x != 0:# skip the first line which is the header
        b = b.split()
        print(b)
        if len(b) == 12:# check if the line has 12 elements to ensure it is a valid word detection
            # b[0] is the word, b[6] is the x-coordinate, b[7] is the y-coordinate, b[8] is the width, b[9] is the height
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img2, (x,y),(x+w,y+h),(0,255,0),3)
            cv2.putText(img2, b[11], (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 3)

#if we want to detect only numbers and boxes around each single number we will use image_to_boxes and configure it to recognize only numbers
#boxes = pytesseract.image_to_boxes(img2, lang="eng", config = config)


cv2.imshow("character", img)
cv2.imshow("word", img1)
cv2.imshow("number", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()    