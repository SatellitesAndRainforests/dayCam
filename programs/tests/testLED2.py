import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)

GPIO.output(20, GPIO.HIGH)
sleep(5)
GPIO.output(20, GPIO.LOW)

GPIO.cleanup()



