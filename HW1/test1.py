import rospy
import threading
from pub_web_cam import PublishWebCam
from save_web_cam import SaveWebCam

if __name__ == "__main__":
    rospy.init_node('Test1', anonymous=False)
    
    pwc = PublishWebCam()
    swc = SaveWebCam()

    pwc.run()

