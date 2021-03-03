#!/bin/bash


while [ True ]
do
    YES="PLUGGED"
    VAR1="$(termux-battery-status | grep plugged | cut -d ':' -f 2 | cut -d ',' -f 1 | cut -d '"' -f 2)"
    echo $YES
    echo $VAR1
done
