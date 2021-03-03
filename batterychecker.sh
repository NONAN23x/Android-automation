#!/bin/bash

TWENTYFIVE="25"
FIFTY="50"
FULL="99"
VAR3="$(termux-battery-status | grep percentage | cut -d ':' -f 2 | cut -d ',' -f 1)"

if [[ "$VAR3" == "$TWENTYFIVE" ]]; then
    termux-tts-speak "My battery is low, please charge immediately"
elif [[ "$VAR3" == "$FIFTY" ]]; then
    termux-tts-speak "My battery is half full"
elif [[ "$VAR3" == "$FULL" ]]; then
    termux-tts-speak "Battery full"
fi
