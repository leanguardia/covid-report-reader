from readers.parsers import OcrDataParser

import cv2
import pytesseract as ocr
from unittest import TestCase

class TestReportReader(TestCase):
    def test_returns_list(self):
        img = cv2.imread('test/fixtures/210125-Rep-COVID-316-2030-01-scaled.jpg')
        ocr_data = ocr.image_to_data(img)
        parser = OcrDataParser()
        rows = parser.parse(ocr_data)
        self.assertIsInstance(rows, list)
