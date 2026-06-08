import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [11, 41, 81, 131]
y = [71, 131, 195, 276]

kef = 9.8067 * 0.2 * 0.9932
for i in range(4):
    y[i] = y[i] * kef

xapr=[81, 131]
yapr=[195, 276]
for i in range(2):
    yapr[i] = yapr[i] * kef

t= np.polyfit(xapr, yapr, 1) #аппроксимация
f = np.poly1d(t)



ax.set_xlabel(r"x, см", fontsize=12.5)
ax.set_ylabel(r"P, Па", fontsize=12.5)
ax.set_title(r"Зависимость P(x)", fontsize=15)#название графика

ax.plot(x, f(x), color='red')
ax.plot(x, y, linestyle="None", marker='o', color="b") #график


ax.xaxis.set_minor_locator(plt.MultipleLocator(4)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(4))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')



fig.savefig("P(x)1.png") #сохранение