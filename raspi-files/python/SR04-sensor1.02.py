#!/usr/bin/python3
# https://www.youtube.com/watch?v=JvQKZXCYMUM

import RPi.GPIO as GPIO
import pygame
from threading import Thread
from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from gpiozero import DistanceSensor

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()
pygame.mixer.Sound("raspi-files/audio/1khz.wav")

door_open = True
door_closed = False

reading = True
sensor = DistanceSensor(echo=24, trigger=21)

def safe_exit(signum, frame):
	exit(1)

def play_audio():
	if door_open:
		print("door open")

	if door_closed:
		print("door closed")
	

def read_distance():
	while reading:
		print("Distance: ", sensor.distance)
		sleep(0.1)
		while sensor.distance > 0.2:
			door_open = True
			door_closed = False
		else:
			door_open = False
			door_closed = True

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:
	reader = Thread(target=read_distance, daemon=True)
	reader.start()

	audio_player = Thread(target=play_audio, daemon=True)
	audio_player.start()



	pause()

except KeyboardInterrupt:
	pass

finally:
	reading = False
	sensor.close()
