#!/usr/bin/env python
import roslib; roslib.load_manifest('trackbotJoyMapping')
import rospy
from trackbotCeral.msg import trackbotMotors
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Pose2D 




def mapper(joy_input):
	"""
		Joystick callback function to map axes to motor scalar

		Motors are now controlled by giving a X velocity and a theta velocity, each value from -1 to 1 

		With 1 being forward and Clockwise
	""" 

	# Cheap USB Controller
	# Axis Are like this
	#      1 
	# 1  Center -1
	#     -1
	# Buttons are 0 when off 1 when on
	

	ls_y = 1
	ls_x = 2
	rs_x = 3
	rs_y = 4
	but_1 = 0
	but_2 = 1
	but_3 = 2
	but_4 = 3
	l_pump = 4 
	r_bump = 5
	r_trigger = 7
	l_trigger = 6

	# TODO Add PS3 Controller axis 


 
	scale = 50
	offset = 50 
	pub = rospy.Publisher('arbitratorJoyInput', trackbotMotors)
	motors = trackbotMotors()
	
	vel = Pose2D()
			
	
		
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
