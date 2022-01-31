from datetime import datetime, timedelta
from django.shortcuts import render
from django.utils import timezone
from CC.views import clusteredAnalysis
from CC.models import *


def index(request):
    rfidConnections = RfidConnection.objects.all()
    timesWashed = 0
    durationTotal = 0
    for connection in rfidConnections:
        timesWashed += 1
        durationTotal += connection.time_spent
    avgDuration = durationTotal / timesWashed
    avgDuration = round(avgDuration, 2)

    employees = Employee.objects.all()
    employeeCount = 0
    for _ in employees:
        employeeCount += 1

    sanitizers = SanitizerStation.objects.all()
    emptySanitisers = 0
    for sanitizer in sanitizers:
        if sanitizer.volume_remaining == 0:
            emptySanitisers += 1

    washHistory = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    hour = range(0, 13)
    for h in hour:
        start = timezone.now() - timedelta(hours=h)
        end = timezone.now() - timedelta(hours=(h+1))
        for connection in rfidConnections:
            if (end < connection.time_dispensed) & (connection.time_dispensed < start):
                washHistory[12-h] += 1  # puts the values into the list in reverse order, to work with the histogram

    dataArray = clusteredAnalysis.Clustering()

    # danger donut data
    dangerDonutData = [0, 0, 0]
    riskGroups = RiskGroup.objects.all()

    for userID, riskLevel in zip(dataArray[0], dataArray[1]):
        employee = Employee.objects.get(uid=userID)
        if riskLevel == 0:
            dangerDonutData[0] += 1
            employee.risk_group = riskGroups[0]
        elif riskLevel == 1:
            dangerDonutData[1] += 1
            employee.risk_group = riskGroups[1]
        else:
            dangerDonutData[2] += 1
            employee.risk_group = riskGroups[2]
        employee.save()

    # ["Radiotherapy", "ICU", "Cardiology", "A&E", "Pharmacy"]
    barChartData = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for i, department in enumerate(Department.objects.all()):
        for employee in Employee.objects.filter(department=department):
            employeeIndex = dataArray[0].index(employee.uid)
            riskGroup = dataArray[1][employeeIndex]
            barChartData[riskGroup][i] += 1

    data = {"TimesWashed": timesWashed, "AvgDuration": avgDuration, "Employee": employeeCount,
            "EmptySanitizers": emptySanitisers, "HistogramData": washHistory, "DangerDonutData": dangerDonutData,
            "BarChartDataHigh": barChartData[0], "BarChartDataMed": barChartData[1], "BarChartDataLow": barChartData[2]}
    return render(request, 'index.html', data)
