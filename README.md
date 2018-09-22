# Flashlight tool
The moisture sensor tool is designed to allow the robot to measure soil moisture, a valuable indicator of a plant's irrigation state.\
The measurement process involves penetrating the soil with a YL-60 moisture sensor, risking breaking or soiling the sensor tip.\
To alleviate the risk, we positioned the moisture sensor at the end of a 110mm extension, and furthermore designed the sensor so it could be quickly replaced.\
The cost of the moisture tool is approximately \$30 (excluding 3D-printing).
List of parts (BOM) can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/moistureSensorTool/BOM.txt).\
\
\
![untitled-1](![untitled-9](https://user-images.githubusercontent.com/25335836/45913609-971c2080-bdea-11e8-8a00-ec7c8a0fcf29.png)
## Mechanics and 3D printing
The body of the Moisture sensor tool was 3D printed using Ultimaker 3D printer while using 0.6mm nozzle.\
CAD (Solidworks) and STL files can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/tree/moistureSensorTool).\
The [moisture sensor housing cup](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/moistureSensorTool/STL/moistureHousing%20cup.STL) 
is connected to the [moisture sensor housing](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/moistureSensorTool/STL/moistureHousingBase.STL) 
by mounting inserts into the mounting holes on the moisture sensor housing and using m3\L=8 bolts (see image below).

![untitled3](![insertsmoisture](https://user-images.githubusercontent.com/25335836/45913614-a69b6980-bdea-11e8-9381-3f5137a29ed2.png)

## Hardware and software
A schematic electrical drawing can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/moistureSensorTool/Moisture%20Sensor%20Tool%20electrical%20drawing.pdf).\
A [raspberryPi zero w](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) is installed in the tool and is used as the main computing unit of the moisture sensor tool.\
The connection of the moisture sensor tool with the remote computer is via WiFi. The robot should provide power (24v) to the moisture sensor tool.

### preparing the raspberryPi
Before starting using the raspberryPi please follow the instructions [here](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up). 
In this work we will use the NOOBS installer with **Raspbian**.

After Raspbian is installed we will need to add the [main program 1](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/moistureSensorTool/SendMoistureByRequest.py), [main program 2](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/moistureSensorTool/moistureLocal.py), and the [reset button program](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/flashlightTool/rebootRasPiUsingButton.py)
to the raspberryPi autostart using crontab ([tip](https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up)).

The tool and the remote computer **must** be connected to the same router, and are able to communicate (check using ping).\
Make sure the same network is used when the raspberryPi starts ([tip](https://raspi.tv/2017/how-to-auto-connect-your-raspberry-pi-to-a-hidden-ssid-wifi-network)).

##Controlling the flashlight tool 
The moisture sensor acts as a server and wait for moisture reading request.\
To get moisture value use a remote computer connected to the same network, and run the [moistureRequest](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/moistureSensorTool/moistureRequest.py) program from the remote computer.
For example:
```
cd remoterComputer
python moistureRequest.py
``` 
To get moisture value enter the following in the terminal:
```
moistureReq
```

## Authors

**Ron Berenstein** - [website](http://ronberenstein.com/index.html)

See also the list of [contributors](https://github.com/BerkeleyAutomation/RobotToolChanger/graphs/contributors) who participated in this project.
