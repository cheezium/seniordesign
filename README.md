seniordesign
============

Repository for Senior Design G63 group

Notes: 

Wireless:
Add IPs of computers to /etc/hosts

check connection using ping and netcat

check clock descrepancies 
ntpdate -q other_computer_ip

Add roscore to ROS_MASTER_URI 
export ROS_MASTER_URI=http://izzy-PC:11311

roslaunch trackbot openni.launch

roslaunch rgbdslam rgbdslam.launch
	- press space to begin recording 3D map
roslaunch rgbdslam octomap_server.launch 
	- press Ctrl+M to export 3D map to projected_map

rosrun octomap_server octomap_server_node ieeelounge1.bt - load map 

rosrun rviz rviz


