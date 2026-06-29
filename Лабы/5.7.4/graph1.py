import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

y = [152, 169, 131, 140, 144, 149, 130, 129, 155, 142]
yerr = [12, 13 , 11, 12, 12, 12, 11, 11, 12, 12]
    

ax.set_xlabel(r"$N_{эксп}$", fontsize=12.5)
ax.set_ylabel(r"$N_{имп}$", fontsize=12.5)
#ax.set_title(r"$r^2=f(m)$", fontsize=15)#название графика

t= np.polyfit(x, y, 1) #аппроксимация
f = np.poly1d(t)

#ax.xaxis.set_minor_locator(plt.MultipleLocator(0.02)) #ticks
#ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
#ax.plot(x, f(x), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график

plt.errorbar(x, y, yerr=yerr, fmt='None', ecolor='b')#кресты погрешностей на графике

#plt.xlim(0.8, 5.2)
#plt.ylim(7, 44)

ax.legend()
print(f)

x1 = x[2:]
y1 = y[2:]
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
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-(3.236)**2)/(len(x1)))**0.5
print(sigma)#абсолютная погрешность
print(sigma/(3.236))#относительная погрешность


fig.savefig("graph1.png") #сохранение