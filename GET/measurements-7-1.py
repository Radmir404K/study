
import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM) #настройка пинов и объявление переменных
dac = [26, 19, 13, 6, 5, 11, 9, 10]
measurements = []
GPIO.setup(dac, GPIO.OUT)
comp = 4
troyka = 17
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
maxVoltage = 3.3
levels = 256
value = 0

def decimal2binary(value):
    return [int (element) for element in bin(value)[2:].zfill(8)]

def adc(): #функция для опредления напряжения на конденсаторе
    R = 7
    value = 0
    while R > -1:
        value += 2**R
        GPIO.output(dac, decimal2binary(value))
        time.sleep(0.0005)
        comparatorValue = GPIO.input(comp)
        if comparatorValue == 0:
            value -= 2**R
        R -= 1
    return value

try:
    exp_start = time.time()
    GPIO.output(troyka, 1) #заряжаем конденсатор
    while value < 247:
        value = adc()
        measurements.append(value)
        print(value)
    
    GPIO.output(troyka, 0) #разряжаем конденсатор
    while value > 5:
        value = adc()
        measurements.append(value)
        print(value)
    expt = time.time() - exp_start

    
    size = len(measurements)
    discr = round(size / expt, 3) #дискретизация
    period = round(expt/size, 3) #период
    
    measurements_str = [str(item) for item in measurements] #запись измерений в файл
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(measurements_str))
    
    quant = round(3.3 / 256, 3)
    with open("settings.txt", "w") as outfile: #запись в файл settings
        outfile.write("\n period = {} s".format(period))
        outfile.write("\n quant = {}".format(quant))
    
    print(expt)

    plt.plot(measurements) #график
    plt.show()
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()