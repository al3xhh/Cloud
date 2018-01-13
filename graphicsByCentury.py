import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

temperatures = pd.read_csv(sys.argv[1], sep=";", names = ["col1", "col2", "col3"])

N = 14
temp19 = list(temperatures[temperatures.col2 == 1900]["col3"])
temp20 = list(temperatures[temperatures.col2 == 2000]["col3"])
ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, temp19, width, color='r')

rects2 = ax.bar(ind + width, temp20, width, color='g')

# add some text for labels, title and axes ticks
ax.set_ylabel('Temperature C')
ax.set_title('Average Temperature by century')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('Berlin', 'Brisbane', 'Caracas', 'Fez', 'La Serena', 'Madrid', 'Melbourne',
 'Mexico', 'Moscow', 'New York', 'Peking', 'Sacramento', 'Shanghai', 'Tripoli'))

ax.legend((rects1[0], rects2[0]), ('XIX', 'XX'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.savefig("./results/" + sys.argv[2] + '.png',  bbox_inches='tight')
