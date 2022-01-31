from django.test import TestCase
from django.http import HttpRequest
from CC.views.showRiskGroups import *


class test_showRiskGroups(TestCase):
    fixtures = ['data.json']

    def test_showRiskGroups(self):
        self.assertIsNotNone(showRiskGroups(HttpRequest))
