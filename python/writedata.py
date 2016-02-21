import json

def write(data, fileNm):
    f = open("datafiles/" + fileNm, 'a+')
    f.write(data)
