import os
import Adafruit_DHT
import time
from datetime import datetime
# import board
import RPi.GPIO as GPIO
from time import sleep

# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# PIR
GPIO.setup(17, GPIO.IN)

# DHT22
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_GPIO_PIN = 18

#Flash
GPIO.setup(23, GPIO.OUT)

flashOn = False

# Base-line new moon used in modulos function
baseline_new_moon = datetime(2022, 2, 1)    # There was a new moon on this date at 00:46am.



def useFlash():
    with open("/home/pi/dayCam/useFlash.txt", "r") as flashFile:
        global flashOn 
        flashOn = flashFile.readline().strip()
        write_to_log("flash is on: " + flashOn)



def capture_image():

    tstart = datetime.now()

    cameraCommand = ('libcamera-still '
                '--autofocus '
                '-o /home/pi/dayCam/programs/tests/case.jpg')
    os.system( cameraCommand )

    tend = datetime.now()
    print()
    print("Camera time from start to finish:")
    print(tend - tstart)
    print()




def main():

    try:
        capture_image()

    except KeyboardInterrupt:
        write_to_log(" --- Keyboard Interrupt --- ")
    except:
        write_to_log(" --- except --- ")
    finally:
        write_to_log(" --- GPIO cleanup ---")
        GPIO.cleanup()
        write_to_log(" --- Finally ---")
        write_status_to_file("status:idle")
        raise SystemExit(0)

main()













