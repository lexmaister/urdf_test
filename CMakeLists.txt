cmake_minimum_required(VERSION 2.8.3)
project(urdf_test)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  roslaunch
  message_generation
)

add_message_files(
  FILES
  joy_data.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
     CATKIN_DEPENDS rospy std_msgs message_runtime
)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

catkin_install_python(PROGRAMS python/PS3_test.py python/Joy_talker.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

