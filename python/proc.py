

def procData(data):
    for el in data: #split by readings
        el.strip('\n').split(',') #get separated data


#take file, make array of each timestamped (line number) data value
def procFile(fileNm):
    data = []
    f = open(fileNm, 'r')
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

## def checkRangeLeftRight(myoUpDown, myoWristTwist):


def main():
    data = procFile("data.txt")
    procData(data)

if __name__ == '__main__':
    main()
