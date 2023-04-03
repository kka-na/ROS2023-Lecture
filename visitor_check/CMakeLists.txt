cmake_minimum_required(VERSION 3.0.2)
project(visitor_check)

find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
  std_msgs
  message_generation
)

add_message_files(
  FILES
  Visitor.msg
)

generate_messages(
  DEPENDENCIES
  sensor_msgs
  std_msgs
)

catkin_package(
 LIBRARIES visitor_check
 CATKIN_DEPENDS rospy sensor_msgs std_msgs message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(
  PROGRAMS src/registration.py src/record.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
