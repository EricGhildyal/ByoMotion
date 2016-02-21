import json
import datetime

def write(data, fileNm):
    f = open(fileNm, 'a+')
    f.write(strftime("%Y-%m-%d %X", gmtime()))
    for dataPoint in data:
        f.write(dataPoint + ",")
