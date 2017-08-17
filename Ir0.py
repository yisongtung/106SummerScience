import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

while True:
    if(GPIO.input(17) ==0):
        print("Beam Broken")
        print datetime.now()
    time.sleep(0.1)

