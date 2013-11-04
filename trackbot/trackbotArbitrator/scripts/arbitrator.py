#!/usr/bin/env python
import roslib; roslib.load_manifest('trackbotArbitrator')
import rospy
from trackbotCeral.msg import trackbotMotors
from sensor_msgs.msg import Joy



def arbitrator_callback(joy_motor_input):
	"""
		Controls arbitrator logic, passes through logic right now
	""" 
	
	pub = rospy.Publisher('arbitratorOutput', trackbotMotors)	
	motorInput = trackbotMotors()
	#rospy.loginfo(motorInput)
	motorInput = joy_motor_input
	pub.publish( motorInput )
     
   	

def arbitrator():
	"""
		Starts arbirator
	"""
	rospy.init_node('arbitrator')    
	rospy.Subscriber("arbitratorJoyInput", trackbotMotors, arbitrator_callback)
	rospy.spin()	



if __name__ == '__main__':
    try:
        arbitrator()
    except rospy.ROSInterruptException:
        pass
