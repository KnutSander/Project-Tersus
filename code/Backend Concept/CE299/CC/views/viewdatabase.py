#page file
from django.shortcuts import render
from django.http import JsonResponse
from CC.models import DBTable

def index(request):
    data = []
    db = DBTable.objects.all() #all objects in database
    for x in db: #x is the db object
        data.append({
            'id': x.id,
            'times_washed_today': x.timesWashedToday,
            'times_washed_month': x.timesWashedMonth
        })

    return JsonResponse(data, safe=False)
