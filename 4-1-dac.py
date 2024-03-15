import RPi.GPIO as GPIO

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

try:
    while True:
        num = input("Input number: ")
        try:
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, dec_to_bin(num))
                voltage = float(num)/256.0*3.3
                print(f"Output voltage is {voltage:.4} volt") 
                
            else:
                if num < 0 or num > 255: print("Wrong number")
        except Exception:
            if num == "q": break
            print("sring type inputed")
finally: 
    GPIO.output(dac,0)
    GPIO.cleanup()
    print("EOP")