#Lars Haukland Uke13 Numpy
from matplotlib import axes
from matplotlib.artist import Artist
import numpy as np
import matplotlib.pyplot as plt
import math

def get_x_when_y_is(y,xlist,ylist):
    # Sort
    order = ylist.argsort()
    ylist = ylist[order]
    xlist = xlist[order]

    return xlist[ylist.searchsorted(y, 'left')]

def get_y_when_x_is(x,xlist,ylist):
    # Sort
    order = ylist.argsort()
    ylist = ylist[order]
    xlist = xlist[order]

    return np.interp(x, ylist, xlist)

np.random.seed(12)

N_steps = 1000000
expected_R = np.sqrt(N_steps)
repeats = 5

max_point = 0

# List of lines to used for legend
lines = []

# List of labels used for legende
labels = []

for i in range(repeats):
    ###################################
    #     generate one random walk    #
    ###################################
    # a list of 4 directions 0,1,2,3
    dirs = np.random.randint(0, 4, N_steps)
    # a 2D list of steps, empty for now
    steps = np.empty((N_steps, 2))
    # fill the list of steps according to direction
    steps[dirs == 0] = [0, 1]  # 0 - right
    steps[dirs == 1] = [0, -1]  # 1 - left
    steps[dirs == 2] = [1, 0]  # 2 - up
    steps[dirs == 3] = [-1, 0]  # 3 - down
    ###################################
    # use cumsum to sum up the individual steps to get current position
    steps = steps.cumsum(axis=0)
    ###################################
    ###################################
    # draw only a selection of points, max 5000, to save memory
    skip = N_steps // 5000 + 1
    xs = steps[::skip, 0]
    ys = steps[::skip, 1]
    # Get maximum distanse away from 0,0 in plot and make it a legend
    newMaxX = max(steps[::,0])
    newMaxY = steps[::,1][np.where(steps[::,0] == newMaxX)]
    maxDistanse = math.sqrt((float(newMaxY[0]) ** 2) + (float(newMaxX) ** 2) )

    plt.plot(xs, ys, label=f"maxdist = {maxDistanse}")
    ###################################

###################################
# add a circle with expected distance
circle = plt.Circle((0, 0), radius=expected_R, color="k")
plt.gcf().gca().add_artist(circle)
# equal axis size
plt.gcf().gca().set_aspect("equal")
###################################

#set 0 as middle for xaxis and yaxis
x = plt.gca().get_xlim()
y = plt.gca().get_ylim()
highest_x = max(abs(x[0]),abs(x[1]))
highest_y = max(abs(y[0]),abs(y[1]))
max_point = max(highest_x,highest_y)
plt.xlim(-max_point,max_point)
plt.ylim(-max_point,max_point)

# Set title
plt.title(f"{repeats} random walks of {N_steps} steps")

# Set legend and position upperleft (loc=2)
plt.legend(loc=2)

plt.savefig("uke_13_oppg_10.png")

plt.show()