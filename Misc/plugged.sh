#!/bin/bash

while [ True ]
do
    FULL="PLUGGED_AC"
    VAR3="$(termux-battery-status | grep plugged | cut -d ':' -f 2 | cut -d ',' -f 1 | cut -d '"' -f 2)"
    ALLOW=TRUE
    if [[ "$VAR3" = "$FULL" ]]; then
        if [[ $ALLOW ]]
            termux-tts-speak "Charger connected"
            $ALLOW = FALSE
        fi
    else
        ALLOW=TRUE
        sleep 1
       
    fi
done
