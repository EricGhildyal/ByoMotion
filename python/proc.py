

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

def main():
    data = procFile("data.txt")
    procData(data)

if __name__ == '__main__':
    main()
