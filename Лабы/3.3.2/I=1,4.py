import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки


I = [8.35, 20.54, 33.68, 51.02, 67.74, 90.03, 112.1, 132.3, 156.23, 182.65, 207.11, 238.09, 297.2, 360.11, 430.95, 501.06, 966.1, 1490.7, 2105.5, 2770.2, 3489.1, 4254.7, 5144, 6019]
U = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 7, 8, 9, 10, 15, 20, 25, 30, 35, 40, 45, 50]

for i in range(len(U)):
    U[i] = U[i] ** 1.5

for i in range(len(I)):
    I[i] = I[i] * 0.000001

ax.set_xlabel(r"$U^{3/2}, В^{3/2}$", fontsize=12.5)
ax.set_ylabel(r"I, А", fontsize=12.5)
ax.set_title(r"$I=f(U^{3/2})$", fontsize=15)#название графика

ax.xaxis.set_minor_locator(plt.MultipleLocator(1)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.00002))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

t= np.polyfit(U, I, 1) #аппроксимация
f = np.poly1d(t)

#ax.plot(U, f(U), linestyle="-", marker='None', color="b") #график
ax.plot(U[:16], I[:16], linestyle="None", marker='o', color="b") #график

print(f)


yerr = []
for i in range(len(I)):
    yerr.append(I[i] * 0.02)

#plt.errorbar(U, I, yerr=yerr, fmt='None', ecolor='red')


plt.xlim(-1, 33)
plt.ylim(-0.00002, 0.00052)

x1 = U
y1 = I
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
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-(1.698*10**(-5))**2)/(len(x1)))**0.5
print(sigma)
print(sigma/(1.698*10 **(-5)))
print(f)

# ax.legend()

fig.savefig("I=1,4.png") #сохранение