import json
name = ""

#Process data
def procData(type, dataMin, dataMax):
    if type == "roll":
        print "roll with max = " + dataMax + " and min: " + dataMin
    elif type == "pitch":
        print "pitch with max = " + dataMax + " and min: " + dataMin
    elif type == "yaw":
        print "yaw with max = " + dataMax + " and min: " + dataMin


#take file, make array of each timestamped (line number) data value
def procFile(fileNm):
    f = open("datafiles/" + fileNm, 'r') #file *should be* created and filled
    #split the line up
    line = f.read()
    line = line.strip('\n').split(',')
    print line
    #setup for data being sent in, 1 index gap between sets of numbers
    procData("roll", line[0], line[1])
    procData("pitch", line[2], line[3])
    procData("yaw", line[4], line[5])

#status being how much user has left to reach average human movement.
def getUserStatusUpDown(myoUpDown):
    maxRange = 17
    minRange = 0

	if (myoUpDown <= maxRange and myoUpDown >= minRange):
		userStatus = maxRange - myoUpDown

    return userStatus

def getUserStatusRoll(myoRoll):
    maxRange = 12
    minRange = 0

	if (myoRoll <= maxRange and myoRoll >= minRange):
    	userStatus = maxRange - myoRoll

    return userStatus

def getUserStatusYaw(myoYaw):
	maxRange = 17
	minRange = 0

	if (myYaw <= maxRange and myoRoll >= minRange):
		userStatus = maxRange - myoYaw

	return userStatus
