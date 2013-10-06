; Auto-generated. Do not edit!


(cl:in-package trackbot-msg)


;//! \htmlinclude trackbotMotors.msg.html

(cl:defclass <trackbotMotors> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (rightMotor
    :reader rightMotor
    :initarg :rightMotor
    :type cl:fixnum
    :initform 0)
   (leftMotor
    :reader leftMotor
    :initarg :leftMotor
    :type cl:fixnum
    :initform 0))
)

(cl:defclass trackbotMotors (<trackbotMotors>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <trackbotMotors>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'trackbotMotors)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name trackbot-msg:<trackbotMotors> is deprecated: use trackbot-msg:trackbotMotors instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <trackbotMotors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trackbot-msg:header-val is deprecated.  Use trackbot-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'rightMotor-val :lambda-list '(m))
(cl:defmethod rightMotor-val ((m <trackbotMotors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trackbot-msg:rightMotor-val is deprecated.  Use trackbot-msg:rightMotor instead.")
  (rightMotor m))

(cl:ensure-generic-function 'leftMotor-val :lambda-list '(m))
(cl:defmethod leftMotor-val ((m <trackbotMotors>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader trackbot-msg:leftMotor-val is deprecated.  Use trackbot-msg:leftMotor instead.")
  (leftMotor m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <trackbotMotors>) ostream)
  "Serializes a message object of type '<trackbotMotors>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'rightMotor)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'leftMotor)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <trackbotMotors>) istream)
  "Deserializes a message object of type '<trackbotMotors>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rightMotor) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'leftMotor) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<trackbotMotors>)))
  "Returns string type for a message object of type '<trackbotMotors>"
  "trackbot/trackbotMotors")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'trackbotMotors)))
  "Returns string type for a message object of type 'trackbotMotors"
  "trackbot/trackbotMotors")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<trackbotMotors>)))
  "Returns md5sum for a message object of type '<trackbotMotors>"
  "04b4f83ab2eaece160583f6933db3e0e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'trackbotMotors)))
  "Returns md5sum for a message object of type 'trackbotMotors"
  "04b4f83ab2eaece160583f6933db3e0e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<trackbotMotors>)))
  "Returns full string definition for message of type '<trackbotMotors>"
  (cl:format cl:nil "Header header~%~%int16 rightMotor~%int16 leftMotor~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'trackbotMotors)))
  "Returns full string definition for message of type 'trackbotMotors"
  (cl:format cl:nil "Header header~%~%int16 rightMotor~%int16 leftMotor~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <trackbotMotors>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <trackbotMotors>))
  "Converts a ROS message object to a list"
  (cl:list 'trackbotMotors
    (cl:cons ':header (header msg))
    (cl:cons ':rightMotor (rightMotor msg))
    (cl:cons ':leftMotor (leftMotor msg))
))
