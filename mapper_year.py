import sys

cities = ['Sacramento', 'New York', 'Mexico', 'Recife', 'La Serena', 'Madrid',
            'Berlin', 'Moscow', 'Tripoli', 'Johannesburg', 'Singapore', 'Melbourne', 'Peking', 'New Delhi']

for line in sys.stdin:
    line = line.split(";")

    if line[2] in cities:
        print line[2] + ";" + line[6] + "," + line[1]
    