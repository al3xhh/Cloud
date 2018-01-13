import sys

key = None
for line in sys.stdin:
    line = line.strip()
    line = line.split(";")
    currentKey = line[0]
    if key is None or key != currentKey:
        if not (key is None):
            print key + ";" + str(minTemp) + ";" + str(maxTemp)
        minTemp = 100
        maxTemp = -100
        key = currentKey

    if float(line[2]) < minTemp:
        minTemp = float(line[2])
    if float(line[2]) > maxTemp:
        maxTemp = float(line[2])

print key + ";" + str(minTemp) + ";" + str(maxTemp)
