#!/usr/bin/env python
import roslib; roslib.load_manifest('trackbot')
import rospy
import struct 
from std_msgs.msg import UInt8MultiArray
from trackbot.msg import trackbotMotors


def serialTransmit( motorInput ):
	"""
		Recieves Data from the Arbitrator and Transmits it to the rxtx node 
	"""

	pub = rospy.Publisher('/rxtx/sendMA', UInt8MultiArray)
	motorByteToSend = int( '00000000', 2 ) 
	armByteToSend = int( '00000000', 2 ) 
	buttonByteToSend = int( '00000000', 2 ) 
	checksumByteToSend = 'A'

	rospy.loginfo("MotorByteToSend: " + str( motorByteToSend ) )
	
	if motorInput.leftMotor > 50:
		# Set bit to forward
		motorByteToSend += 1 << 8

	if motorInput.rightMotor > 50: 
 		# Set bit to forward
		motorByteToSend += 1 << 4

	# Set Mag divided into 3 quadrents, 
	if motorInput.leftMotor < ( 50 / 3 ) or motorInput.leftMotor > ( 100 - ( 50 / 3 ) ):
		# Set to 3 
		motorByteToSend += 1 << 6
		motorByteToSend += 1 << 5
	elif motorInput.leftMotor < ( ( 50 / 3 ) * 2 ) or motorInput.leftMotor > ( 100 - ( ( 50 / 3 ) * 2 ) ):
		# Set to 2 		
		motorByteToSend += 1 << 6
	elif motorInput.leftMotor < ( ( 50 / 3 ) * 3 ) or motorInput.leftMotor > ( 100 - ( ( 50 / 3 ) * 3 ) ):
		# Set to 2 		
		motorByteToSend += 1 << 5	

	# Set Mag divided into 3 quadrents, 
	if motorInput.rightMotor < ( 50 / 3 ) or motorInput.rightMotor > ( 100 - ( 50 / 3 ) ):
		# Set to 3 
		motorByteToSend += 1 << 1
		motorByteToSend += 1 << 0
	elif motorInput.rightMotor < ( ( 50 / 3 ) * 2 ) or motorInput.rightMotor > ( 100 - ( ( 50 / 3 ) * 2 ) ):
		# Set to 2 		
		motorByteToSend += 1 << 1
	elif motorInput.rightMotor < ( ( 50 / 3 ) * 3 ) or motorInput.rightMotor > ( 100 - ( ( 50 / 3 ) * 3 ) ):
		# Set to 2 		
		motorByteToSend += 1 << 0	


	message = struct.pack('>BBBBB', ';', motorByteToSend, armByteToSend, buttonByteToSend, checksumByteToSend )



	# Old Test Code
	#	if motorInput.leftMotor == 50 and motorInput.rightMotor == 50:
	#	message = struct.pack('>BBBBB', ';', motorInput.leftMotor, motorInput.rightMotor)			
		#message = struct.pack('>BBB', 123, motorInput.leftMotor, motorInput.rightMotor)
	#	else:
	#	message = struct.pack('>BBBBB', 122, motorInput.leftMotor, motorInput.rightMotor)
		#message = struct.pack('>BBB', 122, motorInput.leftMotor, motorInput.rightMotor)


	pub.publish( data=message )
	#rospy.loginfo(message)


def recieveArbirator():
	"""
		Recieves arbitrator input and transmits it out
	"""
	rospy.init_node('arbitrator')    
	rospy.Subscriber("arbitratorOutput", trackbotMotors, serialTransmit)
	rospy.spin()	


if __name__ == '__main__':
    try:
        recieveArbirator()
    except rospy.ROSInterruptException:
        pass
