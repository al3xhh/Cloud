import sys
import math

previous = None
sum = 0
nan = False
count = 0
if sys.argv[1] == "decade":
    count = 10
elif sys.argv[1] == "century":
    count = 100
else:
    count = -1

for line in sys.stdin:
    key, value = line.split(",")

    if key != previous:
        if previous is not None:
            print key + ";" + str(sum / (12 * count))

        previous = key
        sum = 0
        nan = False

    if not math.isnan(float(value)):
        sum = sum + float(value)
