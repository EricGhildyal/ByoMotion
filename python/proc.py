import json
name = ""

#returns file name
def intro():
    print("============================ WELCOME TO ByoMotion ============================")
    name = raw_input("What is your name?")
    print "Hello", name, "Please follow the on screen commands:"
    print "Your file will be named: ", name,"-data.txt"
    print "Please follow the on screen prompts:"
    return name + "-data.txt"

def procData(data):
    for el in data: #split by readings
        el.strip('\n').split(',') #get separated data

#def saveData(data):


#take file, make array of each timestamped (line number) data value
def procFile(fileNm):
    data = []
    f = open("datafiles/" + fileNm, 'a+')
    for line in f:
        data.append(line)
    return data

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

def main():
    fileNm = intro()
    data = procFile(fileNm)
    procData(data)

if __name__ == '__main__':
    main()
