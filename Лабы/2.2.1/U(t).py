import csv
from tkinter import Y
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

t=[]
t1=[]
t2=[]
U=[]
U1=[]
U2=[]
with open("20220328_1648452379305_40.csv", newline='') as csvfile:
    reader=csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        t.append(float(row['t_(s)']))
        U.append(float(row['V_(mV)']))

with open("20220328_1648453465024_80.csv", newline='') as csvfile:
    reader=csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        t1.append(float(row['t (s)']))
        U1.append(float(row['V (mV)']))

with open("20220328_1648454900585_124.csv", newline='') as csvfile:
    reader=csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        t2.append(float(row['t (s)']))
        U2.append(float(row['V (mV)']))

t.pop(0)
U.pop(0)
t1.pop(0)
U1.pop(0)
t2.pop(0)
U2.pop(0)
for i in range(len(t)):
    U[i]=np.log(U[i])

for i in range(len(t1)):
    U1[i]=np.log(U1[i])

for i in range(len(t2)):
    U2[i]=np.log(U2[i])

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

xapr=[0] * len(t)
yapr=[0] * len(t)
for i in range(len(t)):
    xapr[i - 1]=t[i]
    yapr[i - 1]=U[i]

xapr1=[0] * len(t1)
yapr1=[0] * len(t1)
for i in range(len(t1)):
    xapr1[i - 1]=t1[i]
    yapr1[i - 1]=U1[i]

xapr2=[0] * len(t2)
yapr2=[0] * len(t2)
for i in range(len(t2)):
    xapr2[i - 1]=t2[i]
    yapr2[i - 1]=U2[i]


y= np.polyfit(xapr, yapr, 1) #аппроксимация
f = np.poly1d(y)

y1= np.polyfit(xapr1, yapr1, 1) #аппроксимация
f1 = np.poly1d(y1)

y2= np.polyfit(xapr2, yapr2, 1) #аппроксимация
f2 = np.poly1d(y2)

ax.set_xlabel(r"t, c", fontsize=12.5)
ax.set_ylabel(r"ln U", fontsize=12.5)
ax.set_title(r"Зависимость ln U от t", fontsize=15)#название графика


ax.plot(xapr, f(xapr), color='g')
ax.plot(t, U, linestyle="None", marker='.', color="b") #график

ax.plot(xapr1, f1(xapr1), color='g')
ax.plot(t1, U1, linestyle="None", marker='.', color="y") #график

ax.plot(xapr2, f2(xapr2), color='g')
ax.plot(t2, U2, linestyle="None", marker='.', color="r") #график

ax.xaxis.set_minor_locator(plt.MultipleLocator(0.0004)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.text(348, 2.7, "f =", fontsize="xx-large")
ax.text(366, 2.7, f, fontsize='xx-large')

ax.text(346, 2.6, "f1 =", fontsize="xx-large")
ax.text(366, 2.6, f1, fontsize='xx-large')

ax.text(346, 2.5, "f2 =", fontsize="xx-large")
ax.text(366, 2.5, f2, fontsize='xx-large')

avgx= mean(t)
avgy=mean(U)
x_2 =[0] * len(t)
y_2=[0] * len(t)
for i in range(len(t)):
    x_2[i]=t[i]**2
for i in range(len(t)):
    y_2[i]=U[i]**2
avgx2=mean(x_2)
avgy2=mean(y_2)
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-0.003757**2)/(len(t)+1))**0.5
print(sigma/0.003757)

avgx= mean(t1)
avgy=mean(U1)
x_2 =[0] * len(t1)
y_2=[0] * len(t1)
for i in range(len(t1)):
    x_2[i]=t1[i]**2
for i in range(len(t1)):
    y_2[i]=U1[i]**2
avgx2=mean(x_2)
avgy2=mean(y_2)
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-0.00244**2)/(len(t1)))**0.5
print(sigma/0.00244)

avgx= mean(t2)
avgy=mean(U2)
x_2 =[0] * len(t2)
y_2=[0] * len(t2)
for i in range(len(t2)):
    x_2[i]=t2[i]**2
for i in range(len(t2)):
    y_2[i]=U2[i]**2
avgx2=mean(x_2)
avgy2=mean(y_2)
sigma=(((avgy2 - avgy**2)/(avgx2-avgx**2)-0.001638**2)/(len(t)))**0.5
print(sigma/0.001638)

fig.savefig("U(t)1.png") #сохранение