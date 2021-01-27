from readers.report_reader import ReportReader

import cv2
from unittest import TestCase

class TestReportReader(TestCase):
    def setUp(self):
        self.report_img = cv2.imread("test/fixtures/210125-Rep-COVID-316-2030-01-scaled.jpg")
        self.reader = ReportReader(self.report_img)

    def test_returns_a_dictionary(self):
        report = self.reader.read()
        self.assertIsInstance(report, dict)

    def test_returns_a_dataframe(self):
        report = self.reader.read()
        self.assertEqual(report["new_cases"], "1.781")
