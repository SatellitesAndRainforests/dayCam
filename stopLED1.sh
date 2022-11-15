#!/bin/bash
led1Status=$(</home/pi/dayCam/led1Status.txt)
if [ $led1Status != "status:on" ]
then
	echo "LED 1 is not on"
	echo $led1Status
	echo "exiting status code:1"
	exit 1
else
	echo "Turning LED 1 off"
	python3 /home/pi/dayCam/programs/led1off.py
	exitCode=$?
	if [ $exitCode -eq 0 ]
	then
		echo "LED 1 set to off"
		echo "status:off " > '/home/pi/dayCam/led1Status.txt'
	else
		echo "** could not stop led 1 **"
		echo "status:error"
		echo "** should reboot **"
		echo "status:error" > '/home/pi/dayCam/led1Status.txt'
	fi
fi

