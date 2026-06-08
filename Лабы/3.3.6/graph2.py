import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки


B = [0.072, 0.265, 0.315, 0.35, 0.38]
I = [0.07, 0.28, 0.35, 0.42, 0.56]
U = [0.842, 2.177, 2.684, 3.035, 3.45]
R = []

for i in range(len(B)):
    B[i] = B[i] ** 2

I1 = [0.07, 0.14, 0.21, 0.28, 0.35, 0.42, 0.49, 0.56]
U1 = [0.676, 0.720, 0.783, 0.84, 0.886, 0.918, 0.939, 0.956]
R1 = []

I2 = [0.07, 0.14, 0.21, 0.28, 0.35, 0.42, 0.49, 0.56]
U2 = [0.7, 0.808, 0.945, 1.091, 1.206, 1.278, 1.332, 1.365]
R2 = []

for i in range(len(U1)):
    R1.append(U1[i]/10)

for i in range(len(U2)):
    R2.append(U2[i]/10)

for i in range(len(U)):
    R.append(U[i]/23.5)
ax.set_xlabel(r"$I_{м}$, мА", fontsize=12.5)
ax.set_ylabel(r"R, Ом", fontsize=12.5)
ax.set_title(r"$R=f(I_{м})$", fontsize=15)#название графика

#ax.xaxis.set_minor_locator(plt.MultipleLocator(0.02)) #ticks
#ax.yaxis.set_minor_locator(plt.MultipleLocator(0.004))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

t= np.polyfit(B, R, 1) #аппроксимация
f = np.poly1d(t)

t1 = np.polyfit(I1[:4], R1[:4], 1) #аппроксимация
f1 = np.poly1d(t1)

t2 = np.polyfit(I2[:4], R2[:4], 1) #аппроксимация
f2 = np.poly1d(t2)

#ax.plot(I1, R1, linestyle="None", marker='o', color="g", label = "Пластинка(перпендикулярно)") #график
#ax.plot(I1, f1(I1), linestyle="-", marker='None', color="g") #график

ax.plot(B, R, linestyle="None", marker='o', color="b", label = "Диск") #график
ax.plot(B, f(B), linestyle="-", marker='None', color="b") #график

#ax.plot(I2, R2, linestyle="None", marker='o', color="r", label = "Пластинка(вдоль)") #график
#ax.plot(I2, f2(I2), linestyle="-", marker='None', color="r") #график

#plt.xlim(0.06, 0.6)
#plt.ylim(0.028, 0.172)

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

ax.legend()


fig.savefig("graph2.png") #сохранение