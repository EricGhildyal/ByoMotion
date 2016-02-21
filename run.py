import proc
import writedata
#import display
import subprocess

fileNm = ""

def getData():
    cmd = "read.exe"
    subprocess.call(cmd, stdin=None, stdout=None, stderr=None, shell=False)

def intro():
    print("============================ WELCOME TO ByoMotion ============================")
    name = raw_input("What is your name?")
    print "Hello " + name + " Please follow the on screen commands:"
    print "Your file will be named: " + name + "-data.json"
    print "Please follow the on screen prompts:"
    return name + "-data.json"

def main():
    fileNm = intro()
    #getData()
    offset = proc.procFile("data.txt")


if __name__ == '__main__':
    main()
