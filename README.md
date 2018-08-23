# Tool changer for robots
In this work we developed a tool changer for robots. 
With minor adjustments, the tool changer design can be retrofited to most mobile and stationary robots.
The project includes the design, manufacture, programing, and evaluation of a tool changer for robots. 
To examine the design we evaluated the tool changer on the ABB YUMI, a two-arm stationary robot. 


## Getting Started
This work was first published at [CASE-2018](http://ronberenstein.com/papers/CASE2018-Ron-Tool-Changer-Final.pdf). 
This publication presents the three main components needed to create a tool changer, robot, tool, and tool housing.
Most of the components were 3D printed which may contribute to the adoption of the design.


## The tools
For this case study we created 4 tools: camera, light, cutting, and moister sensor tool. 
For each tool we provide the CAD design, the electrical drawing, and the program to control it.

A [raspberryPi zero w](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) is installed in each tool and is used as the main computing unit of the tool. 
The connection of the tool with the remote computer is via WIFI. The robot provides power (24v) to the tool.

### preparing the raspberryPi
Before starting using the raspberryPi please follow the instructions [here](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up). 
In this work we will use the NOOBS installer with **Raspbian**.

After Raspbian is installed we will need to add the main program and the [reset button program](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/master/rebootUsingButton.py)
to the raspberryPi autostart using crontab ([tip](https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up)).

The tool and the remote computer **must** be connected to the same router, and be able to communicate (check using ping).
Make sure the same network is used when the raspberryPi starts ([tip](https://raspi.tv/2017/how-to-auto-connect-your-raspberry-pi-to-a-hidden-ssid-wifi-network)).

### Camera-tool
The Camera-tool utilizes a raspberryPi camera [PiCamera](http://a.co/cbe3Pey). 
The camera is capable of capturing RGB and IR images.

CAD design of the Camera-tool can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/tree/supportingDocuments/CAD/Camera%20Tool),
and electrical drawing [here](https://github.com/BerkeleyAutomation/RobotToolChanger/tree/supportingDocuments/ElectricalDrawings).

The Camera-tool acts as a server and waits for an image request. The Program running on the Camera-tool raspberryPi can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/master/sendImageByRequest.py).
To get an image from the Camera-tool we use a remote computer connected to the same network, and run [this](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/remoteComputer/imageRequest.py) program.
For example:
```
cd remoterComputer
python imageRequest.py
``` 

### Light-tool
The Light-tool is used as a flashlight for the robot. For lightening we used three [LED's](https://www.amazon.com/BRIGHTEST-Light-Bolt-Interior-Motorcycle/dp/B01ADHUXGU/ref=sr_ph_1?ie=UTF8&qid=1534665958&sr=sr-1&keywords=led+11mm)
installed facing inwards. The intensity of each LED can be controlled.

CAD design of the Light-tool can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/tree/supportingDocuments/CAD/Light%20Tool),
and electrical drawing [here](https://github.com/BerkeleyAutomation/RobotToolChanger/tree/supportingDocuments/ElectricalDrawings).

The Light-tool acts as a server and wait for set light command. The Program running on the Light-tool raspberryPi can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/master/lightToolServer.py).
To set a light to the three LED's use a remote computer connected to the same network, and run [this](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/remoteComputer/setLight.py) program.
For example:
```
cd remoterComputer
python setLight.py
``` 
To set intensity light 1, 10, 99 to the corresponding right, middle, and left LED's, enter the following in the terminal:
```
setLight_001_010_099
```

### Cutting-tool
The Cutting-tool uses a small diameter, rotation saw to cut miniature garden grass. We use a 24v, 9000RPM [motor](https://www.amazon.com/uxcell-9000RPM-Models-Remote-Control/dp/B0784W8HXF/ref=sr_1_12?ie=UTF8&qid=1534667758&sr=8-12&keywords=24v+motor+9000+rpm), 
and a 30mm steel saw. The rotating direction and speed can be controlled using PWM. 

CAD design of the Cutting-tool can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/tree/supportingDocuments/CAD/Cutting%20Tool),
and electrical drawing [here](https://github.com/BerkeleyAutomation/RobotToolChanger/tree/supportingDocuments/ElectricalDrawings).

The Cutting-tool acts as a server and wait for set speed command. The Program running on the Cutting-tool raspberryPi can be found [here](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/master/cuttingToolServer.py).
To set a motor speed we use a remote computer connected to the same network, and run [this](https://github.com/BerkeleyAutomation/RobotToolChanger/blob/remoteComputer/setMotor.py) program.
For example:
```
cd remoterComputer
python setMotor.py
``` 
To set motor speed to 50% power, enter the following in the terminal:
```
setSpeed_000_050
```
where 000 is clockwise (001 is counterclockwise) and 050 is the 50% power.

## Authors

* **Ron Berenstein** - [website](http://ronberenstein.com/index.html)

See also the list of [contributors](https://github.com/BerkeleyAutomation/RobotToolChanger/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [CITRIS invention lab](https://invent.citris-uc.org/)
* Jacob Gallego from UC Berkeley machine shop
