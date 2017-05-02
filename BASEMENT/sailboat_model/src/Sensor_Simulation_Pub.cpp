//
// Created by hywel on 17-3-23.
//

#include "ros/ros.h"
#include "sailboat_message/Sensor_Simulation_msg.h"
#include <sstream>

#define pi 3.1415926

int main(int argc, char **argv)
{

  ros::init(argc, argv, "Sensor_Simulation_Talker");
  ros::NodeHandle n;
  ros::Publisher Sensor_pub = n.advertise<sailboat_message::Sensor_Simulation_msg>("sensor", 10);
  ros::Rate loop_rate(10);

  while (ros::ok())
  {
    //float64 WindAngle
    sailboat_message::Sensor_Simulation_msg msg;
    msg.WindAngle = pi/4;
    msg.WindSpeed = 2;
    ROS_INFO("I talk WindAngle: [%f]", msg.WindAngle);
    Sensor_pub.publish(msg);

    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}
