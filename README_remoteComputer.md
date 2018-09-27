# Remote Computer Software   

The ```remoteComputer``` branch is a set of Python programs to control and interact with the tool-changer and the tools.\
The ```connectCameraTool.py```, ```connectLightTool.py```, and ```connectMoistureTool.py```, are programs designed to 
control the ABB YUMI to connect with the relevant tool.\
With minor modification and adjustment the coordinate system and values, these programs can be used with other robot arms.\
\
The ```imageRequest.py``` and ```moistureRequest.py``` are designed to request data from the tool (image and moisture value respectively).\
The ```setLight.py``` and ```setMotor.py``` are designed the set values to the tools.\
\
```main.py``` is an overall program design to execute the use of the four tools (flashlight, camera, trimmer, and moisture sensor). 