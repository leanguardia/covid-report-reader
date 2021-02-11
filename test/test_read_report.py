from readers.report_reader import ReportReader

import cv2
from unittest import TestCase

class TestReportReader(TestCase):
    def setUp(self):
        report_img = cv2.imread("test/fixtures/210125-Rep-COVID-316-2030-01-scaled.jpg")
        self.reader = ReportReader(report_img)
        self.report = self.reader.read()

    def test_returns_a_dictionary(self):
        self.assertIsInstance(self.report, dict)

    def test_read_number(self):
        self.assertEqual(self.report["number"], "316")

    def test_read_date(self):
        self.assertEqual(self.report["date"], "Lunes 25 de enero de 2021")

    def test_read_time(self):
        self.assertEqual(self.report["time"], "(20:30)")

    def test_read_new_cases(self):
        self.assertEqual(self.report["new_cases"], "1.781")

    def test_read_new_deaths(self):
        self.assertEqual(self.report["new_deaths"], "+66")

    def test_read_recovered(self):
        self.assertEqual(self.report["recovered"], "151.469")

    def test_read_active(self):
        self.assertEqual(self.report["active"], "41.298")

    def test_read_deaths(self):
        self.assertEqual(self.report["deaths"], "[10.051")

    def test_read_suspicious(self):
        self.assertEqual(self.report["suspicious"], "4.263")

    def test_read_accumulated(self):
        self.assertEqual(self.report["accumulated"], "202.818")

    def test_read_discarted(self):
        self.assertEqual(self.report["discarted"], "315.414")
