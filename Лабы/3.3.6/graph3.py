import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

I1 = [0.07, 0.14, 0.21, 0.28, 0.35, 0.42, 0.49, 0.56]
U1 = [0.676, 0.720, 0.783, 0.84, 0.886, 0.918, 0.939, 0.956]
R1 = []

for i in range(len(U)):
    R1.append(U[i]/10)
ax.set_xlabel(r"$I_{м}$, мА", fontsize=12.5)
ax.set_ylabel(r"R, Ом", fontsize=12.5)
ax.set_title(r"$R=f(I_{м})$", fontsize=15)#название графика

ax.xaxis.set_minor_locator(plt.MultipleLocator(0.02)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.001))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

t1 = np.polyfit(I1[:4], R1[:4], 1) #аппроксимация
f1 = np.poly1d(t)

ax.plot(I1, R1, linestyle="None", marker='o', color="b", label = "эксперименты") #график
ax.plot(I1, f1(I1), linestyle="-", marker='None', color="r", label = "теория") #график

plt.xlim(0.06, 0.58)
plt.ylim(0.066, 0.107)

x1 = I
y1 = R
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
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-0.2711**2)/(len(x1)+1))**0.5
print(sigma)
print(sigma/0.2711)
print(f)

#ax.legend()


fig.savefig("graph3.png") #сохранение