# Research Track 1 assignment 2

Second assignment for the Research Track 1 course.

## Description

In this assignment we are going to learn how to operate _ROS_ costum messages, costum services, and actions. We are also going to use the graphical interfaces (_Rviz_ and _Gazebo_) to view the robot's simulation.
The new package was built starting from the template provided, [_assignment_2_2022_](https://github.com/CarmineD8/assignment_2_2022).<br>
The task of this assignment was to implement three new nodes in the robot simulation:

- a node that implements an _action client_, allowing the user to set a target (x, y) or to cancel it. Then publish the robot position and velocity as a custom message by relying on the values published on the topic `/odom`;
- a _service node_ that, when called, prints the number of goals reached and cancelled;
- a node that subscribes to the robot’s position and velocity (using a _custom message_) and prints the distance of the robot from the target and the robot’s average speed. Use a parameter to set how fast the node publishes the information.

It is also required to create a _launch file_ to start the simulation ([_assignment1.launch_](launch/assignment1.launch)).

For more information visit the [documentation page](https://gabri00.github.io/RT1-assignment2/).

## Run the simulation

Before running the program it is required to install the **xterm** library, if it is not already installed on the system:

```sh
sudo apt install xterm
```

Now we need to run the ROS master in a separete terminal:

```sh
roscore
```

We can then install the module. Go inside the root directory of your ROS workspace and run the command:

```sh
catkin_make
```

Finally, launch the simulation with the _roslaunch_ command:

```sh
roslaunch RT_assignment_2 assignment1.launch
```

## Usage

The program will open four windows:

- **Rviz**: a tool for ROS visualization, is used for debugging and adding additional functionalities to the robot;
- **Gazebo**: a 3D visualization environment, where the arena and the robot will be displayed;
- [_info_node.py_](scripts/info_node.py): the window where the robot's information will be printed;
- [_client.py_](scripts/client.py): the window where the user can input the desired position or cancel it.

If you want to know the number of goals that have been reached/canceled, in another command window type:

```sh
rosservice call /goals
```

If you want to change the the frequency with which the information are printed in the _info_node_ window, you have to open the launch file [_assignment1.launch_](launch/assignment1.launch) inside of the `launch` directory, and change the _value_ attribute:

```xml
<param name="publish_frequency" type="double" value="1.0" />
```

## Code description

The _client_ node has the following structure:
![client node structure](client.png)

## Possible improvements

- A good improvement could be to add a marker in the simulation to visualize the goal location, since it is not clear where the robot is going.<br>
- Another useful improvement could be controlling that the goal coordinates are actually valid, hence they must be integer values and in the range of the canvas width and height.
