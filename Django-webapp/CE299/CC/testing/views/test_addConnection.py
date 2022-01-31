from django.test import TestCase
from django.http import HttpResponse, HttpRequest
from datetime import *
from CC.views.addConnection import addRFIDConnection


def createEmptyRequest():
    request = HttpRequest()
    request.method = ""
    return request


def createWrongMethodRequest():
    request = HttpRequest()
    request.method = "GET"
    return request


def createMissingFieldsRequest():
    request = HttpRequest()
    request.method = "POST"
    request.POST = {"EmployeeUID": "9981", "SanitizerID": 1538}
    return request


def createWrongEmployeeRequest():
    request = HttpRequest()
    request.method = "POST"
    request.POST = {"EmployeeUID": "0", "SanitizerID": 1538, "Time": str(datetime.now()), "Duration": 7, "Volume": 2}
    return request


def createWrongStationRequest():
    request = HttpRequest()
    request.method = "POST"
    request.POST = {"EmployeeUID": "7767", "SanitizerID": 10, "Time": str(datetime.now()), "Duration": 7, "Volume": 2}
    return request


def creatWorkingRequestNoScore():
    request = HttpRequest()
    request.method = "POST"
    request.POST = {"EmployeeUID": "9981", "SanitizerID": 1570, "Time": str(datetime.now()), "Duration": 7, "Volume": 2}
    return request


def createWorkingRequestWithScore():
    # Do employee with achievement
    request = HttpRequest()
    request.method = "POST"
    request.POST = {"EmployeeUID": "7767", "SanitizerID": 1570, "Time": str(datetime.now()), "Duration": 7, "Volume": 2}
    return request


class test_addConnection(TestCase):
    fixtures = ['data.json']

    def test_addRFIDConnection(self):
        # test that giving no method gives the correct response
        self.assertEqual(addRFIDConnection(createEmptyRequest()).getvalue(),
                         HttpResponse('Must be POST').getvalue())

        # test that giving the wrong method gives the correct response
        self.assertEqual(addRFIDConnection(createWrongMethodRequest()).getvalue(),
                         HttpResponse('Must be POST').getvalue())

        # test that giving missing fields gives the correct response
        self.assertEqual(addRFIDConnection(createMissingFieldsRequest()).getvalue(),
                         HttpResponse('Incorrect parameters').getvalue())

        # test that giving a wrong employeeUID gives the correct response
        self.assertEqual(addRFIDConnection(createWrongEmployeeRequest()).getvalue(),
                         HttpResponse("Employee doesn't exist").getvalue())

        # test that giving a wrong SanitizerID gives the correct response
        self.assertEqual(addRFIDConnection(createWrongStationRequest()).getvalue(),
                         HttpResponse("Sanitizer station doesn't exist").getvalue())

        # test that giving valid values gives the correct response, user without previous score
        self.assertEqual(addRFIDConnection(creatWorkingRequestNoScore()).getvalue(),
                         HttpResponse('Success').getvalue())

        # test that giving valid values gives the correct response, user with previous score
        self.assertEqual(addRFIDConnection(createWorkingRequestWithScore()).getvalue(),
                         HttpResponse('Success').getvalue())
