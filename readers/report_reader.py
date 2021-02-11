from readers.parsers import OcrDataParser
from img.processing import grayscale, threshold

import pytesseract as ocr

class ReportReader:
    def __init__(self, report_img):
        self.img = report_img

    def read(self):
        # custom_config = r'--oem 3 --psm 6'
        # string = ocr.image_to_data(self.departments_img())#, config=custom_config)
        string = ocr.image_to_data(self.img)
        print(string)
        # print(repr(string))

        rows = OcrDataParser().parse(string)
        date_words = rows[22].text()
        for i in range(23, 28):
            date_words += " " + rows[i].text()

        return {
            "number":      rows[14].text(),
            "date":        date_words,
            "time":        rows[28].text(),
            "new_cases":   rows[36].text(),
            "new_deaths":  rows[82].text(),
            "recovered":   rows[43].text(),
            "active":      rows[46].text(),
            "deaths":      rows[76].text(),
            "suspicious":  rows[79].text(),
            "accumulated": rows[98].text(),
            "discarted":   rows[88].text(),
            "beni":        rows[66].text(),
            "chuquisaca":  rows[95].text(),
            "cochabamba":  rows[78].text(),
            "la_paz":      rows[70].text(),
            "pando":       rows[64].text(),
            "santa_cruz":  rows[71].text(),
            "tarija":      rows[105].text(),
        }

if __name__ == "__main__":
    img = cv2.imread("test/fixtures/210125-Rep-COVID-316-2030-01-scaled.jpg")
    img = process(img)

    reader = ReportReader(img)
    report = reader.read()
    print(report)
