from readers.parsers import OcrDataParser

import cv2
import pytesseract as ocr
from unittest import TestCase

class TestReportReader(TestCase):
    def setUp(self):
        with open('test/fixtures/ocr_data.txt', 'r') as data:
            self.raw_data = data.read()
        # print(repr(self.raw_data))
        self.parser = OcrDataParser()

    def test_returns_list(self):
        rows = self.parser.parse(self.raw_data)
        self.assertIsInstance(rows, list)

    def test_returns_text(self):
        rows = self.parser.parse(self.raw_data)
        self.assertEqual(len(rows), 111)

    def test_returns_text(self):
        rows = self.parser.parse(self.raw_data)
        self.assertEqual(rows[14].text(), "316")
