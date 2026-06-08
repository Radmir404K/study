import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [0.02, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
y = [0.328, 0.72, 1.03, 1.26, 1.44, 1.6, 1.75, 1.87]

x1 = np.linspace(0, 0.74, 1000)
f = 2 * np.pi * np.sqrt(1390 * x1) * 0.01

ax.set_xlabel(r"C, мкФ", fontsize=12.5)
ax.set_ylabel(r"T, мс", fontsize=12.5)
ax.set_title(r"Зависимость T(C)", fontsize=15)#название графика

ax.xaxis.set_minor_locator(plt.MultipleLocator(0.02)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(x1, f, linestyle="-", marker='None', color="r", label = "теория") #график

plt.xlim(-0.04, 0.8)
plt.ylim(0, 2.8)

ax.legend()

for i in x:
    print(2 * np.pi * np.sqrt(1390 * i) * 0.01)

fig.savefig("graph1.png") #сохранение