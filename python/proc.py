import json
name = ""

#Process data
def procData(data):
    

#take file, make array of each timestamped (line number) data value
def procFile(fileNm):
    data = []
    f = open("datafiles/" + fileNm, 'r') #file *should be* created and filled
    for line in f:
        data.append(line.strip('\n').split(','))
    procData(data)

def checkRangeShoulderUpDown(myoUpDown):
    maxRange = 90
    minRange = -120

    if myoUpDown < maxRange and myoUpDown > minRange:
        inRange = true
    else:
        inRange = false

    return inRange

# status being how much user has left to reach average human movement.
def getUserStatusUpDown(myoUpDown):
    maxRange = 90
    minRange = -120

    if (myoUpDown < 0):
        userStatus = minRange + myoUpDown
    else if (myoUpDown > 0):
        userStatus = maxRange - myoUpDown

    return userStatus

def checkRangeWristTwist(myoWristTwist):
    maxRange = 80
    minRange = -80

    if (myoWristTwist < maxRange and myoWristTwist > minRange):
        inRange = true
    else:
        inRange = false

    return inRange

def getUserStatusTwist(myoWristTwist):
    maxRange = 80
    minRange = -80

    if (myoWristTwist < 0):
        userStatus = minRange + myoWristTwist
    else if (myoWristTwist > 0):
        userStatus = maxRange - myoWristTwist

    return userStatus

# Returns boolean true if arm is outward (i.e. armIsOutward == true)
def checkRangeInwardOutward(myoUpDown, myoWristTwist):
    upDownMaxRange = 90
    upDownMinRange = -90

    wristMaxRange = 80 # twist outward
    wristMinRange = -80 # twist inward

    if (checkRangeShoulderUpDown(myoUpDown) == true and myoWristTwist > 0 and myoWristTwist <= wristMaxRange):
        armIsOutward = true

    if (checkRangeShoulderUpDown(myoUpDown) == true and myoWristTwist < 0 and myoWristTwist >= wristMinRange):
        armIsOutward = false

    return armIsOutward

def getUserStatusInwardOutward(myoUpDown, myoWristTwist):
    if armIsLeft = checkRangeInwardOutward(myoUpDown, myoWristTwist) == true:
        
