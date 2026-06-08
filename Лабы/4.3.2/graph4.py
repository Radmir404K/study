import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [-1, 0, 1]
y = [-142, 0 ,141]


for i in range(len(x)):
    y[i] *= 4

ax.set_xlabel(r"m", fontsize=12.5)
ax.set_ylabel(r"$x_m$, $мкм$", fontsize=12.5)
#ax.set_title(r"$r^2=f(m)$", fontsize=15)#название графика

t= np.polyfit(x, y, 1) #аппроксимация
f = np.poly1d(t)

ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(40))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(x, f(x), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график

#plt.xlim(0.8, 5.2)
plt.ylim(-600, 600)

ax.legend()
print(f)

x1 = x
y1 = y
avgx= mean(x1)
avgy=mean(y1)
x_2 =[0] * len(x1)
y_2=[0] * len(y1)
for i in range(len(x1)):
    x_2[i]=x1[i]**2
for i in range(len(x1)):
    y_2[i]=y1[i]**2
avgx2=mean(x_2)
avgy2=mean(y_2)
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-(566)**2)/(len(x1)))**0.5
print(sigma)
print(sigma/(566))
fig.savefig("graph4.png") #сохранение