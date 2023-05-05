#! /usr/bin/env python

"""
.. module: info_node
   :platform: Unix
   :synopsis: This module contains the node that prints the distance from the desired position and the average velocity of the robot.

.. moduleauthor: Gabriele Nicchiarelli

ROS node that prints the distance from the desired position and the average velocity of the robot.

Subscribes to:
   /pos
"""

import rospy
import math
import time

from RT_assignment_2.msg import Pos

frequency = 1.0 # Frequency of the node in Hz
"""float: Frequency of the node in Hz.
"""
old_time = 0    # Time of the last print

def callback(data):
   """Callback function for the subscriber to the odometry of the robot.
   
   Args:
      data (Pos message): Position and velocity of the robot.
   """
   global frequency, old_time
   # Get the current time in milliseconds
   current_time = time.time() * 1000
   
   # If the time difference is greater than the period print the info
   if current_time - old_time > 1000 / frequency:
      # Get desired position
      des_x = rospy.get_param('des_pos_x')
      des_y = rospy.get_param('des_pos_y')

      # Calculate the (Euclidean) distance from the desired position
      distance = math.sqrt((des_x - data.x)**2 + (des_y - data.y)**2)

      # Calculate the average velocity
      velocity = math.sqrt(data.vx**2 + data.vy**2)

      # Print the info
      rospy.loginfo('Distance from desired position: %f', distance)
      rospy.loginfo('Average velocity: %f', velocity)

      # Update old time
      old_time = current_time

def main():
   global frequency
   # Initialize the node
   rospy.init_node('info_node')
   # Get publish frequency
   frequency = rospy.get_param('publish_frequency')
   # Subscribe to the msg
   odom = rospy.Subscriber('/pos', Pos, callback)
   rospy.spin()

if __name__ == '__main__':
   main()