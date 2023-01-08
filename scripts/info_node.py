#! /usr/bin/env python

import rospy
import math
import time

from RT_assignment_2.msg import Pos

frequency = 1.0
old_time = 0

def callback(data):
   global frequency, old_time
   # Get the current in milliseconds
   current_time = time.time() * 1000
   
   # If the time difference is greater than the period print the info
   if current_time - old_time > 1000 / frequency:
      # Get desired position
      des_x = rospy.get_param('des_x')
      des_y = rospy.get_param('des_y')

      # Calculate the distance
      distance = math.sqrt((des_x - data.x)**2 + (des_y - data.y)**2)

      # Calculate the average velocity
      velocity = math.sqrt(data.vx**2 + data.vy**2)

      # Print the info
      rospy.loginfo('Distance from desired position: %f', distance)
      rospy.loginfo('Average velocity: %f', velocity)

      # Update the old time
      old_time = current_time

def main():
   global frequency
   rospy.init_node('info_node')
   # Get publish frequency
   frequency = rospy.get_param('publish_frequency')
   # Subscribe to the msg
   odom = rospy.Subscriber('/pos', Pos, callback)
   rospy.spin()

if __name__ == '__main__':
   main()