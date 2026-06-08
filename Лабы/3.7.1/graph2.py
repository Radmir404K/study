from cmath import pi
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

nu1 = [22.5, 31.5, 40.5, 49.5, 58.5, 67.5, 76.5, 85.5, 94.5, 103.5]
U1 = [151, 214, 270, 321, 369, 413, 452, 483, 517, 544]
I1 = [424, 433, 428, 424, 419, 413, 407, 398, 394, 387]

nu2 = [112.5, 135, 157.5, 180, 202.5, 225, 325, 425, 525, 625, 725, 825, 925, 1025, 1125]
U2 = [575, 627, 667, 694, 713, 735, 766, 780, 776, 766, 750, 740, 722, 710, 690]
I2 = [385, 372, 363, 353, 345, 341, 322, 312, 303, 295, 287, 281, 273, 268, 260]
t2 = [3, 2.6, 2.4, 2.15, 1.9, 1.78, 1.3, 1.06, 0.88, 0.72, 0.66, 0.58, 0.53, 0.48, 0.44]

nu3 = [1415, 1770, 2221, 2786, 3495, 4385, 5500, 6901, 8657, 10860, 13624, 17092, 21442, 26899]
U3 = [638, 576, 506, 433, 361, 298, 234, 183, 139, 104, 76, 56, 41, 32]
I3 = [240, 217, 191, 165, 139, 115, 94, 76, 61, 48, 37, 27, 19, 11]
t3 = [0.365, 0.265, 0.21, 0.162, 0.122, 0.094, 0.07, 0.052, 0.037, 0.0265, 0.0176, 0.0108, 0.0066, 0.0036]

tanpsi = []

for i in range(len(nu2)):
    tanpsi.append(np.tan((t2[i] * nu2[i] / 1000 * 2 - 0.5) * np.pi))

nu = nu2[:6]
tan = tanpsi[:6]
t= np.polyfit(nu, tan, 1) #аппроксимация
f = np.poly1d(t)


ax.xaxis.set_minor_locator(plt.MultipleLocator(40)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.set_xlabel(r"$\nu$, Гц", fontsize=12.5)
ax.set_ylabel(r"$tan~ \psi$", fontsize=12.5)
ax.set_title(r"График $tan~ \psi = f(\nu)$", fontsize=15)#название графика

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(nu2, tanpsi, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(nu2, f(nu2), linestyle="-", marker='None', color="r", label = "теория") #график

plt.xlim(80, 1160)
plt.ylim(0, 33)

#ax.legend()
print(f)
#sigma = 2* 

fig.savefig("graph2.png") #сохранение