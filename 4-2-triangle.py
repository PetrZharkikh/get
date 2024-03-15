import RPi.GPIO as GPIO
from time import sleep

def dec_to_bin(num):
    a = [0, 0, 0, 0, 0, 0, 0, 0]
    i=7
    while num>0:
        a[i] = num % 2
        num //= 2
        i-=1
    return a

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

flag = 1
t = 0
x = 0

try:
    period = float(input("input period: "))

    while True:
        GPIO.output(dac, dec_to_bin(x))

        if x==0: flag = 1
        if x==255: flag = 0

        if flag == 1: x+=1
        else: x-=1

        sleep(period/512)
        t+=1
except ValueError:
    print("wrong period")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")
