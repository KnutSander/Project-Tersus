from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User
from CC.views import analytics
import random


def getUserWithWash():
    request = HttpRequest()
    request.user = User.objects.get(is_superuser=False, first_name='Jimmy')
    return request


def getUserWithoutWash():
    request = HttpRequest()
    request.user = User.objects.get(is_superuser=False, first_name='Aaron')
    return request


def getAdminUser():
    request = HttpRequest()
    request.user = random.choice(User.objects.filter(is_superuser=True))
    return request


class test_analytics(TestCase):
    fixtures = ['data.json']

    def test_analytics(self):

        self.assertNotEqual(analytics(getUserWithWash()), analytics(getAdminUser()))
        self.assertNotEqual(analytics(getUserWithWash()), analytics(getUserWithoutWash()))
