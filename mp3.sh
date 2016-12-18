#!/bin/bash



find /mnt/usb/mp3 -name "*.mp3" | sort --random-sort| head -n 1|xargs -d '\n' mpg123
