# Research Track assignment #2
 Second assignment o the Research Track course

## Description

## Run

The program **xterm** is required to run the code:
```sh
> sudo apt install xterm
```

First run the master in a separete terminal:
```sh
> roscore
```

Then you need to install the module. Go inside the root directory of your ROS workspace and run the command:
```sh
> catkin_make
```

Finally, launch the program, type the following command:
```sh
> roslaunch assignment_2_2022 assignment1.launch
```

## Usage

The program will open four windows:
- **Rviz** is a tool for ROS visualization and it's used for debugging and adding additional functionalities to the robot
- **Gazebo** is the 3D visualization environment in which you'll see the arena and the robot
- [*info_node.py*](scripts/info_node.py) is the window where the robot's informations will be printed
- [*client.py*](scripts/client.py) is the window where the user can input the desired position or cancel it

To get the number of goals reached and canceled, open another command window and type:
```sh
> rosservice call /goals
```

The frequency with which the information is printed in the info_node.py window can be set in the launch file [*assignment1.launch*](launch/assignment1.launch) inside of the `launch` directory. To do so, modify the value in the following line:

```xml
<param name="frequency" type="double" value="1.0" />
```