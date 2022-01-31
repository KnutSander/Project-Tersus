from django.test import TestCase
from django.http import HttpRequest
from CC.views.generateEmployeeUsers import *


class test_generateEmployeeUsers(TestCase):
    fixtures = ['data_noUsers.json']

    def test_generateEmployeeUsers(self):
        self.assertIsNotNone(generateUsers(HttpRequest))
        self.assertIsNotNone(generateEmails(HttpRequest))
        self.assertIsNotNone(generateSickDays(HttpRequest))
