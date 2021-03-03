#!/bin/bash

while [ True ]
do
    FULL="PLUGGED_AC"
    VAR3="$(termux-battery-status | grep plugged | cut -d ':' -f 2 | cut -d ',' -f 1 | cut -d '"' -f 2)"
    ALLOW=TRUE
    if [[ "$VAR3" = "$FULL" ]]; then
        echo "Charger Connected"
        termux-tts-speak "Charger Connected"
        sleep 2
    else
        echo "Charget not Connected"
        sleep 2
       
    fi
done
