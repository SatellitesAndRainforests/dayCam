#!/bin/bash
#sudo pkill -9 -f dayWatch.py     # is giving a 137 out of memoury exit code ?

dayCamStatus=$(</home/pi/dayCam/dayCamStatus.txt)

if [ $dayCamStatus != "status:capturing" ] 
then
	echo "Automated capturing is not running."
	echo $dayCamStatus
	echo "exiting status code:1"
	exit 1
fi

# kill's everythin python3
sudo pkill python3
exitCode1=$?
python3 /home/pi/dayCam/programs/cleanGPIOs.py
exitCode2=$?

if [ $exitCode1 -eq 0 -a $exitCode2 -eq 0 ] 
then
	echo "dayCam has stopped automated capturing"
       	echo "status:idle"
	echo "status:idle" > '/home/pi/dayCam/dayCamStatus.txt'
	echo "status:off" > '/home/pi/dayCam/led1Status.txt'
	echo "status:off" > '/home/pi/dayCam/led2Status.txt'
else
	echo "** could not stop automated capturing **"
	echo "status:error"
	echo "should reboot"
	echo "status:error" > '/home/pi/dayCam/dayCamStatus.txt'
	echo "status:error" > '/home/pi/dayCam/led1Status.txt'
	echo "status:error" > '/home/pi/dayCam/led2Status.txt'
fi
