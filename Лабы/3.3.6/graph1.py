import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

I = [0.02, 0.1, 0.2, 0.3, 0.4, 0.5, 0.57]
B = [21.4, 103.3, 193.1, 286, 342, 371, 386]

ax.set_xlabel(r"$I_{м}$", fontsize=12.5)
ax.set_ylabel(r"B, мТл", fontsize=12.5)
ax.set_title(r"$B=f(I_{м})$", fontsize=15)#название графика

ax.xaxis.set_minor_locator(plt.MultipleLocator(0.02)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(10))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(I, B, linestyle="None", marker='o', color="b", label = "эксперименты") #график
#ax.plot(x1, f, linestyle="-", marker='None', color="r", label = "теория") #график

plt.xlim(0, 0.6)
plt.ylim(0, 400)

#ax.legend()


fig.savefig("graph1.png") #сохранение