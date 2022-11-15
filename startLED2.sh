#!/bin/bash
led2Status=$(</home/pi/dayCam/led2Status.txt)
if [ $led2Status == "status:off" ]
then 
	echo "$led2Status"
	echo "status is off: starting led 2"
	sudo nohup python3 /home/pi/dayCam/programs/led2on.py &
	echo "status:on" > '/home/pi/dayCam/led2Status.txt'
else 
	echo "led 2 is not off"
	echo "$led2Status"
	echo "exiting status code:1"
	exit 1
fi
