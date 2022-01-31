from django.test import TestCase
from django.http import HttpRequest
from CC.views.runSimulation import *


class test_runSimulation(TestCase):
    fixtures = ['data.json']

    def test_runSimulation(self):
        self.assertIsNotNone(runSimulation(HttpRequest))
        self.assertIsNotNone(updateSimulation(HttpRequest))
