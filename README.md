# mini_ros_project

* creating a simple robot model with ultrasonic sensor mounted on the top to simulate in gazebo and visualize it in RViz to control the robot movement 

* This repo also contains the python code to move the robot manually if the rqt steering or teleop_twist_keyboard is not working either use move_robot.py or moveit.py

* Moreover, this repo contains the python code needed to measure the distance with ultrasonic sensor mounted on the top.

# To run the project, follow below steps in the terminal:
```
$ mkdir robotmodel_ws

$ cd robotmodel_ws/
```
* Inside the directory, git clone this repository and continue the below steps:
```
$ catkin_make

$ source devel/setup.bash

$ roslaunch my_robot display.launch
```
* The above command opens the gazebo with the robot URDF model. Open another terminal to run RViz.
```
$ rviz
```
* In RViz, click add button and select RobotModel to add the model to RViz. In shell, open another terminal
```
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```
* The above command is used to control the robot movement with appropriate keys.
```
$ rostopic list
```
* Open another terminal in the shell to exexute the above command and see the topics created by the robot model.

If the robot movement is not controlled by the teleop_twist_keyboard, use the python code available under scripts folder named `move_robot.py` or `moveit.py` in a new terminal
```
$ rosrun my_robot move_robot.py 
$ rosrun my_robot moveit.py
```

The robot model is mounted with a ultrasonic laser on top to detect the distance between the robot and the object in the gazebo environment. 

The laser measures the obstacle distance and prints the range in a list stored in the /scan node which publishes to gazebo model and subscribes to my_robot_node of python code. Note: Stop the manual control of robot movement to execute the below commands:
```
$ rosrun my_robot obstacle.py
```
* Next run the below commands in a new terminal:
```
$ rostopic list

$ rostopic info /scan

$ rostopic echo /scan
```

`Ctrl+C` - to stop everything currently in the terminal

