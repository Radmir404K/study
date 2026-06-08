import numpy as np
import matplotlib.pyplot as plt
from statistics import mean
import math

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

nu = [0.021, 0.01, 0.0066, 0.0046, 0.0034, 0.0026, 0.0022]
tau = [0.00002, 0.00005, 0.00008, 0.00011, 0.00014, 0.00017, 0.0002]

for i in range(len(nu)):
    tau[i] = 1/tau[i]

ax.set_xlabel(r"$1/\tau$", fontsize=12.5)
ax.set_ylabel(r"$\nu$", fontsize=12.5)
ax.set_title(r"$\nu=f(1/\tau)$", fontsize=15)#название графика

ax.xaxis.set_minor_locator(plt.MultipleLocator(2000)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.0005))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

t= np.polyfit(tau, nu, 1) #аппроксимация
f = np.poly1d(t)

ax.plot(tau, f(tau), linestyle="-", marker='None', color="b") #график
ax.plot(tau, nu, linestyle="None", marker='o', color="b") #график

print(f)




#plt.errorbar(U, I, yerr=yerr, fmt='None', ecolor='red')


plt.xlim(4000, 52000)
plt.ylim(0.0015, 0.0225)

x1 = tau
y1 = nu
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
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-(4.147*10**(-7))**2)/(len(x1)))**0.5
print(sigma)
print(sigma/(4.147 **(-7)))

# ax.legend()

fig.savefig("f1.png") #сохранение