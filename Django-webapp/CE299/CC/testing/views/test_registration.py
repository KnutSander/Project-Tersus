from django.test import TestCase
from django.http import HttpRequest
from CC.views import registration


class test_registration(TestCase):

    def test_registration(self):
        self.assertIsNotNone(registration.reset(HttpRequest))
        self.assertIsNotNone(registration.create_acc(HttpRequest))
