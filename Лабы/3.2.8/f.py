import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки


T = [0.026, 0.019, 0.0165, 0.015, 0.0126, 0.0104, 0.0078, 0.0052, 0.0028, 0.00094]
C = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]

for i in range(len(C)):
    C[i] = C[i] * 10**(-9)

ax.set_xlabel(r"$С, Ф$", fontsize=12.5)
ax.set_ylabel(r"T, с", fontsize=12.5)
ax.set_title(r"$T=f(C)$", fontsize=15)#название графика

ax.xaxis.set_minor_locator(plt.MultipleLocator(0.000000002)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.001))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')
t= np.polyfit(C, T, 1) #аппроксимация
f = np.poly1d(t)

ft = []
for i in range(len(C)):
    ft.append(408000 * C[i])

t= np.polyfit(C, ft, 1) #аппроксимация
f2 = np.poly1d(t)

ax.plot(C, f2(C), color="r", linestyle='-', label = "Теория") #график
ax.plot(C, f(C), linestyle="-", marker='None', color="b", label = 'Эксперименты') #график
ax.plot(C, T, linestyle="None", marker='o', color="b") #график





#plt.errorbar(U, I, yerr=yerr, fmt='None', ecolor='red')


plt.xlim(0.2 * 0.00000001, 5.2* 0.00000001)
plt.ylim(0, 0.027)

# x1 = U
# y1 = I
# avgx= mean(x1)
# avgy=mean(y1)
# x_2 =[0] * len(x1)
# y_2=[0] * len(y1)
# for i in range(len(x1)):
#     x_2[i]=x1[i]**2
# for i in range(len(x1)):
#     y_2[i]=y1[i]**2
# avgx2=mean(x_2)
# avgy2=mean(y_2)
# sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-(1.607*10**(-5))**2)/(len(x1)))**0.5
# print(sigma)
# print(sigma/(1.607*10 **(-5)))
# print(f)

ax.legend()

fig.savefig("f(C).png") #сохранение