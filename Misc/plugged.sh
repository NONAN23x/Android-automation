#!/bin/bash


FIFTY="UNPLUGGED"
FULL="PLUGGED_AC"
VAR3="$(termux-battery-status | grep plugged | cut -d ':' -f 2 | cut -d ',' -f 1 | cut -d '"' -f 2)"

if [[ "$VAR3" -eq "$FIFTY" ]]; then
    termux-tts-speak "Please connect the charger"
elif [[ "$VAR3" -eq "$FULL" ]]; then
    termux-tts-speak "Charger connected"
fi
