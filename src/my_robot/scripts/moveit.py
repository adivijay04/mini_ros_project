#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

rospy.init_node('lastforward')
rate=rospy.Rate(4)
pub=rospy.Publisher('/cmd_vel', Twist, queue_size=1)


while not rospy.is_shutdown():
    move = Twist()

    # move forward
    move.linear.x = 0.4
    pub.publish(move)
    rospy.sleep(4)

    # move backward
    move.linear.x = -0.4
    pub.publish(move)
    rospy.sleep(4)

    
    # stop
    move.linear.x = 0.0
    pub.publish(move)
    rospy.sleep(4)