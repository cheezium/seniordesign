#!/usr/bin/env python
import roslib; roslib.load_manifest('arduo_joy')
import rospy

# Import Python struct to unpack binary data
import struct

# Import rxtx incoming message type
from std_msgs.msg import UInt8MultiArray

# Importing the Velocity command
from turtlesim.msg import Velocity

from turtlesim.srv import *
from std_srvs.srv import *
import random

def checksum_check(data):
    """
	checksum_check(data) - takes data (a tuple) and attempts to validate the 	 		checksum

	Returns True if checksum passes or else it returns false. 
    	
	Notes: The checksum was created by adding up all of the elements from start
	to stop
    """

    # The Checksum value
    check_sum = data[7]	

    # The Sum of the Data
    sum_data = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6]
    
    # Because the checksum is a byte 
    # need to account for roll over if it is greater than 255
    roll_over_sum = sum_data & 255

    if roll_over_sum == check_sum:
	return True
    else:
	return False

def turtle_control( valid_data ): 
    """
	turtle_control( valid_data ) - sends commands to the turtle with the valid data

    """
    # Topic on which to publish on
    pub = rospy.Publisher('/turtle1/command_velocity', Velocity)
    
    # X value - magical numbers are center
    linear = ( valid_data[ 5 ] - 120 ) / 30
    
    # Y value 
    angular = -( ( valid_data[ 4 ] - 127 ) / 30 ) 

    pub.publish( linear, angular ) 
 
    if valid_data[ 6 ] == 0:
	try: 
	    color = rospy.ServiceProxy( '/turtle1/set_pen', SetPen )
	    color( random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 3, 0)  
	    print "Setting a random color" 
	except rospy.ServiceException, e: 
	    print "Color Failed" 

    if valid_data[ 3 ] == 0:
	try: 
	    clear = rospy.ServiceProxy( '/clear', Empty )
	    clear()  
	    print "Clearing the Screen" 
	except rospy.ServiceException, e: 
	    print "Clear Failed"

    return True    	

def process_data(data):
    """
	process_data(data) - processes the incoming byte packets from the
	arduino, calls turtle_control( valid_data ) when a packet has been found

	Note: 
	Requires an entire packet from A - z to mark as valid
	Pack structure: A + lb + rb + ub + db + x + y + pb + checksum + z
	The joystick data has been reduced to a byte, e.g. the 2 least significant
	bits have been removed.  (For easier unpacking) 
    """
    
    message = ''
    message_start = False
    for i in data.data:
	
	# A is the Start of a Packet	
	if i == 'A':
	   
	   # Intilized the start variables
	   message_start = True
	   message = ''
	
	# z is the end of a packet
	elif i == 'z': 

	   # Check to make sure there are 8 bytes 
	   # between the start and end		   
	   if len(message) == 8 and message_start:
		

		# Unpacking the data from unsiged ints
		joy_data = struct.unpack(">BBBBBBBB", message)

		# Check to See if the checksum is valid		
		if checksum_check(joy_data):
		
		    # Checksum valid, calling turtle control		
		    #print "Data is Valid! (Most Likely)" 
		    turtle_control( joy_data )
		
	   # if a z has been found, reset to start 	
	   message = ''
	   message_start = False
	
	# Neither a start byte or a stop byte, add to the message
	else:
	   message += i
    # End Data Processing 		
    	

def process_serial_data():
    """
	process_serial_data() - overhead processing functionality,  

    """
    print "Process function" 
    
    rospy.init_node('rxtx_turtle_command')
    rospy.Subscriber("/rxtx/receiveMA", UInt8MultiArray, process_data)
    rospy.spin()
	

if __name__ == '__main__':
    try:
        process_serial_data()
    except rospy.ROSInterruptException:
        pass
