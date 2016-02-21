import json
import datetime

def write(data, fileNm):
    f = open(fileNm, 'a+')
    f.write(datetime.date)
    for dataPoint in data:
        f.write(dataPoint + ",")
