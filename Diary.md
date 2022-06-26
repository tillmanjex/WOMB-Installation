Research:

2022-04-27: Speaker Systems + Rasbperry Pi Research - 1hr  
  
2022-05-04: Speaker Systems Research - 0.5hr  
  
2022-04-05: Emails / Communication - 0.5hr  
  
2022-04-06: Sensors Research - 1hr  
    - [3.3v to 5v converter](https://www.conrad.com/p/sparkfun-spk12009-converter-1-pcs-compatible-with-development-kits-arduino-raspberry-pi-095848  )     
    - [Grove Sensor (No voltage conversion needed)](https://www.seeedstudio.com/Grove-Ultrasonic-Distance-Sensor.html  )        
    - [SR04 Tutorial](https://www.youtube.com/watch?v=xACy8l3LsXI  )        
    - [SR04 with Raspberry setup tutorial](https://thepihut.com/blogs/raspberry-pi-tutorials/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi  )     
    - [Voltage converter connection and code tutorial](https://www.diymachines.co.uk/tsx0108e-logic-level-converter  )      
    - Echo pin from sensor needs to have output voltage decreased to 3.3v. Otherwise all pins can connect straight to raspberry.  

2022-05-20 - Started looking at additionally turning AC lighting systems on/off - 1hr
    - [Relay Board](https://www.conrad.com/p/whadda-wpm464-4-channel-fixed-body-relay-module-2481916)    
    - [Instructables Tutorial](https://www.instructables.com/Raspberry-Pi-Home-Automation-Control-lights-comput/)  

2022-05-21: Amplifier research and purchase / first production meeting - 3hr
    - [Aniyama 05](https://www.amazon.de/-/en/gp/product/B0978W11BY/ref=ox_sc_act_title_4?smid=A1KEFHE3KMZSAL&psc=1)        

2022-05-22: Music Composition - 3hr

2022-05-25: Raspberry Pi Setup, Speaker Pickup, First Visit to Workshop (Woodboom) - 5hr
- [play audio from terminal ](https://www.makeuseof.com/tag/play-mp3-audio-raspberry-pi/)
- [play audio from terminal python](https://www.circuitbasics.com/how-to-play-audio-with-the-raspberry-pi/) (the sensor code runs from a python script, so this is probably the most elegant audio playback solution) 

2022-05-26: Raspberry Pi Sensor Coding and Voltage Converter Soldering: 4hr
- [python SR04 tutorial showcasing gpizero library](https://www.youtube.com/watch?v=JvQKZXCYMUM)
  - Also shows how to multithread in python
- [This tutorial includes a different library](https://randomnerdtutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/). End result is a continuous output of distance, which is what I want. 


2022-05-29: Raspberry Pi Sensor Coding and Music Composition 5h
- Continuouse reading achieved using the [gpiozero library](https://gpiozero.readthedocs.io/en/stable/index.html)

Caught this error during readout:  
```
Distance:  69.37784043527472
/usr/lib/python3/dist-packages/gpiozero/input_devices.py:978: DistanceSensorNoEcho: no echo received
  warnings.warn(DistanceSensorNoEcho('no echo received'))
Distance:  69.37784043527472
``` 

This could most likely caus bugs if I'm running a simple ```if``` statement checking if the value falls below a certain distance. If it encounters a string, it may break? Keep in mind for future error handling

2022-06-03: Sensor / Raspberry Pi Debugging 6h
- NOTE TO SELF: When working in code, don't forget the physical reality of the hardware you're using. Spent good time trying to debug a "no echo received" error. When digging into the library code, it was commented that if this error happens that "something terrible has gone wrong"... That terrible thing was that the sensor was not facing a perpendicular surface, so the echo was of course bouncing everywhere except back into the unit itself... 
- Really weird problem where if the audio cable is plugged from the Raspberry to my audio interface, the sensor stops working. Get the same "no echo received error". But when the audio interface end is left unplugged, the code works. The code also works when my headphones are plugged in. So I don't think it's a power delivery issue, maybe a ground problem?
- Proving to be really convoluted to get audio output running. Tried pygame and vlc. Had a look at pyAudio too, but looks unnecessarily complicated.
- After installing python-vlc or PulseAudio packages, the raspberry pi menu bar dissapeared and I'm now also getting a "no session for pid xxx" error. Searched a lot and keep coming back to the fix to ```rm -r ~/.config/lxpanel``` and then ```sudo reboot```. But it's not fixing it for me.

2022-06-04: Sensor / Raspberry Pi Debugging 7h
- Ridiculously, the audio cable bug mentioned yesterday had to do with the wrong pin numbering value in my python code for the sensor trigger output. What is bizarre is that, despite the pin number being incorrect, the sensor still worked totally as expected and returned distance values to the console... So I had no reason to believe it was a problem with the code... I really thought it must be at the hardware level or a bug with gpiozero library. I only noticed this because I had my technical notes open next to the code and noticed the different pin numbering... Thank god for self documentation...
  
2022-06-05: Speakers test 2h
- Fabricate speaker cables and tested amp with the speakers at the workshop. Everything working fine. 

2022-06-05: 2h
- python script is working, ie, when distance is in range, audio plays and when distance is out of range, audio stops with a fadeout of three seconds. 
- script added to boot process so no manual start up is needed
- adding scripts to auto start: https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/

2022-06-18: 1h
- Final touches on composition

2022-06-20: 4h
- Speaker troubleshooting
- System installation
- System testing

2022-06-25 + 26: Exhibition Day - 16h
- Day 1: Sensor became unreliable. It was reading approx +5cm than the actual distance. 
- Day 2: Full day. No technical problems. Pack down.