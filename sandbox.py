import cv2
import pytesseract as ocr

def show_img(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


img = cv2.imread('test/fixtures/210125-Rep-COVID-316-2030-01-scaled.jpg')

departments = img[250:, :1518]
cases_today = img[250:420, :1518]
# summary = img[250:, 1518:]
# header = img[:250, :2000]

img = cases_today.copy()
img = get_grayscale(img)
img = thresholding(img)
show_img(img)

conf = r'--oem 3 --psm 6'
string = ocr.image_to_data(img, config=conf)
# string = ocr.image_to_data(cases_today)#, config=conf)
print(string)
