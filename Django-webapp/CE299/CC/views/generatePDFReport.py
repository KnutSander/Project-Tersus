from fpdf import FPDF
from datetime import date
import matplotlib.pyplot as plt
from django.db.models.functions import ExtractWeekDay
from django.db.models import Count
from django.http import HttpResponse
from CC.models import Employee
from CC.models import RfidConnection
WIDTH = 210
HEIGHT = 297


def generatePDFReport(request):
    currentUser = Employee.objects.get(uid=9272)
    # washed = RfidConnection.objects.filter(uid=9272)
    annotatedConn = RfidConnection.objects.filter(uid=9272).annotate(weekday=ExtractWeekDay('time_dispensed'))
    groupedConn = annotatedConn.values('weekday').annotate(weekCount=Count('id')).values('weekday', 'weekCount')
    # [{'weekday': 1, 'count': 534}, {'weekday': 2, 'count': 574},.......}
    for record in groupedConn:
        print(record)
    # currentUser = Employee.objects.get(email=currentEmail)
    CreateReport(currentUser.first_name + currentUser.last_name, "Med", [5, 6, 7, 5, 8])
    return HttpResponse(currentUser.risk_group.name)


def WeeklyGraph(name, Count):
    thisname = name
    wash = Count
    days = ["Mon", "Tues", "Wed", "Thurs", "Fri"]
    plt.bar(days, wash)
    plt.title(f'{thisname} Weekly Washes')
    plt.savefig(f'CE299/CC/temp/{thisname}.png')


# INFORMATION NEEDED,
# USERNAME (name of employee)
# RISKGROUP (String of RiskGroup "High/Medium/Low")
# Weeklycount (Array of mon-Fri of washcounts)

def CreateReport(UserName, RiskGroup, WeeklyCount):
    name = UserName
    today = date.today()
    out = "error, unknown risk group"
    color = (0, 0, 0)
    if (RiskGroup == "High"):
        out = "Please Sanitize Your hands more to avoid sanctions"
    elif (RiskGroup == "Medium"):
        out = "Increase levels of hand sanitization."

    elif (RiskGroup == "Low"):
        out = "Continue with appropriate consistency of sanitization."
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    print(color)
    pdf.set_draw_color(255, 0, 0)
    pdf.rect(5, 10, 2, HEIGHT - 20, style='F')
    pdf.image("CE299/CC/static/img/logo.png", 0, 0, WIDTH - 5)  # Adds logo
    pdf.cell(0.5, 120, "{} Report {}".format(name, today))
    pdf.cell(0.5, 130, "Your Weekly Sanitization count is as follows:")
    WeeklyGraph(name, WeeklyCount)
    pdf.image("CE299/CC/temp/" + name + ".png", 0, 80, WIDTH - 5)

    pdf.cell(0.5, 140, "Your current risk group is " + RiskGroup)
    pdf.cell(0.5, 150, out)

    pdf.output(f"CE299/CC/temp/{name}Report.pdf", "F")
