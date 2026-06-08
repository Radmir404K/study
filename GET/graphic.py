import numpy as np
import matplotlib.pyplot as plt

with open("settings.txt", "r") as data: 
    tmp = [float(i) for i in data.read().split("\n")]

data_array = np.loadtxt("data.txt", dtype = int)

fig, ax = plt.subplots(figsize = (16, 10), dpi=400) #настройка картинки

x = np.arange(0, len(data_array))

ax.set_xlim(0, 10) #оси
ax.set_ylim(0, 3.5)
ax.set_xlabel("Время, с", fontsize=10)
ax.set_ylabel("Напряжение, В", fontsize=10)

ax.set_title("Зависимость напряжения на RC-цепи от времени", fontsize=15)#название графика

xi = np.arange(0, max(x), 20)
yi = np.interp(xi, x, data_array)

markers=np.arange(0, max(x), 20)

ax.plot(x * tmp[1], data_array * tmp[0], '-o', markevery=markers, color = 'green', label='V(t)') #график


ax.legend(loc='best', fontsize='x-large') #легенда

ax.xaxis.set_minor_locator(plt.MultipleLocator(0.2)) #ticks
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
plt.tick_params(axis='both', which='major', direction='inout', length=10)
plt.tick_params(axis='both', which='minor', direction='inout', length=6)

ax.grid(which='major', linestyle='-') #сетка
ax.grid(which='minor', linestyle='--')

ax.text(8.0, 3.1, 'Время заряда = {} c'.format(round(np.argmax(data_array) * tmp[1], 2)), fontsize='x-large') #текст на графике
ax.text(8.0, 2.9, 'Время разряда = {} c'.format(round(len(data_array) * tmp[1] - np.argmax(data_array) * tmp[1], 2)), fontsize='x-large')

fig.savefig("test.svg") #сохранение
