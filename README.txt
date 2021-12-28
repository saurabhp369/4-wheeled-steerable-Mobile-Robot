1) Copy and Paste the mobile_robot folder which is inside the Package folder in the zip file, into catkin_ws/src/

2) For launching the robot in the given maze world, run: roslaunch mobile_robot template_launch.launch

3) To teleop the bot, run: rosrun mobile_robot teleop_template.py
   Set linear velocity of around 15.59 and turn speed of around 1.18 using w/x and e/c commands. Use the key commands shown in the terminal for teleopping the bot.
   
4) To start Rviz, type rviz. Click on Add-->By topic-->LaserScan. Click on Add--> By display type --> RobotModel

5) To start robot in an empty world, use roslaunch mobile_robot mr_gazebo_world.launch

6) To start the publisher to publish the commands to move robot in a circle, use rosrun mobile_robot mr_publisher.py

7) To start the subscriber to print the current linear and angular velocities and to make the robot actually follow the commands and move in a circle, use rosrun mobile_robot mr_subscriber.py
