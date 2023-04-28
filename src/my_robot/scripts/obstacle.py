#! /usr/bin/env python

import rospy

from geometry_msgs.msg import Twist

from sensor_msgs.msg import LaserScan

def callback(msg):
    rospy.loginfo(rospy.get_caller_id()+ 'The distance to obstacle is - %s',msg.ranges[0])
    print(len(msg.ranges))

    if msg.ranges[0] > .3:
        print('in')
        move.linear.x = .5
        move.angular.z = .2
        pub.publish(move)

    if msg.ranges[0] < .2:
        print('out')
        move.linear.x = .5
        move.angular.z = -.2
        pub.publish(move)

    if msg.ranges[0] > .2 and msg.ranges[0] < .3:
        print('in')
        move.linear.x = .5
        move.angular.z = 0
        pub.publish(move)

rospy.init_node('my_robot_node')

move = Twist()

pub = rospy.Publisher('/cmd_vel',Twist,queue_size = 1)

sub = rospy.Subscriber('/scan',LaserScan,callback)

rospy.spin()