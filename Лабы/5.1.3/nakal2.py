import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [0.379,
0.46,
0.649,
0.846,
1.613,
1.818,
2.045,
2.248,
2.535,
2.978,
3.23,
3.737,
4.039,
4.542,
4.864,
0.909,
0.968,
1.053,
1.291,
1.408,
5.326,
5.827,
6.152,
6.554,
6.773,
7.101,
7.633,
7.94,
8.627,
9.121,
9.465,
9.837,
10.219,
10.725,
11.304,
]

y = [
2.6,
5.7,
20.4,
47.4,
158.85,
155.09,
142.21,
135.49,
114.05,
87.27,
76.41,
62.24,
56.46,
49.61,
46.33,
66.58,
79.39,
97.2,
138.27,
150.26,
43.61,
42.43,
41.8,
41.69,
42.14,
42.97,
44.64,
46.53,
50.86,
55.58,
62.18,
67.26,
70.75,
80.01,
91.23,

]

for i in range(len(y)):
    y[i] = y[i]/100000


yerr = [10, 21, 10, 9, 19, 15, 30, 9, 28, 9, 13, 13, 11, 9]
    

ax.set_xlabel(r"$V_{кат}$, В", fontsize=12.5)
ax.set_ylabel(r"$I_{ан}$, мА", fontsize=12.5)
#ax.set_title(r"$r^2=f(m)$", fontsize=15)#название графика

t= np.polyfit(x, y, 1) #аппроксимация
f = np.poly1d(t)

ax.xaxis.set_minor_locator(plt.MultipleLocator(0.4)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.00004))
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


fig.savefig("nakal2.png") #сохранение