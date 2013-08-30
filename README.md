RPi-LED
=======

Python-Applikation zum Tutorial auf www.wbss.ch/wikiIOT

##Installation
Benötigte Packete:  
```sudo aptitude install python-dev python-rpi.gpio python-pip```  
```sudo pip install -r requirements.txt```  

##Wiring
GPIO 4 (Gemäss BCM Schema) ---- 330 Ohm ---- (+) LED (-) ---- GND  
BCM Numbering: http://elinux.org/RPi_Low-level_peripherals

##Usage
Start der Applikation: sudo python led_server.py  
Das UI ist mittels Browser unter der URL  
```http://<IP Adresse des Raspberry>:5000/control``` erreichbar.  
Der Status der LED kann auch per GET Requests an /toggle_led gesetzt werden:  
EIN: /toggle_led?led_state=1  
AUS: /toggle_led?led_state=-1  

