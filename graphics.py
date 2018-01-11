import numpy as np
import matplotlib.pyplot as plt
import sys

tempSac = []
tempNeY = []
tempMex = []

with open('../MinMaxYears.csv', 'r') as inF:
        for line in inF:
            minYear = line.split(";")[0]
            maxYear = line.split(";")[1]

years = [x for x in xrange(int(minYear), int(maxYear) + 1)]

with open('../AverageByCity14Filtered.csv', 'r') as inF:
        for line in inF:
            splitedLine = line.split(";")

            if splitedLine[0] == " ":
                tempSac.append(float(splitedLine[2]))
            if splitedLine[0] == "New York":
                tempNeY.append(float(splitedLine[2]))
            if splitedLine[0] == "Mexico":
                tempMex.append(float(splitedLine[2]))

fig, ax = plt.subplots()
ax.plot(years, tempSac, 'k--', label='Sacramento')
ax.plot(years, tempNeY, 'k:', label='New York')
ax.plot(years, tempMex, 'k', label='Mexico')

legend = ax.legend(loc='upper left', shadow=True, fontsize='small')

legend.get_frame().set_facecolor('#00FFCC')

# Get the bounding box of the original legend
bb = legend.get_bbox_to_anchor().inverse_transformed(ax.transAxes)

# Change to location of the legend. 
xOffset = 1
bb.x0 += xOffset
bb.x1 += xOffset
legend.set_bbox_to_anchor(bb, transform = ax.transAxes)

plt.show()