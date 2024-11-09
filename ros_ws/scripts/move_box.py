#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_straight(velocity_publisher, speed, duration):
    vel_msg = Twist()
    vel_msg.linear.x = speed
    vel_msg.angular.z = 0.0

    # Publish the speed for the given duration
    end_time = rospy.Time.now() + rospy.Duration(duration)
    while rospy.Time.now() < end_time:
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)
    
    # Stop the turtle after moving straight
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)

def turn(velocity_publisher, angular_speed, duration):
    vel_msg = Twist()
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = angular_speed

    # Publish the angular speed for the given duration
    end_time = rospy.Time.now() + rospy.Duration(duration)
    while rospy.Time.now() < end_time:
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)
    
    # Stop the turtle after turning
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)

def move_in_box():
    # Initialize the ROS node
    rospy.init_node('move_turtle_box_node', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Box movement parameters
    speed = 1.0        # Linear speed
    side_duration = 2  # Duration to move in a straight line for each side of the box
    angular_speed = 1.57  # Approximately 90 degrees per second (π/2 radians per second)
    turn_duration = 1.0   # Duration to turn 90 degrees

    rospy.loginfo("Moving the turtle in a continuous box pattern...")

    # Move in a box pattern continuously
    while not rospy.is_shutdown():
        for _ in range(4):
            move_straight(velocity_publisher, speed, side_duration)
            turn(velocity_publisher, angular_speed, turn_duration)

if __name__ == '__main__':
    try:
        move_in_box()
    except rospy.ROSInterruptException:
        pass

