import json

#take file, make array of each timestamped (line number) data value
def procFile(fileNm):
    f = open("datafiles/" + fileNm, 'r') #file *should be* created and filled
    #split the line up
    line = f.read()
    line = line.strip('\n').split(',')
    #setup for data being sent in, 1 index gap between sets of numbers
    procData("roll", line[0])
    procData("pitch", line[1])
    procData("yaw", line[2])

#status being how much user has left to reach average human movement.
def getUserStatusUpDown(myoUpDown):
    maxRange = 17
    minRange = 0
    userStatus = -1

    if myoUpDown <= maxRange and myoUpDown >= minRange:
        userStatus = maxRange - myoUpDown

    return userStatus

def getUserStatusRoll(myoRoll):
    maxRange = 12
    minRange = 0
    userStatus = -1

    if myoRoll <= maxRange and myoRoll >= minRange:
        userStatus = maxRange - myoRoll

    return userStatus

def getUserStatusYaw(myoYaw):
    maxRange = 17
    minRange = 0
    userStatus = -1

    if myoYaw <= maxRange and myoRoll >= minRange:
        userStatus = maxRange - myoYaw

	return userStatus

#Process data
def procData(type, data):
    if type == "roll":
        getUserStatusRoll(data)
    elif type == "pitch":
        getUserStatusUpDown(data)
    elif type == "yaw":
        getUserStatusYaw(data)
