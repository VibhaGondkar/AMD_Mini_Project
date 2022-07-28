#!/bin/bash
#nmon -f -s 30 -c 20
cd


#./MonteCarlo $1 $2 $3 $4  > results_"$(date +"%Y_%m_%d_%I_%M_%p").log"

echo $1
echo $2
echo $3
echo $4




# sleep for 30 mins

#sleep 2000
#cp *.nmon /test_mount
#cp results_* /test_mount
#ps -ef | grep nmon | grep -v grep | awk '{print $2}' | xargs kill