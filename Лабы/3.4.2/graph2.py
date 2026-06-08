import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

eps = [0.013, 0.0193, 0.02, 0.0179, 0.0176, 0.0186, 0.0186, 0.0185, 0.0185, 0.0169, 0.0184, 0.0191, 0.0188, 0.0196, 0.019]

x = [14.00, 16.02, 18.02, 20.03, 21.01, 22.01, 24.01, 26.01, 28.01, 30.01, 32.00, 34.00, 36.00, 38.00, 40.00]
y = [10.072, 9.960, 9.767, 9.431, 9.234, 9.032, 8.748, 8.609, 8.534, 8.486, 8.454, 8.429, 8.410, 8.396, 8.384]

x1 = []
y1 = []

for j in range(len(x)):
    x[j] = x[j] - eps[j] * 24
    print(x[j])

for i in range(len(y)):
    y[i] = 1/ (y[i]**2 - 8.252**2)

for i in range(4, len(x)):
    x1.append(x[i])
    y1.append(y[i])

t= np.polyfit(x1, y1, 1) #аппроксимация
f = np.poly1d(t)

ax.set_xlabel(r"T, $\degree C$", fontsize=12.5)
ax.set_ylabel(r"$1/(\tau^{2} - \tau_{0}^{2}$, $1/мкс^{2})$", fontsize=12.5)
ax.set_title(r"Зависимость $1/(\tau^{2} - \tau_{0}^{2})$=f(T)", fontsize=15)#название графика


ax.xaxis.set_minor_locator(plt.MultipleLocator(1)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.02))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.errorbar(x1, y1, xerr=0.0012 * 24, linestyle="None", marker='o', color="b", markersize = 5)

ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты", markersize = 5) #график
ax.plot(x, f(x), color='red')

print(f)

print(0.3799 / 0.02131)

plt.xlim(13, 40)
plt.ylim(0, 0.5)

ax.text(14, 0.46, "f =", fontsize="xx-large")
ax.text(15, 0.46, f, fontsize = "xx-large")

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
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-0.02131**2)/(len(x1)+1))**0.5
print(sigma)
print(sigma/0.02131)

fig.savefig("graph2.png") #сохранение