# WOMB Installation at 48hours Neukölln 
Documentation for the 2022 installation project "WOMB", which was exhibited at 48h Neukölln in Berlin. 

The installation itself was the combination of a phyiscal interactable wooden structure, an audio system, a sensor system and a musical composition. 

# Components

## Raspberry Pi 3b and HC-SR04 Ultrasonic Range Sensor

![raspberry and sensor components](./img/raspi-setup-parts.png)     

The Raspberry was in charge of registering distance data of the installation door and playing audio. If the door was open, the audio would stop / not be playing. If the door was closed (ie someone had entered the exhibition) the audio would play.

### Raspberry Pi and Sensor Wiring

![raspi and sensor diagram](./img/raspi-sensor-diagram.jpg)     

General Notes:
- TRIG = GPIO 23 (output)
- ECHO = GPIO 24 (input) via level shifter
- VCC receives 5v from Raspberry Pi. 
- Ground connection to sensor via voltage transformer

Voltage transformer receives: 
- 3.3v on the LV side 
- 5v on the HV side
- GND connects to ground on Raspberry and ground on sensor. 
- Output from ECHO pin of sensor into HV channel, then from LV partner channel to GPIO 24 on Raspi (as mentioned above)

![raspi sensor wired pic](./img/raspi-sensor-wired.png)


## Sound System
