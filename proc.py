import json

#take file, make array of each timestamped (line number) data value
def procFile(data):
    #setup for data being sent in, 1 index gap between sets of numbers
    data = data.strip('\n').split(',')
    offsetR = procData("roll", data[0])
    offsetP = procData("pitch", data[1])
    offsetY = procData("yaw", data[2])

    return [offsetR, offsetP, offsetY]


#status being how much user has left to reach average human movement.
def getUserStatusRoll(myoRoll):
    maxRange = 12
    minRange = 0
    userStatus = -1

    if myoRoll <= maxRange and myoRoll >= minRange:
        userStatus = maxRange - myoRoll

    return userStatus

def getUserStatusUpDown(myoUpDown):
    maxRange = 17
    minRange = 0
    userStatus = -1

    if myoUpDown <= maxRange and myoUpDown >= minRange:
        userStatus = maxRange - myoUpDown

    return userStatus

def getUserStatusYaw(myoYaw):
    maxRange = 17
    minRange = 0
    userStatus = -1

    if myoYaw <= maxRange and myoYaw >= minRange:
        userStatus = maxRange - myoYaw

    return userStatus

#Process data
def procData(type, data):
    offset = -1
    data = int(data)
    if type == "roll":
        offset = getUserStatusRoll(data)
    elif type == "pitch":
        offset = getUserStatusUpDown(data)
    elif type == "yaw":
        offset = getUserStatusYaw(data)
    return offset
