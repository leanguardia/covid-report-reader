import cv2
import pytesseract as ocr

from readers.parsers import OcrDataParser
from img.processing import show_img, process, rectangle_to_relative

class ReportReader:
    def __init__(self, report_img):
        self.img = report_img
        # rectangle_to_relative(self.img, (332, 1200), (487, 1260))
        self.h, self.w = self.img.shape
        # custom_config = r'--oem 3 --psm 6'
        # ocr_data = ocr.image_to_data(self.departments_img())#, config=custom_config)
        ocr_data = ocr.image_to_data(self.img)
        # print(ocr_data)
        # print(repr(ocr_data))
        self.rows = OcrDataParser().parse(ocr_data)
        # portion = self.img[40:150, 1475:1800]

    def read(self):
        return {
            "number":      self._read_relative((0.5761, 0.028), (0.6905, 0.0975)),
            "date_time":   self._read_relative((0.0180, 0.0900), (0.62, 0.1680)),
            "new_cases":   self._read_relative((0.092, 0.2000), (0.2080, 0.270)),
            
            "recovered":   self._read_relative((0.638, 0.270), (0.765, 0.352)),
            "suspicious":  self._read_relative((0.638, 0.595), (0.765, 0.668)),
            "accumulated": self._read_relative((0.628, 0.852), (0.777, 0.929)),
            "active":      self._read_relative((0.818, 0.312), (0.955, 0.388)),
            "deaths":      self._read_relative((0.818, 0.552), (0.945, 0.618)),
            "new_deaths":  self._read_relative((0.808, 0.642), (0.950, 0.70)),
            "discarted":   self._read_relative((0.808, 0.852), (0.955, 0.929)),
            
            "beni":        self._read_relative((0.379, 0.33), (0.4710, 0.399)), # "9"
            "chuquisaca":  self._read_relative((0.4719, 0.8126), (0.5273, 0.8543)),
            "cochabamba":  self._read_relative((0.0898, 0.5989), (0.1465, 0.6384)),
            "la_paz":      self._read_relative((0.084, 0.4754), (0.1445, 0.5135)), #"224"
            "oruro":       self._read_relative((0.1008, 0.7176), (0.1605, 0.7606)),
            "pando":       self._read_relative((0.0887, 0.3511), (0.1523, 0.3935)),
            "potosi":      self._read_relative((0.1297, 0.8328), (0.1902, 0.8744)),
            "santa_cruz":  self._read_relative((0.4613, 0.4961), (0.5253, 0.5655)),
            "tarija":      self._read_relative((0.3867, 0.9299), (0.4441, 0.9715)), #"34"
        }

    def _read_relative(self, topleft, bottomright):
        portion = self.img[
            int(topleft[1]*self.h):int(bottomright[1]*self.h),
            int(topleft[0]*self.w):int(bottomright[0]*self.w)
        ]
        # show_img(portion)
        string = ocr.image_to_string(portion)
        # print(string)
        # print(repr(string))
        return string[:-2]

if __name__ == "__main__":
    img = cv2.imread("test/fixtures/210125-Rep-COVID-316-2030-01-scaled.jpg")
    processed = process(img)

    reader = ReportReader(processed)
    report = reader.read()
    print(report)
