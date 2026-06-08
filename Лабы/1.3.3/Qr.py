import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x1 = [3.95, 5.25, 5.85]
y1 = [0.026, 0.091, 0.123]

for i in range(3):
    x1[i] = np.log(x1[i])
    y1[i] = np.log(y1[i])


t= np.polyfit(x1, y1, 1)
f = np.poly1d(t)

ax.set_xlabel(r"$ln~ R$", fontsize=12.5)
ax.set_ylabel(r"$ln~ Q$", fontsize=12.5)
ax.set_title(r"Зависимость $Q(R)$", fontsize=15)#название графика

ax.plot(x1, y1, linestyle="None", marker='o', color="b") #график
ax.plot(x1, f(x1), color="green")


plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)


ax.xaxis.set_minor_locator(plt.MultipleLocator(0.01)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.04))
ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

avgx= mean(x1)
avgy=mean(y1)
x_2 =[0, 0, 0]
y_2=[0, 0, 0]
for i in range(3):
    x_2[i]=x1[i]**2
for i in range(3):
    y_2[i]=y1[i]**2
avgx2=mean(x_2)
avgy2=mean(y_2)
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-4.048**2)/7)**0.5
print(sigma)

ax.text(1.36, -2.1, "f =", fontsize="x-large")
ax.text(1.37, -2.1, f, fontsize="x-large")

fig.savefig("Q(r).png") #сохранение