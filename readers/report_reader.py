import cv2
import pytesseract as ocr

from readers.parsers import OcrDataParser
from img.processing import show_img, process

class ReportReader:
    def __init__(self, report_img):
        self.img = report_img
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
            # "number":      self.rows[14].text(),
            "number":      self._read_relative((0.5761, 0.028), (0.6905, 0.0975)),
            "date":        self._read_date(),
            "time":        self.rows[28].text(),
            "new_cases":   self.rows[36].text(),
            "new_deaths":  self.rows[82].text(),
            "recovered":   self.rows[43].text(),
            "active":      self.rows[46].text(),
            "deaths":      self.rows[76].text(),
            "suspicious":  self.rows[79].text(),
            "accumulated": self.rows[98].text(),
            "discarted":   self.rows[88].text(),
            "beni":        self.rows[66].text(),
            "chuquisaca":  self.rows[95].text(),
            "cochabamba":  self.rows[78].text(),
            "la_paz":      self.rows[70].text(),
            "pando":       self.rows[64].text(),
            "santa_cruz":  self.rows[71].text(),
            "tarija":      self.rows[105].text(),
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

    def _read_date(self):
        date_words = self.rows[22].text()
        for i in range(23, 28):
            date_words += " " + self.rows[i].text()
        return date_words

if __name__ == "__main__":
    img = cv2.imread("test/fixtures/210125-Rep-COVID-316-2030-01-scaled.jpg")
    processed = process(img)

    reader = ReportReader(processed)
    report = reader.read()
    print(report)
