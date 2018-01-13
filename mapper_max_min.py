import sys

firstLine = True
lastCity = None
lastYear = ""
ret = ""

for line in sys.stdin:
    line = line.split(";")

    if lastCity is None:
        lastCity =  line[0]
        ret += line[0] + ";" + line[1] + ";"
    elif lastCity != line[0]:
            print ret + lastYear
            lastCity = line[0]
            ret = ""
            ret += line[0] + ";" + line[1] + ";"
    lastYear = line[1]

print ret + line[1]