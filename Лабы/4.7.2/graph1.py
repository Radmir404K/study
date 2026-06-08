import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [1, 2, 3, 4, 5]
y = [3, 4, 4.8, 5.8, 6.5]

for i in range(len(y)):
    y[i] = y[i]**2

ax.set_xlabel(r"m", fontsize=12.5)
ax.set_ylabel(r"$r^{2}$, $см^2$", fontsize=12.5)
ax.set_title(r"$r^2=f(m)$", fontsize=15)#название графика

t= np.polyfit(x, y, 1) #аппроксимация
f = np.poly1d(t)

ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(x, f(x), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график

plt.xlim(0.8, 5.2)
plt.ylim(7, 44)

ax.legend()
print(f)


fig.savefig("graph1.png") #сохранение