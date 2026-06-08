import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки


T = [0.076, 0.072, 0.062, 0.052, 0.045, 0.036, 0.029, 0.0215, 0.014]
R = [940000, 900000, 800000, 700000, 600000, 500000, 400000, 300000, 200000]


ax.set_xlabel(r"$R, Ом$", fontsize=12.5)
ax.set_ylabel(r"T, с", fontsize=12.5)
ax.set_title(r"$T=f(R)$", fontsize=15)#название графика

ax.xaxis.set_minor_locator(plt.MultipleLocator(20000)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.002))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')
t= np.polyfit(R, T, 1) #аппроксимация
f = np.poly1d(t)

ft = []
for i in range(len(R)):
    ft.append(0.000000067 * R[i])

t= np.polyfit(R, ft, 1) #аппроксимация
f2 = np.poly1d(t)

ax.plot(R, f2(R), color="r", linestyle='-', label = "Теория") #график
ax.plot(R, f(R), linestyle="-", marker='None', color="b", label = 'Эксперименты') #график
ax.plot(R, T, linestyle="None", marker='o', color="b") #график





#plt.errorbar(U, I, yerr=yerr, fmt='None', ecolor='red')


plt.xlim(180000, 960000)
plt.ylim(0.01, 0.078)

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

fig.savefig("f(R).png") #сохранение