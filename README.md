# Flashlight tool
Using the flashlight tool, the robot is able to illuminate areas of interest in desired times and directions, to create more controlled lighting conditions.\
The flashlight tool consists of three LEDs 30mm apart, of which the two exterior LEDs are tilted inwards by 6&deg;.\
The intensity of each LED can be modulated, up to a maximum power of 1W.\
The cost of the flashlight tool is approximately $70 (excluding 3D-printing).\
List of parts (BOM) can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/flashlightTool/BOM.txt).\
\
\
![untitled-1](https://user-images.githubusercontent.com/25335836/45912819-5e754a80-bddc-11e8-8bad-d006e987187a.png)
## Mechanics and 3D printing
The body of the flashlight tool was 3D printed using Ultimaker 3D printer while using 0.6mm nozzle.\
CAD (Solidworks) and STL files can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/tree/flashlightTool).\
The [flashlight housing cup](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/flashlightTool/STL/flashlightHousing%20cup.STL) 
is connected to the [flashlight housing](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/flashlightTool/STL/flashlightHousing.STL) 
by mounting inserts into the mounting holes on the flashlight housing and using m3\L=8 bolts (see image below).

![untitled3](https://user-images.githubusercontent.com/25335836/45912203-6e882c80-bdd2-11e8-9bd3-04d784c21a46.png)

## Hardware and software
A schematic electrical drawing can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/flashlightTool/Flashlight%20Tool%20electrical%20drawing.pdf).\
A [raspberryPi zero w](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) is installed in the tool and is used as the main computing unit of the flashlight tool.\
The connection of the flashlight tool with the remote computer is via WiFi. The robot should provide power (24v) to the flashlight tool.

### preparing the raspberryPi
Before starting using the raspberryPi please follow the instructions [here](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up). 
In this work we will use the NOOBS installer with **Raspbian**.

After Raspbian is installed we will need to add the [main program](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/flashlightTool/flashlightTool.py) and the [reset button program](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/flashlightTool/rebootRasPiUsingButton.py)
to the raspberryPi autostart using crontab ([tip](https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up)).

The tool and the remote computer **must** be connected to the same router, and are able to communicate (check using ping).\
Make sure the same network is used when the raspberryPi starts ([tip](https://raspi.tv/2017/how-to-auto-connect-your-raspberry-pi-to-a-hidden-ssid-wifi-network)).

##Controlling the flashlight tool 
The Light-tool acts as a server and wait for set light command.\
To set a light to the three LED's use a remote computer connected to the same network, and run the [setLight](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/flashlightTool/setLight.py) program from the remote computer.
For example:
```
cd remoterComputer
python setLight.py
``` 
To set intensity light 1, 10, 99 to the corresponding right, middle, and left LED's, enter the following in the terminal:
```
setLight_001_010_099
```

## Authors

**Ron Berenstein** - [website](http://ronberenstein.com/index.html)

See also the list of [contributors](https://github.com/BerkeleyAutomation/RobotToolChanger/graphs/contributors) who participated in this project.
