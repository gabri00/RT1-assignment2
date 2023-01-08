#! /usr/bin/env python

import rospy
import actionlib
import actionlib.msg
import RT_assignment_2.msg
from RT_assignment_2.srv import Goals, GoalsResponse

# Counter for reached and cancelled goal positions
reached = 0
cancelled = 0

def callback(data):
   global reached, cancelled
   # Get status of the goal
   status = data.status.status
   # If the goal is reached
   if status == 3:
      reached += 1
   # If the goal is cancelled
   elif status == 2:
      cancelled += 1

# Service callback
def get_goals(req):
   global reached, cancelled
   # Return the response
   return GoalsResponse(reached, cancelled)

def main():
   # Initialize the node
   rospy.init_node('goals_srv')
   # Create the service
   srv = rospy.Service('goals_srv', Goals, get_goals)
   # Subscribe to the action server
   action = rospy.Subscriber('/reaching_goal/result', RT_assignment_2.msg.PlanningActionResult, callback)
   # Spin
   rospy.spin()

if __name__ == '__main__':
   main()