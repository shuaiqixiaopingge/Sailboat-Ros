cmake_minimum_required(VERSION 2.8.3)
project(sailboat_message)

## Add support for C++11, supported in ROS Kinetic and newer
# add_definitions(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
        roscpp
        rospy
        std_msgs
        message_generation
        )
################################################
## Declare ROS messages, services and actions ##
################################################

## Generate messages in the 'msg' folder
add_message_files(
        FILES

        Mach_msg.msg
        GPS_msg.msg
        Ahrs_msg.msg
        WTST_msg.msg
        WTST_Pro_msg.msg
        Sensor_msg.msg
        Arduino_msg.msg

        Wind_Simulation_msg.msg
        Sailboat_Simulation_msg.msg
        Target_msg.msg

        station_keeping_out.msg
        fleet_race_out.msg
        scanning_out.msg
        avoidance_out.msg
        station_keeping_para.msg
        fleet_race_para.msg
        scanning_para.msg
        avoidance_para.msg

        traj_following_para.msg
        traj_following_out.msg

        Point.msg
        PointArray.msg

        #cmd
        cmd_battery_status.msg
        cmd_camera_status.msg
        cmd_commander_cfg_status.msg
        cmd_commander_status.msg
        cmd_communication_status.msg
        cmd_home_position.msg
        cmd_navigation_status.msg
        cmd_path_planning_mode.msg
        cmd_path_planning_status.msg
        cmd_sensor_status.msg
        cmd_vehicle_control_mode.msg
        cmd_vehicle_control_status.msg

)

## Generate added messages and services with any dependencies listed here
generate_messages(
        DEPENDENCIES
        std_msgs
)


catkin_package(
        # INCLUDE_DIRS include
        #LIBRARIES sailboat_message
        CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
        #DEPENDS system_lib
)

