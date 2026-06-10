import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [0,
0.2,
0.4,
0.6,
0.8,
1,
1.2,
1.4,
1.6,
1.8,
2,
2.2,
2.4,
2.6,
2.8,
3,
3.2,
3.4,
3.6,
3.8,
4,
4.05,
4.1,
4.15,
4.2,
4.25,
4.3,
4.35,
4.4,
4.45,
4.5,
4.55,
4.6,
4.65,
4.7,
4.75,
3.95,
]

y = [0.1705,
0.02969932,
-0.0311013600000001,
0.16809796,
0.00729727999999996,
0.3464966,
1.71469592,
3.72389524,
5.61209456,
8.16029388,
9.5094932,
10.60869252,
11.64689184,
10.13709116,
8.90629048,
7.6064898,
6.45568912,
3.46588844,
1.80508776,
0.85528708,
3.3834864,
5.18228623,
7.07208606,
9.98088589,
12.50968572,
13.76948555,
12.94928538,
10.62008521,
8.68988504,
6.52068487,
3.7914847,
2.04128453,
1.02208436,
0.63188419,
0.22168402,
0.00148384999999995,
1.45368657,
]

    

ax.set_xlabel(r"I, A", fontsize=12.5)
ax.set_ylabel(r"N", fontsize=12.5)
#ax.set_title(r"$r^2=f(m)$", fontsize=15)#название графика

t= np.polyfit(x, y, 1) #аппроксимация
f = np.poly1d(t)

ax.xaxis.set_minor_locator(plt.MultipleLocator(0.2)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.4))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
#ax.plot([1, 2500], f([1, 2500]), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график

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


fig.savefig("exp.png") #сохранение