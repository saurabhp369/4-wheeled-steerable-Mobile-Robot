#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import Float64

global pub_steer, pub_move

def callback_speed(data):
    rospy.loginfo("Robot_Velocity: %f", data.data)
    rate = rospy.Rate(2)
    pub_move.publish(data.data)
    rate.sleep()
    

def callback_turn(data):
    rospy.loginfo("Robot_Angular_Velocity: %f", data.data)
    rate = rospy.Rate(2)
    pub_steer.publish(data.data)
    rate.sleep()

def robot_subscriber():
    rospy.init_node("mr_subscriber")

    rospy.Subscriber("/mr_lin_vel", Float64, callback_speed)
    rospy.Subscriber("/mr_ang_vel", Float64, callback_turn)
    
    rospy.spin()

if __name__ == '__main__':
    pub_steer = rospy.Publisher('/mobile_robot/controller_fa/command', Float64, queue_size=10) 
    pub_move = rospy.Publisher('/mobile_robot/controller_ra/command', Float64, queue_size=10)
    robot_subscriber()
