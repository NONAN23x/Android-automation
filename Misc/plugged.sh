#!/bin/bash

while [ True ]
do
   VAR1="$(termux-battery-status | grep plugged | cut -d ':' -f 2 | cut -d ',' -f 1)"
done
