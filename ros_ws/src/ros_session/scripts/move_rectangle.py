#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def move_straight(speed, distance, is_forward):
    velocity_message = Twist()
    velocity_message.linear.x = abs(speed) if is_forward else -abs(speed)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    loop_rate = rospy.Rate(10)
    start_time = rospy.Time.now().to_sec()
    current_distance = 0

    while current_distance < distance:
        velocity_publisher.publish(velocity_message)
        current_time = rospy.Time.now().to_sec()
        current_distance = speed * (current_time - start_time)
        loop_rate.sleep()
    
    velocity_message.linear.x = 0
    velocity_publisher.publish(velocity_message)

def rotate(angle_in_degrees, clockwise):
    angle_in_radians = math.radians(angle_in_degrees)
    velocity_message = Twist()
    velocity_message.angular.z = -1.0 if clockwise else 1.0
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    loop_rate = rospy.Rate(10)
    start_time = rospy.Time.now().to_sec()
    current_angle = 0

    while current_angle < angle_in_radians:
        velocity_publisher.publish(velocity_message)
        current_time = rospy.Time.now().to_sec()
        current_angle = (current_time - start_time)
        loop_rate.sleep()
    
    velocity_message.angular.z = 0
    velocity_publisher.publish(velocity_message)

def move_rectangle(length, width):
    while not rospy.is_shutdown():
        for _ in range(2):
            move_straight(speed=1.0, distance=length, is_forward=True)
            rotate(angle_in_degrees=90, clockwise=True)  # 90-degree turn
            move_straight(speed=1.0, distance=width, is_forward=True)
            rotate(angle_in_degrees=90, clockwise=True)

if __name__ == '__main__':
    try:
        rospy.init_node('turtle_rectangle', anonymous=True)
        move_rectangle(length=4.0, width=2.0)
    except rospy.ROSInterruptException:
        pass

