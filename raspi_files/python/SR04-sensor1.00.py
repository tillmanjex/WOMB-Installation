import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print "Distance measurement in progress"
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Gives time for the sensor to settle back to baseline before measuring again
GPIO.output(TRIG, False)
print "Waiting for sensor to settle..."
time.sleep(2)

# Create trigger pulse
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

# Sensor sets echo to 1 after it sends the trigger pulse and is waitng for it to retrun
# Take time stamp at last moment echo was 0
while GPIO.input(ECHO)==0:
    pulse_start = time.time()
   
# Take time stamp at last moment when echo was 1
while GPIO.input(ECHO)==1:
    pulse_end = time.time()
    
# Time echo was 1
pulse_duration = pulse_end - pulse_start

# Calcualte time from sensor and back again
distance = pulse_duration * 17150
distance = round(distance, 2)

print "Distance:", distance, "cm"

GPIO.cleanup()








