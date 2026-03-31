# ros2-obstacle-avoidance-fsm
FSM-based obstacle avoidance using LiDAR in ROS 2

Overview
This project implements an autonomous obstacle avoidance system using a Finite State Machine (FSM) in ROS 2.
The robot uses LiDAR sensor data to detect obstacles and dynamically changes its behavior to move safely in the environment.
Concept
The system follows a reactive control approach:
    • Sense environment using LiDAR
    • Decide action using FSM
    • Act by publishing velocity commands
System Architecture
/scan (LiDAR) → FSM Node → /cmd_vel (Robot Movement)
Finite State Machine (FSM)
State
Condition
Action
FORWARD
Distance > 0.5 m
Move forward
TURN
0.2 m < Distance ≤ 0.5 m
Rotate
STOP
Distance ≤ 0.2 m
Stop
Topics Used
    • /scan → LiDAR sensor data (sensor_msgs/msg/LaserScan)
    • /cmd_vel → Velocity commands (geometry_msgs/msg/Twist)
Technologies Used
    • ROS 2 (Humble)
    • Python (rclpy)
    • Gazebo Simulation
    • TurtleBot3
How to Run
1. Install dependencies
sudo apt install ros-humble-turtlebot3*
2. Set TurtleBot3 model
export TURTLEBOT3_MODEL=burger
3. Launch simulation
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
4. Build workspace
cd ~/ros2_ws
colcon build
source install/setup.bash
5. Run node
ros2 run robot_fsm obstacle_avoidance
Implementation Details
    • LiDAR data is processed by selecting front-facing ranges
    • Invalid values (inf, NaN) are filtered
    • Minimum distance is computed for obstacle detection
    • FSM logic determines the robot’s behavior
    • Velocity commands are published accordingly
Key Features
    • Real-time obstacle avoidance
    • Simple and efficient FSM design
    • Clean ROS 2 node implementation
    • Easily extendable to modular architecture
Future Improvements
    • Modular multi-node architecture
    • Integration with SLAM and navigation stack
    • Dynamic threshold tuning
    • Advanced path planning
Design Decision
This project is implemented as a single ROS 2 node for simplicity and low latency.
It can be further modularized into separate perception and decision nodes for scalability.
