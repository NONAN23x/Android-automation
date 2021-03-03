#!/bin/bash
YES="PLUGGED"
while [ True ]
do
    VAR1="$(termux-battery-status | grep plugged | cut -d ':' -f 2 | cut -d ',' -f 1 | cut -d '"' -f 2)"
    if [[ "$VAR1" -eq "$YES" ]]; then
    termux-tts-speak "My battery is low, please charge immediately"
    fi 
done
