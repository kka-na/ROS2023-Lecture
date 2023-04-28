import rospy
import numpy as np
import cv2
from cv_bridge import CvBridge
import time
from std_msgs.msg import Int8
from sensor_msgs.msg import Image, CompressedImage


class SaveWebCam:
    def __init__(self):
        rospy.Subscriber("/test/cam", Image, self.cam_cb)
        rospy.Subscriber("/darknet_ros/detection_image/compressed", CompressedImage, self.detection_cb)
        rospy.Subscriber("/test/web/do_capture", Int8, self.do_capture_cb)
        self.img = None 
        self.detection = None
        self.bridge = CvBridge()

    def cam_cb(self, msg):
        self.img = msg
    
    def detection_cb(self, msg):
        self.detection = msg
    
    def do_capture_cb(self, msg):
        now = time.localtime(time.time())
        file_name = time.strftime('%Y%m%d_%I%M%S',now)
        if msg.data == 1:
            self.save_image(file_name)
        elif msg.data == 2:
            self.save_compressed_image(file_name)

    def save_image(self,file_name):
        cv2_img = self.bridge.imgmsg_to_cv2(self.img, "passthrough")
        cv2.imwrite(f"./captured/{file_name}.png", cv2_img)
        print(f"Successfully Saved on ./captured/{file_name}.png")
    
    def save_compressed_image(self, file_name):
        np_arr = np.frombuffer(self.detection.data, np.uint8)
        cv2_img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        cv2.imwrite(f"./captured/{file_name}_compressed.jpg", cv2_img)
        print(f"Successfully Saved on ./captured/{file_name}.jpg")