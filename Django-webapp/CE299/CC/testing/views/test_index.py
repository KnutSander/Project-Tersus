from django.test import TestCase
from django.http import HttpRequest
from CC.views import index


class test_index(TestCase):
    fixtures = ['data.json']

    def test_index(self):
        self.assertIsNotNone(index(HttpRequest))
