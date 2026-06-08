import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

phi0 = 48716
phii = 696295
phi1 = [6248, 3106, 1293248, 1287183, 1283805, 1283568, 1279916, 1278819, 90610, 741905, 747771, 753420, 756693, 756908, 760481, 761605]
lambda1 = [404.7, 435.8, 491.6, 546.1, 577.0, 579.1, 623.4, 690.7, 404.7, 435.8, 491.6, 546.1, 577.0, 579.1, 623.4, 690.7]

for i in range(len(phi1)):
    if i == 0 or i == 1:
        phi1[i] =math.sin((phi0 - phi1[i])/206265)

    elif i == 8:
        phi1[i] =math.sin((phi1[i] - phi0)/206265)
    
    elif 1 < i < 8: 
        phi1[i] = math.sin((1296000 - phi1[i] + phi0)/206265)

    elif i > 8:
        phi1[i] = math.sin((phi1[i] - phii)/206265)

    lambda1[i] = lambda1[i] * 10**(-9)

ax.set_xlabel(r"$\lambda$, м", fontsize=12.5)
ax.set_ylabel(r"sin$\varphi$", fontsize=12.5)
ax.set_title(r"sin$\varphi$ = $\frac{\lambda}{d}$", fontsize=15)#название графика

ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1 * 10**(-7))) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.004))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

t= np.polyfit(lambda1[:6], phi1[:6], 1) #аппроксимация
f = np.poly1d(t)

ax.plot(lambda1, f(lambda1), linestyle="-", marker='None', color="b") #график
ax.plot(lambda1[:8], phi1[:8], linestyle="None", marker='o', color="b") #график
ax.plot(lambda1[8:], phi1[8:], linestyle="None", marker='o', color="r") #график

print(f)




#plt.errorbar(U, I, yerr=yerr, fmt='None', ecolor='red')


plt.xlim(3.9 * 10 ** (-7), 7 * 10 **(-7))
plt.ylim(0.2, 0.32)

x1 = lambda1[:len(phi1) - 2]
y1 = phi1[:len(phi1) - 2]
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
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-(5.049*10**(5))**2)/(len(x1)))**0.5
print(sigma)
print(sigma/(5.049 * 10 **(5)))

# ax.legend()

fig.savefig("graph1'.png") #сохранение