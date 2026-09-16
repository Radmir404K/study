import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [910, 1030, 1140, 1240, 1350, 1450, 1560, 1680, 1780, 1890, 1990]

y = [0.0006748, 0.0009468, 0.00126191, 0.00175212, 0.00224764, 0.00300105, 0.00364056, 0.00419925, 0.00554152, 0.0061177, 0.00961995]

for i in range(len(x)):
    x[i] = np.log(x[i])
    y[i] = np.log(y[i])


yerr = [10, 21, 10, 9, 19, 15, 30, 9, 28, 9, 13, 13, 11, 9]
    

ax.set_xlabel(r"ln T", fontsize=12.5)
ax.set_ylabel(r"ln W", fontsize=12.5)
#ax.set_title(r"$r^2=f(m)$", fontsize=15)#название графика

t= np.polyfit(x, y, 1) #аппроксимация
f = np.poly1d(t)

ax.xaxis.set_minor_locator(plt.MultipleLocator(0.02)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(x, f(x), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график

#plt.errorbar(x, y, yerr=yerr, fmt='None', ecolor='b')#кресты погрешностей на графике

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