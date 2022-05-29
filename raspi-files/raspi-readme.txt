Readme for WOMB Installation
Originally built by Tillman Jex
tillmanjex@mailbox.org
www.tillmanjex.info

Raspberry Wiring:
TRIG = GPIO 23 (output)
ECHO = GPIO 24 (input) via voltage trasnformer
VCC receives 5v from Raspi.
GRD to ground via voltage transformer
Voltage transformer receives: 
- 3.3v on the LV side 
- 5v on the HV side
- GND connects to ground on Raspi and ground on sensor. 
- Output from Echo pin of sensor into HV channel
- Output from LV partner channel to GPIO 24 on Raspi (as mentioned above)


Run python script:
sudo python /home/pi/WOMB-Installation/raspi-files/python/SR04-sensor1.00.py
