
from time import sleep
from datetime import datetime, timedelta
import random
import requests

# ip = '127.0.0.1:8000'
ip = '165.232.106.34:8000'
maximumPoints = 8  # maximum score for each given day
coolDownTime = 60  # currently 60 minutes

# def updatePoints(employeeUID, time_dispensed):
#     points_request = requests.get('http://' + ip + '/updateScore/' + employeeUID)
#     if (points_request.status_code == 200):
#        print("Score updated sucessfully")


def logRFIDConnection(sanID, empUID, time, duration, volume):

    dat = {'SanitizerID': sanID, 'EmployeeUID': empUID, 'Time': time, 'Duration': duration, 'Volume':  volume}
    x = requests.post('http://' + ip + '/add/', data = dat)
    if (x.status_code == 200):
        print("# Record created sucessfully [" + ip + "]")
        # updatePoints(empUID, time_dispensed)
    else:
        print("# Couldn't create record")

def refill(sanitizer):
    sanitizer_request = requests.get('http://' + ip + '/refillSan/' + str(sanitizer))
    if (sanitizer_request.status_code == 200):
        print("Sanitizer " + str(sanitizer) + " has been refilled successfully")
    else:
        print("Failed to refill sanitizer " + str(sanitizer))
def detectedRFID(duration):
    RFID = random.choice(RFIDs)
    sanitizer = random.choice(sanitizers)
    sanitizer_request = requests.get('http://' + ip + '/getSanVol/' + str(sanitizer))
    if (sanitizer_request.status_code == 200):
        sanitizerVol = int(sanitizer_request.text)
        volume_used = random.randint(1, 3)
        if (sanitizerVol - volume_used <= 0):
            print("Sanitizer " + str(sanitizer) + " is empty")
            refill(sanitizer)
            return
        print(
            f"Employee with RFID number {RFID} washed in sanitizer with ID {sanitizer} ({sanitizerVol} ml left) at {datetime.now().strftime('%H:%M:%S')}, for {duration} seconds!")

        logRFIDConnection(sanitizer, RFID, datetime.now(), duration, volume_used)
    else:
        print("# Couldn't read sanitizer volume left")



x = requests.get('http://' + ip + '/getSimData/')
if (x.status_code == 200):
    simData = x.json()
    RFIDs = simData["RFIDs"]
    sanitizers = simData["Sanitizers"]
    try:
        while True:
            duration = random.randint(1, 3)
            # time between connections
            # sleep(random.randint(2, 4))
            detectedRFID(duration)
            # washing time
            sleep(duration)
    except KeyboardInterrupt:
        print("Press Ctrl-C to terminate")
else:
    print("ERROR: Couldn't fetch simulation data")
