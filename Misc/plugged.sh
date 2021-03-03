#!/bin/bash


while [ True ]
do
    YES="PLUGGED_AC"
    NOT="UNPLUGGED"
    VAR1="$(termux-battery-status | grep plugged | cut -d ':' -f 2 | cut -d ',' -f 1 | cut -d '"' -f 2)"
    
    
    if [[ "$VAR1" -eq "$YES" ]]; then
        echo "CHARGER CONNECTED"
    elif [[ "$VAR1" -eq "$NOT" ]]; then
        echo "NOT CONNECTED"
    fi
    
    
done
