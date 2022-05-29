# https://www.youtube.com/watch?v=JvQKZXCYMUM

from time import sleep
from gpiozero import DinstanceSensor
sensor = DistanceSensor(echo=24, trigger=21)


def safe_exit(signum, frame):
	exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUB, safe_exit)

try:
	while True:
		print(sensor.value)
		sleep(0.1)

except KeyboardInterrupt:
	pass

finally:
	sensor.close()
