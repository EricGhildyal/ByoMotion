import json
name = ""

def procData(data):
    for el in data: #split by readings
        print(el.strip('\n').split(',')) #get separated data

#take file, make array of each timestamped (line number) data value
def procFile(fileNm):
    data = []
    f = open("datafiles/" + fileNm, 'a+')
    for line in f:
        data.append(line)
    procData(data)

def checkRangeShoulderUpDown(myoUpDown):
    maxRange = 90
    minRange = -90

    if myoUpDown < maxRange and myoUpDown > minRange:
        inRange = true
    else:
        inRange = false

    return inRange

def checkRangeWristTwist(myoWristTwist):
    maxRange = 80
    minRange = -80

    if myoWristTwist < maxRange and myoWristTwist > minRange:
        inRange = true
    else:
        inRange = false

    return inRange

# Returns boolean true if arm is outward (i.e. armIsOutward == true)
def checkRangeInwardOutward(myoUpDown, myoWristTwist):
    upDownMaxRange = 90
    upDownMinRange = -90

    wristMaxRange = 80 # twist outward
    wristMinRange = -80 # twist inward

    if checkRangeShoulderUpDown(myoUpDown) == true and myoWristTwist > 0 and myoWristTwist <= wristMaxRange:
        armIsOutward = true

    if checkRangeShoulderUpDown(myoUpDown) == true and myoWristTwist < 0 and myoWristTwist >= wristMinRange:
        armIsOutward = false

    return armIsOutward
