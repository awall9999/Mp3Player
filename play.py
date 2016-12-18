#!/usr/bin/python


import os
import subprocess
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)


GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
os.system('mpg123 /home/system.mp3')
while True:

      if GPIO.input(17) ==0:
                      print ("Pulse")      
                      os.system('/home/mp3.sh')
                      time.sleep(1)

      time.sleep(0.5)
GPIO.cleanup()

#find -name "*.mp3" | sort --random-sort| head -n 5|xargs -d '\n' mpg123
