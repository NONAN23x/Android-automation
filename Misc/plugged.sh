#!/bin/bash

TWENTYFIVE="25"
FIFTY="50"
FULL="99"
VAR3="$(termux-battery-status | grep plugged | cut -d ':' -f 2 | cut -d ',' -f 1)"

if [[ "$VAR3" -eq "$TWENTYFIVE" ]]; then
    termux-tts-speak "My battery is low, please charge immediately"
elif [[ "$VAR3" -eq "$FIFTY" ]]; then
    termux-tts-speak "My battery is 50%"
elif [[ "$VAR3" -eq "$FULL" ]]; then
    termux-tts-speak "Device fuly charged, you may unplug now "
fi
