# Victron Cerbero Modus Server
A modbus server instance to run on the the cerbero or venus on port 5020 and use a usb to 485 device to allow another service to use it as a modbus TCP server so that it can interigte what is on the other side, for me its a sunsynk inverter


Instalation instructions
Enable SSH
Login via SSH

Execute 
```
/opt/victronenergy/swupdate-scripts/set-feed.sh candidate 
```
enables other packages that can be installed by opkg
```
opkg update
```
```
/opt/victronenergy/serial-starter/stop-tty.sh ttyUSB0 
```
<<https://github.com/victronenergy/venus/wiki/howto-add-a-driver-to-Venus#3-installing-a-driver>>
```
opkg install python-pip
```
```
pip install pymodbus twisted 
```
```
nano modbusserver.py
```
<< Paste the code from the file >>
 << Save and Exit >>

```
 python modbusserver.py
```

This is a starting point for a bigger suite that i am playing with, but i thought let me create this at the moment as a modbus bridge, since i use a Synsynk Inverter with additional Victron chargers for the batteries and i have been using a Pi with mbusd on for some time, but now that i have the cerbero i can reuse that pi for something else.

Limitations
This project should be considered as for testing, if there is a need for it i can on request update it to be more elgant to run as a service since at the moment the exits arent quite graceful, its just slapped to gether to get the sunsunk poller to get the data back into Home assistant for now, this is prob best run in screen or a similar tty sesion manager as im sure this will break when the SSH session drops as described below
# THIS WILL MOSTL LIKELY NOT LIVE PAST A FIRMWARE UPGRADE AND WOULD HAVE TO BE INSTALLED AGAIN

options would be nohup and screen
there is many guides on both of these as well
but in short 
```
nohup python modbusserver.py &
```
and then to exit it you would have to 
```
ps | grep modbusserver.py
```
and then pkill the number in the first line

screen would be screen -r and then kill it.

### if i get some stars and downloads or sponsors on this i will prob put a bit more time into it. make it a serivce and make the code more robust
