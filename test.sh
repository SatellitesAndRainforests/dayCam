#!/bin/bash
ledStatus=$(</home/pi/dayCam/led1Status.txt)

echo "$ledStatus"

if [ $ledStatus == "status:off" ]
then 
	echo "$ledStatus"
	echo "if == status:off"
fi

if [ $ledStatus == "status:on" ]
then
	echo "$ledStatus"
	echo "if == status:on"
fi
