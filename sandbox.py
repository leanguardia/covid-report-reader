from readers.parsers import OcrDataParser
from img.processing import process#, grayscale, threshold 

import cv2
import pytesseract as ocr

def show_img(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('test/fixtures/210125-Rep-COVID-316-2030-01-scaled.jpg')
print("Shape:", img.shape)
processed = process(img)

# departments = img[250:, :1518]
# cases_today = img[250:420, :1518]
# summary = img[250:, 1518:]
# header = img[:250, :2000]

# img = cases_today.copy()
# img = get_grayscale(img)
# img = thresholding(img)
# show_img(img)

string = ocr.image_to_data(processed)
# conf = r'--oem 3 --psm 6'
# string = ocr.image_to_data(processed, config=conf)
print(string)

rows = OcrDataParser().parse(string)
print("ROWS: {}".format(len(rows)))

# for index, row in enumerate(rows):
#   print(str(index) + " " + str(len(row.elements)))

# h, w, c = img.shape

for row in rows[1:-1]:
    # print(row.text())
    top_left = (row.left(), row.top())
    # print(top_left)
    bottom_right  = (row.left() + row.width(), row.top() + row.height())
    # print(bottom_right)
    processed = cv2.rectangle(processed, top_left, bottom_right, (0, 0, 0), 2)
show_img(processed)

