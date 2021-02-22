#!/usr/bin/env python

import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Joy
from urdf_test.msg import joy_data

joint_1 = 0.
joint_2 = 0.
joint_3 = 0.

# called when joy message is received
def joy_callback(data):

    global joint_1
    joint_1 = data.axes[3]

    global joint_2
    joint_2 = data.axes[1]

    global joint_3
    joint_3 = data.axes[4]
        

def talker():

    # publishing to topic "joy_axes_coords" 
    pub = rospy.Publisher('joy_axes_coords',joy_data, queue_size=10)
    rospy.init_node('Joy_talker')
    rate = rospy.Rate(10) #10 Hz
    msg_str = joy_data()
    msg_str.header = Header()

    while not rospy.is_shutdown():
        msg_str.header.stamp = rospy.Time.now()
        msg_str.j1 = joint_1
        msg_str.j2 = joint_2
        msg_str.j3 = joint_3
        pub.publish(msg_str)
        rate.sleep()
        # subscribe to joystick messages on topic "joy"
        rospy.Subscriber("joy", Joy, joy_callback, queue_size=1)

    

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass