import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x1 = [1/41.47, 1/82.94, 1/120.64]
y1 = [7.1, 4.61, 3.1]


t= np.polyfit(x1, y1, 1)
f = np.poly1d(t)

ax.set_xlabel(r"1/P, $торр^{-1}$", fontsize=12.5)
ax.set_ylabel(r"D, $см^{2}$/с", fontsize=12.5)
ax.set_title(r"Зависимость D(1/P)", fontsize=15)#название графика

yerr=[0] * 3
for i in range(3):
    yerr[i]= y1[i] * 0.03
ax.errorbar(x1, y1, yerr=yerr, linestyle="None", marker='o', color="b") #график
ax.plot(x1, f(x1), color="green")


ax.xaxis.set_minor_locator(plt.MultipleLocator(0.0004)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.2))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

plt.xlim(0.0076, 0.0248)
plt.ylim(2.8, 7.6)

ax.text(50, 0.138, "f =", fontsize="x-large")
ax.text(60, 0.138, f)


fig.savefig("D(P).png") #сохранение