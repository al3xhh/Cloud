import sys

cities = ['Berlin', 'Brisbane', 'Caracas', 'Fez', 'La Serena', 'Madrid', 'Melbourne',
 'Mexico', 'Moscow', 'New York', 'Peking', 'Sacramento', 'Shanghai', 'Tripoli']

def seasons(month):
    if month in [12, 1, 2]:
        return "1"
    if month in [3, 4, 5]:
        return "2"
    if month in [6, 7, 8]:
        return "3"
    if month in [9, 10, 11]:
        return "4"

for line in sys.stdin:
    line = line.split(";")

    if line[2] in cities:
        if line[7] == 01:
            line[6] = int(line[6]) - 1
        print line[2] + ";" + line[6] + ";" + seasons(int(line[7])) + "," + line[1]
