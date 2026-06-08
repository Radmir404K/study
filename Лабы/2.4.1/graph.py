import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x1 = [1/293.88, 1/295.05, 1/296.06, 1/297.06, 1/298.07, 1/299.07, 1/300.05, 1/301.05, 1/302.03, 1/303.04, 1/304.06, 1/305.06, 1/306.04, 1/307.05, 1/308.04, 1/309.04, 1/310.05]
y1 = [3211.10, 3450.94, 3597.50, 3717.42, 3943.93, 4050.52, 4277.03, 4443.58, 4603.47, 4816.65, 5116.45, 5296.32, 5795.97, 5929.22, 6169.05, 6408.88, 6688.69]

x2 = [1/309.03, 1/308.02, 1/307.01, 1/306.02, 1/305.04, 1/304.03, 1/303.03, 1/302.03, 1/301.04, 1/300.03, 1/299.04, 1/298.04, 1/297.05, 1/296.03, 1/295.07, 1/294.07]
y2 = [6748.65, 6455.52, 6215.68, 5922.55, 5622.76, 5369.60, 5129.77, 4903.26, 4650.10, 4443.58, 4223.73, 3997.22, 3877.31, 3684.11, 3517.56, 3357.69]

for i in range(len(y1)):
    y1[i] = np.log(y1[i])


for i in range(len(y2)):
    y2[i] = np.log(y2[i])

t= np.polyfit(x1, y1, 1)
f = np.poly1d(t)

t2= np.polyfit(x2, y2, 1)
f2 = np.poly1d(t2)

ax.set_xlabel(r"1/T, $K^{-1}$", fontsize=12.5)
ax.set_ylabel(r"ln P", fontsize=12.5)
ax.set_title(r"Зависимость ln P от 1/T", fontsize=15)#название графика


ax.plot(x1, y1, linestyle="None", marker='o', color="r") #график
ax.plot(x1, f(x1), color="r")

ax.plot(x2, y2, linestyle="None", marker='o', color="b") #график
ax.plot(x2, f2(x2), color="b")


ax.xaxis.set_minor_locator(plt.MultipleLocator(0.000005)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.02))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

plt.xlim(0.003220, 0.003410)
#plt.ylim(2.8, 7.6)

ax.text(0.003368, 8.75, "f =", fontsize="xx-large")
ax.text(0.003375, 8.75, f, fontsize='xx-large')

ax.text(0.003368, 8.65, "f =", fontsize="xx-large")
ax.text(0.003375, 8.65, f2, fontsize='xx-large')

avgx= mean(x1)
avgy=mean(y1)
x_2 =[0] * len(x1)
y_2=[0] * len(x1)
for i in range(len(x1)):
    x_2[i]=x1[i]**2
for i in range(len(x1)):
    y_2[i]=y1[i]**2
avgx2=mean(x_2)
avgy2=mean(y_2)
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-4135**2)/(len(x1)+1))**0.5
print(sigma/4135)

avgx= mean(x2)
avgy=mean(y2)
x_2 =[0] * len(x2)
y_2=[0] * len(x2)
for i in range(len(x2)):
    x_2[i]=x2[i]**2
for i in range(len(x2)):
    y_2[i]=y2[i]**2
avgx2=mean(x_2)
avgy2=mean(y_2)
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-4288**2)/(len(x2)+1))**0.5
print(sigma/4288)

fig.savefig("graph.png") #сохранение