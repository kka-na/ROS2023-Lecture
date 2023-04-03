#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
import sys
import cv2	
from cv_bridge import CvBridge
from visitor_check.msg import Visitor   

def hook():
    print("Registration Finished")

def main():
    rospy.init_node('start_node', anonymous=False)
    pub_visitor = rospy.Publisher('/visitor_check/visitor', Visitor, queue_size=1)
    rate = rospy.Rate(1)

    print("Typing Name Age ( If not want press 0 )\n")
    user = input('Name Age: ').split()
    capture = False

    if user[0] == '0':
        print("Exist")
        rospy.on_shutdown("Existing by User")
        sys.exit(0)
    else:
        name = user[0]
        age = int(user[1])
        capture = True

    print(f"Welcome {name}, Take a picture of yourself using the space bar.\n")

    cap = cv2.VideoCapture(0)
    bridge = CvBridge()

    if capture:
        while capture:
            _, frame = cap.read()
            cv2.imshow("Tab to Capture", frame)
            k = cv2.waitKey(30)
            if k%256 == 32:
                img = bridge.cv2_to_imgmsg(frame, "bgr8")
                capture = False
                cv2.destroyAllWindows()

    cnt = 0
    while not rospy.is_shutdown():
        if cnt >= 30:
            rospy.on_shutdown(hook())
            sys.exit(0)

        visitor = Visitor()
        visitor.name = name
        visitor.age = age
        visitor.img = img
        pub_visitor.publish(visitor)
        cnt += 1

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
