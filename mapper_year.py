import sys

cities = ['Berlin', 'Brisbane', 'Caracas', 'Fez', 'La Serena', 'Madrid', 'Melbourne',
 'Mexico', 'Moscow', 'New York', 'Peking', 'Sacramento', 'Shanghai', 'Tripoli']

for line in sys.stdin:
    line = line.split(";")

    if line[2] in cities:
        print line[2] + ";" + line[6] + "," + line[1]
