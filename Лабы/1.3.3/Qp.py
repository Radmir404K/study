import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x1 = [21, 27, 37, 45, 55, 65, 75]
y1 = [0.025, 0.032, 0.043, 0.053, 0.064, 0.074, 0.085]

x2 = [98, 103, 121, 158, 199, 222, 243]
y2 = [0.095, 0.096, 0.103, 0.115, 0.127, 0.136, 0.142]

kef = 9.8067 * 0.2 * 0.9932
for i in range(7):
    x1[i] = x1[i] * kef
for i in range(7):
    x2[i] = x2[i] * kef

t= np.polyfit(x1, y1, 1)
f = np.poly1d(t)

ax.set_xlim(30, 500) #оси
ax.set_ylim(0.02, 0.15)

ax.set_xlabel(r"$\Delta$P, Па", fontsize=12.5)
ax.set_ylabel(r"Q, л/с", fontsize=12.5)
ax.set_title(r"Зависимость Q($\Delta$P)", fontsize=15)#название графика

m=[20, 160]
ax.plot(x1, y1, linestyle="None", marker='o', color="b") #график
ax.plot(m, f(m), color="green")
ax.plot(x2, y2, marker="o", linestyle="None", color="b")

ax.xaxis.set_minor_locator(plt.MultipleLocator(10)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.002))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

avgx= mean(x1)
avgy=mean(y1)
x_2 =[0, 0, 0, 0, 0, 0, 0]
y_2=[0, 0, 0, 0, 0, 0, 0]
for i in range(7):
    x_2[i]=x1[i]**2
for i in range(7):
    y_2[i]=y1[i]**2
avgx2=mean(x_2)
avgy2=mean(y_2)
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-0.0005708**2)/7)**0.5
print(sigma/0.0005708)

ax.text(50, 0.138, "f =", fontsize="x-large")
ax.text(60, 0.138, f)

fig.savefig("QP1.png") #сохранение