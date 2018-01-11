import sys
import math

previous = None
sum = 0
nan = False

for line in sys.stdin:
    key, value = line.split(",")

    if key != previous:
        if previous is not None and not nan:
            print key + ";" + str(sum / 3)
            
        previous = key
        sum = 0
        nan = False
    
    if not math.isnan(float(value)) and not nan:
        sum = sum + float(value)
    else:
        nan = True