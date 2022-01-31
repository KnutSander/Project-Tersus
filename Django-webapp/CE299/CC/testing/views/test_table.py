from django.test import TestCase
from django.http import HttpRequest
from CC.views.table import *


class test_table(TestCase):
    fixtures = ['data.json']

    def test_table(self):
        self.assertIsNotNone(table(HttpRequest))
