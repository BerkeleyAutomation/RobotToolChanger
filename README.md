# Tool-changer and tools for collaborative and service robots
This repo include the design and software needed to create a tool-changer for collaborative and service robots.\
The repo also include several tools that can be created and used with or without the tool-changer.

The [tool-changer](https://github.com/BerkeleyAutomation/RobotToolChanger/tree/tool-changer) is described in branch `tool-changer`, 
which include the three main components of the tool-changer: robot component, tool-component, and tool-housing.

The tool-changer was originally designed to be used with ABB YUMI collaborative robot.\
With minor adjustments the tool-changer design can be retrofit to most mobile and stationary robots.\
The project includes the design, manufacturing, programming, and evaluation of a tool-changer for robots.\
To examine the design we evaluated the tool-changer on ABB YuMi, a two-arm stationary robot.

![yumiwithtools2](https://user-images.githubusercontent.com/25335836/45905394-0ff88980-bda5-11e8-9efd-d0f7ab4f56cf.png)

<!---
The tool-changer mechanism was first published at [CASE-2018](http://ronberenstein.com/papers/CASE2018-Ron-Tool-Changer-Final.pdf) conference.\
This publication present the three main components needed to create a tool-changer, robot, tool, and tool housing.\
Most of the component were 3D printed which may contributes to the adoption of the design.
--->
## Getting Started
The tool-changer and the different tools are organized in separate branches.\
To get started with the tool-changer, open the `tool-changer` branch and follow instructions.\
To manufacture a tool, open the tool branch and follow the design instructions and supplementary material (software, electrical drawings, etc.).       

## Adding new tool
To add new tool the developer will work on branch `new-tool`, and ask the contributors to do `pull-request`. 

## Authors

**Ron Berenstein** - [website](http://ronberenstein.com/index.html)

See also the list of [contributors](https://github.com/BerkeleyAutomation/RobotToolChanger/graphs/contributors) who participated in this project.
<!---
## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
--->
## Acknowledgments
* [CITRIS invention lab](https://invent.citris-uc.org/)
* Jacob Gallego from UC Berkeley machine shop
