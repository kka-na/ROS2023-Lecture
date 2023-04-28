import rospy
import cv2
from cv_bridge import CvBridge
import time
import numpy as np
from std_msgs.msg import Int8
from sensor_msgs.msg import Image,CompressedImage
from darknet_ros_msgs.msg import BoundingBoxes

class CarlaMonitoring:
    def __init__(self):
        rospy.Subscriber("/darknet_ros/detection_image/compressed", CompressedImage, self.detection_cb)
        rospy.Subscriber("/darknet_ros/bounding_boxes",BoundingBoxes, self.bounding_box_cb)
        rospy.Subscriber("/test/web/do_capture", Int8, self.do_capture_cb)
        self.pub_warning = rospy.Publisher("/test/warning", Int8, queue_size=1)
        self.detection = None
        self.bridge = CvBridge()
        self.tick = 0

    def detection_cb(self, msg):
        self.detection = msg
    
    def bounding_box_cb(self, msg):
        for bbox in msg.bounding_boxes:
            if bbox.Class == "person":
                self.tick = 0
                self.pub_warning.publish(Int8(1))
            elif bbox.Class == "car":
                self.tick = 0
                self.pub_warning.publish(Int8(2))
                
        if self.tick >= 10:
            self.pub_warning.publish(Int8(0))
        self.tick += 1

    def do_capture_cb(self, msg):
        now = time.localtime(time.time())
        file_name = time.strftime('%Y%m%d_%I%M%S',now)
        self.save_compressed_image(file_name)

    def save_compressed_image(self, file_name):
        np_arr = np.frombuffer(self.detection.data, np.uint8)
        cv2_img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        cv2.imwrite(f"./captured/{file_name}_compressed.jpg", cv2_img)
        print(f"Successfully Saved on ./captured/{file_name}.jpg")