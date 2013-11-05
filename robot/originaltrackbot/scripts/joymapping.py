#!/usr/bin/env python
import roslib; roslib.load_manifest('trackbot')
import rospy
from trackbot.msg import trackbotMotors
from sensor_msgs.msg import Joy



def mapper(joy_input):
	"""
		Joystick callback function to map axes to motor scalar
	""" 
	ls_y = 1
	rs_y = 4 
	scale = 50
	offset = 50
	pub = rospy.Publisher('arbitratorJoyInput', trackbotMotors)
	motors = trackbotMotors()
		
	if joy_input.axes[ls_y] > 0.0:
		motors.leftMotor = ( ( joy_input.axes[ls_y] ) * scale ) + offset
	else:
		motors.leftMotor = offset - ( ( joy_input.axes[ls_y] ) * -1.0 * scale ) 

	if joy_input.axes[rs_y] > 0.0:
		motors.rightMotor = ( ( joy_input.axes[rs_y] ) * scale ) + offset
	else:
		motors.rightMotor = offset - ( ( joy_input.axes[rs_y] ) * -1.0 * scale )	
        
	pub.publish( motors )
     
   	

def joy_listener():
	"""
		Starts joystick calculation node
	"""
	rospy.init_node('joyCalculations')    
	rospy.Subscriber("joy", Joy, mapper)
	rospy.spin()	



if __name__ == '__main__':
    try:
        joy_listener()
    except rospy.ROSInterruptException:
        pass
