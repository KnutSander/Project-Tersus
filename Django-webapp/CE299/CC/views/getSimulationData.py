from django.http import HttpResponse
from CC.models import RfidConnection
from CC.models import SanitizerStation
from CC.models import Achievement
from datetime import datetime, timedelta
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


@csrf_exempt
def getSimulationData(request):
    if request.method == 'GET':
        # result = serializers.serialize("json", RfidConnection.objects.all())
        result = json.dumps({"RFIDs": list(RfidConnection.objects.values_list('uid', flat=True)), "Sanitizers":
            list(SanitizerStation.objects.values_list('id', flat=True))})
        return HttpResponse(result)
    else:
        return HttpResponse('Must be GET')


def getSanitizerVolume(request, id):
    sanitizer = SanitizerStation.objects.filter(id=id)
    if not sanitizer.exists():
        return HttpResponse("Sanitizer not found")
    else:
        return HttpResponse(sanitizer[0].volume_remaining)


def refillSanitizer(request, id):
    sanitizer = SanitizerStation.objects.filter(id=id)
    if not sanitizer.exists():
        return HttpResponse("Sanitizer not found")
    else:
        sanitizer[0].volume_remaining = sanitizer[0].volume_capacity
        sanitizer[0].save()
        return HttpResponse("Success")


def updateScore(request, id):
    global score
    maximumPoints = 8  # maximum score for each given day
    coolDownTime = 60  # currently 60 minutes
    try:
        score = Achievement.objects.get(employee_id=id, updated_at__date=datetime.today(), name="Score")
        last_rfid = RfidConnection.objects.filter(UID=id)
        if score.updated_at + timedelta(minutes=coolDownTime) <= last_rfid[-1].time_dispensed and score.value < maximumPoints:
            score.value += 1
            score.save()
    except ObjectDoesNotExist:  # employee has not washed their hands today
        score = Achievement(employee_id=id, value=1)
        score.save()
    finally:
        return score.value
