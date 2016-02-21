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

#atus being how much user has left to reach average human movement.
# def getUserStatusUpDown(myoUpDown):
#     maxRange = 90
#     minRange = -120
#
#     if myoUpDown < 0:
#         userStatus = minRange + myoUpDown
#     elif myoUpDown > 0:
#         userStatus = maxRange - myoUpDown
#
#     return userStatus
#
# def checkRangeWristTwist(myoWristTwist):
#     maxRange = 80
#     minRange = -80
#
#     if (myoWristTwist < maxRange and myoWristTwist > minRange):
#         inRange = true
#     else:
#         inRange = false
#
#     return inRange
#
# def getUserStatusTwist(myoWristTwist):
#     maxRange = 80
#     minRange = -80
#
#     if (myoWristTwist < 0):
#         userStatus = minRange + myoWristTwist
#     elif (myoWristTwist > 0):
#         userStatus = maxRange - myoWristTwist
#
#     return userStatus
#
# # Returns boolean true if arm is outward (i.e. armIsOutward == true)
# def checkRangeInwardOutward(myoUpDown, myoWristTwist):
#     upDownMaxRange = 90
#     upDownMinRange = -90
#
#     wristMaxRange = 80 # twist outward
#     wristMinRange = -80 # twist inward
#
#     if (checkRangeShoulderUpDown(myoUpDown) == true and myoWristTwist > 0 and myoWristTwist <= wristMaxRange):
#         armIsOutward = true
#
#     if (checkRangeShoulderUpDown(myoUpDown) == true and myoWristTwist < 0 and myoWristTwist >= wristMinRange):
#         armIsOutward = false
#
#     return armIsOutward
#
# def getUserStatusInwardOutward(myoUpDown, myoWristTwist):
#     if armIsLeft = checkRangeInwardOutward(myoUpDown, myoWristTwist) == true:
