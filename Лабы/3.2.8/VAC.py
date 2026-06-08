import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки


I = [1.68, 3.455, 4.171, 4.568, 5.505, 6.927, 8.618, 10.455, 11.760, 13.52, 16.158]
U = [83.4, 90.5, 93.7, 95.7, 101.18, 108.98, 116.97, 127.04, 134.04, 143.16, 157.01]


ax.set_xlabel(r"$U, В$", fontsize=12.5)
ax.set_ylabel(r"I, А", fontsize=12.5)
ax.set_title(r"$I=f(U)$", fontsize=15)#название графика

ax.xaxis.set_minor_locator(plt.MultipleLocator(2)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.4))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

#ax.plot(U, f(U), linestyle="-", marker='None', color="b") #график
ax.plot(U, I, linestyle="None", marker='o', color="b") #график





#plt.errorbar(U, I, yerr=yerr, fmt='None', ecolor='red')


plt.xlim(80, 160)
plt.ylim(1.2, 16.8)

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

# ax.legend()

fig.savefig("VAC.png") #сохранение