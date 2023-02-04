#!/bin/bash

city=$1

add=$2

if [[ $add = long ]]
then
	curl wttr.in/$city?2n 

else
	curl wttr.in/$city?0n

fi

