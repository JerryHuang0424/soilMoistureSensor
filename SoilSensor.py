# Jiarui Huang / 20109685 / 2025.4.16
# Semester 3, 2025
# Project Title: soilMoistureSenser
# Project Description: Use to obverse the moisture for a plant, test if it need water

import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
	if GPIO.input(channel):
		print("Water Detected!")
	else:
		print("Water Detected!")
		
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(channel,callback)

# infinite loop
while True:
	time.sleep(0)
	
