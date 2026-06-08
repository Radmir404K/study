import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
comp = 4
troyka = 17
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)
maxVoltage = 3.3
levels = 256


def decimal2binary(value):
    return [int (element) for element in bin(value)[2:].zfill(8)]

def adc():
    R = 7
    value = 0
    while R > -1:
        value += 2**R
        GPIO.output(dac, decimal2binary(value))
        time.sleep(0.0007)
        comparatorValue = GPIO.input(comp)
        if comparatorValue == 0:
            value -= 2**R
        R -= 1
    return value


try:
    while True:
        value = adc()
        voltage = value / levels * maxVoltage
        print("ADC voltage = {:.2f} -> {}".format(voltage, value))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()