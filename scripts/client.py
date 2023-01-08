#! /usr/bin/env python

import rospy
import math
import time
import sys
import select
import actionlib
import actionlib.msg
from std_srvs.srv import *
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Pose, Twist
import RT_assignment_2.msg
from RT_assignment_2.msg import Pos

def callback(data):
   # Get position and linear velocity from odometry
   position = data.pose.pose.position
   linear_velocity = data.twist.twist.linear
   # Create a message of type Pos
   msg = Pos()
   # Fill the message with the position and linear velocity
   msg.x = position.x
   msg.y = position.y
   msg.vx = linear_velocity.x
   msg.vy = linear_velocity.y
   # Publish the message
   pub.publish(msg)

# Function for the action client
def action_client():
   # Create an action client
   client = actionlib.SimpleActionClient('/reaching_goal', RT_assignment_2.msg.PlanningAction)
   # Wait for the action server to start
   client.wait_for_server()

   while not rospy.is_shutdown():
      # Print instructions
      print("Insert the goal coordinates (x,y) or 'c' to cancel the goal and press enter")

      # Read the input from the terminal
      input, o, e = select.select( [sys.stdin], [], [], 1)
      if (input):
         # Read the input
         input = sys.stdin.readline().rstrip()
         # If the input is 'c' cancel the goal
         if input == 'c':
            client.cancel_goal()
            print("Goal cancelled")
         else:
            # Create a message of type PlanningGoal
            goal = RT_assignment_2.msg.PlanningGoal()
            # Fill the message with the goal coordinates
            goal.target_pose.pose.position.x = float(input.split(',')[0])
            goal.target_pose.pose.position.y = float(input.split(',')[1])
            # Send the goal to the action server
            client.send_goal(goal)

def main():
   global pub
   # Initialize the node
   rospy.init_node('client')
   # Publisher for the position of the robot
   pub = rospy.Publisher('/pos', Pos, queue_size=1)
   # Subscriber to the odometry of the robot to get the position and velocity
   odom = rospy.Subscriber('/odom', Odometry, callback)
   # Call the action client
   action_client()

if __name__ == '__main__':
   main()