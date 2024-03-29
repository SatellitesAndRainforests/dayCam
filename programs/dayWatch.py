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
#GPIO.setup(25, GPIO.IN)
GPIO.setup(16, GPIO.IN)

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


def write_to_log( message ):
    with open("/home/pi/dayCam/log.txt", "a") as log_file:
        print( message + "\n" )
        log_file.write( message + "\n" )


def write_status_to_file( status ):
    with open("/home/pi/dayCam/dayCamStatus.txt", "w") as status_file:
        print( status + "\n" )
        status_file.write( status + "\n" )


def capture_image():

    write_to_log(" --- flash on --- ")
    if (flashOn == "True"): GPIO.output(23, GPIO.HIGH)

    tstart = datetime.now()

    write_to_log(" --- taking photo --- ")

    cameraCommand = ('libcamera-still '
                '--autofocus '   
                '--vflip=yes '   
                '-o /home/pi/dayCam/images/temp/temp.jpg')
    os.system( cameraCommand )

    tend = datetime.now()
    print()
    print("Camera time from start to finish:")
    print(tend - tstart)
    print()

    write_to_log(" --- flash off --- ")
    GPIO.output(23, GPIO.LOW)



def calc_moon_phase():

    now = datetime.now()
    difference = float((now - baseline_new_moon).days) - 0.0319 # Days since baseline new-moon as a float + 46 mins.
                                                                # subtract 46 mins, 3.19% of a day to give whole-days.
    modulos = difference % 29.53    # Subtract all full moon cycles, (29.53 days, Wikipedia)
                                    # remander is the current mooncycle's progress/ phase.
    moonphase = ""

    if (modulos < 1.84 or modulos >= 27.68 ):       # The new-moon will be really noticable if wrong
        # currently ~ +/- 19 hour variation either way.  
        moonphase = "newMoon"                      # Each phase is 29.53 / 8 (for the 8 phases) with the new-moon center = 0

    elif (modulos >= 1.84 and modulos < 5.53):
        moonphase = "cresent(right)"

    elif (modulos >= 5.53 and modulos < 9.22):
        moonphase = "halfMoon(right)"

    elif (modulos >= 9.22 and modulos < 12.91):
        moonphase = "3of4moon(right)"

    elif (modulos >= 12.91 and modulos < 16.61):
        moonphase = "fullMoon"

    elif (modulos >= 16.61 and modulos < 20.30):
        moonphase = "3of4moon(left)"

    elif (modulos >= 20.30 and modulos < 23.99):
        moonphase = "halfMoon(left)" 

    elif (modulos >= 23.99 and modulos < 27.68):
        moonphase = "cresent(left)"

    return moonphase



def add_information_to_filename():

    filename_sensor_data="sensorError"
    file_ext=".jpg"

    moon_phase = calc_moon_phase()

    current_datetime = datetime.now().strftime("%H:%M:%Ss__%d:%m:%Y__")

    for i in range(3):
        try:
            # Will freeze and crash program is not working (fixed ? on 31/12/22 )
            humidity, temperature = Adafruit_DHT.read_retry( DHT_SENSOR, DHT_GPIO_PIN )

            if humidity is not None and temperature is not None:
                filename_sensor_data = "{:.1f}c__{:.1f}h".format(temperature, humidity)
                write_to_log( "Temp: {:.1f} C    Humidity: {:.1f}% ".format(temperature, humidity))
                break
            else:
                write_to_log( "error to retrieve data from dht" )

        except RuntimeError as error:
            # dht errors are common 
            write_to_log(" --- dht error: attempt 1 of 3 --- ")
            write_to_log(error.args[0])
            time.sleep(0.4)
            continue

    new_filename = current_datetime + filename_sensor_data + "__" + moon_phase + file_ext
    old_name=r"/home/pi/dayCam/images/temp/temp.jpg"
    new_name=r"/home/pi/dayCam/images/" + new_filename
    os.rename(old_name, new_name)
    write_to_log (" --- image saved --- " + new_filename)



def main():

    write_status_to_file("status:capturing")
    useFlash()

    try:
        while True:
            i = GPIO.input(16)      # sensor sends 1 for motion, otherwise 0
            if i==1:
                write_to_log(" --- Motion Detected --- ")
                capture_image()
                add_information_to_filename()
                sleep(1)

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













