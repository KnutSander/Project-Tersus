################ RESEARCH ####################################################################################
##############################################################################################################
##rfid ref          https://pimylifeup.com/raspberry-pi-rfid-rc522/
##                  https://github.com/pimylifeup/MFRC522-python

##infared sensor    https://circuitdigest.com/microcontroller-projects/raspberry-pi-ir-sensor-tutorial
##to detect length of time person spends in front of dispenser?

##mysql ref         https://www.w3schools.com/python/python_mysql_getstarted.asp

##weight sensor ref https://www.seeedstudio.com/blog/2019/11/26/10-things-you-can-do-with-your-hx711-and-load-cell/
##                  https://tutorials-raspberrypi.com/digital-raspberry-pi-scale-weight-sensor-hx711/
##to detect remaining soap/alcohol

##screen ref        
##dispensing ref    https://www.raspberrypi.org/blog/how-to-use-a-servo-motor-with-raspberry-pi/
##                  https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/
##                  solenoids are motor pushers - squeeze to dispense?
##                  http://www.davidhunt.ie/water-droplet-photography-with-raspberry-pi/
##                  https://create.arduino.cc/projecthub/Oniichan_is_ded/yet-another-solenoid-valve-based-sanitizer-dispenser-ecec7a

###############################################################################################################

##Code

from time import sleep
from datetime import datetime
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()
import mysql.connector

class Sanitizer:
    def __init__(self, ID, location):
        self.ID = ID
        self.location = location
        self.soapLvl = 100
        
    def updateSoapLvl(self):
        soap = int(input("How much soap is left in %s? " % self.location))
        self.soapLvl = soap

    def is_empty(self):
        if self.soapLvl == 0:
            return True
        else:
            return False


mySanitizer = Sanitizer(1,"Kitchen")

myDB =  mysql.connector.connect(
    host = "localhost",
    user = "yourusername",
    password = "yourpassword"
)
myCursor = myDB.cursor()

try:
    while True:
        mySanitizer.updateSoapLvl
        if mySanitizer.is_empty:
            print("SOAP EMPTY. REFILL IMMEDIATELY")
        id, text = reader.read()
        ##once the rfid card is detected, activate dispense - solenoid to squeeze packet?
        sleep(5)
        ##log time
        ##use infared to detect how long they clean?
        ##when infared input no longer interrupted
        ##timeSpent = logged time - new time

        currentTime = datetime.now()

        sql = "INSERT INTO RFID_connections (UID, sanitizer_id, time dispensed) VALUES (%s,%i,%s)"
        val = ("id", mySanitizer.ID, now.strftime("%c"))

except KeyboardInterrupt:
    GPIO.cleanup()
    raise

