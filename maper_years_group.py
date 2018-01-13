import sys

grouping = sys.argv[1]

cities = ['Berlin', 'Brisbane', 'Caracas', 'Fez', 'La Serena', 'Madrid', 'Melbourne',
 'Mexico', 'Moscow', 'New York', 'Peking', 'Sacramento', 'Shanghai', 'Tripoli']


def decade(year):
    return  year[:len(year)-1] + "0"

def century(year):
    return  year[:len(year)-2] + "00"

for line in sys.stdin:
    line = line.split(";")

    if line[2] in cities:
        print line[2] + ";" + ((decade(line[6])) if grouping == "decade" else century(line[6])) + "," + line[1]
