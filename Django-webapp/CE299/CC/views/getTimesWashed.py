from django.db.models import Count
from CC.models import Employee


def getTimesWashed():
    userOccurrences = Employee.objects.annotate(timesWashed=Count('rfidconnection'))
    timesWashed = {}
    for x in userOccurrences:
        timesWashed[x.uid] = x.timesWashed
    return timesWashed
