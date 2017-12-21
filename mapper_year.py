import sys

for line in sys.stdin:
    line = line.split(";")

    print line[2] + ";" + line[6] + "," + line[1]
    