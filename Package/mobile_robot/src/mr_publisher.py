#!/usr/bin/env python

import rospy
import time
from std_msgs.msg import Float64

def robot_publisher():
    rospy.init_node('mr_publisher', anonymous = True)

    pub_steer = rospy.Publisher('/mr_ang_vel', Float64, queue_size=10) 
    
    pub_move = rospy.Publisher('/mr_lin_vel', Float64, queue_size=10)

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        t0 = rospy.Time.now().to_sec()
        t1 = rospy.Time.now().to_sec()
        loop_rate = rospy.Rate(2)
        err = 0
        while(err < 5):
            t1 = rospy.Time.now().to_sec()
            err = t1-t0
            pub_move.publish(-8)
            pub_steer.publish(2.5)
            rospy.loginfo("Publishing commands to move the robot in a Circle.....")
            
            loop_rate.sleep()
            
        pub_move.publish(0)
        pub_move.publish(0)
        rate.sleep()



if __name__ == '__main__':
    try:
        robot_publisher()
    except rospy.ROSInterruptException:
        pass


