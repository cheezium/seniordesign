#!/usr/bin/env python
import roslib; roslib.load_manifest('trackbotCeral')
import rospy
import struct 
from std_msgs.msg import UInt8MultiArray
from trackbotCeral.msg import trackbotMotors


def serialTransmit( motorInput ):
	"""
		Recieves Data from the Arbitrator and Transmits it to the rxtx node 
	"""

	pub = rospy.Publisher('/rxtx/sendMA', UInt8MultiArray)
	if motorInput.leftMotor == 50 and motorInput.rightMotor == 50:
		message = struct.pack('>BBB', 123, motorInput.leftMotor, motorInput.rightMotor)
	else:
		message = struct.pack('>BBB', 122, motorInput.leftMotor, motorInput.rightMotor)
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
