#!/bin/bash
dayCamStatus=$(</home/pi/dayCam/dayCamStatus.txt)
if [ "$dayCamStatus" == "status:idle" ] 
then
	echo "$dayCamStatus"
	echo "status is idle: starting automated day camera capturing"
	sudo pkill python3
	sudo nohup python3 /home/pi/dayCam/programs/dayWatch.py &
else 
	echo "dayCam is not idle"
	echo "$dayCamStatus"
	echo "exiting status code:1"
	exit 1
fi

