import sys

for line in sys.stdin:
    minYear = line.split(";")[0]
    maxYear = line.split(";")[1]

with open('../AverageByCity14.csv', 'r') as inF:
        for line in inF:
            splitedLine = line.split(";")

            if splitedLine[1] >= minYear and splitedLine[1] <= maxYear:
                print line,