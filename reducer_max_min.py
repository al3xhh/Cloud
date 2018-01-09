import sys

minYear = 1750
maxYear = 2018

for line in sys.stdin:
    line = line.split(";")

    if int(line[1]) > minYear:
        minYear = int(line[1])
    if int(line[2]) < maxYear:
        maxYear = int(line[2])

print str(minYear) + ";" + str(maxYear)