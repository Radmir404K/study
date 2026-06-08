import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

nu = [40, 150, 250, 300, 400, 500, 600, 750, 800, 1000, 1500, 2000, 2500, 3000]
L = [10.28, 7.35, 5.38, 4.79, 4.08, 3.69, 3.45, 3.25, 3.21, 3.1, 2.97, 2.93, 2.91, 2.9]

y = []
for i in range(len(L) - 1):
    y.append((L[0] - L[i])/(L[i] - L[len(L) - 1]))
for i in range(len(L) - 1):
    nu[i] = nu[i] ** 2

t= np.polyfit(nu[:len(L) - 4], y[:len(y) - 3], 1) #аппроксимация
f = np.poly1d(t)
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.2*10**6)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(20))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.set_xlabel(r"$\nu^2$, $Гц^2$", fontsize=12.5)
ax.set_ylabel(r"$\frac{L_{max} - L}{L - L_{min}}$", fontsize=12.5)
ax.set_title(r"$\frac{L_{max} - L}{L - L_{min}}$=$f(\nu^2)$", fontsize=15)#название графика

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(nu[:len(nu) - 1], y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(nu, f(nu), linestyle="-", marker='None', color="r", label = "теория") #график

x1 = nu[:len(L) - 4]
y1 = y[:len(y) - 3]
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
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-0.00003612**2)/(len(x1)+1))**0.5
print(sigma)
print(sigma/0.00003612)
plt.xlim(0, 7*10**6)
plt.ylim(0, 800)
print(f)
fig.savefig("graph4.png") #сохранение