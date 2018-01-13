import numpy as np
import matplotlib.pyplot as plt
import sys

fileText = sys.argv[1]

with open('maxMinYears.csv', 'r') as inF:
        for line in inF:
            minYear = line.split(";")[0]
            maxYear = line.split(";")[1]

years = [x for x in xrange(int(minYear), int(maxYear) + 1)]

cities = []
with open("configFile", 'r') as inF:
        for line in inF:
            cities.append(line.strip())

data = []
with open(fileText, 'r') as inF:
        for line in inF:
            if line.split(";")[0] in cities:
                data.append(line.strip())

citiesData = []
key = None
temperature = []
for line in data:
    splitedLine = line.split(";")
    currentKey = splitedLine[0]
    if key is None or key != currentKey:
        if not (key is None):
            citiesData.append(temperature)
        temperature = []
        key = currentKey
    temperature.append(float(splitedLine[2]))
citiesData.append(temperature)



pattern = ['k', 'k--', 'k:']

fig, ax = plt.subplots()
print cities
for i in xrange(0, len(cities)):
    ax.plot(years, citiesData[i], pattern[i], label=cities[i])


legend = ax.legend(loc='upper left', shadow=True, fontsize='small')

legend.get_frame().set_facecolor('#00FFCC')

# Get the bounding box of the original legend
bb = legend.get_bbox_to_anchor().inverse_transformed(ax.transAxes)

# Change to location of the legend.
xOffset = 1
bb.x0 += xOffset
bb.x1 += xOffset
legend.set_bbox_to_anchor(bb, transform = ax.transAxes)

#plt.show()
plt.savefig("./results/" + sys.argv[2] + '.png',  bbox_inches='tight')
