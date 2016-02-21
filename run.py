import proc
import writedata
import display
import subprocess
from time import gmtime, strftime

def getData():
    cmd = "hello_myo"
    subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=False)

def intro():
    print("============================ WELCOME TO ByoMotion ============================")
    name = raw_input("What is your name?")
    print "Hello " + name + " Please follow the on screen commands:"
    print "Your file will be named: " + name + "-data.txt"
    return name + "-data.json"

def run():
    print("Please keep your arm as steady as possible, follow the prompts")
    print("Hold your arm straight OUT and rotate it LEFT as far as you can go: ")
    getData()
    print("Hold your arm straight DOWN and move it UP as high as it will go: ")
    getData()
    print("Hold your arm straight OUT and move it LEFT from your body as far as you can go: ")
    getData()

def readDatFile(fileNm):
    f = open(fileNm, 'r')
    dates = []
    datas = []
    for line in f:
        line = line.split("=")
        dates.append(line[0])
        ln = line[1].strip("\n").split(",")
        for num in ln:
            datas.append(num)
    return [dates, datas]

def graph(data):
    display.graph(data)

def main():
    fileNm = intro()
    run()
    offset = proc.procFile("data.txt")
    writedata.write(offset, fileNm)
    data = readDatFile(fileNm)
    graph(data)

if __name__ == '__main__':
    main()
