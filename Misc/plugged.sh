#!/bin/bash

while [ True ]
do
    FULL="PLUGGED_AC"
    VAR3="$(termux-battery-status | grep plugged | cut -d ':' -f 2 | cut -d ',' -f 1 | cut -d '"' -f 2)"

    if [[ "$VAR3" -ne "$FULL" ]]; then
        echo "Not plugged"
    elif [[ "$VAR3" -eq "$FULL" ]]; then
        echo "Cable connected"
    fi
done
