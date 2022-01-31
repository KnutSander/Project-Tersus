from CC.models import Employee, SickLeave
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
import random
from faker import Faker

# this function simulates user generation, in real life application, the password would be taken from the company database
def generateUsers(request):
    for employee in Employee.objects.all():
        fname = employee.first_name
        lname = employee.last_name
        uname = fname[0] + lname
        user = User.objects.filter(username=uname)
        if not user.exists():
            User.objects.create_user(username=uname,
                                     first_name=fname,
                                     last_name=lname,
                                     email=employee.email,
                                     password=lname + "123")
    return HttpResponse("Success")

def generateEmails(request):
    for employee in Employee.objects.all():
        if not employee.email:
            employee.email = employee.first_name + "." + employee.last_name + "@example.com"
            employee.save()
    return HttpResponse("Success")

def generateSickDays(request):
    fake = Faker()
    for employee in Employee.objects.all():
        if not employee.sick_days_left:
            employee.sick_days_left = 10
            employee.save()
        for i in range(random.randrange(2, 6)):
            sickLeave = SickLeave(employee=employee, duration=random.randrange(1, 3), covid_related=bool(random.getrandbits(1)), day_started=fake.date_between(start_date='-2y', end_date='today'))
            sickLeave.save()


    return HttpResponse("Success")