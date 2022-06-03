#!/usr/bin/python3
# https://www.youtube.com/watch?v=JvQKZXCYMUM

import RPi.GPIO as GPIO
import pygame
from threading import Thread
from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from gpiozero import DistanceSensor

pygame.mixier.init()
mygame.mixer.music.load("../audio/1khz.wav")

reading = True
sensor = DistanceSensor(echo=24, trigger=21)

def safe_exit(signum, frame):
	exit(1)

def play_audio():
	while sensor.distance < 0.2
		pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue

def read_distance():
	while reading:
		print("Distance: ", sensor.distance * 100)
		sleep(0.1)	

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:
	reader = Thread(target=read_distance, daemon=True)
	reader.start()

	audio = Thread(target=play_audio, daemon=True)
	audio.start()



	pause()

except KeyboardInterrupt:
	pass

finally:
	reading = False
	sensor.close()
