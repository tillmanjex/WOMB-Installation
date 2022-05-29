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

