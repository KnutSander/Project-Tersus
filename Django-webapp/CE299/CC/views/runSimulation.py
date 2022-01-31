from django.http import HttpResponse
from django.shortcuts import render
from time import sleep
from datetime import datetime, timedelta
import random
from CC.models import *
from django.core.exceptions import ObjectDoesNotExist


# these variables are subject to change
maximumPoints = 8  # maximum score for each given day
coolDownTime = 60  # currently 60 minutes


# selects a random user and returns the employee object
def getRandomEmployee():
    return random.choice(Employee.objects.all())


# selects random sanitiser
def getRandomSanitizer():
    return random.choice(SanitizerStation.objects.all())


# creates a random time the sanitizer was used and a random time of how long
def getRandomWashTime():
    started = datetime.now()
    sleep(random.randint(2, 20))
    finished = datetime.now()
    timeSpent = (finished - started).seconds
    return timeSpent, started


# decreases the sanitizer amount
def decreaseSanitizerAmount(sanitizer):
    sanitizer.volume_remaning -= 2
    sanitizer.save()


# the three methods below are for the point based system
# creates a new score for the day if a score isn't found
def createNewScore(score, washTime, employeeID):
    score.employee_id = employeeID
    score.created_at = washTime
    score.updated_at = washTime
    score.value = 1
    score.save()


# updates the score if a score exists
def updateScore(score, washTime):
    score.updated_at = washTime
    score.value += 1
    score.save()


# TODO: Do something with the scores
# increases the point amount of an employee
def increasePoints(washTime, employeeID):
    score = Achievement()
    try:
        score = Achievement.objects.get(employee_id=employeeID, updated_at__date=datetime.today())
        if score.updated_at + timedelta(minutes=coolDownTime) <= washTime and score.value < maximumPoints:
            updateScore(score, washTime)
    except ObjectDoesNotExist:  # employee has not washed their hands today
        createNewScore(score, washTime, employeeID)
    finally:
        return score.value


# TODO: Create less random and more believable data
# Currently the number of washes every hour and day is about the same
# Should make code where the number of washes differs from hour to hour
# I.e. more washes at the start and end of work, as well as around lunch
# A hospital would have a higher use during the day than during the night
# Could also differ between employees, like it would in an actual workplace


def simulate_RFID_connection():
    random.seed()
    newRfidConnection = RfidConnection()

    # select random user
    newRfidConnection.uid = getRandomEmployee()

    # select random sanitizer
    # need to store the sanitizer so the liquid amount can be updated
    sanitizer = getRandomSanitizer()
    newRfidConnection.sanitizer = sanitizer

    # get a semi-random amount of time the employee is washing their hands
    # set time spent washing hands and time started
    newRfidConnection.time_spent, newRfidConnection.time_dispensed = getRandomWashTime()

    # based on research done by the NCBI, 2 ml of sanitizer is a sufficient amount
    # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3851816/
    newRfidConnection.volume_used = 2
    newRfidConnection.save()

    points = increasePoints(newRfidConnection.time_dispensed, newRfidConnection.uid.id)

    message = "Badge number " + newRfidConnection.uid.uid
    message += " washed hands in " + newRfidConnection.sanitizer.location
    message += " at " + newRfidConnection.time_dispensed.strftime("%H:%M:%S")
    message += " for " + str(newRfidConnection.time_spent) + " seconds. "
    message += "Total score today is: " + str(points)
    # display total score, and if they gained a point or not

    # decrease the amount of sanitiser in the station after use
    # decreaseSanitizerAmount(sanitizer)
    # message += " (Sanitizer capacity remaining " + str(sanitizer.volume_remaining) + "ml )"

    # sleep for a couple of minutes to reduce number of washes
    sleep(random.randint(180, 300))

    return message


def runSimulation(request):
    return render(request, 'simulation.html', {})


def updateSimulation(request):
    return HttpResponse(simulate_RFID_connection())
