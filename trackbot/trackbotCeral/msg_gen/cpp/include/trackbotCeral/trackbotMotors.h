/* Auto-generated by genmsg_cpp for file /projects/ros/seniordesign/trackbot/trackbotCeral/msg/trackbotMotors.msg */
#ifndef TRACKBOTCERAL_MESSAGE_TRACKBOTMOTORS_H
#define TRACKBOTCERAL_MESSAGE_TRACKBOTMOTORS_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"

namespace trackbotCeral
{
template <class ContainerAllocator>
struct trackbotMotors_ {
  typedef trackbotMotors_<ContainerAllocator> Type;

  trackbotMotors_()
  : header()
  , rightMotor(0)
  , leftMotor(0)
  {
  }

  trackbotMotors_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , rightMotor(0)
  , leftMotor(0)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef int16_t _rightMotor_type;
  int16_t rightMotor;

  typedef int16_t _leftMotor_type;
  int16_t leftMotor;


  typedef boost::shared_ptr< ::trackbotCeral::trackbotMotors_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::trackbotCeral::trackbotMotors_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct trackbotMotors
typedef  ::trackbotCeral::trackbotMotors_<std::allocator<void> > trackbotMotors;

typedef boost::shared_ptr< ::trackbotCeral::trackbotMotors> trackbotMotorsPtr;
typedef boost::shared_ptr< ::trackbotCeral::trackbotMotors const> trackbotMotorsConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::trackbotCeral::trackbotMotors_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::trackbotCeral::trackbotMotors_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace trackbotCeral

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::trackbotCeral::trackbotMotors_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::trackbotCeral::trackbotMotors_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::trackbotCeral::trackbotMotors_<ContainerAllocator> > {
  static const char* value() 
  {
    return "04b4f83ab2eaece160583f6933db3e0e";
  }

  static const char* value(const  ::trackbotCeral::trackbotMotors_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x04b4f83ab2eaece1ULL;
  static const uint64_t static_value2 = 0x60583f6933db3e0eULL;
};

template<class ContainerAllocator>
struct DataType< ::trackbotCeral::trackbotMotors_<ContainerAllocator> > {
  static const char* value() 
  {
    return "trackbotCeral/trackbotMotors";
  }

  static const char* value(const  ::trackbotCeral::trackbotMotors_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::trackbotCeral::trackbotMotors_<ContainerAllocator> > {
  static const char* value() 
  {
    return "Header header\n\
\n\
int16 rightMotor\n\
int16 leftMotor\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
";
  }

  static const char* value(const  ::trackbotCeral::trackbotMotors_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::trackbotCeral::trackbotMotors_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::trackbotCeral::trackbotMotors_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::trackbotCeral::trackbotMotors_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.rightMotor);
    stream.next(m.leftMotor);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct trackbotMotors_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::trackbotCeral::trackbotMotors_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::trackbotCeral::trackbotMotors_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "rightMotor: ";
    Printer<int16_t>::stream(s, indent + "  ", v.rightMotor);
    s << indent << "leftMotor: ";
    Printer<int16_t>::stream(s, indent + "  ", v.leftMotor);
  }
};


} // namespace message_operations
} // namespace ros

#endif // TRACKBOTCERAL_MESSAGE_TRACKBOTMOTORS_H

