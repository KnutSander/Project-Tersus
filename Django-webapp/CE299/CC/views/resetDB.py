import random

from django.http import HttpResponse
from CC.models import *
from django.contrib.auth.models import *


# use this to fully reset the database, deleting all stored data
def resetDB(request):
    # delete all values in the following tables
    User.objects.all().delete()
    Achievement.objects.all().delete()
    SickLeave.objects.all().delete()
    RfidConnection.objects.all().delete()
    SanitizerStation.objects.all().delete()
    Employee.objects.all().delete()
    RiskGroup.objects.all().delete()
    Department.objects.all().delete()
    Goal.objects.all().delete()
    
    sanitizers = [["First Dept Sanitizer", "Bathroom"], ["First Dept Sanitizer", "Entrance"],
                        ["Second Dept Sanitizer", "Entrance"], ["Second Dept Sanitizer", "Exit"],
                        ["Third Dept Sanitizer", "Entrance"], ["Third Dept Sanitizer", "Bathroom"],
                        ["Fourth Dept Sanitizer", "The Balcony"], ["Fourth Dept Sanitizer", "The Attic"]]

    employees = []

    UID = (1132, 1135, 1250, 1257, 1305, 1444, 1733, 1740, 2117, 2405, 2504,  2553,  2578,  2893,  3024,  3099,  3378,  3576,  3861,  3867,  4011,  4100,  4184,  4221,  4266,  4600,  4872,  4902,  4907,  4918,  4971,  5002,  5059,  5190,  5204,  5205,  5440,  5482,  5536,  5785,  5865,  6020,  6057,  6143,  6209,  6289,  6351,  6553,  6711,  6996,  7048,  7089,  7115,  7131,  7219,  7280,  7335,  7342,  7351,  7418,  7611,  7694,  7767,  7781,  8216,  8335,  8352,  8547,  8570,  8832,  8906,  9002,  9272,  9312,  9404,  9541,  9720,  9791,  9903,  9981)
    firstNames = ("Aaron", "Adam", "Jamie", "Jade", "Jimmy", "Robert", "Luke", "Arif", "Micheal", "Bob", "James", "Al", "Alex", "Charlie", "Knut", "Andrei", "Hazim", "Sam", "Megan", "Julie", "Jiminy", "Joseph", "Leo", "Christopher", "Samuel", "Vernon", "Nigel", "Harry", "Undyne", "Wendy", "Patrick", "Barry", "Frank", "Dave", "Jack", "Zelda", "Patricia", "Freddie", "Jemery", "Mike", "Pheobe", "Rachel", "Monica", "Ross", "Joey", "Chandler", "Clark", "Harley", "Selina", "Miguel", "Tulio", "Danny", "Kevin", "Mario", "Peach", "Luigi", "Doug", "Cloud", "Leon", "Squal", "Zidane", "Sora", "Garnet", "Roy", "Rose", "Jack", "Tifa", "Aerith", "Aeris", "Shaoib", "Vishnu", "Erdrick", "Kratos", "Aloy", "Rey", "Finn", "Clive", "Joshua", "Jill", "Chris")
    lastNames = ("Jones", "Smith", "Bloggs", "Dias", "Markle", "Doe", "Smith", "Plisskin", "Strife", "Leonheart", "Tribal", "Gainsbourough", "Lockheart", "Kopparberd", "McDonald", "Tennant", "Jones", "Cloggs", "Fring", "Smith", "Dursley", "Potter", "Trotter", "Pennyworth", "Preda", "Sceats", "Smeets", "Bown", "Brown", "Urban", "Dross", "Boss", "Loss", "Rowe", "Applegate", "Binar", "Hexa", "See", "Seeplusplus", "Seesharp", "Pie", "Thon", "Ruby", "Jahva", "Stark", "Rogers", "Wayne", "Kent", "Wilson", "Quinn", "Kyle", "Johnson", "Luceum", "Cole", "Smith", "Kite", "Kuczmejno", "Hyman", "Jacobs", "Daniels", "Sorenson", "Potter", "Bull", "Reed", "Reid", "Parrick", "Green", "Maddams", "Adams", "Duthie", "Ten", "Nien", "Ahyt", "Sehven", "Sicks", "Thighve", "Free", "Too", "Wun", "Null")

    listOfRiskGroups = ["Low", "Medium", "High"]

    i = 0
    for name in firstNames:
        employees.append([str(UID[i]), name, lastNames[i]])
        i += 1

    goals = [["Average hand sanitizations", "Achieve more than 5 Hand sanitizations on average per employee per day", 5],
             ["Max number of high risk employees", "Have less then 10% of employees in high risk category", 0.1]
             ]
    for goal in goals:
        newGoal = Goal(name=goal[0], description=goal[1], has_been_achieved=False, value=goal[2])
        newGoal.save()

# Save departments
    targetGoal = Goal.objects.get(name="Average hand sanitizations")
    departments = [["Radiotherapy", "Floor 1"], ["ICU", "Ground floor"], ["Cardiology", "Floor 2"], ["A&E", "Ground floor"], ["Pharmacy", "Floor 1"]]
    for department in departments:
        newDepartment = Department(name=department[0], location=department[1], goal=targetGoal)
        newDepartment.save()

    riskGroups = ['High', 'Medium', 'Low']
    for riskGroup in riskGroups:
        newRiskGroup = RiskGroup(name=riskGroup)
        newRiskGroup.save()

# Save sanitizer stations
# ID's and created/update at are automatically generated
    for sanitizer in sanitizers:
        newSanStation = SanitizerStation(name=sanitizer[0], location=sanitizer[1], volume_capacity=100, volume_remaining=100)
        newSanStation.save()

# Save risk groups
    for riskGroup in listOfRiskGroups:
        newRiskGroup = RiskGroup()
        newRiskGroup.name = riskGroup
        newRiskGroup.save()

# Save employees
    for employee in employees:
        newEmployee = Employee(uid=employee[0], first_name=employee[1], last_name=employee[2])
        newEmployee.department = random.choice(Department.objects.all())
        newEmployee.save()


    return HttpResponse('Success: All databases data has been reset to default values')
