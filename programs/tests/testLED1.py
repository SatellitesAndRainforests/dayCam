import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

GPIO.output(21, GPIO.HIGH)
sleep(5)
GPIO.output(21, GPIO.LOW)

GPIO.cleanup()



