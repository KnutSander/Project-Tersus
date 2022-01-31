from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Count
from CC.models import *
import datetime
import json


def analytics(request):
    global totalHandWashes
    context={}
    if request.user.is_superuser == True: # admin
        updateDepartmentAchievementStatus() 
        total_employees = Employee.objects.all().count()
        low_risk_employees = Employee.objects.all().filter(risk_group_id='4').count()
        medium_risk_employees = Employee.objects.all().filter(risk_group_id='5').count()
        high_risk_employees = Employee.objects.all().filter(risk_group_id='6').count()
        allDepartments = Department.objects.select_related('goal')
        for obj in allDepartments:
            print(obj.goal)
            print(obj.name,obj.goal.has_been_achieved,obj.goal.value)

        context={"totalEmployees":total_employees,
        "lowRisk":low_risk_employees,
        "percentLow":round((low_risk_employees/total_employees) *100,1),
        "percentMedium":round((medium_risk_employees/total_employees) *100,1),
        "percentHigh":round((high_risk_employees/total_employees) *100,1),
        "mediumRisk":medium_risk_employees,
        "highRisk":high_risk_employees,
        "allDepartments":allDepartments
        }
    elif request.user.is_superuser == False and request.user.is_authenticated == True: # employees logged in
        
        #print(request.user.first_name)
        logged_user = Employee.objects.filter(first_name=request.user.first_name, last_name=request.user.last_name,email=request.user.email)
        
        #print(logged_user)
        pastWeekWashes=[]
        one_week_ago = datetime.date.today() - datetime.timedelta(days=7)

        sick_days_left = 0
        for obj in logged_user:
            totalHandWashes = RfidConnection.objects.select_related('uid').filter(uid=obj.uid)
            sick_days_left = obj.sick_days_left
        #print(totalHandWashes)
        time=0
        for connection in totalHandWashes:
            if connection.time_dispensed.date() >= one_week_ago:
                pastWeekWashes.append(connection)
                time+=connection.time_spent
            

        employees_obj = Employee.objects.select_related('department','risk_group').filter(first_name=request.user.first_name, last_name=request.user.last_name,email=request.user.email)

        # get the id of the user to be able to extract points from achievement
        id = Employee.objects.get(first_name=request.user.first_name).id
        # attempt to get current user points
        try:
            employeePointsToday = Achievement.objects.get(employee_id=id, updated_at__date=datetime.date.today()).value
        except ObjectDoesNotExist:  # employee has not washed their hands today
            employeePointsToday = 0

        #print("*********")
        #print(employees_obj)

        # for e in employees_obj:
        #     print(e.department.name+" "+e.risk_group.name)

        if len(pastWeekWashes)!=0:
            time=round(time/len(pastWeekWashes),1)
            context={"employee":employees_obj,"pastWeekWashes":len(pastWeekWashes),"avg_duration":time,
            "points":employeePointsToday,"sickDays":sick_days_left}
        else:
            context={"employee":employees_obj,"pastWeekWashes":0,"avg_duration":time,
             "points":employeePointsToday,"sickDays":sick_days_left}

        context ={**departmentAnalytics(logged_user), **context}
        context = {**dailyUserWashes(logged_user),**context}
    return render(request, 'analytics.html',context)


def departmentAnalytics(logged_user):
    nr_of_handwashes_per_department=0
    context={}
    one_week_ago = datetime.date.today() - datetime.timedelta(days=7)
    user_washes=0
    
    for e in logged_user:
        employee_id = e.uid
        departmentId=e.department.id
        departmentName = e.department.name
        dep_goal_id = e.department.goal_id
        user_washes_set=RfidConnection.objects.select_related('uid').filter(uid=e.uid)
    
    for connection in user_washes_set:
            if connection.time_dispensed.date() >= one_week_ago:
                user_washes +=1

    all_dep_employees=Employee.objects.filter(department_id=departmentId)
    #print("Number of employees in "+departmentName+" is "+ str(all_dep_employees.count()))
    for empl in all_dep_employees:
        totalHandWashes = RfidConnection.objects.select_related('uid').filter(uid=empl.uid)
     
        
        for connection in totalHandWashes:
            if connection.time_dispensed.date() >= one_week_ago:
                nr_of_handwashes_per_department+=1

    #print(departmentName+" handwashes in the past week = "+str(nr_of_handwashes_per_department))
    
    if nr_of_handwashes_per_department!=0:
        percentage = (user_washes/nr_of_handwashes_per_department)*100
    else:
        percentage=0

    if percentage >=75:
        message="Among the best. Keep going!"
    elif percentage>=50:
        message = "Above average - Good job!"
    elif percentage>=25:
        message="Below average - Can do better!"
    else:
        message="Too low - Can wash your hands more often!"

    departmentGoal = Goal.objects.get(id = dep_goal_id).value
    context={"departmentHandwashes":nr_of_handwashes_per_department,"status":message, "departmentGoal":departmentGoal}
    return context


def dailyUserWashes(logged_user):
    context={}
    data=[]
    my_dict={}

    for e in logged_user:
       user_washes_set=RfidConnection.objects.select_related('uid').filter(uid=e.uid)
    
    q = user_washes_set.values('time_dispensed').annotate(total=Count('time_dispensed')).order_by('-time_dispensed')
    
    for obj in q:
        #print(obj.get('time_dispensed'),obj.get('total'))
        newArray=[]
        newArray.append(str(obj.get('time_dispensed').strftime("%m/%d/%Y"))+" GMT")
        newArray.append(obj.get('total'))
        if my_dict.get(str(obj.get('time_dispensed').strftime("%m/%d/%Y"))+" GMT")!=None:
            my_dict.update({str(obj.get('time_dispensed').strftime("%m/%d/%Y"))+" GMT":my_dict.get(str(obj.get('time_dispensed').strftime("%m/%d/%Y"))+" GMT")+1})
        else : 
            my_dict.update({str(obj.get('time_dispensed').strftime("%m/%d/%Y"))+" GMT":obj.get('total')})
        data.append(newArray)

   
    dictlist=[]
    for key, value in my_dict.items():
        temp = [key,value]
        dictlist.append(temp)
    json_object = json.dumps(dictlist,indent=4)
    json_object=json_object.replace("/","-")
    
    context={"WashesArray":json_object}
    return context


# this method iterates over all employees from all departments and 
# checks if the daily goal has been reached by all department employees and updates the database
# BooleanField is required on has_been_achieved column 
def updateDepartmentAchievementStatus():
    
    reachedDailyDepGoal = True
    allDepartments = Department.objects.all()

    for dep in allDepartments:
      
        employeeAchievementCount =0
        reachedDailyDepGoal = True
        allDepEmployees = Employee.objects.filter(department_id=dep.id)
        for empl in allDepEmployees:
            try: # empl.uid vs empl.id ??
                employeePointsToday = Achievement.objects.get(employee_id=empl.id, updated_at__date = datetime.date.today()).value
            except Exception:  # employee has not washed their hands today
                employeePointsToday = 0
            if dep.goal.value <= employeePointsToday:
                employeeAchievementCount+=1
            else:
                reachedDailyDepGoal = False
        if employeeAchievementCount == 0:
            reachedDailyDepGoal = False
        #print(dep.name," goal reached? ",reachedDailyDepGoal," how many reached goal? ",employeeAchievementCount)
        
        depGoal = Goal.objects.get(id = dep.goal_id)
        depGoal.has_been_achieved = reachedDailyDepGoal
        depGoal.save()
        #print(depGoal.name," ",depGoal.has_been_achieved)
