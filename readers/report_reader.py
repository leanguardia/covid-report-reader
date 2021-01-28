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
        # string = ocr.image_to_data(self.departments_img())#, config=custom_config)
        string = ocr.image_to_data(self.img)
        print(string)
        rows = string.split('\n')
        elements = [row.split('\t') for row in rows]
        return {
            "new_cases": elements[36][-1],
            "number":    elements[14][-1],
        }
    
    def departments_img(self):
        return self.img[250:, :1518]

if __name__ == "__main__":
    img = cv2.imread("test/fixtures/210125-Rep-COVID-316-2030-01-scaled.jpg")
    reader = ReportReader(img)
    report = reader.read()
    print(report)
