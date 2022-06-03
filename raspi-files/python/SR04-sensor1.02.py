#!/usr/bin/python3
# https://www.youtube.com/watch?v=JvQKZXCYMUM

import RPi.GPIO as GPIO
import pygame
from threading import Thread
from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from gpiozero import DistanceSensor

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.fadeout(2000)
audio_file = pygame.mixer.Sound("raspi-files/audio/1khz.wav")
audio_file.set_volume(0.9)

reading = True
sensor = DistanceSensor(echo=24, trigger=21)

def safe_exit(signum, frame):
	exit(1)

	

def read_distance():
	while reading:
		print("Distance: ", sensor.distance)
		sleep(0.1)
		if sensor.distance < 0.2:
			pygame.mixer.Sound.play(audio_file)
		else:
			pygame.mixer.Sound.stop(audio_file)


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
