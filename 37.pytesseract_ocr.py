import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"pytesseract/Tesseract-OCR/tesseract.exe"
'''
here we are using pytesseract to perform OCR on an image of a book page.
the image need to some preprocessing to improve the OCR results.
in the pytesseract ocr must do image preprocessing before performing OCR.
so the image have some different in its brightness and contrast.
we can use adaptive thresholding to improve the contrast of the image. 
'''
# 1. Load the image
img = cv2.imread("data/book_page.jpg")
img1 = cv2.imread("data/chinese_text.jpg")

# 2. Resize the image
# img = cv2.resize(img, None, fx=0.5, fy=0.5)# this will reduce the image size by half ,shirnking the x and y dimensions to 50%
# but here we are not resizing the image because it's small enough for OCR

# 3. Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# 4. Convert image to black and white (using adaptive threshold)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
adaptive_threshold1 = cv2.adaptiveThreshold(gray1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

config = "--psm 6" # page segmentation mode
text = pytesseract.image_to_string(adaptive_threshold)  # chi_sim/ lang= "chi_sim" for Chinese, "eng" for English
# you can also use config = "--psm 6" to specify the page segmentation mode

text1 = pytesseract.image_to_string(adaptive_threshold1, lang="chi_sim", config=config)  # Chinese text

print(text)
print(text1)

cv2.imshow("gray", gray)
cv2.imshow("adaptive th", adaptive_threshold)
cv2.imshow("gray1", gray1)
cv2.imshow("adaptive th1", adaptive_threshold1)
cv2.waitKey(0)
cv2.destroyAllWindows()
