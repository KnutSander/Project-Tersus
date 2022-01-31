
from time import sleep
from datetime import datetime
import random

class Sanitizer:
    def __init__(self, ID, name, location):
        self.ID = ID
        self.name = name
        self.location = location
        self.alcohol_content = 5
        self.is_empty = self.emptyCheck()
        
    ##update soap level -- would be done with hardware sensing
    def updateAlcLvl(self):
        currentLvl = int(input("How much soap is left in %s? " % self.location))
        self.alcohol_content = currentLvl
        self.is_empty = self.emptyCheck()
    
    ##for autonomous simulation
    def updateAlcLvl(self, updater):
        self.alcohol_content -= updater
        self.is_empty = self.emptyCheck()

    def emptyCheck(self):
        if self.alcohol_content <= 0:
            refillSanitiser()
            return True
        else:
            return False

##at run time, the sanitizer will currently randomly select one of the sanitizers to be
##on a multiple device hardware level, this would be hardcoded
random.seed()

listOfSanitizers = []

listOfSanitizers.append(Sanitizer(1,"First Dept","Bathroom"))
listOfSanitizers.append(Sanitizer(2,"First Dept","Entrance"))
listOfSanitizers.append(Sanitizer(3,"Second Dept","Entrance"))
listOfSanitizers.append(Sanitizer(4,"Second Dept","Exit"))
listOfSanitizers.append(Sanitizer(5,"Third Dept","Entrance"))
listOfSanitizers.append(Sanitizer(6,"Third Dept","Bathroom"))
listOfSanitizers.append(Sanitizer(7,"Fourth Dept","The Balcony"))
listOfSanitizers.append(Sanitizer(8,"Fourth Dept","The Attic"))

thisSanitizer=random.choice(listOfSanitizers)

##current possible RFID chips
RFID = [1132, 1135, 1250, 1257, 1305, 1444, 1733, 1740, 2117, 2405, 2504,  2553,  2578,  2893,  3024,  3099,  3378,  3576,  3861,  3867,  4011,  4100,  4184,  4221,  4266,  4600,  4872,  4902,  4907,  4918,  4971,  5002,  5059,  5190,  5204,  5205,  5440,  5482,  5536,  5785,  5865,  6020,  6057,  6143,  6209,  6289,  6351,  6553,  6711,  6996,  7048,  7089,  7115,  7131,  7219,  7280,  7335,  7342,  7351,  7418,  7611,  7694,  7767,  7781,  8216,  8335,  8352,  8547,  8570,  8832,  8906,  9002,  9272,  9312,  9404,  9541,  9720,  9791,  9903,  9981]

##function to simulate RFID input
def RFID_sensing():
    ##this is a random number generator that can be replaced with the hardware sensor, principle the same
    
    ##wait a random amount of time (anywhere between 1 minute to an 5~ minutes)
    sleep(random.randint(600,300))

    ##simulate actual dispensing
    thisSanitizer.updateAlcLvl((random.randint(1,6)))
    ##pick a random RFID chip from above -- small sample size but can be increased
    return random.choice(RFID)

##function to simulate the sensing of soap content left
def soap_sensing():
    ##H/W:could be done in hardware with wieghts, for now will just deduct randomly b/w 1 and 6 f rom each dispense
    print(f"{thisSanitizer.name}'s {thisSanitizer.location} soap level is {thisSanitizer.alcohol_content}%")

    ##Python < 3.6 compatible:
    ##print "%s soap level is %i%" % (thisSanitizer.location, thisSanitizer.alcohol_content)

    ##simple notifications -- these instead would be sent to server rather than console
    if thisSanitizer.is_empty:
        print("SOAP EMPTY. REFILL IMMEDIATELY")
        
        refillSanitiser()
        ##if no soap, put some more in! 
    elif thisSanitizer.alcohol_content < 30:
        print("Soap levels low. Refill soon.")

##a function to simulate washing of hands.
def time_at_dispenser():
    ## Uses RNG to randomly select a time between 1 and 25
    ## H/W: can be done by detecting time spent infront of IR sensor
    firsttime = datetime.now()
    sleep(random.randint(1,25))
    secondtime = datetime.now()

    return secondtime - firsttime

##Refill the 
def refillSanitiser():
    sleep(900)
    thisSanitizer.alcohol_content=100
    print(f"Sanitizer is now refilled. Alcohol Content: {thisSanitizer.alcohol_content}")

##this code will keep running until the soap dispenser runs out of soap
def main():
    while True:
        soap_sensing()
        
        badge = RFID_sensing()
        
        currentTime = datetime.now()

        timeSpentWashing=time_at_dispenser()
        
        print(f"Badge number {badge} washed in {thisSanitizer.location} (Sanitizer {thisSanitizer.ID}) at {currentTime:%c}, for {timeSpentWashing.seconds} seconds!")
        
        ##Python < 3.6 compatible:
        ##print "Badge number %i washed in %s (Sanitizer %i) at %s, for %s seconds!" % (badge,thisSanitizer.location,thisSanitizer.ID,.strftime("%m/%d/%Y, %H:%M:%S"),str(timeSpentWashing.total_seconds))
        ## man, aren't fstrings so much nicer?

if __name__=="__main__":
    main()
