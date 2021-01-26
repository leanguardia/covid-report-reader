from readers.report_reader import ReportReader

import cv2
import pandas as pd
from unittest import TestCase

class TestReportReader(TestCase):
    def setUp(self):
        self.report_img = cv2.imread('fixtures/210125-Rep-COVID-316-2030-01-scaled.jpg')
        self.reader = ReportReader()

    def test_returns_a_dataframe(self):
        report = self.reader.read(self.report_img)
        self.assertIsInstance(report, pd.DataFrame) 
