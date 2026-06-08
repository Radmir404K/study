import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [7.539,
7.025,
6.593,
5.948,
5.305,
4.69,
4.414,
4.09,
0.385,
1.057,
0.75,
1.088,
1.372,
1.736,
1.97,
2.173,
2.524,
2.896,
3.292,
3.801,
8.047,
8.623,
9.091,
9.665,
10.202,
10.662,
11.285,
11.756,
0.522,
0.673,
0.886,
1.436,
1.325,
1.196,
1.536,
]

y = [104.6,
99.8,
97.2,
94.5,
93.8,
97.2,
100.2,
104.1,
6.5,
117.85,
51.92,
123.93,
167.4,
182.5,
176.3,
167,
148.9,
132.7,
120,
108.9,
112.8,
121,
129.9,
151.4,
166.7,
183.7,
214.3,
242.1,
17.1,
37.7,
80.7,
172.3,
161.9,
143.8,
178.4,
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
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.0001))
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


fig.savefig("nakal1.png") #сохранение