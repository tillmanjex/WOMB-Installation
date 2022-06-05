#!/usr/bin/python3
# https://www.youtube.com/watch?v=JvQKZXCYMUM

from gpiozero.pins.native import NativeFactory
from time import sleep
from gpiozero import Device, DistanceSensor

Device.pin_factory = NativeFactory()
sensor = DistanceSensor(echo=24, trigger=21)

while True:
    print("Distance (cm): ", sensor.distance * 100)
    sleep(0.1)


