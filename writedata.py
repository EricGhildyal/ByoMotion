import json
import datetime
import os

def write(data, fileNm):
    f = open(fileNm, 'a+')
    if(os.stat(fileNm).st_size == 0):
        i = 0
    else:
        f.seek(-10, 2)
        tst = f.read()
        tst = tst.split('=')
        i = tst[0]
        i = int(i)
        i = i+1
        f.seek(0,0)
    for arr in data:
        f.write(str(i))
        f.write('=')
        for dataPoint in arr:
            f.write(str(dataPoint) + ',')
        f.write('\n')
        i = i+1
