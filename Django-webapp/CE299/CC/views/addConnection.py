from django.http import HttpResponse
from CC.models import *
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta, timezone

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def addRFIDConnection(request):
    if request.method == 'POST':
        data = request.POST
        if data.get('EmployeeUID') and data.get('SanitizerID') \
                and data.get('Time') and data.get('Duration') and data.get('Volume'):
            try:
                employee = Employee.objects.get(uid=data.get('EmployeeUID'))
            except ObjectDoesNotExist:
                return HttpResponse("Employee doesn't exist")

            try:
                sanitizer = SanitizerStation.objects.get(id=data.get('SanitizerID'))
            except ObjectDoesNotExist:
                return HttpResponse("Sanitizer station doesn't exist")

            dispensedDatetime = datetime.strptime(data.get('Time'), "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=timezone.utc)
            newRFID = RfidConnection(uid = employee, sanitizer = sanitizer, time_dispensed = dispensedDatetime, time_spent = data.get('Duration'), volume_used = data.get('Volume'))
            newRFID.save()

            sanitizer.volume_remaining -= int(data.get('Volume'))
            sanitizer.save()

            score = Achievement.objects.filter(employee=employee, updated_at__date=datetime.today())
            if score.exists():
                if score[0].updated_at + timedelta(minutes=10) <= newRFID.time_dispensed and score[0].value < 8:
                    score[0].value += 1
                    score[0].save()
            else:
                newScore = Achievement(employee = employee, value=1, name="Score")
                newScore.save()

            return HttpResponse('Success')
        else:
            return HttpResponse('Incorrect parameters')
    else:
        return HttpResponse('Must be POST')
