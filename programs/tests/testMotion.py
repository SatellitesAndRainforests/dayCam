from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)

while True:
    i = GPIO.input(25)
    if i==1:
        print(" --- Motion Detected --- ")
        sleep(0.3);
