import rospy
import cv2
from cv_bridge import CvBridge
import numpy as np
from sensor_msgs.msg import Image,CompressedImage

class PublishWebCam:
    def __init__(self):
        self.pub_cam = rospy.Publisher("/test/cam", Image, queue_size=1)
        self.pub_cam_compressed = rospy.Publisher("/test/cam/compressed", CompressedImage, queue_size=1)
        self.bridge = CvBridge()

    def run(self):
        r = rospy.Rate(10)
        cap = cv2.VideoCapture(0)
        image = Image()
        comp_image = CompressedImage()
        while not rospy.is_shutdown():
            b, frame = cap.read()
            if b:
                image = self.bridge.cv2_to_imgmsg(frame, "bgr8")
                self.pub_cam.publish(image)

                comp_image.header.stamp = rospy.Time.now()
                comp_image.format = "jpeg"
                encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),30]
                comp_image.data = np.array(cv2.imencode('.jpg', frame, encode_param)[1]).tostring()
                self.pub_cam_compressed.publish(comp_image)
            r.sleep()
