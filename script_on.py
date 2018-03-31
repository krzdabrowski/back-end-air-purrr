#!/usr/bin/python3

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges. Try 'sudo' to run this script")
import time
<<<<<<< HEAD
import test
=======
import continuous_run as run
>>>>>>> 853649c... Alpha release
from sds011 import SDS011


# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
pinList = [14, 15]


def turn_on():
    for i in pinList:
        GPIO.setwarnings(False)
        print("Setup is changing to OUT for pin no. ", i)
        GPIO.setup(i, GPIO.OUT)
    
<<<<<<< HEAD
    test.sensor.workstate = SDS011.WorkStates.Sleeping
=======
    run.sensor.workstate = SDS011.WorkStates.Sleeping
>>>>>>> 853649c... Alpha release

    while True:
    	time.sleep(0.1)
  

if __name__ == "__main__":

    try: 
        turn_on()
             
    except KeyboardInterrupt:
        print("Quitting...") 
        GPIO.cleanup()