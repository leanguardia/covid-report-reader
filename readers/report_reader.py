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
            "number":      self._read_relative((57.61, 02.8), (69.05, 09.75)),
            "date_time":   self._read_relative((1.80, 09.00), (62, 16.80)),
            "new_cases":   self._read_relative((09.2, 20.00), (20.80, 27.0)),
            
            "recovered":   self._read_relative((63.8, 27.0), (76.5, 35.2)),
            "suspicious":  self._read_relative((63.8, 59.5), (76.5, 66.8)),
            "accumulated": self._read_relative((62.8, 85.2), (77.7, 92.9)),
            "active":      self._read_relative((81.8, 31.2), (95.5, 38.8)),
            "deaths":      self._read_relative((81.8, 55.2), (94.5, 61.8)),
            "new_deaths":  self._read_relative((80.8, 64.2), (95.0, 70)),
            "discarted":   self._read_relative((80.8, 85.2), (95.5, 92.9)),
            
            "beni":        self._read_relative((37.9, 33), (47.10, 39.9)), # "9"
            "chuquisaca":  self._read_relative((47.19, 81.26), (52.73, 85.43)),
            "cochabamba":  self._read_relative((08.98, 59.89), (14.65, 63.84)),
            "la_paz":      self._read_relative((08.4, 47.54), (14.45, 51.35)), #"224"
            "oruro":       self._read_relative((10.08, 71.76), (16.05, 76.06)),
            "pando":       self._read_relative((08.87, 35.11), (15.23, 39.35)),
            "potosi":      self._read_relative((12.97, 83.28), (19.02, 87.44)),
            "santa_cruz":  self._read_relative((46.13, 49.61), (52.53, 56.55)),
            "tarija":      self._read_relative((38.67, 92.99), (44.41, 97.15)), #"34"
        }

    def _read_relative(self, topleft, bottomright):
        """ Isolates a portion of the image and reads the text inside.
            Args:
            -   topleft: point (x,y) in % relative to full image
            -   bottomright: point (x,y) in % relative to full image
            Returns:
            -   OCR output of sub-image
        """
        x1, y1 = topleft
        x2, y2 = bottomright
        portion = self.img[
            int(y1 * self.h / 100):int(y2 * self.h / 100),
            int(x1 * self.w / 100):int(x2 * self.w / 100)
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
