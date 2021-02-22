#!/usr/bin/env python
# script recieves data from /joy topic 

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from urdf_test.msg import joy_data

joint_1 = 0.
joint_2 = 0.
joint_3 = 0.

# called when joy message is received
def joy_callback(msg):

    divider = 0.001

    global joint_1
    joint_1 += divider * msg.j1

    global joint_2
    if -1.57 <= joint_2 <= 1.57 or (joint_2 < -1.57 and msg.j2 > 0) or (joint_2 > 1.57 and msg.j2 < 0):
        joint_2 += divider * msg.j2

    global joint_3
    if -1.57 <= joint_3 <= 1.57 or (joint_3 < -1.57 and msg.j3 > 0) or (joint_3 > 1.57 and msg.j3 < 0):
        joint_3 += divider * msg.j3
       

def talker():

    # publishing to topic "joint_states" to control robot joints 
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('PS3_test')
    rate = rospy.Rate(10) #10 Hz
    msg_str = JointState()
    msg_str.header = Header()
    msg_str.name = ['joint_1', 'joint_2', 'joint_3']
    msg_str.velocity = []
    msg_str.effort = []

    while not rospy.is_shutdown():
        msg_str.header.stamp = rospy.Time.now()
        msg_str.position = [joint_1, joint_2, joint_3]
        pub.publish(msg_str)
        rate.sleep()
        # subscribe to joystick messages on topic "joy"
        rospy.Subscriber('joy_axes_coords', joy_data, joy_callback, queue_size=1)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass