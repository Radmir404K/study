import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

y = [1.6, 1.5, 1.3, 1.25, 1.15, 1, 0.9, 0.45]
x = [1.9, 1.85, 1.65, 1.5, 0.75, 0.65, 0.5, 0.25]

ax.set_xlabel(r"$I_{м}$", fontsize=12.5)
ax.set_ylabel(r"B, мТл", fontsize=12.5)
ax.set_title(r"$B=f(I_{м})$", fontsize=15)#название графика

#ax.xaxis.set_minor_locator(plt.MultipleLocator(0.02)) #ticks
#ax.yaxis.set_minor_locator(plt.MultipleLocator(10))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
#ax.plot(x1, f, linestyle="-", marker='None', color="r", label = "теория") #график

#plt.xlim(0, 0.6)
#plt.ylim(0, 400)

#ax.legend()


fig.savefig("graph2.png") #сохранение