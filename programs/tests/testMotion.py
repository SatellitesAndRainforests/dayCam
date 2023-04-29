from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#GPIO.setup(25, GPIO.IN)
GPIO.setup(16, GPIO.IN)

while True:
    i = GPIO.input(16)
    if i==1:
        print(" --- Motion Detected --- ")
        sleep(0.3);
