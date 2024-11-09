# Orangewod-Task

# Turtlesim Rectangle Path ROS Package

This ROS package moves the turtle in the Turtlesim simulator in a rectangular path. The project builds on the existing movement capabilities, which include straight-line and circular trajectories, and adds a rectangular movement path with configurable length and breadth.

# Installation

- Install the `turtlesim` package

    ```bash
    sudo apt update
    sudo apt install ros-noetic-turtlesim
    ```

- Clone the ROS Session Package

    ```bash
    cd ~/catkin_ws/src
    git clone https://github.com/topguns837/ros_session
    ```

- Build the Package
  Navigate to your catkin workspace and build the packages.

    ```bash
    cd ~/catkin_ws
    catkin_make
    ```

- Source the Workspace
  Source your workspace to include the new packages.
  
    ```bash
    source devel/setup.bash
    ```

# Instructions to Run the Code

- In terminal 1
Launch the Turtlesim node in a new terminal.

    ```bash
    roscore
    ```

- In terminal 2

    Launch the Turtlesim node in a new terminal.

    ```bash
    rosrun turtlesim turtlesim_node
    ```

- In terminal 3

  Execute the custom node that moves the turtle in a rectangular path. Open another terminal and     run:

    ```bash
    rosrun ros_session move_box.py
    ```



#video Link
https://www.loom.com/share/bdbcb4b1f2964f37a8b47dd1ab9380b1
