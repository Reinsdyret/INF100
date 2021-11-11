from matplotlib import axes
import matplotlib.pyplot as plt
from math import sin

# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]

plt.plot(xs, ys_1, "-.r")
plt.plot(xs, ys_2, "--b")

# Set minor ticks on
# plt.minorticks_on()

# Draw arrow from (0,0) to about the first intersection
# plt.arrow(0,0,2.5,0,width = 0.001,length_includes_head = True,head_width = 0.2)

# Comment under arrow
# plt.text(0,-0.3,"Første interseksjonen")

# savefig lagrer filene
plt.savefig("uke_12_oppg_1.png")
plt.savefig("test.pdf")

# interaktivt vindu
plt.show()
