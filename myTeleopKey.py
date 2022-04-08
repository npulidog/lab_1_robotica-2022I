#!/sur/bin/env

# Script de python correspondiente a un nodo tipo Teleop_key

import rospy
from pynput.keyboard import Key, Listener
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from numpy import pi


def callback(data):
    rospy.loginfo(data.x)

def turtlemove():
    rospy.init_node('move_turtlebot', anonymous=False)
    rospy.Subscriber("turtle1/cmd_vel", Twist, callback)
    
    vel = Twist()
    while not rospy.is_shutdown():
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel
        
        if(key == Key.w):
                vel.linear.x = 1.0

        if(key == Key.s):
                vel.linear.x = -1.0

        if(key == Key.d):
                vel.angular.z = 1.0

        if(key == Key.a):
                vel.angular.z = -1.0


def on_press(key):
    if key == Key.space:
    rospy.wait_for_service('/turtle1/teleport_relative')
    try:
        linear=0.0
        angular=180
        teleportR = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        respr = teleportR(linear, angular)

    if key == Key.r
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        x=0.0
        y=0.0
        ang=0.0
        teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        respa = teleportA(x, y, ang) 


def on_release(key):
    if key == Key.esc:
        return False