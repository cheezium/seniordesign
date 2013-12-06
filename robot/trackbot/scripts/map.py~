#!/usr/bin/env python
import roslib; roslib.load_manifest('trackbot')
import rospy
from time import sleep
from sensor_msgs.msg import Joy
from trackbot.msg import trackbotMotors


class mapRoom: 
	
	def __init__( self ): 
		"""
			Intialize the nodes and class variables
		"""
		rospy.Subscriber( "joy", Joy, self.__joy ) 
		self.arb_pub = rospy.Publisher('arbitratorMapInput', trackbotMotors)

		self.motors = trackbotMotors()
	

	def map_room( self ):
		"""
			go around in a circle 
		"""
		while( not rospy.is_shutdown() ): 

			# Move motors for 1 second
			set_motors( 70, 30 )
			sleep( 1 )

			# Stop for 15 seconds
			set_motor( 50, 50 ) 
			sleep( 15 ) 

		
	def set_motors( self, rightMotor, leftMotor ): 
		"""
			Turn the robot 
		"""
		self.motors.rightMotor = rightMotor
		self.motors.leftMotor = leftMotor
		
		self.arb_pub( self.motors )
		
				


	def __joy( self, data ): 
		"""
			Tell What State to Goto 
		"""

		if( data.buttons[13] is 1 ): 
			self.state = True
			self.map_room()
		elif( data.buttons[14] is 1):

			#If x button turn off
			self.state = False 
			self.set_motors( 50, 50 ) 
	
		
if __name__ == '__main__':
	
	try:
		x = mapRoom()
		rospy.spin()		
	except rospy.ROSInterruptException:
		pass



