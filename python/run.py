import proc
import writedata
#import readdata

def intro():
    print("============================ WELCOME TO ByoMotion ============================")
    name = raw_input("What is your name?")
    print "Hello", name, "Please follow the on screen commands:"
    print "Your file will be named: ", name,"-data.json"
    print "Please follow the on screen prompts:"
    return name + "-data.json"

def main():
    fileNm = intro()
    proc.procFile(fileNm)

if __name__ == '__main__':
    main()
