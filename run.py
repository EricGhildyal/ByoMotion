import proc
import writedata
import display
import os
import subprocess
import time

def getData():
    subprocess.call(['/Users/joshgulden/Desktop/SteelHacks/ByoMotion/./hello-myo'])

def intro():
    print("============================ WELCOME TO ByoMotion ============================")
    name = raw_input("What is your name?")
    print "Hello " + name + " Please follow the on screen commands:"
    print "Your file will be named: " + name + "-data.txt"
    return name + "-data.txt"

def run():
    print("Please keep your arm as steady as possible, follow the prompts")
    print("Hold your arm straight OUT and rotate it LEFT as far as you can go: ")
    time.sleep(5)
    getData()
    print("Hold your arm straight DOWN and move it UP as high as it will go: ")
    time.sleep(5)
    getData()
    print("Hold your arm straight OUT and move it LEFT from your body as far as you can go: ")
    time.sleep(5)
    getData()

def readDatFile(fileNm):
    f = open(fileNm, 'r')
    dates = []
    datas = []
    for line in f:
        line = line.split("=")
        dates.append(line[0])
        ln = line[1].strip("\n").split(",")
        datas.append(ln)
    return [dates, datas]

def graph(data):
    display.displayGraph(data)

def main():
    fileNm = intro()
    run()
    offset = []
    f = open('data.txt', 'r')
    for line in f:
        offset.append(proc.procFile(line))
    writedata.write(offset, fileNm)
    data = readDatFile(fileNm)
    graph(data)
    os.remove('data.txt')

if __name__ == '__main__':
    main()
