#!/usr/bin/python3
# https://www.youtube.com/watch?v=JvQKZXCYMUM

import RPi.GPIO as GPIO
import pygame
from threading import Thread
from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from gpiozero import DistanceSensor

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

audio_file = pygame.mixer.Sound('/home/pi/WOMB-Installation/raspi-files/audio/womb-track-2.01-16bit.wav')

reading = True
sensor = DistanceSensor(echo=24, trigger=23, max_distance=1, threshold_distance=0.2)

def safe_exit(signum, frame):
	exit(1)

def play_audio():
	audio_file.play()

def stop_audio():
	#audio_file.stop()
	pygame.mixer.fadeout(3000)

def read_distance():
    while reading:
        print("Distance (cm): ", sensor.distance * 100)
        sleep(0.1)
        sensor.when_in_range = play_audio
        sensor.when_out_of_range = stop_audio


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
