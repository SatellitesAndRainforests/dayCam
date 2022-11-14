from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

while True:
    i = GPIO.input(17)
    if i==1:
        print(" --- Motion Detected --- ")
        sleep(1);
