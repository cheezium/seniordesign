#!/usr/bin/env python
import roslib; roslib.load_manifest('ballCollector')
import rospy
from time import sleep
from sensor_msgs.msg import Joy
from trackbot.msg import trackbotMotors


class ballCollector: 
	"""
		Class that controls ball Collector Parameters 

	"""

	def __init__( self ): 
		"""
			Intialize the nodes and class variables
		"""
		
		#publisher for control message
		self.control_pub = rospy.Publisher('ballCollector/Control', Transform)
		# Publishish a True Message when ball Detection is needed 		
		self.detecting_balls = rospy.Publisher('ballCollector/Detecting_balls', Bool) 
		self.servo = rospy.Publisher( 'hoverboard/PWMRaw', PWMRaw, latch=True )

		# Opening up nodes and such
		rospy.init_node('ballcollector')    

		# Variables to Store ball Location and Landmark Distance
		self.ballLocation = ballDistance()
		self.landmarkLocation = landmarkDistance()
		self.servoControl = PWMRaw() 
		self.gyro = Gyro()
		self.joy = Joy()

		
	
		# Subscribe to Ball / Object Distance Location
		rospy.Subscriber( "distance/Landmark", landmarkDistance, self.__landmark_location )
		rospy.Subscriber( "distance/Ball", ballDistance, self.__ball_location )
		rospy.Subscriber( "hovercraft/Gyro", Gyro, self.__gyro )
		rospy.Subscriber( "joy", Joy, self.__joy ) 
		rospy.Subscriber( "ircm/IRoutput", IRdistance, self.__ir )
		

		# Pull in ROS params 
		self.pickupDistance = rospy.get_param("ballcollector/PickupDistance")
		self.pickupDegreeTolerance = rospy.get_param("ballcollector/PickupDegreeTolerance")
		self.dropOffDegreeTolerance = rospy.get_param("ballcollector/DropOffDegreeTolerance")
		self.pickupDistanceTolerance = rospy.get_param("ballcollector/PickupDistanceTolerance")	
			
		

		# State Machine Logic & States 		
		self.state = 0
		self.wait = 0
		self.searchForBall = 1
		self.pickUpBall = 2
		self.searchForTarget = 3
		self.moveToTarget = 4
		self.ejectBall = 5
		
		self.previousState = -1;
		self.logPreviousState = -1;
		
		self.sawTarget = False
		self.targetAngle = 0.0

		# IR distance 
		self.irDistance = 0.0
		self.irAverage = 0.0
		self.irPervious = 0.0

		# Spin Stuff
		self.startAngle = 0.0
		self.angleOffSet = 0.0
		self.turnAngle = 30.0
		self.locateTurnAngle = 35.0
		self.landmarkTurnAngle = -120.0
		self.power = .75

	def start_state_machiene( self ): 
		"""
			Starts State Machiene in Infinite LOOP 
		"""
		self.__set_catcher( False )
		self.sawTarget = False
		while( not rospy.is_shutdown() ): 

			# Store Previous State 
			if self.previousState is not self.state:
				self.previousState = self.state
			
			self.__state_machiene( )
	

	def __state_machiene( self ):
		"""
			Contains High Level Logic for ball collection alogoritims 

		"""


		# In the Wait State Until we get told to move 
		if self.state == self.wait: 
			#rospy.loginfo("S.M.- Waiting...")
			self.__print_state( "S.M.- Waiting..." )
			#self.state = self.searchForBall
		
		elif self.state == self.searchForBall:
			#rospy.loginfo("S.M.- Searching For Ball...")
			self.__print_state( "S.M.- Searching For Ball..." )
			self.__detecting_balls( True )
		
			
			if self.__search_for_ball() == True: 
				# If a Ball is found Set State to Pick Up the Ball
				self.state = self.pickUpBall



		elif self.state == self.pickUpBall:
			#rospy.loginfo("S.M.- Picking Up Ball...")
			self.__detecting_balls( True )	
			self.__print_state( "S.M.- Picking Up Ball..." )

			if self.__pick_up_ball() == True: 
				# If a Ball is Picked Up time to find the target 
				self.state = self.searchForTarget


		elif self.state == self.searchForTarget:
			#rospy.loginfo("S.M.- Searching For Target...")
			self.__print_state( "S.M.- Searching For Target..." )
			self.__detecting_balls( False )

			if self.__search_for_target() == True: 
				# If target is found, move to target 
				self.state = self.moveToTarget
		

		elif self.state == self.moveToTarget:
			#rospy.loginfo("S.M.- Moving to Target...")
			self.__print_state( "S.M.- Moving to Target..." )
			self.__detecting_balls( False )

			if self.__move_to_target() == True: 
				# If moved to target, Eject ball
				self.state = self.ejectBall 


		elif self.state == self.ejectBall:
			#rospy.loginfo("S.M.- Ejecting Ball...")
			self.__print_state( "S.M.- Ejecting Ball..." )
			self.__detecting_balls( False )
		
			if self.__eject_ball() == True: 
				# If ball is ejected Smile 
				rospy.loginfo("B.C. - Ball Ejected! Yeah! I hope it actually Works!")
				self.state = self.wait

		else:
			rospy.loginfo("S.M.- Warning: Ball Collector State Machine in Unknown State") 
	


	def __search_for_ball( self ):
		"""
			State: 1
			Logic Used to search for the Ball 
		"""

		
		# Check to see if we see ball
		if( self.__is_active( self.ballLocation ) and self.ballLocation.distance < 160):
			# WE FOUND THE BALL THERE IS NOTHING ELSE TO DO 
			return True 
		else: 
			
			#rospy.loginfo("Gyro Rate: " + str(self.gyro.rate) )

			# We saw the ball then lost it, attempt to goto previous location
			if( self.previousState == self.pickUpBall ): 
				
				if( self.ballLocation.distance < 30 ):
					# Distance was short, back up
					self.__publish_thruster_control( self.gyro.angle, -.3 )
				elif( self.ballLocation.angle > 0 ):
					# Ball was to the Right, move right 
					self.__publish_thruster_control( self.gyro.angle - 30.0, 0 )
				elif( self.ballLocation.angle < 0 ): 
					# Ball was on the Left, Turn Left 
					self.__publish_thruster_control( self.gyro.angle + 30.0, 0 )
									
			
	
			# Check and make sure the Rate isn't to much 
			if( self.gyro.rate < 20.0 and self.gyro.rate > -20.0 ): 

				#rospy.loginfo("Turing to find a ball" )

				self.currentAngle = self.gyro.angle
				angleSpin = self.locateTurnAngle
				targetAngle = self.currentAngle + angleSpin			

				self.__publish_thruster_control( targetAngle + 75.0, 0 )
				
		
		return False


	def __pick_up_ball( self ):
		"""
			State: 2
			Logic to pick up Ball
		"""

		# Check and make sure we still see the ball, if not goto Search For Ball State
		# 160 is max distance, don't want to be calling noise a ball   
		if( not ( self.__is_active( self.ballLocation ) and self.ballLocation.distance < 120 ) ): 
			self.state = self.searchForBall

		else: 
			
			# Center the Ball
			# If we are in the tolerance Zone, Move Forward
			#rospy.loginfo( "Ball Angle: " + str( self.ballLocation.angle ) + " Tolerance: " + str( self.pickupDegreeTolerance ) )
			Left = self.ballLocation.angle > ( -1.0 * self.pickupDegreeTolerance ) 
			Right = self.ballLocation.angle < self.pickupDegreeTolerance 
			#rospy.loginfo( "Left: " + str( Left ) + " Right: " + str( Right ) ) 
			if( Left and Right ):
				# We are 5 degrees to the Left or Right of the center of the robot

				# Check to see how close we are 
				if( self.ballLocation.distance <= self.pickupDistance ): 
					# We Are in Distance! Catch IT!
					self.__publish_thruster_control( self.gyro.angle, 0, z=0.0 ) 
					self.__set_catcher( True )
					rospy.loginfo( "Tried Catching Ball" )
					sleep(5)
					self.__publish_thruster_control( self.gyro.angle, 0 )
					return True
				else:
					# To Far Away, move forward 
					self.__publish_thruster_control( self.gyro.angle, self.power - .20 )  

			else: 
				# Need to Turn to center the Ball
				if( self.ballLocation.angle < 0.0 ):
					#Ball is on left, Turn Left 
					rospy.loginfo("Ball On Left, Turning Left")
					self.__publish_thruster_control( ( self.gyro.angle + self.turnAngle + 75.0 ), 0 ) 
				else: 
					#Ball on Right, Turn Right 
					rospy.loginfo("Ball On Right, Turning Right")
					self.__publish_thruster_control( ( self.gyro.angle - self.turnAngle + 10 ), 0 ) 				   
		return False


	def __search_for_target( self ):
		"""
			State: 3
			Logic to search for the Target  
		"""
		
		
		# Check to see if we see target 
		if( self.__is_active( self.landmarkLocation ) and self.landmarkLocation.code == rospy.get_param("ballcollector/TargetNumber") ):
			# We found the CORRECT TARGET, MOVE TO TARGET NEXT!
			self.sawTarget = True
			self.targetAngle = self.landmarkLocation.angle + self.gyro.angle
			# Target Found
			return True
		else:

			#rospy.loginfo("Gyro Angle: " + str(self.gyro.angle) ) 
			
			#Spin around until we see the goal
			if( self.gyro.rate < 20 and self.gyro.rate > -20 ): 

				self.currentAngle = self.gyro.angle
				angleSpin = self.landmarkTurnAngle
				targetAngletemp = self.currentAngle + angleSpin			

				self.__publish_thruster_control( targetAngletemp, 0 )
				#rospy.loginfo("Turing to find a target" )



		return False


	def __move_to_target( self ):
		"""
			State: 4
			Logic to move to target 
		"""

		if self.irAverage > 0: 

			if( self.irAverage <= rospy.get_param("ballcollector/DropDistance") ):	
				self.__publish_thruster_control( self.gyro.angle, 0, z=0.0 ) 
				rospy.loginfo( "We Are At the Landmark!" )
				return True	
			else:	
				rospy.loginfo("Moving to Target, Set Target Angle and Power" )
				# Set to target angle 
				self.__publish_thruster_control( self.targetAngle, self.power )

		if False:	

			# Check and make sure we still see the landmark, if not goto Search For Target State  
			if( not( self.__is_active( self.landmarkLocation ) and self.landmarkLocation.code == rospy.get_param("ballcollector/TargetNumber") ) or self.sawTarget): 
				self.state = self.moveToTarget
			else: 
			




				if False: 
					# Center the Landmark
					# If we are in the tolerance Zone, Move Forward
					mleft = self.landmarkLocation.angle > ( -1.0 * self.dropOffDegreeTolerance )
					mright =  self.landmarkLocation.angle < self.dropOffDegreeTolerance 
					if( mleft and mright ):
						# We are 5 degrees to the Left or Right of the center of the robot

						# Check to see how close we are 
						if( self.landmarkLocation.distance <= rospy.get_param("ballcollector/DropDistance") ): 
							# We Are in Distance! Drop IT!
							self.__publish_thruster_control( self.gyro.angle, 0, z=0.0 ) 
							rospy.loginfo( "We Are At the Landmark!" )
							return True
						else:
							# To Far Away, move forward 
							self.__publish_thruster_control( self.gyro.angle, self.power)  

					else: 
						# Need to Turn to center the Landmark
						if( self.landmarkLocation.angle < 0.0 ):
							#Ball is on left, Turn Left 
							rospy.loginfo("Target On Left, Turning Left")
							self.__publish_thruster_control( ( self.gyro.angle + self.turnAngle ), 0 ) 
						else: 
							#Ball on Right, Turn Right 
							rospy.loginfo("Target On Right, Turning Right")
							self.__publish_thruster_control( ( self.gyro.angle - self.turnAngle ), 0 ) 	
		

		return False	

	def __eject_ball( self ):
		"""
			State: 5
			Logic to eject a Ball
		"""
		self.__set_catcher( False )
		sleep(5)
		return True

	def __is_active( self, data ): 
		"""
			Checks to see if the current message header is active
			i.e. there is a ball or not  
		"""

		now = rospy.Time.now()
		sec  = rospy.get_param("ballcollector/ActiveTime") 
		#nanosec = sec * 1000000
		
		header = data.header.stamp

		#rospy.loginfo("Is Active - Nano Seconds: " + str( now.secs ) + " Header Seconds: " + str( data.header.stamp.secs ) )
		# Check to See if time Stamp (epoch time is within the Active time		
		if( ( header.secs + sec ) >= now.secs ):
			return True
		else: 
			return False


	def __landmark_location( self, data ):
		"""
			Callback function used when New Landmark Data comes in  
		"""
		
		self.landmarkLocation = data
	
	def __ir( self, ir ):
		"""
			IR Call Back
		"""
		
		if ir.IR2 > 0:
			self.irPrevious = self.irDistance 
			
			self.irDistance = ir.IR2
			self.irAverage = ( self.irPervious + self.irDistance ) / 2.0

	def __ball_location( self, data ):
		"""
			Callback function used when New Ball location Data comes in
		"""
		
		self.ballLocation = data
	
			
	def __detecting_balls( self, Boolean ):
		"""
			Publishish a True / False message when ball detection is needed
		"""
		self.detecting_balls.publish( Boolean )

	def __print_state( self, string ):
		"""
			Limit My state information junk
		"""
		
		if self.logPreviousState is not self.state:
			rospy.loginfo(string)  
			self.logPreviousState = self.state


	def __publish_thruster_control( self, theta, y, z=.5 ):
		"""
			Used to publish the postion topic
			Theta = Target Angle
			Y = Forward / Backward Velocity 
		"""

		transform = Transform()
	
		transform.translation.x = 0.0
		transform.translation.y = y
		transform.translation.z = z
		transform.rotation.w = theta 

		self.control_pub.publish( transform )

	def __joy( self, data ): 
		"""
			Tell What State to Goto 
		"""

		if( data.buttons[12] is 1 ): 
			self.state = self.searchForBall
			self.__set_catcher( False )
		elif( data.buttons[2] is 1):
			self.state = 5 

	def __gyro( self, data ):
		"""
		Gyro CallBack 		
		"""		

		self.gyro = data
	
	def __set_catcher( self, up_or_down ):
		"""
		Set the Servo value
		 	False - Up
			True - Down	
		""" 
		
		servoPWM = PWMRaw()
		servoPWM.channel = 3
		if up_or_down: 
			servoPWM.pwm = rospy.get_param("ballcollector/ServoUpValue")
		else: 
			servoPWM.pwm = rospy.get_param("ballcollector/ServoDownValue")
		
		rospy.loginfo("Setting Servo")	
		self.servo.publish( servoPWM ) 

		
if __name__ == '__main__':
	
	try:
		x = ballCollector()
		x.start_state_machiene()
		
	except rospy.ROSInterruptException:
		pass



