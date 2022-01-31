from django.test import TestCase
from django.http import HttpRequest
from CC.views import resetDB


class test_resetDB(TestCase):

    def test_resetDB(self):
        self.assertIsNotNone(resetDB(HttpRequest))