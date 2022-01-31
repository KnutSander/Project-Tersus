from django.shortcuts import render
from django.http import HttpResponse
from CC.models import DBTable
import random

def createuser(request):
    newuser = DBTable()
    newuser.timesWashedToday = random.randint(1,10)
    newuser.timesWashedMonth = random.randint(1,50)
    newuser.save()
    return HttpResponse("It worked idiot")
