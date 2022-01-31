from django.test import TestCase
from django.http import HttpRequest
from CC.views.getSimulationData import *


class test_getSimulationData(TestCase):
    fixtures = ['data.json']

    def test_getSimulationData(self):
        request = HttpRequest
        request.method = ''
        self.assertEqual(getSimulationData(request).getvalue(),
                         HttpResponse('Must be GET').getvalue())

        request.method = 'GET'
        self.assertIsNotNone(getSimulationData(request))

    def test_getSanitizerVolume(self):
        self.assertEqual(getSanitizerVolume(HttpRequest, 0).getvalue(),
                         HttpResponse("Sanitizer not found").getvalue())
        self.assertIsNotNone(getSanitizerVolume(HttpRequest, 1570))

    def test_refillSanitizer(self):
        self.assertEqual(refillSanitizer(HttpRequest, 0).getvalue(),
                         HttpResponse("Sanitizer not found").getvalue())
        self.assertEqual(refillSanitizer(HttpRequest, 1570).getvalue(),
                         HttpResponse("Success").getvalue())

    def test_updateScore(self):
        self.assertIsNotNone(updateScore(HttpRequest, 383))
        self.assertIsNotNone(updateScore(HttpRequest, 321))
