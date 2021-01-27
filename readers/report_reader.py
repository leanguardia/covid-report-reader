import cv2
import pytesseract as ocr

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def threshold(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

class ReportReader:
    def __init__(self, report_img):
        self.img = threshold(grayscale(report_img))

    def read(self):
        # custom_config = r'--oem 3 --psm 6'
        string = ocr.image_to_data(self.departments_img())#, config=custom_config)
        rows = string.split('\n')
        elements = [row.split('\t') for row in rows]
        return {
            "new_cases": elements[5][-1]
        }
    
    def departments_img(self):
        return self.img[250:, :1518]
