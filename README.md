# Trimmer tool
The trimmer tool was designed to allow the robot to cut vegetation in the micro-scale garden.\
The trimmer tool consists of a circular saw (40mm diameter), driven by a 24V DC motor with maximum rotation speed of 9000 RPM.\
The rotation of the saw can be controlled using PWM.\
The cost of the trimmer tool is approximately \$45 (excluding 3D-printing).
List of parts (BOM) can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/trimmerTool/BOM.txt).\
\
\
![untitled-8](https://user-images.githubusercontent.com/25335836/45913528-0264f300-bde9-11e8-9dff-2ba6162adf00.png)

## Mechanics and 3D printing
The body of the trimmer tool was 3D printed using Ultimaker 3D printer while using 0.6mm nozzle.\
CAD (Solidworks) and STL files can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/tree/trimmerTool).\
The [trimmer housing cup](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/trimmerTool/STL/cameraHousing1%20cup.STL) 
is connected to the [trimmer housing](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/trimmerTool/STL/trimmerHousing.STL) 
by mounting inserts into the mounting holes on the trimmer housing and using m3\L=8 bolts (see image below).

![insertstrimmer](https://user-images.githubusercontent.com/25335836/45913533-1d376780-bde9-11e8-9eb4-0b40654c3dd6.png)


## Hardware and software
A schematic electrical drawing can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/trimmerTool/Trimmer%20Tool%20electrical%20drawing.pdf).\
A [raspberryPi zero w](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) is installed in the tool and is used as the main computing unit of the trimmer tool.\
The connection of the trimmer tool with the remote computer is via WiFi. The robot should provide power (24v) to the trimmer tool.

### preparing the raspberryPi
Before starting using the raspberryPi please follow the instructions [here](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up). 
In this work we will use the NOOBS installer with **Raspbian**.

After Raspbian is installed we will need to add the [main program](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/trimmerTool/trimmerTool.py) and the [reset button program](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/trimmerTool/rebootRasPiUsingButton.py)
to the raspberryPi autostart using crontab ([tip](https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up)).

The tool and the remote computer **must** be connected to the same router, and are able to communicate (check using ping).\
Make sure the same network is used when the raspberryPi starts ([tip](https://raspi.tv/2017/how-to-auto-connect-your-raspberry-pi-to-a-hidden-ssid-wifi-network)).

##Controlling the flashlight tool 
The trimmer tool acts as a server and wait for set speed command.\
To set the rotational speed of the trimmer tool motor, use a remote computer connected to the same network, and run the [setTrimmer](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/trimmerTool/setTrimmer.py) program from the remote computer.
For example:
```
cd remoterComputer
python setTrimmer.py
``` 
To set motor speed to 50% power, enter the following in the terminal:
```
setSpeed_000_050
```
where 000 is clockwise (001 is counterclockwise) and 050 is the 50% power.

## Authors

**Ron Berenstein** - [website](http://ronberenstein.com/index.html)

See also the list of [contributors](https://github.com/BerkeleyAutomation/RobotToolChanger/graphs/contributors) who participated in this project.
