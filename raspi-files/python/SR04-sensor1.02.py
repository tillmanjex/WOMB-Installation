#!/usr/bin/python3
# https://www.youtube.com/watch?v=JvQKZXCYMUM

import RPi.GPIO as GPIO
from threading import Thread
from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from gpiozero import DistanceSensor

reading = True
sensor = DistanceSensor(echo=24, trigger=21)

def safe_exit(signum, frame):
	exit(1)

def read_distance():
	while reading:
		print("Distance: ", sensor.distance * 100)
		sleep(0.1)	

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:
	reader = Thread(target=read_distance, daemon=True)
	reader.start()

	pause()

except KeyboardInterrupt:
	pass

finally:
	reading = False
	sensor.close()
