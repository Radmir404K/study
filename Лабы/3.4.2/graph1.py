import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

eps = [0.013, 0.0193, 0.02, 0.0179, 0.0176, 0.0186, 0.0186, 0.0185, 0.0185, 0.0169, 0.0184, 0.0191, 0.0188, 0.0196, 0.019]

x = [14.00, 16.02, 18.02, 20.03, 21.01, 22.01, 24.01, 26.01, 28.01, 30.01, 32.00, 34.00, 36.00, 38.00, 40.00]
y = [10.072, 9.960, 9.767, 9.431, 9.234, 9.032, 8.748, 8.609, 8.534, 8.486, 8.454, 8.429, 8.410, 8.396, 8.384]


for i in range(len(y)):
    y[i] = y[i]**2 - 8.252**2
    x[i] = x[i] - eps[i] * 24
    print(round(x[i], 1), end = ' ')
    print(round(y[i], 2), end = ' ')
    print(1/y[i])

#x1 = np.linspace(0, 0.74, 1000)
#f = 2 * np.pi * np.sqrt(1390 * x1) * 0.01

ax.set_xlabel(r"T, $\degree C$", fontsize=12.5)
ax.set_ylabel(r"$\tau^{2} - \tau_{0}^{2}$, $мкс^{2}$", fontsize=12.5)
ax.set_title(r"Зависимость $\tau^{2} - \tau_{0}^{2}$=f(T)", fontsize=15)#название графика


ax.xaxis.set_minor_locator(plt.MultipleLocator(1)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
#ax.plot(x1, f, linestyle="-", marker='None', color="r", label = "теория") #график

plt.xlim(13, 41)
plt.ylim(0, 35)

#ax.legend()


fig.savefig("graph1.png") #сохранение