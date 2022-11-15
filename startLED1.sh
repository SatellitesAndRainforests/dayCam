#!/bin/bash
led1Status=$(</home/pi/dayCam/led1Status.txt)
if [ $led1Status == "status:off" ]
then 
	echo "$led1Status"
	echo "status is off: starting led 1"
	sudo nohup python3 /home/pi/dayCam/programs/led1on.py &
	echo "status:on" > '/home/pi/dayCam/led1Status.txt'
else 
	echo "led 1 is not off"
	echo "$led1Status"
	echo "exiting status code:1"
	exit 1
fi
