from django.test import TestCase
from django.http import HttpRequest
from CC.views import generatePDFReport


class test_generatePDFReport(TestCase):
    fixtures = ['data.json']

    def test_generatePDFReport(self):
        self.assertIsNotNone(generatePDFReport(HttpRequest))
