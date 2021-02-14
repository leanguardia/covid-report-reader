from readers.report_reader import ReportReader
from img.processing import process

import cv2
from unittest import TestCase

report_img = cv2.imread("test/fixtures/210125-Rep-COVID-316-2030-01-scaled.jpg")
processed = process(report_img)
reader = ReportReader(processed)
report = reader.read()

class TestReportReader(TestCase):
    def setUp(self):
        self.report = report 

    def test_returns_a_dictionary(self):
        self.assertIsInstance(self.report, dict)

    def test_read_number(self):
        self.assertEqual(self.report["number"], "N° 316")

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

    def test_read_beni(self):
        self.assertEqual(self.report["beni"], "9")

    def test_read_cochabamba(self):
        self.assertEqual(self.report["cochabamba"], "217")
    
    def test_read_potosi(self):
        self.assertEqual(self.report["chuquisaca"], "222")

    def test_read_la_paz(self):
        self.assertEqual(self.report["la_paz"], "224")

    def test_read_pando(self):
        self.assertEqual(self.report["pando"], "22")

    def test_read_santa_cruz(self):
        self.assertEqual(self.report["santa_cruz"], "870")

    def test_read_tarija(self):
        self.assertEqual(self.report["tarija"], "34")
