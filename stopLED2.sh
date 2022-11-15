#!/bin/bash
led2Status=$(</home/pi/dayCam/led2Status.txt)
if [ $led2Status != "status:on" ]
then
	echo "LED 2 is not on"
	echo $led2Status
	echo "exiting status code:1"
	exit 1
else
	echo "Turning LED 2 off"
	python3 /home/pi/dayCam/programs/led2off.py
	exitCode=$?
	if [ $exitCode -eq 0 ]
	then
		echo "LED 2 set to off"
		echo "status:off " > '/home/pi/dayCam/led2Status.txt'
	else
		echo "** could not stop led 2 **"
		echo "status:error"
		echo "** should reboot **"
		echo "status:error" > '/home/pi/dayCam/led2Status.txt'
	fi
fi

