#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
import cv2
from cv_bridge import CvBridge				
from visitor_check.msg import Visitor


bridge = CvBridge() 

def visitor_cb(msg):
    cv2_img = bridge.imgmsg_to_cv2(msg.img, "passthrough")
    cv2.imwrite(f"./captured/{msg.name}-{msg.age}.png", cv2_img)
    print(f"Successfully Saved on ./captured/{msg.name}-{msg.age}.png")

def main():
    rospy.init_node('end_node', anonymous=False)
    rospy.Subscriber("visitor_check/visitor", Visitor, visitor_cb)
    rospy.spin()

if __name__ == '__main__':
    main()