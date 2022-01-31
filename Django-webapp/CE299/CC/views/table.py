from django.shortcuts import render
from CC.models import Employee
from CC.models import SanitizerStation
from CC.models import RfidConnection


def table(request):
    employees_obj = Employee.objects.select_related('department','risk_group') # joining the 2 tables
    sanitizer_obj = SanitizerStation.objects.all()
    
    sanitizer_cols=[]
    for e in SanitizerStation._meta.fields: # getting column names
        sanitizer_cols.append(e.name.replace("_"," "))
    
    rfid_obj = RfidConnection.objects.select_related('uid')

    context = {"allemployees":employees_obj, "allstations":sanitizer_obj,"sanitizerCols":sanitizer_cols,"allRfids":rfid_obj}

    return render(request, 'table.html',context)
