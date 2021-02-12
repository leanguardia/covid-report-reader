from readers.parsers import OcrDataParser
from img.processing import grayscale, threshold

import pytesseract as ocr

class ReportReader:
    def __init__(self, report_img):
        self.img = report_img
        # custom_config = r'--oem 3 --psm 6'
        # ocr_data = ocr.image_to_data(self.departments_img())#, config=custom_config)
        ocr_data = ocr.image_to_data(self.img)
        # print(ocr_data)
        # print(repr(ocr_data))
        self.rows = OcrDataParser().parse(ocr_data)

    def read(self):
        return {
            "number":      self.rows[14].text(),
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

    def _read_date(self):
        date_words = self.rows[22].text()
        for i in range(23, 28):
            date_words += " " + self.rows[i].text()
        return date_words

if __name__ == "__main__":
    img = cv2.imread("test/fixtures/210125-Rep-COVID-316-2030-01-scaled.jpg")
    img = process(img)

    reader = ReportReader(img)
    report = reader.read()
    print(report)
