import csv
import openpyxl
from tkinter import Y
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = [190, 210, 220]
y = [465, 590, 1175]

#yerr = [10, 21, 10, 9, 19, 15, 30, 9, 28, 9, 13, 13, 11, 9]
    

ax.set_xlabel(r"энергия обратного рассеяния", fontsize=12.5)
ax.set_ylabel(r"энергия фотопика", fontsize=12.5)
#ax.set_title(r"$r^2=f(m)$", fontsize=15)#название графика


t= np.polyfit(x, y, 1) #аппроксимация
f = np.poly1d(t)

ax.xaxis.set_minor_locator(plt.MultipleLocator(1)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(20))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.plot(x, y, linestyle="None", marker='o', color="b", label = "эксперименты") #график
#ax.plot(x, f(x), linestyle="-", marker='None', color="r", label = "Аппроксимация") #график

#plt.errorbar(x, y, yerr=yerr, fmt='None', ecolor='b')

#plt.xlim(0.8, 5.2)
#plt.ylim(7, 44)

ax.legend()
print(f)

#x1 = x[2:]
#y1 = y[2:]
#avgx= mean(x1)
#avgy=mean(y1)
#x_2 =[0] * len(x1)
#y_2=[0] * len(y1)
#for i in range(len(x1)):
#    x_2[i]=x1[i]**2
#for i in range(len(x1)):
#    y_2[i]=y1[i]**2
#avgx2=mean(x_2)
#avgy2=mean(y_2)
#sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-(443)**2)/(len(x1)))**0.5
#print(sigma)
#print(sigma/(443))


fig.savefig("piki.png") #сохранение