# Camera tool
The camera tool allows the robot to capture images in a wider range of positions and directions than is possible with a
fixed-mount camera, for example by extending the robot arm to penetrate between branches and foliage and reduce occlusion.\
A [Raspberry Pi camera module](https://www.amazon.com/gp/product/B0759GYR51/ref=oh_aui_search_detailpage?ie=UTF8&psc=1)
is installed in the tool base, with a max resolution of 2592x1944 pixels.\
The camera is IR-enabled and equipped with two IR LEDs. An image is captured on request from a remote computer and the captured image is sent back to the remote computer.\
The cost of the camera tool is approximately \$40 (excluding 3D-printing).
List of parts (BOM) can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/cameraTool/BOM.txt).\
\
\
![untitled-7](https://user-images.githubusercontent.com/25335836/45912940-b319c500-bdde-11e8-9420-e353e10661d6.png)\
\
The body of the camera tool was 3D printed using Ultimaker 3D printer while using 0.6mm nozzle.\
CAD (Solidworks) and STL files can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/tree/cameraTool).\
The [camera housing cup](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/cameraTool/STL/cameraHousing%20cup.STL) 
is connected to the [camera housing](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/cameraTool/STL/cameraHousing.STL) 
by mounting inserts into the mounting holes on the camera housing and using m3\L=8 bolts (see image below).

![insertscamera](https://user-images.githubusercontent.com/25335836/45913393-7b168000-bde6-11e8-8bdf-d205d2842720.png)


## Hardware and software
A schematic electrical drawing can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/cameraTool/Camera%20tool%20electrical%20drawing.pdf).\
A [raspberryPi zero w](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) is installed in the tool and is used as the main computing unit of the camera tool.\
The connection of the camera tool with the remote computer is via WiFi. The robot should provide power (24v) to the camera tool.

### preparing the raspberryPi
Before starting using the raspberryPi please follow the instructions [here](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up). 
In this work we will use the NOOBS installer with **Raspbian**.

After Raspbian is installed we will need to add the [main program](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/cameraTool/cameraTool.py) and the [reset button program](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/cameraTool/rebootRasPiUsingButton.py)
to the raspberryPi autostart using crontab ([tip](https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up)).

The tool and the remote computer **must** be connected to the same router, and are able to communicate (check using ping).\
Make sure the same network is used when the raspberryPi starts ([tip](https://raspi.tv/2017/how-to-auto-connect-your-raspberry-pi-to-a-hidden-ssid-wifi-network)).

##Getting an image from the camera tool 
The camera tool acts as a server and wait for command to request an image.
To request image use a remote computer connected to the same network as the camera tool, and run the [imageRequest](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/cameraTool/imageRequest.py) program from the remote computer.
For example:
```
cd remoterComputer
python imageRequest.py
```

## Authors

**Ron Berenstein** - [website](http://ronberenstein.com/index.html)

See also the list of [contributors](https://github.com/BerkeleyAutomation/RobotToolChanger/graphs/contributors) who participated in this project.
