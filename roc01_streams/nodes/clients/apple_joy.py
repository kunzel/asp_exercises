#! /usr/bin/env python

import roslib; roslib.load_manifest('rosoclingo_examples')
from rosoclingo.msg import *
from sensor_msgs.msg import Joy
import rospy
import actionlib

client = actionlib.ActionClient('ROSoClingo',ROSoClingoAction)
handlers = 0 #Global variable with the pt for the new goal

def send_goal(id):
 goal = ROSoClingoGoal(str(id))
 print "send " + str(id)
 return client.send_goal(goal)

def cancel_goal(goal):
 print "cancel " + str(goal)
 goal.cancel()

# New data arrived
def callback( data ):
 global handlers
 if( data.buttons[3] == 1 ): #Green Button
  handlers = send_goal( 2 )
  #rospy.loginfo( "Cancel" )
 if( data.buttons[1] == 1 ): #Red Button
  cancel_goal( handlers )
  #rospy.loginfo( "Set Goal" )


#def example():
# aux = 1;
# while aux == 1 :
#  client.wait_for_server()
#  handlers = send_goal( 2 )
#  rospy.sleep(2.0)
#  cancel_goal( handlers )
#  rospy.sleep(2.0)

if __name__ == '__main__':
    try:
        rospy.init_node('apple_joy')
        rospy.Subscriber("joy", Joy, callback)
        #       result = example()
	rospy.spin()
    except rospy.ROSInterruptException:
        print "program interrupted before completion"
